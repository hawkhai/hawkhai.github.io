---
layout: post
title: "Using OS specific stores for storing CLI credentials for golang apps"
location: "Japan"
tags: [go, nativestore, keychain, wincred, pass]
comments: true
---

This post is to show a simple way of using Docker's [credential helper package](https://github.com/docker/docker-credential-helpers) to utilize the system's native credential store as storage for your Golang-based CLI applications' login credentials. This means Keychain for OSX, [`wincred`](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374792(v=vs.85).aspx) for Windows, and [`pass`](https://www.passwordstore.org/) for Linux. We use [`pass`](https://www.passwordstore.org/) here since [`secretservice`](https://specifications.freedesktop.org/secret-service/), although supported, doesn't work out of the box in headless servers.

Here's a simple implementation of our `Set`, `Get`, and `Del` functions.

<script charset="UTF-8" src="https://gist-it.appspot.com/github.com/mobingilabs/mobingi-sdk-go/blob/master/pkg/nativestore/nativestore.go?footer=minimal"></script>

Then we create our `_darwin.go`, `_linux.go`, and `_windows.go` files for OS specific implementations.

<script charset="UTF-8" src="https://gist-it.appspot.com/github.com/mobingilabs/mobingi-sdk-go/blob/master/pkg/nativestore/nativestore_darwin.go?footer=minimal"></script>

<script charset="UTF-8" src="https://gist-it.appspot.com/github.com/mobingilabs/mobingi-sdk-go/blob/master/pkg/nativestore/nativestore_windows.go?footer=minimal"></script>

<script charset="UTF-8" src="https://gist-it.appspot.com/github.com/mobingilabs/mobingi-sdk-go/blob/master/pkg/nativestore/nativestore_linux.go?footer=minimal"></script>

Here's a quickstart guide to setup [`pass`](https://www.passwordstore.org/) in Ubuntu systems.

{% highlight shell %}
# install pass
$ sudo apt-get install pass

# generate your own key using gpg2, do not use a passphrase
$ gpg2 --gen-key

# if the cmd seems stuck due to lack of entropy, you can open another window and run the ff cmd:
# dd if=/dev/sda of=/dev/zero

# list your keys
$ gpg2 --list-keys
/home/user/.gnupg/pubring.kbx
------------------------------
pub   rsa2048/5486B0F6 2017-09-22 [SC]
uid         [ultimate] IamGroot <iamgroot@domain.com>
sub   rsa2048/CDC4C430 2017-09-22 [E]

# initialize pass (use the pub key id)
$ pass init 5486B0F6
{% endhighlight %}

Here's an example on how to use our nativestore functions.

<script charset="UTF-8" src="https://gist-it.appspot.com/github.com/mobingilabs/mobingi-sdk-go/blob/master/pkg/nativestore/nativestore_test.go?footer=minimal"></script>

Finally, you can refer to the whole package [here](https://github.com/mobingilabs/mobingi-sdk-go/tree/master/pkg/nativestore).
