---
layout: post
title: "Using Homebrew for distributing Go (golang) apps"
location: "Japan"
tags: [homebrew, go, golang, ruby]
---

For personal reference:

#### a) Create your own homebrew tap

Create a new GitHub public repository with a prefix `homebrew-`, i.e. `homebrew-tap`. This will house all the apps that you want to distribute via your tap. Users will install your apps using the following commands:

{% highlight shell %}
# No need to include the 'homebrew-' prefix
$ brew tap hawkhai/tap
$ brew install <toolname>
{% endhighlight %}

The `toolname` part will correspond to the filename inside your repository tap. If your repository has an entry with a filename of `toolx.rb`, it can be installed using the following commands:

{% highlight shell %}
$ brew tap hawkhai/tap
$ brew install toolx
{% endhighlight %}

Here's an example of a formula for a golang app:

{% highlight ruby %}
class Kubepfm < Formula
  desc "A simple wrapper to kubectl port-forward for multiple pods."
  homepage "https://github.com/hawkhai/kubepfm"
  url "https://github.com/hawkhai/kubepfm/archive/v0.0.3.tar.gz"
  sha256 "7852a5500f3e35a47b57d138c756de5641bc3c48bf7e329d2724c1107ccb1207"

  depends_on "go"

  def install
    ENV["GOPATH"] = buildpath
    ENV["GO111MODULE"] = "on"
    ENV["GOFLAGS"] = "-mod=vendor"
    ENV["PATH"] = "#{ENV["PATH"]}:#{buildpath}/bin"
    (buildpath/"src/github.com/hawkhai/kubepfm").install buildpath.children
    cd "src/github.com/hawkhai/kubepfm" do
      system "go", "build", "-o", bin/"kubepfm", "."
    end
  end

  test do
    assert_match /Simple port-forward wrapper tool for multiple pods/, shell_output("#{bin}/kubepfm -h", 0)
  end
end
{% endhighlight %}

You can check out [https://github.com/hawkhai/homebrew-tap](https://github.com/hawkhai/homebrew-tap) for reference.

The `url` part is the path of the source `tar.gz` of your source files. You can create this by using [tagged releases](https://help.github.com/en/enterprise/2.16/user/articles/about-releases) in GitHub.

You can generate the `sha256` part by running the `shasum` (OSX) or `sha256sum` (Linux) tool against your `tar.gz` file.

#### b) Updating your formula

If you have a new version of your tool, first, create a new tag or release. Download the new `tar.gz` file of the new release, run the `sha256sum/shasum` tool against it, and update the `.rb` file in your tap repository.

Example:

{% highlight shell %}
$ git clone https://github.com/hawkhai/kubepfm
$ cd kubepfm/
$ git tag v1.0.1 # our new tag
$ git push --tags # push tags to remote
$ wget https://github.com/hawkhai/kubepfm/archive/v1.0.1.tar.gz
# OSX
$ shasum -a 256 v1.0.1.tar.gz
7852a5500f3e35a47b57d138c756de5641bc3c48bf7e329d2724c1107ccb1207  v1.0.1.tar.gz
# Linux
$ sha256sum v1.0.1.tar.gz
7852a5500f3e35a47b57d138c756de5641bc3c48bf7e329d2724c1107ccb1207  v1.0.1.tar.gz
{% endhighlight %}

Finally, update the `url` and `sha256` part of your `.rb` file. Users will now be able to update their copies:

{% highlight shell %}
$ brew upgrade kubepfm
{% endhighlight %}

