---
title : 自动快照存档
---

* TIME: 2021-02-05 22:58:34
* URL: <https://github.com/pytorch/pytorch/issues/25039>

-----

Skip to content

[ ](https://github.com/)

[ Sign up
](/join?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-
name%3E%2F%3Crepo-name%3E%2Fissues%2Fshow&source=header-repo)

  * Why GitHub? 

[Features →](/features)

    * [Code review](/features/code-review/)
    * [Project management](/features/project-management/)
    * [Integrations](/features/integrations)
    * [Actions](/features/actions)
    * [Packages](/features/packages)
    * [Security](/features/security)
    * [Team management](/features#team-management)
    * [Hosting](/features#hosting)
    * [Mobile](/mobile)
    * [Customer stories →](/customer-stories)
    * [Security →](/security)

  * [Team](/team)
  * [Enterprise](/enterprise)
  * Explore 

    * [Explore GitHub →](/explore)

#### Learn & contribute

    * [Topics](/topics)
    * [Collections](/collections)
    * [Trending](/trending)
    * [Learning Lab](https://lab.github.com/)
    * [Open source guides](https://opensource.guide)

#### Connect with others

    * [Events](https://github.com/events)
    * [Community forum](https://github.community)
    * [GitHub Education](https://education.github.com)
    * [GitHub Stars program](https://stars.github.com)

  * [Marketplace](/marketplace)
  * Pricing 

[Plans →](/pricing)

    * [Compare plans](/pricing#feature-comparison)
    * [Contact Sales](https://enterprise.github.com/contact)
    * [Nonprofit →](/nonprofit)
    * [Education →](https://education.github.com)

![](https://github.githubassets.com/images/search-key-slash.svg)

  * [ ![]() In this repository  All GitHub  ↵ Jump to ↵ ]()

  * No suggested jump to results

  * [ ![]() In this repository  All GitHub  ↵ Jump to ↵ ]()
  * [ ![]() In this repository  All GitHub  ↵ Jump to ↵ ]()

[ Sign in ](/login?return_to=%2Fpytorch%2Fpytorch%2Fissues%2F25039) [ Sign up
](/join?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-
name%3E%2F%3Crepo-name%3E%2Fissues%2Fshow&source=header-
repo&source_repo=pytorch%2Fpytorch)

{{ message }}

#  [pytorch](/pytorch) / **[pytorch](/pytorch/pytorch) **

  * [ Watch ](/login?return_to=%2Fpytorch%2Fpytorch) [ 1.6k ](/pytorch/pytorch/watchers)
  * [ Star ](/login?return_to=%2Fpytorch%2Fpytorch) [ 44.8k ](/pytorch/pytorch/stargazers)
  * [ Fork ](/login?return_to=%2Fpytorch%2Fpytorch) [ 11.9k ](/pytorch/pytorch/network/members)

  * [ Code ](/pytorch/pytorch)
  * [ Issues 5k+ ](/pytorch/pytorch/issues)
  * [ Pull requests 2.2k ](/pytorch/pytorch/pulls)
  * [ Actions ](/pytorch/pytorch/actions)
  * [ Projects 11 ](/pytorch/pytorch/projects)
  * [ Wiki ](/pytorch/pytorch/wiki)
  * [ Security ](/pytorch/pytorch/security)
  * [ Insights ](/pytorch/pytorch/pulse)

More

  * [ Code ](/pytorch/pytorch)
  * [ Issues ](/pytorch/pytorch/issues)
  * [ Pull requests ](/pytorch/pytorch/pulls)
  * [ Actions ](/pytorch/pytorch/actions)
  * [ Projects ](/pytorch/pytorch/projects)
  * [ Wiki ](/pytorch/pytorch/wiki)
  * [ Security ](/pytorch/pytorch/security)
  * [ Insights ](/pytorch/pytorch/pulse)

New issue

**Have a question about this project?** Sign up for a free GitHub account to
open an issue and contact its maintainers and the community.

Pick a username

    

Email Address

    

Password

    
Sign up for GitHub

By clicking “Sign up for GitHub”, you agree to our [terms of
service](https://docs.github.com/terms) and [privacy
statement](https://docs.github.com/privacy). We’ll occasionally send you
account related emails.

Already on GitHub? [Sign
in](/login?return_to=%2Fpytorch%2Fpytorch%2Fissues%2Fnew) to your account

Jump to bottom

#  Add new interpolation modes to `grid_sample`  #25039

Open

[bnehoran](/bnehoran) opened this issue on 23 Aug 2019 · 4 comments

Open

#  Add new interpolation modes to `grid_sample` #25039

[bnehoran](/bnehoran) opened this issue on 23 Aug 2019 · 4 comments

Labels

[ function request ](/pytorch/pytorch/labels/function%20request "A request for
a new function or the addition of new arguments/modes to an existing
function.") [ module: interpolation
](/pytorch/pytorch/labels/module%3A%20interpolation) [ module: nn
](/pytorch/pytorch/labels/module%3A%20nn "Related to torch.nn") [ triaged
](/pytorch/pytorch/labels/triaged "This issue has been looked at a team
member, and triaged and prioritized into an appropriate module")

## Comments

[![@bnehoran](https://avatars3.githubusercontent.com/u/9757500?s=88&v=4)](/bnehoran)

Copy link  Quote reply

Contributor

###
[![@bnehoran](https://avatars2.githubusercontent.com/u/9757500?s=60&v=4)](/bnehoran)
**[bnehoran](/bnehoran) ** commented on 23 Aug 2019 •

edited by pytorch-probot bot

_Note: This issue is expanded out
of[#24870](https://github.com/pytorch/pytorch/issues/24870) to allow more room
for discussion._

## 🚀 Feature

Currently, `torch.nn.functional.grid_sample()` supports two interpolation
modes: `bilinear` and `nearest`.

Other interpolation modes that could be added:

  * [`bicubic`](https://en.wikipedia.org/wiki/Bicubic_interpolation): This is already implemented for `torch.nn.functional.interpolate()` [here](https://github.com/pytorch/pytorch/blob/master/aten/src/ATen/native/UpSampleBicubic2d.cpp), so this shouldn't be difficult to adapt for `grid_sample`, which should work in a similar way.  
There has been mention of this in the past
([forum/39515](https://discuss.pytorch.org/t/bicubic-grid-sampler/39515),
[pytorch/vision#514
(comment)](https://github.com/pytorch/vision/issues/514#issuecomment-402718886)),
but so far no real plan. (Also see discussions regarding its implementation in
`interpolate`: [#9849](https://github.com/pytorch/pytorch/pull/9849),
[#19703](https://github.com/pytorch/pytorch/pull/19703).)

  * `area`: Like `bicubic`, this mode already exists in `torch.nn.functional.interpolate()`. However, it is not as clear how to adapt this to work in `grid_sample` where the sampling points will in general not be a regular grid. This might require some research and definition design, and discussion is ongoing in [#21457](https://github.com/pytorch/pytorch/issues/21457).

  * [`lanczos`](https://en.wikipedia.org/wiki/Lanczos_resampling): Another option for smoother interpolation. This is currently [implemented](https://github.com/torch/image/blob/5aa18819b6a7b44751f8a858bd232d1c07b67985/generic/image.c#L1894) in [Torch](https://github.com/torch/image/blob/master/doc/paramtransform.md), so a PyTorch implementation could possibly take inspiration from there.  
I am personally not particularly familiar with the practical uses of this
mode, so we could discuss whether this is a desired feature, or if other
interpolation/sampling filters are more in demand.

cc [@albanD](https://github.com/albanD)
[@mruberry](https://github.com/mruberry) [@SsnL](https://github.com/SsnL)
[@fmassa](https://github.com/fmassa) [@ailzhang](https://github.com/ailzhang)  
  
---  
  
The text was updated successfully, but these errors were encountered:

  
  
👍 7

[![@bnehoran](https://avatars2.githubusercontent.com/u/9757500?s=60&v=4)](/bnehoran)
[bnehoran](/bnehoran) mentioned this issue  on 23 Aug 2019

[ Recommendations for Grid Sample/Affine Grid/Displacement Fields/Optical Flow
#24870 ](/pytorch/pytorch/issues/24870)

Open

6 of 22 tasks complete

[![@andreaskoepf](https://avatars0.githubusercontent.com/u/9976399?s=88&u=f364e8da1ddd870ccc7c6aaf51db03493ddbef8b&v=4)](/andreaskoepf)

Copy link

Collaborator

###
[![@andreaskoepf](https://avatars3.githubusercontent.com/u/9976399?s=60&u=f364e8da1ddd870ccc7c6aaf51db03493ddbef8b&v=4)](/andreaskoepf)
**[andreaskoepf](/andreaskoepf) ** commented on 23 Aug 2019

Lanczos generates a less blurry image than bicubic but can introduce ringing
artifacts at sharp edges, see for example [Image
Reconstruction](http://www.pbr-
book.org/3ed-2018/Sampling_and_Reconstruction/Image_Reconstruction.html#x1-WindowedSincFilter)
in the pbr book.

[![image](https://user-
images.githubusercontent.com/9976399/63556641-eeb89400-c545-11e9-8f90-58e1c0eb0840.png)](https://user-
images.githubusercontent.com/9976399/63556641-eeb89400-c545-11e9-8f90-58e1c0eb0840.png)  
(extracted from the matlibplot docs: [interpolation
methods](https://matplotlib.org/1.4.2/examples/images_contours_and_fields/interpolation_methods.html))

I looked at the legacy lanczos implementation by Jonathan Tompson in the
`warp` function. The implementation implements `padding_mode="border"`. In
general it seems to be ok but I guess it has to be written from scratch anyway
to match the quality / structure of the new GridSampler of ATen.  
  
---  
  
[![@izdeby](https://avatars3.githubusercontent.com/u/47012416?s=60&u=51c579b88e3f299ab3db3eb9bf8d34ed3fe781f7&v=4)](/izdeby)
[izdeby](/izdeby) added [ enhancement ](/pytorch/pytorch/labels/enhancement
"Not as big of a feature, but technically not a bug. Should be easy to fix") [
triaged ](/pytorch/pytorch/labels/triaged "This issue has been looked at a
team member, and triaged and prioritized into an appropriate module") [
module: nn ](/pytorch/pytorch/labels/module%3A%20nn "Related to torch.nn") [
module: operators ](/pytorch/pytorch/labels/module%3A%20operators) labels on
24 Aug 2019

[![@dashesy](https://avatars1.githubusercontent.com/u/873905?s=88&v=4)](/dashesy)

Copy link

Contributor

###
[![@dashesy](https://avatars0.githubusercontent.com/u/873905?s=60&v=4)](/dashesy)
**[dashesy](/dashesy) ** commented on 20 Nov 2019

lanczos prefilter will be helpful to have an interpolation similar to PIL, and
thus torchvision.transforms.Resize. Bilinear shrinking without prefilter
produces a very different image.  
  
---  
  
[![@bobchennan](https://avatars1.githubusercontent.com/u/939088?s=60&v=4)](/bobchennan)
[bobchennan](/bobchennan) mentioned this issue  on 1 Apr

[ Implement SpecAug for ESPnet2 espnet/espnet#1746 ](/espnet/espnet/pull/1746)

Merged

[![@soulslicer](https://avatars3.githubusercontent.com/u/3193196?s=88&v=4)](/soulslicer)

Copy link

###
[![@soulslicer](https://avatars2.githubusercontent.com/u/3193196?s=60&v=4)](/soulslicer)
**[soulslicer](/soulslicer) ** commented on 1 Apr

are there any plans by anyone to implement bicubic for grid_sample  
  
---  
  
👍 1

[![@bnehoran](https://avatars3.githubusercontent.com/u/9757500?s=88&v=4)](/bnehoran)

Copy link

Contributor  Author

###
[![@bnehoran](https://avatars2.githubusercontent.com/u/9757500?s=60&v=4)](/bnehoran)
**[bnehoran](/bnehoran) ** commented on 7 Apr

[@soulslicer](https://github.com/soulslicer) As far as I know, no one is
working on it yet, and it is just waiting for someone to take it up and
implement.  
  
---  
  
👍 1

[![@pomelyu](https://avatars3.githubusercontent.com/u/2679561?s=60&u=dfe1cb59b40f0cb503d37f1c51afbaf361a19409&v=4)](/pomelyu)
[pomelyu](/pomelyu) mentioned this issue  on 13 Sep

[ Implementation of 2d bicubic grid sampler #44601
](/pytorch/pytorch/issues/44601)

Closed

[![@mruberry](https://avatars1.githubusercontent.com/u/38511765?s=60&v=4)](/mruberry)
[mruberry](/mruberry) added [ function request
](/pytorch/pytorch/labels/function%20request "A request for a new function or
the addition of new arguments/modes to an existing function.") [ module:
interpolation ](/pytorch/pytorch/labels/module%3A%20interpolation) and removed
[ enhancement ](/pytorch/pytorch/labels/enhancement "Not as big of a feature,
but technically not a bug. Should be easy to fix") [ module: operators
(deprecated)
](/pytorch/pytorch/labels/module%3A%20operators%20%28deprecated%29) labels on
10 Oct

[Sign up for free](/join?source=comment-repo) **to join this conversation on
GitHub**. Already have an account? [Sign in to
comment](/login?return_to=https%3A%2F%2Fgithub.com%2Fpytorch%2Fpytorch%2Fissues%2F25039)

Assignees

No one assigned

Labels

[ function request ](/pytorch/pytorch/labels/function%20request "A request for
a new function or the addition of new arguments/modes to an existing
function.") [ module: interpolation
](/pytorch/pytorch/labels/module%3A%20interpolation) [ module: nn
](/pytorch/pytorch/labels/module%3A%20nn "Related to torch.nn") [ triaged
](/pytorch/pytorch/labels/triaged "This issue has been looked at a team
member, and triaged and prioritized into an appropriate module")

Projects

None yet

Milestone

No milestone

Linked pull requests

Successfully merging a pull request may close this issue.

None yet

6 participants

[ ![@dashesy](https://avatars2.githubusercontent.com/u/873905?s=52&v=4)
](/dashesy) [
![@soulslicer](https://avatars0.githubusercontent.com/u/3193196?s=52&v=4)
](/soulslicer) [
![@bnehoran](https://avatars0.githubusercontent.com/u/9757500?s=52&v=4)
](/bnehoran) [
![@andreaskoepf](https://avatars2.githubusercontent.com/u/9976399?s=52&v=4)
](/andreaskoepf) [
![@mruberry](https://avatars3.githubusercontent.com/u/38511765?s=52&v=4)
](/mruberry) [
![@izdeby](https://avatars3.githubusercontent.com/u/47012416?s=52&v=4)
](/izdeby)

  * © 2020 GitHub, Inc.
  * [Terms](https://github.com/site/terms)
  * [Privacy](https://github.com/site/privacy)
  * [Security](https://github.com/security)
  * [Status](https://githubstatus.com/)
  * [Help](https://docs.github.com)

[ ](https://github.com "GitHub")

  * [Contact GitHub](https://github.com/contact)
  * [Pricing](https://github.com/pricing)
  * [API](https://docs.github.com)
  * [Training](https://services.github.com)
  * [Blog](https://github.blog)
  * [About](https://github.com/about)

You can’t perform that action at this time.

You signed in with another tab or window. [Reload]() to refresh your session.
You signed out in another tab or window. [Reload]() to refresh your session.

