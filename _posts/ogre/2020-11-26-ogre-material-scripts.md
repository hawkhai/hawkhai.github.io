---
layout: post
title: "3D 引擎 Ogre3D -- Ogre3D 材质脚本文档 Material Scripts"
author:
location: "珠海"
categories: ["3D 引擎"]
tags: ["图形学", "Ogre3D"]
toc: true
toclistyle: none
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---


## Material Scripts {#Material-Scripts}

Material scripts offer you the ability to define complex materials in a script which can be reused easily. Whilst you could set up all materials for a scene in code using the methods of the Material and TextureLayer classes, in practice it's a bit unwieldy. Instead you can store material definitions in text files which can then be loaded whenever required.

@tableofcontents

It’s important to realise that materials are not loaded completely by the parsing process: only the definition is loaded, no textures or other resources are loaded. This is because it is common to have a large library of materials, but only use a relatively small subset of them in any one scene. To load every material completely in every script would therefore cause unnecessary memory overhead. You can access a ’deferred load’ Material in the normal way (Ogre::MaterialManager::getSingleton().getByName()), but you must call the ’load’ method before trying to use it. Ogre does this for you when using the normal material assignment methods of entities etc.

To start with, we only consider fixed-function materials which don’t use vertex, geometry or fragment programs, these are covered later:

```cpp
// This is a comment
material walls/funkywall1
{
    // first, preferred technique
    technique
    {
        // first pass
        pass
        {
            ambient 0.5 0.5 0.5
            diffuse 1.0 1.0 1.0

            // Texture unit 0
            texture_unit
            {
                texture wibbly.jpg
                scroll_anim 0.1 0.0
                wave_xform scale sine 0.0 0.7 0.0 1.0
            }
            // Texture unit 1 (this is a multitexture pass)
            texture_unit
            {
                texture wobbly.png
                rotate_anim 0.25
                colour_op add
            }

            // Additional RT Shader system options
            rtshader_system
            {
                // Do lighting calculations per-pixel
                lighting_stage per_pixel
            }
        }
    }

    // Second technique, can be used as a fallback or LOD level
    technique
    {
        // .. and so on
    }
}
```

A material can be made up of many @ref Techniques - a technique is one way of achieving the effect you are looking for. You can supply more than one technique in order to provide fallback approaches where a card does not have the ability to render the preferred technique, or where you wish to define lower level of detail versions of the material in order to conserve rendering power when objects are more distant.

Each technique can be made up of many @ref Passes, that is a complete render of the object can be performed multiple times with different settings in order to produce composite effects. Ogre may also split the passes you have defined into many passes at runtime, if you define a pass which uses too many texture units for the card you are currently running on (note that it can only do this if you are not using a fragment program). Each pass has a number of top-level attributes such as ’ambient’ to set the amount & colour of the ambient light reflected by the material. Some of these options do not apply if you are using vertex programs, See @ref Passes for more details.

Within each pass, there can be zero or many @ref Texture-Units in use. These define the texture to be used, and optionally some blending operations (which use multitexturing) and texture effects.

You can also reference vertex and fragment programs (or vertex and pixel shaders, if you want to use that terminology) in a pass with a given set of parameters. Programs themselves are declared in separate .program scripts (See @ref Declaring-Vertex_002fGeometry_002fFragment-Programs) and are used as described in @ref Using-Vertex_002fGeometry_002fFragment-Programs-in-a-Pass.

<a name="Top_002dlevel-material-attributes"></a>


## Material {#Material}

The outermost section of a material definition does not have a lot of attributes of its own (most of the configurable parameters are within the child sections. However, it does have some, and here they are:

<a name="lod_005fstrategy"></a>
<a name="lod_005fstrategy-1"></a>


## lod_strategy

Sets the name of the LOD strategy to use. Defaults to ’Distance’ which means LOD changes based on distance from the camera. Also supported is ’PixelCount’ which changes LOD based on an estimate of the screen-space pixels affected.
@par
Format: lod_strategy &lt;name&gt;<br> Default: lod_strategy Distance

<a name="lod_005fvalues"></a>
<a name="lod_005fvalues-1"></a>


## lod_values

This attribute defines the values used to control the LOD transition for this material. By setting this attribute, you indicate that you want this material to alter the Technique that it uses based on some metric, such as the distance from the camera, or the approximate screen space coverage. The exact meaning of these values is determined by the option you select for [lod_strategy](#lod_005fstrategy) - it is a list of distances for the ’Distance’ strategy, and a list of pixel counts for the ’PixelCount’ strategy, for example. You must give it a list of values, in order from highest LOD value to lowest LOD value, each one indicating the point at which the material will switch to the next LOD. Implicitly, all materials activate LOD index 0 for values less than the first entry, so you do not have to specify ’0’ at the start of the list. You must ensure that there is at least one Technique with a [lod_index](#lod_005findex) value for each value in the list (so if you specify 3 values, you must have techniques for LOD indexes 0, 1, 2 and 3). Note you must always have at least one Technique at lod_index 0.

@par
Format: lod_values &lt;value0&gt; &lt;value1&gt; &lt;value2&gt; ...<br> Default: none
@par
Example: <br> lod_strategy Distance lod_values 300.0 600.5 1200

The above example would cause the material to use the best Technique at lod_index 0 up to a distance of 300 world units, the best from lod_index 1 from 300 up to 600, lod_index 2 from 600 to 1200, and lod_index 3 from 1200 upwards.

<a name="lod_005fdistances"></a>


## lod_distances

@deprecated This option is deprecated in favour of [lod_values](#lod_005fvalues) now.

<a name="receive_005fshadows"></a><a name="receive_005fshadows-1"></a>


## receive_shadows

This attribute controls whether objects using this material can have shadows cast upon them.

@par
Format: receive_shadows &lt;on\|off&gt;<br> Default: on

Whether or not an object receives a shadow is the combination of a number of factors, See @ref Shadows for full details; however this allows you to make a material opt-out of receiving shadows if required. Note that transparent materials never receive shadows so this option only has an effect on solid materials.

<a name="transparency_005fcasts_005fshadows"></a><a name="transparency_005fcasts_005fshadows-1"></a>


## transparency_casts_shadows

This attribute controls whether transparent materials can cast certain kinds of shadow.

@par
Format: transparency_casts_shadows &lt;on\|off&gt;<br>
Default: off

Whether or not an object casts a shadow is the combination of a number of factors, See @ref Shadows for full details; however this allows you to make a transparent material cast shadows, when it would otherwise not. For example, when using texture shadows, transparent materials are normally not rendered into the shadow texture because they should not block light. This flag overrides that.

<a name="set_005ftexture_005falias"></a><a name="set_005ftexture_005falias-1"></a>


## set_texture_alias

This attribute associates a texture alias with a texture name.

@par
Format: set_texture_alias &lt;alias name&gt; &lt;texture name&gt;

This attribute can be used to set the textures used in texture unit states that were inherited from another material.(See @ref Texture-Aliases)


## Techniques {#Techniques}

A "technique" section in your material script encapsulates a single method of rendering an object. The simplest of material definitions only contains a single technique, however since PC hardware varies quite greatly in it’s capabilities, you can only do this if you are sure that every card for which you intend to target your application will support the capabilities which your technique requires. In addition, it can be useful to define simpler ways to render a material if you wish to use material LOD, such that more distant objects use a simpler, less performance-hungry technique.

When a material is used for the first time, it is ’compiled’. That involves scanning the techniques which have been defined, and marking which of them are supportable using the current rendering API and graphics card. If no techniques are supportable, your material will render as blank white. The compilation examines a number of things, such as:

-   The number of texture_unit entries in each pass<br> Note that if the number of texture_unit entries exceeds the number of texture units in the current graphics card, the technique may still be supportable so long as a fragment program is not being used. In this case, Ogre will split the pass which has too many entries into multiple passes for the less capable card, and the multitexture blend will be turned into a multipass blend (See [colour_op_multipass_fallback](#colour_005fop_005fmultipass_005ffallback)).
-   Whether vertex, geometry or fragment programs are used, and if so which syntax they use (e.g. vs_1_1, ps_2_x, arbfp1 etc.)
-   Other effects like cube mapping and dot3 blending
-   Whether the vendor or device name of the current graphics card matches some user-specified rules

In a material script, techniques must be listed in order of preference, i.e. the earlier techniques are preferred over the later techniques. This normally means you will list your most advanced, most demanding techniques first in the script, and list fallbacks afterwards.

To help clearly identify what each technique is used for, the technique can be named but its optional. Techniques not named within the script will take on a name that is the technique index number. For example: the first technique in a material is index 0, its name would be "0" if it was not given a name in the script. The technique name must be unique within the material or else the final technique is the resulting merge of all techniques with the same name in the material. A warning message is posted in the Ogre.log if this occurs. Named techniques can help when inheriting a material and modifying an existing technique: (See @ref Script-Inheritance)

@par
Format: technique name

Techniques have only a small number of attributes of their own:

-   [scheme](#scheme)
-   [lod_index](#lod_005findex) (and also see [lod_distances](#lod_005fdistances) in the parent material)
-   [shadow_caster_material](#shadow_005fcaster_005fmaterial)
-   [shadow_receiver_material](#shadow_005freceiver_005fmaterial)
-   [gpu_vendor_rule](#gpu_005fvendor_005frule)
-   [gpu_device_rule](#gpu_005fdevice_005frule)

<a name="scheme"></a><a name="scheme-1"></a>


## scheme

Sets the `scheme` this Technique belongs to. Material schemes are used to control top-level switching from one set of techniques to another. For example, you might use this to define `high` , `medium` and `low` complexity levels on materials to allow a user to pick a performance / quality ratio. Another possibility is that you have a fully HDR-enabled pipeline for top machines, rendering all objects using unclamped shaders, and a simpler pipeline for others; this can be implemented using schemes. The active scheme is typically controlled at a viewport level, and the active one defaults to `Default` .

@par
Format: scheme &lt;name&gt;<br> Example: scheme hdr<br> Default: scheme Default

<a name="lod_005findex"></a><a name="lod_005findex-1"></a>


## lod_index

Sets the level-of-detail (LOD) index this Technique belongs to.

@par
Format: lod_index &lt;number&gt;<br> NB Valid values are 0 (highest level of detail) to 65535, although this is unlikely. You should not leave gaps in the LOD indexes between Techniques.

@par
Example: lod_index 1

All techniques must belong to a LOD index, by default they all belong to index 0, i.e. the highest LOD. Increasing indexes denote lower levels of detail. You can (and often will) assign more than one technique to the same LOD index, what this means is that OGRE will pick the best technique of the ones listed at the same LOD index. For readability, it is advised that you list your techniques in order of LOD, then in order of preference, although the latter is the only prerequisite (OGRE determines which one is `best` by which one is listed first). You must always have at least one Technique at lod_index 0. The distance at which a LOD level is applied is determined by the lod_distances attribute of the containing material, See [lod_distances](#lod_005fdistances) for details.

@par
Default: lod_index 0

Techniques also contain one or more @ref Passes (and there must be at least one).

<a name="shadow_005fcaster_005fmaterial"></a><a name="shadow_005fcaster_005fmaterial-1"></a>


## shadow_caster_material

When using @ref Texture_002dbased-Shadows you can specify an alternate material to use when rendering the object using this material into the shadow texture. This is like a more advanced version of using shadow_caster_vertex_program, however note that for the moment you are expected to render the shadow in one pass, i.e. only the first pass is respected.

<a name="shadow_005freceiver_005fmaterial"></a><a name="shadow_005freceiver_005fmaterial-1"></a>


## shadow_receiver_material

When using @ref Texture_002dbased-Shadows you can specify an alternate material to use when performing the receiver shadow pass. Note that this explicit `receiver` pass is only done when you`re **not** using @ref Integrated-Texture-Shadows - i.e. the shadow rendering is done separately (either as a modulative pass, or a masked light pass). This is like a more advanced version of using shadow_receiver_vertex_program and shadow_receiver_fragment_program, however note that for the moment you are expected to render the shadow in one pass, i.e. only the first pass is respected.

<a name="gpu_005fvendor_005frule"></a><a name="gpu_005fdevice_005frule"></a><a name="gpu_005fvendor_005frule-and-gpu_005fdevice_005frule"></a>


## gpu_vendor_rule and gpu_device_rule

Although Ogre does a good job of detecting the capabilities of graphics cards and setting the supportability of techniques from that, occasionally card-specific behaviour exists which is not necessarily detectable and you may want to ensure that your materials go down a particular path to either use or avoid that behaviour. This is what these rules are for - you can specify matching rules so that a technique will be considered supportable only on cards from a particular vendor, or which match a device name pattern, or will be considered supported only if they **don`t** fulfil such matches. The format of the rules are as follows:

@par
gpu_vendor_rule &lt;include\|exclude&gt; &lt;vendor_name&gt;<br> gpu_device_rule &lt;include\|exclude&gt; &lt;device_pattern&gt; [case_sensitive]

An `include` rule means that the technique will only be supported if one of the include rules is matched (if no include rules are provided, anything will pass). An `exclude` rules means that the technique is considered unsupported if any of the exclude rules are matched. You can provide as many rules as you like, although &lt;vendor_name&gt; and &lt;device_pattern&gt; must obviously be unique. The valid list of &lt;vendor_name&gt; values is currently `nvidia` , `ati` , `intel` , `s3` , `matrox` and `3dlabs` . &lt;device_pattern&gt; can be any string, and you can use wildcards ( `\*` ) if you need to match variants. Here's an example:

@par
gpu_vendor_rule include nvidia<br> gpu_vendor_rule include intel<br> gpu_device_rule exclude \*950\*

These rules, if all included in one technique, will mean that the technique will only be considered supported on graphics cards made by NVIDIA and Intel, and so long as the device name doesn`t have `950` in it.

Note that these rules can only mark a technique `unsupported` when it would otherwise be considered `supported` judging by the hardware capabilities. Even if a technique passes these rules, it is still subject to the usual hardware support tests.


## Passes {#Passes}

A pass is a single render of the geometry in question; a single call to the rendering API with a certain set of rendering properties. A technique can have between one and 16 passes, although clearly the more passes you use, the more expensive the technique will be to render.

To help clearly identify what each pass is used for, the pass can be named but its optional. Passes not named within the script will take on a name that is the pass index number. For example: the first pass in a technique is index 0 so its name would be "0" if it was not given a name in the script. The pass name must be unique within the technique or else the final pass is the resulting merge of all passes with the same name in the technique. A warning message is posted in the Ogre.log if this occurs. Named passes can help when inheriting a material and modifying an existing pass: (See @ref Script-Inheritance)

Passes have a set of global attributes (described below) and optionally
- zero or more nested texture_unit entries (See @ref Texture-Units)
- references to shader programs (See @ref Using-Vertex_002fGeometry_002fFragment-Programs-in-a-Pass)
- additional instructions for the RTSS (See @ref rtss_custom_mat)

Here are the attributes you can use in a `pass` section of a .material script:

-   [ambient](#ambient)
-   [diffuse](#diffuse)
-   [specular](#specular)
-   [emissive](#emissive)
-   [scene_blend](#scene_005fblend)
-   [separate_scene_blend](#separate_005fscene_005fblend)
-   [scene_blend_op](#scene_005fblend_005fop)
-   [separate_scene_blend_op](#separate_005fscene_005fblend_005fop)
-   [depth_check](#depth_005fcheck)
-   [depth_write](#depth_005fwrite)
-   [depth_func](#depth_005ffunc)
-   [depth_bias](#depth_005fbias)
-   [iteration_depth_bias](#iteration_005fdepth_005fbias)
-   [alpha_rejection](#alpha_005frejection)
-   [alpha_to_coverage](#alpha_005fto_005fcoverage)
-   [light_scissor](#light_005fscissor)
-   [light_clip_planes](#light_005fclip_005fplanes)
-   [illumination_stage](#illumination_005fstage)
-   [transparent_sorting](#transparent_005fsorting)
-   [normalise_normals](#normalise_005fnormals)
-   [cull_hardware](#cull_005fhardware)
-   [cull_software](#cull_005fsoftware)
-   [lighting](#lighting)
-   [shading](#shading)
-   [polygon_mode](#polygon_005fmode)
-   [polygon_mode_overrideable](#polygon_005fmode_005foverrideable)
-   [fog_override](#fog_005foverride)
-   [colour_write](#colour_005fwrite)
-   [max_lights](#max_005flights)
-   [start_light](#start_005flight)
-   [iteration](#iteration)
-   [point_size](#point_005fsize)
-   [point_sprites](#point_005fsprites)
-   [point_size_attenuation](#point_005fsize_005fattenuation)
-   [point_size_min](#point_005fsize_005fmin)
-   [point_size_max](#point_005fsize_005fmax)
-   [line_width](#line_width)

<a name="Attribute-Descriptions"></a>


## Attribute Descriptions

<a name="ambient"></a><a name="ambient-1"></a>


## ambient

Sets the ambient colour reflectance properties of this pass.

@par
Format: ambient (&lt;red&gt; &lt;green&gt; &lt;blue&gt; [&lt;alpha&gt;]\| vertexcolour)<br> NB valid colour values are between 0.0 and 1.0.

@copydetails Ogre::Pass::setAmbient
@shaderparam

@par
Example: ambient 0.0 0.8 0.0
@par
Default: ambient 1.0 1.0 1.0 1.0

<a name="diffuse"></a><a name="diffuse-1"></a>


## diffuse

Sets the diffuse colour reflectance properties of this pass.
@par
Format: diffuse (&lt;red&gt; &lt;green&gt; &lt;blue&gt; [&lt;alpha&gt;]\| vertexcolour)<br> NB valid colour values are between 0.0 and 1.0.

@copydetails Ogre::Pass::setDiffuse
@shaderparam

@par
Example: diffuse 1.0 0.5 0.5
@par
Default: diffuse 1.0 1.0 1.0 1.0

<a name="specular"></a><a name="specular-1"></a>


## specular

Sets the specular colour reflectance properties of this pass.
@par
Format: specular (&lt;red&gt; &lt;green&gt; &lt;blue&gt; [&lt;alpha&gt;]\| vertexcolour) &lt;shininess&gt;<br> NB valid colour values are between 0.0 and 1.0. Shininess can be any value greater than 0.

This property determines how much specular light (highlights from instances of the Light class in the scene) is reflected. The default is to reflect no specular light. The colour of the specular highlights is determined by the colour parameters, and the size of the highlights by the separate shininess parameter.
It is also possible to make the specular reflectance track the vertex colour as defined in
the mesh instead of the colour values.

@copydetails Ogre::Pass::setShininess
@shaderparam

@par
Example: specular 1.0 1.0 1.0 12.5

@par
Default: specular 0.0 0.0 0.0 0.0 0.0

<a name="emissive"></a><a name="emissive-1"></a>


## emissive

Sets the amount of self-illumination an object has.

@par
Format: emissive (&lt;red&gt; &lt;green&gt; &lt;blue&gt; [&lt;alpha&gt;]\| vertexcolour)<br> NB valid colour values are between 0.0 and 1.0.

Unlike the name suggests, this object doesn`t act as a light source for other objects in the scene (if you want it to, you have to create a light which is centered on the object).
@copydetails Ogre::Pass::setSelfIllumination
@shaderparam

@par
Example: emissive 1.0 0.0 0.0
@par
Default: emissive 0.0 0.0 0.0 0.0

<a name="scene_005fblend"></a><a name="scene_005fblend-1"></a>


## scene_blend

Sets the kind of blending this pass has with the existing contents of the scene.

Whereas the texture blending operations seen in the texture_unit entries are concerned with blending between texture layers, this blending is about combining the output of this pass as a whole with the existing contents of the rendering target. This blending therefore allows object transparency and other special effects.

There are 2 formats, one using predefined blend types, the other allowing a roll-your-own approach using source and destination factors.
@par
Format1: scene_blend &lt;blend_type&gt;
@par
Example: scene_blend add

This is the simpler form, where the most commonly used blending modes are enumerated using a single parameter.

@param blend_type
<dl compact="compact">
<dt>add</dt>
<dd>@copybrief Ogre::SBT_ADD

Equivalent to `scene_blend one one` .</dd>
<dt>modulate</dt>
<dd>@copybrief Ogre::SBT_MODULATE

Equivalent to `scene_blend dest_colour zero` .</dd>
<dt>colour_blend</dt>
<dd>@copybrief Ogre::SBT_TRANSPARENT_COLOUR

Equivalent to `scene_blend src_colour one_minus_src_colour` </dd>
<dt>alpha_blend</dt>
<dd>@copybrief Ogre::SBT_TRANSPARENT_ALPHA

Equivalent to `scene_blend src_alpha one_minus_src_alpha` </dd>
</dl>

@par
Format2: scene_blend &lt;sourceFactor&gt; &lt;destFactor&gt;

@copydetails Ogre::Pass::setSceneBlending(const SceneBlendFactor, const SceneBlendFactor)

Valid values for both parameters are one of Ogre::SceneBlendFactor without the `SBF_` prefix. E.g. `SBF_DEST_COLOUR` becomes `dest_colour` .

@par
Example: scene_blend one one_minus_dest_alpha

@par
Default: scene_blend one zero (opaque)

Also see [separate_scene_blend](#separate_005fscene_005fblend).

<a name="separate_005fscene_005fblend"></a><a name="separate_005fscene_005fblend-1"></a>


## separate_scene_blend

This option operates in exactly the same way as [scene_blend](#scene_005fblend), except that it allows you to specify the operations to perform between the rendered pixel and the frame buffer separately for colour and alpha components. By nature this option is only useful when rendering to targets which have an alpha channel which you`ll use for later processing, such as a render texture.
@par
Format1: separate_scene_blend &lt;simple_colour_blend&gt; &lt;simple_alpha_blend&gt;
@par
Example: separate_scene_blend add modulate

This example would add colour components but multiply alpha components. The blend modes available are as in [scene_blend](#scene_005fblend). The more advanced form is also available:
@par
Format2: separate_scene_blend &lt;colour_src_factor&gt; &lt;colour_dest_factor&gt; &lt;alpha_src_factor&gt; &lt;alpha_dest_factor&gt;
@par
Example: separate_scene_blend one one_minus_dest_alpha one one

Again the options available in the second format are the same as those in the second format of [scene_blend](#scene_005fblend).

<a name="scene_005fblend_005fop"></a><a name="scene_005fblend_005fop-1"></a>


## scene_blend_op

This directive changes the operation which is applied between the two components of the scene blending equation

@par
Format: scene_blend_op &lt;op&gt;

@copydoc Ogre::Pass::setSceneBlendingOperation
You may change this to `add` , `subtract` , `reverse_subtract` , `min` or `max` .

<a name="separate_005fscene_005fblend_005fop"></a><a name="separate_005fscene_005fblend_005fop-1"></a>


## separate_scene_blend_op

This directive is as scene_blend_op, except that you can set the operation for colour and alpha separately.
@par
Format: separate_scene_blend_op &lt;colourOp&gt; &lt;alphaOp&gt; Default: separate_scene_blend_op add add

<a name="depth_005fcheck"></a><a name="depth_005fcheck-1"></a>


## depth_check

Sets whether or not this pass renders with depth-buffer checking on or not.
@par
Format: depth_check &lt;on\|off&gt;

@copydetails Ogre::Pass::setDepthCheckEnabled

Default: depth_check on

<a name="depth_005fwrite"></a><a name="depth_005fwrite-1"></a>


## depth_write

Sets whether or not this pass renders with depth-buffer writing on or not.

@par
Format: depth_write &lt;on\|off&gt;

@copydetails Ogre::Pass::setDepthWriteEnabled

@par
Default: depth_write on

<a name="depth_005ffunc"></a><a name="depth_005ffunc-1"></a>


## depth_func

Sets the function used to compare depth values when depth checking is on.
@par
Format: depth_func &lt;func&gt;

@copydetails Ogre::Pass::setDepthFunction

@param func one of Ogre::CompareFunction without the `CMPF_` prefix. E.g. `CMPF_LESS_EQUAL` becomes `less_equal` .

@par
Default: depth_func less_equal

<a name="depth_005fbias"></a><a name="depth_005fbias-1"></a>


## depth_bias

Sets the bias applied to the depth value of this pass.
@par
Format: depth_bias &lt;constantBias&gt; [&lt;slopeScaleBias&gt;]

@copydetails Ogre::Pass::setDepthBias

Also see [iteration_depth_bias](#iteration_005fdepth_005fbias)

<a name="iteration_005fdepth_005fbias"></a><a name="iteration_005fdepth_005fbias-1"></a>


## iteration_depth_bias

Sets an additional bias derived from the number of times a given pass has been iterated. Operates just like [depth_bias](#depth_005fbias) except that it applies an additional bias factor to the base depth_bias value, multiplying the provided value by the number of times this pass has been iterated before, through one of the [iteration](#iteration) variants. So the first time the pass will get the depth_bias value, the second time it will get depth_bias + iteration_depth_bias, the third time it will get depth_bias + iteration_depth_bias \* 2, and so on. The default is zero.
@par
Format: iteration_depth_bias &lt;bias_per_iteration&gt;

<a name="alpha_005frejection"></a><a name="alpha_005frejection-1"></a>


## alpha_rejection

Sets the way the pass will have use alpha to totally reject pixels from the pipeline.
@par
Format: alpha_rejection &lt;function&gt; &lt;value&gt;
@par
Example: alpha_rejection greater_equal 128

The function parameter can be any of the options listed in the material depth_function attribute. The value parameter can theoretically be any value between 0 and 255, but is best limited to 0 or 128 for hardware compatibility.

@ffp_rtss_only

@par
Default: alpha_rejection always_pass

<a name="alpha_005fto_005fcoverage"></a><a name="alpha_005fto_005fcoverage-1"></a>


## alpha_to_coverage

Sets whether this pass will use `alpha to coverage` ,

@par
Format: alpha_to_coverage &lt;on\|off&gt;

@copydetails Ogre::Pass::setAlphaToCoverageEnabled

@par
Default: alpha_to_coverage off <a name="light_005fscissor"></a>

<a name="light_005fscissor-1"></a>


## light_scissor

Sets whether when rendering this pass, rendering will be limited to a screen-space scissor rectangle representing the coverage of the light(s) being used in this pass.
@par
Format: light_scissor &lt;on\|off&gt;
@par
Default: light_scissor off

@copydetails Ogre::Pass::setLightScissoringEnabled

<a name="light_005fclip_005fplanes"></a><a name="light_005fclip_005fplanes-1"></a>


## light_clip_planes

Sets whether when rendering this pass, triangle setup will be limited to clipping volume covered by the light.
@par
Format: light_clip_planes &lt;on\|off&gt;
@par
Default: light_clip_planes off

@copydetails Ogre::Pass::setLightClipPlanesEnabled

@see @ref Integrated-Texture-Shadows


## illumination_stage {#illumination_005fstage}

@copydetails Ogre::Pass::setIlluminationStage

@par
Format: illumination_stage &lt;ambient\|per_light\|decal&gt; Default: none (autodetect)

<a name="normalise_005fnormals"></a><a name="normalise_005fnormals-1"></a>


## normalise_normals

Sets whether or not this pass renders with all vertex normals being automatically re-normalised.<br>
@par
Format: normalise_normals &lt;on\|off&gt;

@copydetails Ogre::Pass::setNormaliseNormals

@par
Default: normalise_normals off

<a name="transparent_005fsorting"></a><a name="transparent_005fsorting-1"></a>


## transparent_sorting

Sets if transparent textures should be sorted by depth or not.
@par
Format: transparent_sorting &lt;on\|off\|force&gt;

By default all transparent materials are sorted such that renderables furthest away from the camera are rendered first. This is usually the desired behaviour but in certain cases this depth sorting may be unnecessary and undesirable. If for example it is necessary to ensure the rendering order does not change from one frame to the next. In this case you could set the value to `off` to prevent sorting.

You can also use the keyword `force` to force transparent sorting on, regardless of other circumstances. Usually sorting is only used when the pass is also transparent, and has a depth write or read which indicates it cannot reliably render without sorting. By using `force` , you tell OGRE to sort this pass no matter what other circumstances are present.
@par
Default: transparent_sorting on

<a name="cull_005fhardware"></a><a name="cull_005fhardware-1"></a>


## cull_hardware

Sets the hardware culling mode for this pass.
@par
Format: cull_hardware &lt;clockwise\|anticlockwise\|none&gt;

@copydetails Ogre::Pass::setCullingMode

@par
Default: cull_hardware clockwise<br> NB this is the same as OpenGL's default but the opposite of Direct3D's default (because Ogre uses a right-handed coordinate system like OpenGL).

<a name="cull_005fsoftware"></a><a name="cull_005fsoftware-1"></a>


## cull_software

Sets the software culling mode for this pass.
@par
Format: cull_software &lt;back\|front\|none&gt;

@copydetails Ogre::Pass::setManualCullingMode

@par
Default: cull_software back

<a name="lighting"></a><a name="lighting-1"></a>


## lighting

Sets whether or not dynamic lighting is turned on for this pass or not.

@par
Format: lighting &lt;on\|off&gt;

@copydetails Ogre::Pass::setLightingEnabled
@par
Default: lighting on

<a name="shading"></a><a name="shading-1"></a>


## shading

Sets the kind of shading which should be used for representing dynamic lighting for this pass.
@par
Format: shading &lt;mode&gt;

@copydetails Ogre::Pass::setShadingMode

@param mode one of Ogre::ShadeOptions without the `SO_` prefix. E.g. `SO_FLAT` becomes `flat` .

@par
Default: shading gouraud

<a name="polygon_005fmode"></a><a name="polygon_005fmode-1"></a>


## polygon_mode

@copydetails Ogre::Pass::setPolygonMode

@par
Format: polygon_mode &lt;solid\|wireframe\|points&gt;

@param mode one of Ogre::PolygonMode without the `PM_` prefix. E.g. `PM_SOLID` becomes `solid` .

@par
Default: polygon_mode solid

<a name="polygon_005fmode_005foverrideable"></a><a name="polygon_005fmode_005foverrideable-1"></a>


## polygon_mode_overrideable

Sets whether or not the [polygon_mode](#polygon_005fmode) set on this pass can be downgraded by the camera

@par
Format: polygon_mode_overrideable &lt;override&gt;

@copydetails Ogre::Pass::setPolygonModeOverrideable

<a name="fog_005foverride"></a><a name="fog_005foverride-1"></a>


## fog_override

Tells the pass whether it should override the scene fog settings, and enforce it's own. Very useful for things that you don`t want to be affected by fog when the rest of the scene is fogged, or vice versa.
@par
Format: fog_override &lt;override?&gt; [&lt;type&gt; &lt;colour&gt; &lt;density&gt; &lt;start&gt; &lt;end&gt;]
@par
Default: fog_override false

If you specify `true` for the first parameter and you supply the rest of the parameters, you are telling the pass to use these fog settings in preference to the scene settings, whatever they might be. If you specify `true` but provide no further parameters, you are telling this pass to never use fogging no matter what the scene says.

@param type **none** = No fog, equivalent of just using `fog_override true` <br> **linear** = Linear fog from the &lt;start&gt; and &lt;end&gt; distances<br> **exp** = Fog increases exponentially from the camera (fog = 1/e^(distance \* density)), use &lt;density&gt; param to control it<br> **exp2** = Fog increases at the square of FOG_EXP, i.e. even quicker (fog = 1/e^(distance \* density)^2), use &lt;density&gt; param to control it

@param colour Sequence of 3 floating point values from 0 to 1 indicating the red, green and blue intensities

@param density The density parameter used in the `exp` or `exp2` fog types. Not used in linear mode but param must still be there as a placeholder

@param start The start distance from the camera of linear fog. Must still be present in other modes, even though it is not used.

@param end The end distance from the camera of linear fog. Must still be present in other modes, even though it is not used.

@par
Example: fog_override true exp 1 1 1 0.002 100 10000

<a name="colour_005fwrite"></a><a name="colour_005fwrite-1"></a>


## colour_write

Sets whether this pass renders with colour writing on or not. Alternatively, it can also be used to enable/disable colour writing specific channels.
In the second format, the parameters are in the red, green, blue, alpha order.

@par
Format 1: colour_write &lt;on\|off&gt;
@par
Format 2: colour_write &lt;on\|off&gt; &lt;on\|off&gt; &lt;on\|off&gt; &lt;on\|off&gt;

@copydetails Ogre::Pass::setColourWriteEnabled

@par
Default: colour_write on

<a name="colour_005fmask"></a><a name="colour_005fmask-1"></a>


## start_light

Sets the first light which will be considered for use with this pass.
@par
Format: start_light &lt;number&gt;

@copydetails Ogre::Pass::setStartLight

@par
Default: start_light 0

<a name="max_005flights"></a><a name="max_005flights-1"></a>


## max_lights

Sets the maximum number of lights which will be considered for use with this pass.
@par
Format: max_lights &lt;number&gt;

The maximum number of lights which can be used when rendering fixed-function materials is set by the rendering system, and is typically set at 8. When you are using the programmable pipeline (See [Using Vertex/Geometry/Fragment Programs in a Pass](@ref Using-Vertex_002fGeometry_002fFragment-Programs-in-a-Pass)) this limit is dependent on the program you are running, or, if you use `iteration once_per_light` or a variant (See @ref iteration), it effectively only bounded by the number of passes you are willing to use. If you are not using pass iteration, the light limit applies once for this pass. If you are using pass iteration, the light limit applies across all iterations of this pass - for example if you have 12 lights in range with an `iteration once_per_light` setup but your max_lights is set to 4 for that pass, the pass will only iterate 4 times.
@par
Default: max_lights 8


## iteration {#iteration}

Sets whether or not this pass is iterated, i.e. issued more than once.
@par
Format 1: iteration &lt;once \| once_per_light&gt; [lightType] Format 2: iteration &lt;number&gt; [&lt;per_light&gt; [lightType]]
@par
Format 3: iteration &lt;number&gt; [&lt;per_n_lights&gt; &lt;num_lights&gt; [lightType]] Examples:

<dl compact="compact">
<dt>iteration once</dt> <dd>

The pass is only executed once which is the default behaviour.

</dd> <dt>iteration once_per_light point</dt> <dd>

The pass is executed once for each point light.

</dd> <dt>iteration 5</dt> <dd>

The render state for the pass will be setup and then the draw call will execute 5 times.

</dd> <dt>iteration 5 per_light point</dt> <dd>

The render state for the pass will be setup and then the draw call will execute 5 times. This will be done for each point light.

</dd> <dt>iteration 1 per_n_lights 2 point</dt> <dd>

The render state for the pass will be setup and the draw call executed once for every 2 lights.

</dd> </dl>

By default, passes are only issued once. However, if you use the programmable pipeline, or you wish to exceed the normal limits on the number of lights which are supported, you might want to use the once_per_light option. In this case, only light index 0 is ever used, and the pass is issued multiple times, each time with a different light in light index 0. Clearly this will make the pass more expensive, but it may be the only way to achieve certain effects such as per-pixel lighting effects which take into account 1..n lights.

Using a number instead of "once" instructs the pass to iterate more than once after the render state is setup. The render state is not changed after the initial setup so repeated draw calls are very fast and ideal for passes using programmable shaders that must iterate more than once with the same render state i.e. shaders that do fur, motion blur, special filtering.

If you use once_per_light, you should also add an ambient pass to the technique before this pass, otherwise when no lights are in range of this object it will not get rendered at all; this is important even when you have no ambient light in the scene, because you would still want the objects silhouette to appear.

The lightType parameter to the attribute only applies if you use once_per_light, per_light, or per_n_lights and restricts the pass to being run for lights of a single type (either `point` , `directional` or `spot` ). In the example, the pass will be run once per point light. This can be useful because when you `re writing a vertex / fragment program it is a lot easier if you can assume the kind of lights you` ll be dealing with. However at least point and directional lights can be dealt with in one way.  Default: iteration once

<a name="fur_005fexample"></a>

Example: Simple Fur shader material script that uses a second pass with 10 iterations to grow the fur:

```cpp
// GLSL simple Fur
vertex_program GLSLDemo/FurVS glsl
{
    source fur.vert
    default_params
    {
        param_named_auto lightPosition light_position_object_space 0
        param_named_auto eyePosition camera_position_object_space
        param_named_auto passNumber pass_number
        param_named_auto multiPassNumber pass_iteration_number
        param_named furLength float 0.15
    }
}

fragment_program GLSLDemo/FurFS glsl
{
    source fur.frag
    default_params
    {
        param_named Ka float 0.2
        param_named Kd float 0.5
        param_named Ks float 0.0
        param_named furTU int 0
    }
}

material Fur
{
    technique GLSL
    {
        pass base_coat
        {
            ambient 0.7 0.7 0.7
            diffuse 0.5 0.8 0.5
            specular 1.0 1.0 1.0 1.5

            vertex_program_ref GLSLDemo/FurVS
            {
            }

            fragment_program_ref GLSLDemo/FurFS
            {
            }

            texture_unit
            {
                texture Fur.tga
                tex_coord_set 0
                filtering trilinear
            }
        }

        pass grow_fur
        {
            ambient 0.7 0.7 0.7
            diffuse 0.8 1.0 0.8
            specular 1.0 1.0 1.0 64
            depth_write off

            scene_blend src_alpha one
            iteration 10

            vertex_program_ref GLSLDemo/FurVS
            {
            }

            fragment_program_ref GLSLDemo/FurFS
            {
            }

            texture_unit
            {
                texture Fur.tga
                tex_coord_set 0
                filtering trilinear
            }
        }
    }
}
```

@note use gpu program auto parameters [pass_number](#pass_005fnumber) and [pass_iteration_number](#pass_005fiteration_005fnumber) to tell the vertex, geometry or fragment program the pass number and iteration number.

<a name="point_005fsize"></a><a name="point_005fsize-1"></a>


## point_size

@copydetails Ogre::Pass::setPointSize

@par
Format: point_size &lt;size&gt; Default: point_size 1.0

@ffp_rtss_only

<a name="point_005fsprites"></a><a name="point_005fsprites-1"></a>


## point_sprites

@copydetails Ogre::Pass::setPointSpritesEnabled

@par
Format: point_sprites &lt;on\|off&gt; Default: point_sprites off

<a name="point_005fsize_005fattenuation"></a><a name="point_005fsize_005fattenuation-1"></a>


## point_size_attenuation

Defines whether point size is attenuated with view space distance, and in what fashion.

@par
Format: point_size_attenuation &lt;enabled&gt; [constant linear quadratic] Default: point_size_attenuation off

@copydetails Ogre::Pass::setPointAttenuation

@ffp_rtss_only

<a name="point_005fsize_005fmin"></a><a name="point_005fsize_005fmin-1"></a>


## point_size_min

Sets the minimum point size after attenuation ([point_size_attenuation](#point_005fsize_005fattenuation)). For details on the size metrics, See [point_size](#point_005fsize).
@par
Format: point_size_min &lt;size&gt; Default: point_size_min 0

<a name="point_005fsize_005fmax"></a><a name="point_005fsize_005fmax-1"></a>


## point_size_max

Sets the maximum point size after attenuation ([point_size_attenuation](#point_005fsize_005fattenuation)). For details on the size metrics, See [point_size](#point_005fsize). A value of 0 means the maximum is set to the same as the max size reported by the current card.
@par
Format: point_size_max &lt;size&gt; Default: point_size_max 0

<a name="line_width"></a>


## line_width

@copydetails Ogre::Pass::setLineWidth

@par
Format: line_width &lt;width&gt;
@par
Default: line_width 1


## Texture Units {#Texture-Units}

Here are the attributes you can use in a `texture_unit` section of a .material script:

<a name="Available-Texture-Layer-Attributes"></a>


## Available Texture Layer Attributes

-   [texture_alias](#texture_005falias)
-   [texture](#texture)
-   [anim_texture](#anim_005ftexture)
-   [cubic_texture](#cubic_005ftexture)
-   [tex_coord_set](#tex_005fcoord_005fset)
-   [colour_op](#colour_005fop)
-   [colour_op_ex](#colour_005fop_005fex)
-   [colour_op_multipass_fallback](#colour_005fop_005fmultipass_005ffallback)
-   [alpha_op_ex](#alpha_005fop_005fex)
-   [env_map](#env_005fmap)
-   [scroll](#scroll)
-   [scroll_anim](#scroll_005fanim)
-   [rotate](#rotate)
-   [rotate_anim](#rotate_005fanim)
-   [scale](#scale)
-   [wave_xform](#wave_005fxform)
-   [transform](#transform)
-   [binding_type](#binding_005ftype)
-   [content_type](#content_005ftype)
-   [sampler_ref](#sampler_ref)

Additionally you can use all attributes of @ref Samplers directly to implicitly create a Ogre::Sampler contained in this TextureUnit.

You can also use a nested `texture_source` section in order to use a special add-in as a source of texture data, See @ref External-Texture-Sources for details.

<a name="Attribute-Descriptions-1"></a>


## Attribute Descriptions

<a name="texture_005falias"></a><a name="texture_005falias-1"></a>


## texture_alias

Sets the alias name for this texture unit.
@par
Format: texture_alias &lt;name&gt;
@par
Example: texture_alias NormalMap

Setting the texture alias name is useful if this material is to be inherited by other other materials and only the textures will be changed in the new material.(See @ref Texture-Aliases) Default: If a texture_unit has a name then the texture_alias defaults to the texture_unit name.

<a name="texture"></a><a name="texture-1"></a>


## texture

Sets the name of the static texture image this layer will use.
@par
Format: texture &lt;texturename&gt; [&lt;type&gt;] [unlimited \| numMipMaps] [alpha] [&lt;PixelFormat&gt;] [gamma]
@par
Example: texture funkywall.jpg

This setting is mutually exclusive with the anim_texture attribute. Note that the texture file cannot include spaces. Those of you Windows users who like spaces in filenames, please get over it and use underscores instead.

@param type
specify a the type of texture to create - the default is `2d` , but you can override this; here's the full list:
<dl compact="compact">
<dt>1d</dt> <dd>

A 1-dimensional texture; that is, a texture which is only 1 pixel high. These kinds of textures can be useful when you need to encode a function in a texture and use it as a simple lookup, perhaps in a fragment program. It is important that you use this setting when you use a fragment program which uses 1-dimensional texture coordinates, since GL requires you to use a texture type that matches (D3D will let you get away with it, but you ought to plan for cross-compatibility). Your texture widths should still be a power of 2 for best compatibility and performance.

</dd> <dt>2d</dt> <dd>

The default type which is assumed if you omit it, your texture has a width and a height, both of which should preferably be powers of 2, and if you can, make them square because this will look best on the most hardware. These can be addressed with 2D texture coordinates.

</dd> <dt>3d</dt> <dd>

A 3 dimensional texture i.e. volume texture. Your texture has a width, a height, both of which should be powers of 2, and has depth. These can be addressed with 3d texture coordinates i.e. through a pixel shader.

</dd> <dt>cubic</dt> <dd>

This texture is made up of 6 2D textures which are pasted around the inside of a cube. The base_name in this format is something like `skybox.jpg` , and the system will expect you to provide skybox_fr.jpg, skybox_bk.jpg, skybox_up.jpg, skybox_dn.jpg, skybox_lf.jpg, and skybox_rt.jpg for the individual faces.
Alternatively 1 cube texture can be used if supported by the texture format(DDS for example) and rendersystem. Can be addressed with 3D texture coordinates and are useful for cubic reflection maps and normal maps.
</dd> </dl>

@param numMipMaps
specify the number of mipmaps to generate for this texture. The default is `unlimited` which means mips down to 1x1 size are generated. You can specify a fixed number (even 0) if you like instead. Note that if you use the same texture in many material scripts, the number of mipmaps generated will conform to the number specified in the first texture_unit used to load the texture - so be consistent with your usage.

@param alpha @copydoc Ogre::Texture::setTreatLuminanceAsAlpha
Default: none

@param PixelFormat
specify the desired pixel format of the texture to create, which may be different to the pixel format of the texture file being loaded. Bear in mind that the final pixel format will be constrained by hardware capabilities so you may not get exactly what you ask for.
Names defined in Ogre::PixelFormat are valid values.

@param gamma
informs the renderer that you want the graphics hardware to perform gamma correction on the texture values as they are sampled for rendering. This is only applicable for textures which have 8-bit colour channels (e.g.PF_R8G8B8). Often, 8-bit per channel textures will be stored in gamma space in order to increase the precision of the darker colours (<http://en.wikipedia.org/wiki/Gamma_correction>) but this can throw out blending and filtering calculations since they assume linear space colour values. For the best quality shading, you may want to enable gamma correction so that the hardware converts the texture values to linear space for you automatically when sampling the texture, then the calculations in the pipeline can be done in a reliable linear colour space. When rendering to a final 8-bit per channel display, you`ll also want to convert back to gamma space which can be done in your shader (by raising to the power 1/2.2) or you can enable gamma correction on the texture being rendered to or the render window. Note that the `gamma` option on textures is applied on loading the texture so must be specified consistently if you use this texture in multiple places.

<a name="anim_005ftexture"></a><a name="anim_005ftexture-1"></a>


## anim_texture

Sets the images to be used in an animated texture layer. There are 2 formats, one for implicitly determined image names, one for explicitly named images.
@par
Format1 (short): anim_texture &lt;name&gt; &lt;numFrames&gt; &lt;duration&gt;

@copydetails Ogre::TextureUnitState::setAnimatedTextureName

@par
Example: anim_texture flame.jpg 5 2.5

@par
Format2 (long): anim_texture &lt;frame1&gt; &lt;frame2&gt; ... &lt;duration&gt;
@par
Example: anim_texture flamestart.jpg flamemore.png flameagain.jpg moreflame.jpg lastflame.tga 2.5

This sets up the same duration animation but from 5 separately named image files. The first format is more concise, but the second is provided if you cannot make your images conform to the naming standard required for it.
@par
Default: none

<a name="cubic_005ftexture"></a><a name="cubic_005ftexture-1"></a>


## cubic_texture

Sets the images used in a cubic texture, i.e. one made up of 6 individual images making up the faces of a cube or 1 cube texture if supported by the texture format(DDS for example) and rendersystem.. These kinds of textures are used for reflection maps (if hardware supports cubic reflection maps) or skyboxes. There are 2 formats, a brief format expecting image names of a particular format and a more flexible but longer format for arbitrarily named textures.
@par
Format1 (short): cubic_texture &lt;base_name&gt; &lt;combinedUVW\|separateUV&gt;

@deprecated use the format ' `texture <basename> cubic` ' instead

The base_name in this format is something like `skybox.jpg` , and the system will expect you to provide skybox_fr.jpg, skybox_bk.jpg, skybox_up.jpg, skybox_dn.jpg, skybox_lf.jpg, and skybox_rt.jpg for the individual faces.

@par
Format2 (long): cubic_texture &lt;front&gt; &lt;back&gt; &lt;left&gt; &lt;right&gt; &lt;up&gt; &lt;down&gt; &lt;combinedUVW\|separateUV&gt;

In this case each face is specified explicitly, incase you don`t want to conform to the image naming standards above. You can only use this for the separateUV version since the combinedUVW version requires a single texture name to be assigned to the combined 3D texture (see below).

In both cases the final parameter means the following:

<dl compact="compact">
<dt>separateUV</dt> <dd>

@deprecated Use real cubic textures due to hardware support

The 6 textures are kept separate but are all referenced by this single texture layer. One texture at a time is active (they are actually stored as 6 frames), and they are addressed using standard 2D UV coordinates.
</dd>
<dt>combinedUVW</dt> <dd>

The 6 textures are combined into a single `cubic` texture map which is then addressed using 3D texture coordinates.

</dd>
</dl>

<a name="binding_005ftype"></a><a name="binding_005ftype-1"></a>


## binding_type

@copydetails Ogre::TextureUnitState::setBindingType

@see @ref Vertex-Texture-Fetch

Format: binding_type &lt;vertex\|fragment&gt;
@par
Default: binding_type fragment

<a name="content_005ftype"></a>


## content_type

Tells this texture unit where it should get its content from. The default is to get texture content from a named texture, as defined with the [texture](#texture), [cubic_texture](#cubic_005ftexture), [anim_texture](#anim_005ftexture) attributes. However you can also pull texture information from other automated sources.

@par
Format: content_type &lt;type&gt; [&lt;compositorName&gt;] [&lt;textureName&gt;] [&lt;mrtIndex&gt;]

@param type
<dl compact="compact">
<dt>named</dt> <dd>

@copydoc Ogre::TextureUnitState::CONTENT_NAMED

</dd> <dt>shadow</dt> <dd>

This option allows you to pull in a shadow texture, and is only valid when you use texture shadows and one of the `custom sequence` shadowing types (See @ref Shadows). The shadow texture in question will be from the `n` th closest light that casts shadows, unless you use light-based pass iteration or the light_start option which may start the light index higher. When you use this option in multiple texture units within the same pass, each one references the next shadow texture. The shadow texture index is reset in the next pass, in case you want to take into account the same shadow textures again in another pass (e.g. a separate specular / gloss pass). By using this option, the correct light frustum projection is set up for you for use in fixed-function, if you use shaders just reference the texture_viewproj_matrix auto parameter in your shader.

</dd> <dt>compositor</dt> <dd>

@copydoc Ogre::TextureUnitState::CONTENT_COMPOSITOR This can be either in a render_scene directive inside a compositor script, or in a general pass in a viewport that has a compositor attached. Note that this is a reference only, meaning that it does not change the render order. You must make sure that the order is reasonable for what you are trying to achieve (for example, texture pooling might cause the referenced texture to be overwritten by something else by the time it is referenced).

</dd> </dl>

@copydetails Ogre::TextureUnitState::setCompositorReference

@par
Example: content_type compositor DepthCompositor OutputTexture

@par
Default: content_type named

<a name="tex_005fcoord_005fset"></a><a name="tex_005fcoord_005fset-1"></a>


## tex_coord_set

@copydoc Ogre::TextureUnitState::setTextureCoordSet

@par
Format: tex_coord_set &lt;set_num&gt;

@ffp_rtss_only

@par
Example: tex_coord_set 2
@par
Default: tex_coord_set 0

<a name="colour_005fop"></a><a name="colour_005fop-1"></a>


## colour_op

@ffp_rtss_only

Determines how the colour of this texture layer is combined with the one below it (or the lighting effect on the geometry if this is the first layer).
@par
Format: colour_op &lt;op&gt;

@copydetails Ogre::TextureUnitState::setColourOperation Without the `LBO_` prefix. E.g. `LBO_REPLACE` becomes `replace` .

@par
Default: colour_op modulate

<a name="colour_005fop_005fex"></a><a name="colour_005fop_005fex-1"></a>


## colour_op_ex

@ffp_rtss_only
@par
Format: colour_op_ex &lt;op&gt; &lt;source1&gt; &lt;source2&gt; [&lt;manualBlend&gt;] [&lt;arg1&gt;] [&lt;arg2&gt;]
@par
Example colour_op_ex add_signed src_manual src_current 0.5

@copydetails Ogre::TextureUnitState::setColourOperationEx

Each parameter can be one of Ogre::LayerBlendOperationEx or Ogre::LayerBlendSource without the prefix. E.g. `LBX_MODULATE_X4` becomes `modulate_x4` .

@par
Default: none (colour_op modulate)

<a name="colour_005fop_005fmultipass_005ffallback"></a><a name="colour_005fop_005fmultipass_005ffallback-1"></a>


## colour_op_multipass_fallback

Sets the multipass fallback operation for this layer, if you used colour_op_ex and not enough multitexturing hardware is available.
@par
Format: colour_op_multipass_fallback &lt;src_factor&gt; &lt;dest_factor&gt;
@par
Example: colour_op_multipass_fallback one one_minus_dest_alpha

@copydetails Ogre::TextureUnitState::setColourOpMultipassFallback

<a name="alpha_005fop_005fex"></a><a name="alpha_005fop_005fex-1"></a>


## alpha_op_ex

@ffp_rtss_only

@par
Format: alpha_op_ex &lt;op&gt; &lt;source1&gt; &lt;source2&gt; [&lt;manualBlend&gt;] [&lt;arg1&gt;] [&lt;arg2&gt;]

@copydetails Ogre::TextureUnitState::setAlphaOperation

<a name="env_005fmap"></a><a name="env_005fmap-1"></a>


## env_map

Turns on/off texture coordinate effect that makes this layer an environment map. @ffp_rtss_only
@par
Format: env_map &lt;off\|spherical\|planar\|cubic_reflection\|cubic_normal&gt;

Environment maps make an object look reflective by using automatic texture coordinate generation depending on the relationship between the objects vertices or normals and the eye.

<dl compact="compact">
<dt>spherical</dt> <dd>

A spherical environment map. Requires a single texture which is either a fish-eye lens view of the reflected scene, or some other texture which looks good as a spherical map (a texture of glossy highlights is popular especially in car sims). This effect is based on the relationship between the eye direction and the vertex normals of the object, so works best when there are a lot of gradually changing normals, i.e. curved objects.

</dd> <dt>planar</dt> <dd>

Similar to the spherical environment map, but the effect is based on the position of the vertices in the viewport rather than vertex normals. This effect is therefore useful for planar geometry (where a spherical env_map would not look good because the normals are all the same) or objects without normals.

</dd> <dt>cubic_reflection</dt> <dd>

A more advanced form of reflection mapping which uses a group of 6 textures making up the inside of a cube, each of which is a view if the scene down each axis. Works extremely well in all cases but has a higher technical requirement from the card than spherical mapping. Requires that you bind a [cubic_texture](#cubic_005ftexture) to this texture unit and use the `combinedUVW` option.

</dd> <dt>cubic_normal</dt> <dd>

Generates 3D texture coordinates containing the camera space normal vector from the normal information held in the vertex data. Again, full use of this feature requires a [cubic_texture](#cubic_005ftexture) with the `combinedUVW` option.

</dd> </dl>
@par
Default: env_map off

<a name="scroll"></a><a name="scroll-1"></a>


## scroll

@copybrief Ogre::TextureUnitState::setTextureScroll
@par
Format: scroll &lt;u&gt; &lt;v&gt;

@copydetails Ogre::TextureUnitState::setTextureScroll

@shaderparam

<a name="scroll_005fanim"></a><a name="scroll_005fanim-1"></a>


## scroll_anim

@copybrief Ogre::TextureUnitState::setScrollAnimation
@par
Format: scroll_anim &lt;uSpeed&gt; &lt;vSpeed&gt;

@copydetails Ogre::TextureUnitState::setScrollAnimation

@shaderparam
<a name="rotate"></a><a name="rotate-1"></a>


## rotate

@copybrief Ogre::TextureUnitState::setTextureRotate

@par
Format: rotate &lt;angle&gt;

@copydetails Ogre::TextureUnitState::setTextureRotate

@shaderparam

<a name="rotate_005fanim"></a><a name="rotate_005fanim-1"></a>


## rotate_anim

@copybrief Ogre::TextureUnitState::setRotateAnimation

@par
Format: rotate_anim &lt;speed&gt;

@copydetails Ogre::TextureUnitState::setRotateAnimation

@shaderparam

<a name="scale"></a><a name="scale-1"></a>


## scale

@copybrief Ogre::TextureUnitState::setTextureScale

@par
Format: scale &lt;uScale&gt; &lt;vScale&gt;

@copydetails Ogre::TextureUnitState::setTextureScale

@shaderparam

<a name="wave_005fxform"></a><a name="wave_005fxform-1"></a>


## wave_xform

@copybrief Ogre::TextureUnitState::setTransformAnimation

@par
Format: wave_xform &lt;ttype&gt; &lt;waveType&gt; &lt;base&gt; &lt;frequency&gt; &lt;phase&gt; &lt;amplitude&gt;
@par
Example: wave_xform scale_x sine 1.0 0.2 0.0 5.0

@copydetails Ogre::TextureUnitState::setTransformAnimation

ttype is one of
<dl compact="compact">
<dt>scroll_x</dt> <dd>

Animate the u scroll value

</dd> <dt>scroll_y</dt> <dd>

Animate the v scroll value

</dd> <dt>rotate</dt> <dd>

Animate the rotate value

</dd> <dt>scale_x</dt> <dd>

Animate the u scale value

</dd> <dt>scale_y</dt> <dd>

Animate the v scale value

</dd> </dl>

waveType is one of Ogre::WaveformType without the `WFT_` prefix. E.g. `WFT_SQUARE` becomes `square` .

@shaderparam

<a name="transform"></a><a name="transform-1"></a>


## transform

This attribute allows you to specify a static 4x4 transformation matrix for the texture unit, thus replacing the individual scroll, rotate and scale attributes mentioned above.
@par
Format: transform m00 m01 m02 m03 m10 m11 m12 m13 m20 m21 m22 m23 m30 m31 m32 m33

The indexes of the 4x4 matrix value above are expressed as m&lt;row&gt;&lt;col&gt;.

@shaderparam

<a name="sampler_ref"></a>


## sampler_ref

By default all texture units use a shared default Sampler object. This parameter allows you to explicitly set a different one.

@par
Format: sampler_ref &lt;name&gt;

@par
Example: sampler_ref mySampler


## Samplers {#Samplers}

Samplers allow you to quickly change the settings for all associated Textures. Typically you have many Textures but only a few sampling states in your application.

```cpp
sampler mySampler
{
    filtering bilinear
    max_anisotropy 16
}

...
    texture_unit
    {
        texture myTexture.dds
        sampler_ref mySampler
    }
...
```


## Available parameters

-   [filtering](#filtering)
-   [max_anisotropy](#max_005fanisotropy)
-   [tex_address_mode](#tex_005faddress_005fmode)
-   [tex_border_colour](#tex_005fborder_005fcolour)
-   [mipmap_bias](#mipmap_005fbias)
-   [compare_test](#compare_test)
-   [comp_func](#comp_func)

<a name="tex_005faddress_005fmode"></a><a name="tex_005faddress_005fmode-1"></a>


## tex_address_mode

Defines what happens when texture coordinates exceed 1.0 for this texture layer.You can use the simple format to specify the addressing mode for all 3 potential texture coordinates at once, or you can use the 2/3 parameter extended format to specify a different mode per texture coordinate.
@par
Simple Format: tex_address_mode &lt;uvw_mode&gt; <br> Extended Format: tex_address_mode &lt;u_mode&gt; &lt;v_mode&gt; [&lt;w_mode&gt;]

Valid values for both are one of Ogre::TextureAddressingMode without the `TAM_` prefix. E.g. `TAM_WRAP` becomes `wrap` .

@par
Default: tex_address_mode wrap

<a name="tex_005fborder_005fcolour"></a><a name="tex_005fborder_005fcolour-1"></a>


## tex_border_colour

Sets the border colour of border texture address mode (see [tex_address_mode](#tex_005faddress_005fmode)).
@par
Format: tex_border_colour &lt;red&gt; &lt;green&gt; &lt;blue&gt; [&lt;alpha&gt;]<br> NB valid colour values are between 0.0 and 1.0.
@par
Example: tex_border_colour 0.0 1.0 0.3
@par
Default: tex_border_colour 0.0 0.0 0.0 1.0

<a name="filtering"></a><a name="filtering-1"></a>


## filtering

Sets the type of texture filtering used when magnifying or minifying a texture. There are 2 formats to this attribute, the simple format where you simply specify the name of a predefined set of filtering options, and the complex format, where you individually set the minification, magnification, and mip filters yourself.


### Simple Format

With this format, you only need to provide a single parameter

@par
Format: filtering &lt;none\|bilinear\|trilinear\|anisotropic&gt;<br> Default: filtering bilinear

<dl compact="compact">
<dt>none</dt> <dd>
@copydoc Ogre::TFO_NONE
</dd>
<dt>bilinear</dt> <dd>
@copydoc Ogre::TFO_BILINEAR
</dd>
<dt>trilinear</dt> <dd>
@copydoc Ogre::TFO_TRILINEAR
</dd>
<dt>anisotropic</dt> <dd>
@copydoc Ogre::TFO_ANISOTROPIC
</dd> </dl>


### Complex Format

This format gives you complete control over the minification, magnification, and mip filters.

@par
Format: filtering &lt;minFilter&gt; &lt;magFilter&gt; &lt;mipFilter&gt;
@par
Default: filtering linear linear point

Each parameter can be one of Ogre::FilterOptions without the `FO_` prefix. E.g. `FO_LINEAR` becomes `linear` .

@copydetails Ogre::Sampler::setFiltering(FilterOptions,FilterOptions,FilterOptions)

<a name="max_005fanisotropy"></a><a name="max_005fanisotropy-1"></a>


## max_anisotropy

@copybrief Ogre::Sampler::setAnisotropy

@par
Format: max_anisotropy &lt;maxAniso&gt;<br> Default: max_anisotropy 1

@copydetails Ogre::Sampler::setAnisotropy

<a name="mipmap_005fbias"></a><a name="mipmap_005fbias-1"></a>


## mipmap_bias

@copydetails Ogre::Sampler::setMipmapBias

@par
Format: mipmap_bias &lt;value&gt;<br> Default: mipmap_bias 0

<a name="compare_test"></a>


## compare_test

@copydoc Ogre::Sampler::setCompareEnabled

@par
Format: compare_test on

@par
Default: compare_test off

<a name="comp_func"></a>


## comp_func

The comparison func to use when @c compare_test is enabled
@par
Format: comp_func &lt;func&gt;

@param func one of Ogre::CompareFunction without the `CMPF_` prefix. E.g. `CMPF_LESS_EQUAL` becomes `less_equal` .


## Declaring GPU Programs {#Declaring-Vertex_002fGeometry_002fFragment-Programs}

In order to use a vertex, geometry or fragment program in your materials (See [Using Vertex/Geometry/Fragment Programs in a Pass](@ref Using-Vertex_002fGeometry_002fFragment-Programs-in-a-Pass)), you first have to define them. A single program definition can be used by any number of materials, the only prerequisite is that a program must be defined before being referenced in the pass section of a material.

The definition of a program can either be embedded in the .material script itself (in which case it must precede any references to it in the script), or if you wish to use the same program across multiple .material files, you can define it in an external .program script. You define the program in exactly the same way whether you use a .program script or a .material script, the only difference is that all .program scripts are guaranteed to have been parsed before **all** .material scripts, so you can guarantee that your program has been defined before any .material script that might use it. Just like .material scripts, .program scripts will be read from any location which is on your resource path, and you can define many programs in a single script.

Vertex, geometry and fragment programs can be low-level (i.e. assembler code written to the specification of a given low level syntax such as vs_1_1 or arbfp1) or high-level such as DirectX9 HLSL, Open GL Shader Language, or nVidia's Cg language (See @ref High-level-Programs). High level languages give you a number of advantages, such as being able to write more intuitive code, and possibly being able to target multiple architectures in a single program (for example, the same Cg program might be able to be used in both D3D and GL, whilst the equivalent low-level programs would require separate techniques, each targeting a different API). High-level programs also allow you to use named parameters instead of simply indexed ones, although parameters are not defined here, they are used in the Pass.

Here is an example of a definition of a low-level vertex program:

```cpp
vertex_program myVertexProgram asm
{
    source myVertexProgram.asm
    syntax vs_1_1
}
```

As you can see, that's very simple, and defining a fragment or geometry program is exactly the same, just with vertex_program replaced with fragment_program or geometry_program, respectively. You give the program a name in the header, followed by the word `asm` to indicate that this is a low-level program. Inside the braces, you specify where the source is going to come from (and this is loaded from any of the resource locations as with other media), and also indicate the syntax being used. You might wonder why the syntax specification is required when many of the assembler syntaxes have a header identifying them anyway - well the reason is that the engine needs to know what syntax the program is in before reading it, because during compilation of the material, we want to skip programs which use an unsupportable syntax quickly, without loading the program first.

The current supported syntaxes are:

<dl compact="compact">
<dt>vs_1_1</dt> <dd>

This is one of the DirectX vertex shader assembler syntaxes. <br> Supported on cards from: ATI Radeon 8500, nVidia GeForce 3

</dd> <dt>vs_2_0</dt> <dd>

Another one of the DirectX vertex shader assembler syntaxes. <br> Supported on cards from: ATI Radeon 9600, nVidia GeForce FX 5 series

</dd> <dt>vs_2_x</dt> <dd>

Another one of the DirectX vertex shader assembler syntaxes. <br> Supported on cards from: ATI Radeon X series, nVidia GeForce FX 6 series

</dd> <dt>vs_3_0</dt> <dd>

Another one of the DirectX vertex shader assembler syntaxes. <br> Supported on cards from: ATI Radeon HD 2000+, nVidia GeForce FX 6 series

</dd> <dt>arbvp1</dt> <dd>

This is the OpenGL standard assembler format for vertex programs. It's roughly equivalent to DirectX vs_1_1.

</dd> <dt>vp20</dt> <dd>

This is an nVidia-specific OpenGL vertex shader syntax which is a superset of vs 1.1. ATI Radeon HD 2000+ also supports it.

</dd> <dt>vp30</dt> <dd>

Another nVidia-specific OpenGL vertex shader syntax. It is a superset of vs 2.0, which is supported on nVidia GeForce FX 5 series and higher. ATI Radeon HD 2000+ also supports it.

</dd> <dt>vp40</dt> <dd>

Another nVidia-specific OpenGL vertex shader syntax. It is a superset of vs 3.0, which is supported on nVidia GeForce FX 6 series and higher.

</dd> <dt>ps_1_1, ps_1_2, ps_1_3</dt> <dd>

DirectX pixel shader (i.e. fragment program) assembler syntax. <br> Supported on cards from: ATI Radeon 8500, nVidia GeForce 3 <br> @note for ATI 8500, 9000, 9100, 9200 hardware, this profile can also be used in OpenGL. The ATI 8500 to 9200 do not support arbfp1 but do support atifs extension in OpenGL which is very similar in function to ps_1_4 in DirectX. Ogre has a built in ps_1_x to atifs compiler that is automatically invoked when ps_1_x is used in OpenGL on ATI hardware.

</dd> <dt>ps_1_4</dt> <dd>

DirectX pixel shader (i.e. fragment program) assembler syntax. <br> Supported on cards from: ATI Radeon 8500, nVidia GeForce FX 5 series <br> @note for ATI 8500, 9000, 9100, 9200 hardware, this profile can also be used in OpenGL. The ATI 8500 to 9200 do not support arbfp1 but do support atifs extension in OpenGL which is very similar in function to ps_1_4 in DirectX. Ogre has a built in ps_1_x to atifs compiler that is automatically invoked when ps_1_x is used in OpenGL on ATI hardware.

</dd> <dt>ps_2_0</dt> <dd>

DirectX pixel shader (i.e. fragment program) assembler syntax. <br> Supported cards: ATI Radeon 9600, nVidia GeForce FX 5 series

</dd> <dt>ps_2_x</dt> <dd>

DirectX pixel shader (i.e. fragment program) assembler syntax. This is basically ps_2_0 with a higher number of instructions. <br> Supported cards: ATI Radeon X series, nVidia GeForce FX 6 series

</dd> <dt>ps_3_0</dt> <dd>

DirectX pixel shader (i.e. fragment program) assembler syntax. <br> Supported cards: ATI Radeon HD 2000+, nVidia GeForce FX6 series

</dd> <dt>ps_3_x</dt> <dd>

DirectX pixel shader (i.e. fragment program) assembler syntax. <br> Supported cards: nVidia GeForce FX7 series

</dd> <dt>arbfp1</dt> <dd>

This is the OpenGL standard assembler format for fragment programs. It's roughly equivalent to ps_2_0, which means that not all cards that support basic pixel shaders under DirectX support arbfp1 (for example neither the GeForce3 or GeForce4 support arbfp1, but they do support ps_1_1).

</dd> <dt>fp20</dt> <dd>

This is an nVidia-specific OpenGL fragment syntax which is a superset of ps 1.3. It allows you to use the `nvparse` format for basic fragment programs. It actually uses NV_texture_shader and NV_register_combiners to provide functionality equivalent to DirectX's ps_1_1 under GL, but only for nVidia cards. However, since ATI cards adopted arbfp1 a little earlier than nVidia, it is mainly nVidia cards like the GeForce3 and GeForce4 that this will be useful for. You can find more information about nvparse at <http://developer.nvidia.com/object/nvparse.html>.

</dd> <dt>fp30</dt> <dd>

Another nVidia-specific OpenGL fragment shader syntax. It is a superset of ps 2.0, which is supported on nVidia GeForce FX 5 series and higher. ATI Radeon HD 2000+ also supports it.

</dd> <dt>fp40</dt> <dd>

Another nVidia-specific OpenGL fragment shader syntax. It is a superset of ps 3.0, which is supported on nVidia GeForce FX 6 series and higher.

</dd> <dt>gpu_gp, gp4_gp</dt> <dd>

An nVidia-specific OpenGL geometry shader syntax. <br> Supported cards: nVidia GeForce FX8 series

</dd> <dt>glsles</dt> <dd>

OpenGL Shading Language for Embedded Systems. It is a variant of GLSL, streamlined for low power devices. Supported cards: PowerVR SGX series

</dd> </dl>

You can get a definitive list of the syntaxes supported by the current card by calling GpuProgramManager::getSingleton().getSupportedSyntax().


## Specifying Named Constants for Assembler Shaders {#Specifying-Named-Constants-for-Assembler-Shaders}

Assembler shaders don`t have named constants (also called uniform parameters) because the language does not support them - however if you for example decided to precompile your shaders from a high-level language down to assembler for performance or obscurity, you might still want to use the named parameters. Well, you actually can - GpuNamedConstants which contains the named parameter mappings has a `save` method which you can use to write this data to disk, where you can reference it later using the manual_named_constants directive inside your assembler program declaration, e.g.

```cpp
vertex_program myVertexProgram asm
{
    source myVertexProgram.asm
    syntax vs_1_1
    manual_named_constants myVertexProgram.constants
}
```

In this case myVertexProgram.constants has been created by calling highLevelGpuProgram-&gt;getNamedConstants().save("myVertexProgram.constants"); sometime earlier as preparation, from the original high-level program. Once you`ve used this directive, you can use named parameters here even though the assembler program itself has no knowledge of them.


## Default Program Parameters {#Default-Program-Parameters}

While defining a vertex, geometry or fragment program, you can also specify the default parameters to be used for materials which use it, unless they specifically override them. You do this by including a nested `default_params` section, like so:

```cpp
vertex_program Ogre/CelShadingVP cg
{
    source Example_CelShading.cg
    entry_point main_vp
    profiles vs_1_1 arbvp1

    default_params
    {
        param_named_auto lightPosition light_position_object_space 0
        param_named_auto eyePosition camera_position_object_space
        param_named_auto worldViewProj worldviewproj_matrix
        param_named shininess float 10
    }
}
```

The syntax of the parameter definition is exactly the same as when you define parameters when using programs, See @ref Program-Parameter-Specification. Defining default parameters allows you to avoid rebinding common parameters repeatedly (clearly in the above example, all but `shininess` are unlikely to change between uses of the program) which makes your material declarations shorter.


## Declaring Shared Parameters {#Declaring-Shared-Parameters}

Often, not every parameter you want to pass to a shader is unique to that program, and perhaps you want to give the same value to a number of different programs, and a number of different materials using that program. Shared parameter sets allow you to define a `holding area` for shared parameters that can then be referenced when you need them in particular shaders, while keeping the definition of that value in one place. To define a set of shared parameters, you do this:

```cpp
shared_params YourSharedParamsName
{
    shared_param_named mySharedParam1 float4 0.1 0.2 0.3 0.4
    ...
}
```

As you can see, you need to use the keyword `shared_params` and follow it with the name that you will use to identify these shared parameters. Inside the curly braces, you can define one parameter per line, in a way which is very similar to the [param_named](#param_005fnamed) syntax. The definition of these lines is:
@par
Format: shared_param_name &lt;param_name&gt; &lt;param_type&gt; [&lt;[array_size]&gt;] [&lt;initial_values&gt;]

@param param_name must be unique within the set
@param param_type can be any one of float, float2, float3, float4, int, int2, int3, int4, matrix2x2, matrix2x3, matrix2x4, matrix3x2, matrix3x3, matrix3x4, matrix4x2, matrix4x3 and matrix4x4.
@param array_size allows you to define arrays of param_type should you wish, and if present must be a number enclosed in square brackets (and note, must be separated from the param_type with whitespace).
@param initial_values If you wish, you can also initialise the parameters by providing a list of values.

Once you have defined the shared parameters, you can reference them inside default_params and params blocks using [shared_params_ref](#shared_005fparams_005fref). You can also obtain a reference to them in your code via GpuProgramManager::getSharedParameters, and update the values for all instances using them.


## Adding new Techniques, Passes, to copied materials {#Adding-new-Techniques_002c-Passes_002c-to-copied-materials_003a}

If a new technique or pass needs to be added to a copied material then use a unique name for the technique or pass that does not exist in the parent material. Using an index for the name that is one greater than the last index in the parent will do the same thing. The new technique/pass will be added to the end of the techniques/passes copied from the parent material.

@note if passes or techniques aren`t given a name, they will take on a default name based on their index. For example the first pass has index 0 so its name will be 0.


## Identifying Texture Units to override values {#Identifying-Texture-Units-to-override-values}

A specific texture unit state (TUS) can be given a unique name within a pass of a material so that it can be identified later in cloned materials that need to override specified texture unit states in the pass without declaring previous texture units. Using a unique name for a Texture unit in a pass of a cloned material adds a new texture unit at the end of the texture unit list for the pass.

```cpp
material BumpMap2 : BumpMap1
{
    technique ati8500
    {
        pass 0
        {
            texture_unit NormalMap
            {
                texture BumpyMetalNM.png
            }
        }
    }
}
```


## Texture Aliases {#Texture-Aliases}

Texture aliases are useful for when only the textures used in texture units need to be specified for a cloned material. In the source material i.e. the original material to be cloned, each texture unit can be given a texture alias name. The cloned material in the script can then specify what textures should be used for each texture alias. Note that texture aliases are a more specific version of [Script Variables](#Script-Variables) which can be used to easily set other values.

Using texture aliases within texture units:
@par
Format: texture_alias &lt;name&gt;
@par
Default: &lt;name&gt; will default to texture_unit &lt;name&gt; if set

```cpp
texture_unit DiffuseTex
{
    texture diffuse.jpg
}
```

texture_alias defaults to DiffuseTex.

Example: The base material to be cloned:

```cpp
material TSNormalSpecMapping
{
    technique GLSL
    {
        pass
        {
            ambient 0.1 0.1 0.1
            diffuse 0.7 0.7 0.7
            specular 0.7 0.7 0.7 128

            vertex_program_ref GLSLDemo/OffsetMappingVS
            {
                param_named_auto lightPosition light_position_object_space 0
                param_named_auto eyePosition camera_position_object_space
                param_named textureScale float 1.0
            }

            fragment_program_ref GLSLDemo/TSNormalSpecMappingFS
            {
                param_named normalMap int 0
                param_named diffuseMap int 1
                param_named fxMap int 2
            }

            // Normal map
            texture_unit NormalMap
            {
                texture defaultNM.png
                tex_coord_set 0
                filtering trilinear
            }

            // Base diffuse texture map
            texture_unit DiffuseMap
            {
                texture defaultDiff.png
                filtering trilinear
                tex_coord_set 1
            }

            // spec map for shininess
            texture_unit SpecMap
            {
                texture defaultSpec.png
                filtering trilinear
                tex_coord_set 2
            }

        }
    }

    technique HLSL_DX9
    {
        pass
        {

            vertex_program_ref FxMap_HLSL_VS
            {
                param_named_auto worldViewProj_matrix worldviewproj_matrix
                param_named_auto lightPosition light_position_object_space 0
                param_named_auto eyePosition camera_position_object_space
            }

            fragment_program_ref FxMap_HLSL_PS
            {
                param_named ambientColor float4 0.2 0.2 0.2 0.2
            }

            // Normal map
            texture_unit
            {
                texture_alias NormalMap
                texture defaultNM.png
                tex_coord_set 0
                filtering trilinear
            }

            // Base diffuse texture map
            texture_unit
            {
                texture_alias DiffuseMap
                texture defaultDiff.png
                filtering trilinear
                tex_coord_set 1
            }

            // spec map for shininess
            texture_unit
            {
                texture_alias SpecMap
                texture defaultSpec.png
                filtering trilinear
                tex_coord_set 2
            }

        }
    }
}
```

Note that the GLSL and HLSL techniques use the same textures. For each texture usage type a texture alias is given that describes what the texture is used for. So the first texture unit in the GLSL technique has the same alias as the TUS in the HLSL technique since its the same texture used. Same goes for the second and third texture units.<br> For demonstration purposes, the GLSL technique makes use of texture_unit naming and therefore the texture_alias name does not have to be set since it defaults to the texture unit name. So why not use the default all the time since its less typing? For most situations you can. Its when you clone a material that and then want to change the alias that you must use the texture_alias command in the script. You cannot change the name of a texture_unit in a cloned material so texture_alias provides a facility to assign an alias name.

Now we want to clone the material but only want to change the textures used. We could copy and paste the whole material but if we decide to change the base material later then we also have to update the copied material in the script. With set_texture_alias, copying a material is very easy now. set_texture_alias is specified at the top of the material definition. All techniques using the specified texture alias will be effected by set_texture_alias.

@par
Format: set_texture_alias &lt;alias name&gt; &lt;texture name&gt;

```cpp
material fxTest : TSNormalSpecMapping
{
    set_texture_alias NormalMap fxTestNMap.png
    set_texture_alias DiffuseMap fxTestDiff.png
    set_texture_alias SpecMap fxTestMap.png
}
```

The textures in both techniques in the child material will automatically get replaced with the new ones we want to use.

The same process can be done in code as long you set up the texture alias names so then there is no need to traverse technique/pass/TUS to change a texture. You just call myMaterialPtr-&gt;applyTextureAliases(myAliasTextureNameList) which will update all textures in all texture units that match the alias names in the map container reference you passed as a parameter.

You don`t have to supply all the textures in the copied material.

```cpp
material fxTest2 : fxTest
{
    set_texture_alias DiffuseMap fxTest2Diff.png
    set_texture_alias SpecMap fxTest2Map.png
}
```

Material fxTest2 only changes the diffuse and spec maps of material fxTest and uses the same normal map.

Another example:

```cpp
material fxTest3 : TSNormalSpecMapping
{
    set_texture_alias DiffuseMap fxTest2Diff.png
}
```

fxTest3 will end up with the default textures for the normal map and spec map setup in TSNormalSpecMapping material but will have a different diffuse map. So your base material can define the default textures to use and then the child materials can override specific textures.

<https://ogrecave.github.io/ogre/api/latest/_material-_scripts.html>



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2020-11-26-ogre-material-scripts.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [http://en.wikipedia.org/wiki/Gamma_correction]({% include relrefx.html url="/backup/2020-11-26-ogre-material-scripts.md/en.wikipedia.org/dae24972.html" %})
- [http://developer.nvidia.com/object/nvparse.html]({% include relrefx.html url="/backup/2020-11-26-ogre-material-scripts.md/developer.nvidia.com/7d634c33.html" %})
- [https://ogrecave.github.io/ogre/api/latest/_material-_scripts.html]({% include relrefx.html url="/backup/2020-11-26-ogre-material-scripts.md/ogrecave.github.io/c3de684f.html" %})
