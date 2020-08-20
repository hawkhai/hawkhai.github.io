---
layout: post
title: "Encoding .NET bitmaps to H264 using FFMPEG"
location: "Japan"
categories: ["Code", "C#", "C++"]
comments: true
---

Recently, I was working on a project that involves the encoding of .NET bitmaps using [ffmpeg](https://www.ffmpeg.org/)'s h264 encoder with `mp4` as container. This video output will be used in a `<video>` tag in html5. Sample codes have been all over the place so it took me quite a while to come up with a working solution. The official sample from ffmpeg only encodes to raw h264 stream. This is just a basic sample code for reference.

Check out the source code [here](https://github.com/hawkhai/ffmpeg-encode-h264mp4).

Lastly, some useful links that I used:

* [https://en.code-bude.net/2013/04/17/how-to-create-video-files-in-c-from-single-images/](https://en.code-bude.net/2013/04/17/how-to-create-video-files-in-c-from-single-images/) 
* [https://github.com/FFmpeg/FFmpeg/blob/master/doc/examples/decoding_encoding.c](https://github.com/FFmpeg/FFmpeg/blob/master/doc/examples/decoding_encoding.c) 
* [http://www.imc-store.com.au/Articles.asp?ID=276](http://www.imc-store.com.au/Articles.asp?ID=276) 
