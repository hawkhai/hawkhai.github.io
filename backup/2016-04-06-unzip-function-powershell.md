---
layout: post
title: "A simple unzip function in Powershell"
location: "Japan"
categories: ["Code"]
comments: true
---

{% highlight powershell %}
function UnzipFiles($ZipFileName, $DestDir)
{
    Add-Type -Assembly System.IO.Compression.FileSystem
    [System.IO.Compression.ZipFile]::ExtractToDirectory($ZipFileName, $DestDir)
}
{% endhighlight %}

To use the function:

{% highlight powershell %}
UnzipFiles -ZipFileName .\folder\file.zip -DestDir .\destination
{% endhighlight %}
