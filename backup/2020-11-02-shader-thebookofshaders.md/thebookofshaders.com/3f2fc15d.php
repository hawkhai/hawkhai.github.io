<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml"><head>
		<meta charset="utf-8" />

        <title>GLSL Editor</title>		<link href="/favicon.gif" rel="shortcut icon" />

        <!--— Open Graph data —-->
        <meta property="og:type" content="article" />
        <meta property="og:title" content="GLSL Shader Editor" />
        <meta property="og:site_name" content="The Book of Shaders" />
        <meta property="og:description" content="The Book of Shaders Editor" />


        <meta property="og:image" content="https://thebookofshaders.com/thumb.png" />
        <meta property="og:image:type" content="image/png" />
        <meta property="og:image:width" content="500" />
        <meta property="og:image:height" content="500" />
<!--         <!— Twitter Card—>
        <meta name="twitter:card" content="image">
        <meta name="twitter:site" content="@bookofshaders">
        <meta name="twitter:title" content="GLSL Shader Editor">
        <meta name="twitter:description" content="The Book of Shaders editor">
        <meta name="twitter:domain" content="thebookofshaders.com"> -->
		<style>
			body {
				height: 100%;
    			margin: 0;
	  			background: #272822;
			}

			#glsl_editor {
				height: 100%;
			}
		</style>
	<link href="https://fonts.googleapis.com/icon?family=Material+Icons" type="text/css" rel="stylesheet" media="screen,print" /></head>
	<body style="background-color: rgb(39, 40, 34);">
		<div id="glsl_editor"><ul class="ge_menu_bar"><li class="ge_menu"><button class="ge_menu_button"><i class="material-icons">add</i> New</button></li><li class="ge_menu"><button class="ge_menu_button"><i class="material-icons">folder_open</i>  Open</button></li><li class="ge_menu"><button class="ge_menu_button"><i class="material-icons">timeline</i> Test</button></li><li class="ge_menu"><button class="ge_menu_button"><i class="material-icons">arrow_upward</i> Export</button></li><li class="ge_menu"><button class="ge_menu_button"> <i class="material-icons">autorenew</i> Update: ON</button></li></ul><div class="ge_canvas_container" style="top: 53px;"><canvas class="ge_canvas" data-fragment="// Author:&#10;// Title:&#10;&#10;#ifdef GL_ES&#10;precision mediump float;&#10;#endif&#10;&#10;uniform vec2 u_resolution;&#10;uniform vec2 u_mouse;&#10;uniform float u_time;&#10;&#10;void main() {&#10;    vec2 st = gl_FragCoord.xy/u_resolution.xy;&#10;    st.x *= u_resolution.x/u_resolution.y;&#10;&#10;    vec3 color = vec3(0.);&#10;    color = vec3(st.x,st.y,abs(sin(u_time)));&#10;&#10;    gl_FragColor = vec4(color,1.0);&#10;}" width="500" height="500" style="background-color: rgb(1, 1, 1); width: 500px; height: 500px;"></canvas></div><div class="ge_editor" style="padding-top: 53px;"><div class="CodeMirror cm-s-monokai CodeMirror-wrap CodeMirror-focused" style="height: auto;"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 4px; left: 53px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" style="position: absolute; padding: 0px; width: 1000px; height: 1em; outline: none;" tabindex="0"></textarea></div><div class="CodeMirror-vscrollbar" cm-not-content="true" style="bottom: 0px;"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 45px; margin-bottom: -17px; border-right-width: 13px; min-height: 388px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines"><div style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre><span>xxxxxxxxxx</span></pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style="visibility: hidden;"><div class="CodeMirror-cursor" style="left: 8px; top: 0px; height: 19px;"> </div></div><div class="CodeMirror-code" style=""><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -45px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">1</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"><span class="cm-comment">// Author:</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -45px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">2</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"><span class="cm-comment">// Title:</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -45px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">3</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -45px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">4</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"><span class="cm-meta">#ifdef GL_ES</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -45px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">5</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"><span class="cm-variable">precision</span> <span class="cm-variable">mediump</span> <span class="cm-variable-3">float</span>;</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -45px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">6</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"><span class="cm-meta">#endif</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -45px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">7</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -45px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">8</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"><span class="cm-keyword">uniform</span> <span class="cm-variable-3">vec2</span> <span class="cm-variable">u_resolution</span>;</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -45px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">9</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"><span class="cm-keyword">uniform</span> <span class="cm-variable-3">vec2</span> <span class="cm-variable">u_mouse</span>;</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -45px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">10</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"><span class="cm-keyword">uniform</span> <span class="cm-variable-3">float</span> <span class="cm-variable">u_time</span>;</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -45px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">11</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -45px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">12</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"><span class="cm-variable-3">void</span> <span class="cm-variable">main</span>() {</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -45px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">13</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;">    <span class="cm-variable-3">vec2</span> <span class="cm-variable">st</span> <span class="cm-operator">=</span> <span class="cm-atom">gl_FragCoord</span>.<span class="cm-variable">xy</span><span class="cm-operator">/</span><span class="cm-variable">u_resolution</span>.<span class="cm-variable">xy</span>;</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -45px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">14</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;">    <span class="cm-variable">st</span>.<span class="cm-variable">x</span> <span class="cm-operator">*=</span> <span class="cm-variable">u_resolution</span>.<span class="cm-variable">x</span><span class="cm-operator">/</span><span class="cm-variable">u_resolution</span>.<span class="cm-variable">y</span>;</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -45px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">15</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -45px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">16</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;">    <span class="cm-variable-3">vec3</span> <span class="cm-variable">color</span> <span class="cm-operator">=</span> <span class="cm-variable-3">vec3</span>(<span class="cm-number">0.</span>);</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -45px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">17</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;">    <span class="cm-variable">color</span> <span class="cm-operator">=</span> <span class="cm-variable-3">vec3</span>(<span class="cm-variable">st</span>.<span class="cm-variable">x</span>,<span class="cm-variable">st</span>.<span class="cm-variable">y</span>,<span class="cm-builtin">abs</span>(<span class="cm-builtin">sin</span>(<span class="cm-variable">u_time</span>)));</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -45px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">18</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -45px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">19</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;">    <span class="cm-atom">gl_FragColor</span> <span class="cm-operator">=</span> <span class="cm-variable-3">vec4</span>(<span class="cm-variable">color</span>,<span class="cm-number">1.0</span>);</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -45px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">20</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;">}</span></pre></div></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; top: 388px;"></div><div class="CodeMirror-gutters" style="height: 401px; left: 0px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 29px;"></div><div class="CodeMirror-gutter breakpoints"></div></div></div></div></div></div>
	

	<link type="text/css" rel="stylesheet" href="https://thebookofshaders.com/glslEditor/glslEditor.css" />
    <script async="" src="//www.google-analytics.com/analytics.js"></script><script type="application/javascript" src="https://thebookofshaders.com/glslEditor/glslEditor.js"></script>
    <script type="text/javascript">
        var glslEditor = {};

        function loadjscssfile(filename, filetype, callback){
            if (filetype=="js") { //if filename is a external JavaScript file
                var fileref = document.createElement('script')
                fileref.setAttribute("type","text/javascript")
                fileref.setAttribute("src", filename)
            }
            else if (filetype=="css") { //if filename is an external CSS file
                var fileref = document.createElement("link")
                fileref.setAttribute("rel", "stylesheet")
                fileref.setAttribute("type", "text/css")
                fileref.setAttribute("href", filename)
            }

            fileref.onload = callback;
            fileref.onreadystatechange = callback;

            if (typeof fileref != "undefined") {
                document.getElementsByTagName("head")[0].appendChild(fileref)
            }
        }

        window.onload = function() {
            // if ()
            if (window.GlslEditor &amp;&amp; window.GlslEditor) {
                init();
            }
            else {
                console.log('Try to load a local glslEditor');
                if (!window.glslEditor) {
                    loadjscssfile('src/glslEditor/build/glslEditor.css', 'css');
                    loadjscssfile('src/glslEditor/build/glslEditor.js', 'js', init);
                }
            }
        };

        function init() {
            glslEditor = new GlslEditor('#glsl_editor', {
                                                                    canvas_size: 500,
                                                                    canvas_draggable: true,
                                                                    theme: 'monokai',
                                                                    multipleBuffers: true,
                                                                    watchHash: true,
                                                                    fileDrops: true,
                                                                    menu: true
                                                                });
            document.body.style.backgroundColor = window.getComputedStyle(glslEditor.editor.getWrapperElement(),null).getPropertyValue('background-color');
        }

    </script>
    <script>
        (function(i,s,o,g,r,a,m){i["GoogleAnalyticsObject"]=r;i[r]=i[r]||function(){
        (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
        })(window,document,"script","//www.google-analytics.com/analytics.js","ga");
        ga("create", "UA-18824436-2", "auto");
        ga("send", "pageview");
    </script>

<iframe id="CrossStorageClient-9de12634-bb98-45ad-8667-d458e92c259b" src="https://openframe.io/hub.html" style="display: none; position: absolute; top: -999px; left: -999px;"></iframe></body></html>