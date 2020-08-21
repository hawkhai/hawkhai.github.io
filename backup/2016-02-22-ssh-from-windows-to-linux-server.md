---
layout: post
title: "SSH from a Windows client to a Linux server"
location: "Japan"
categories: ["Tech"]
comments: true
---

At the moment, Im still in the process of setting up my home network server. Ill be taking notes about my progress here so this might be a series of related posts.

Im using an Ubuntu 14.04 Server (headless). Client is a Windows 10 machine.

## The simple way

### Server side

1. Install `ssh`. How to do this depends on what distro you are using. For Ubuntu, you can do an `apt-get install ssh`. I didnt have to do this however as I installed it during the server setup.

### Client side

1. Install Putty. I suggest you download the installer.
2. Open Putty, input your server IP under Host Name (or IP address), and click Open.
3. Enter your server login name and password.

But entering server credentials every time you login is really a bit of a hassle, isnt it? Enter public/private keys.

## The simple and convenient way

### Server side

1. Create a `.ssh` folder in you home folder if you havent got one. Then `cd` to your `.ssh` folder.
2. Generate a public/private key pair inside `.ssh` folder.

{% highlight shell %}
ssh-keygen -t rsa -b 4096 -f <filename>
{% endhighlight %}

You can choose to add a passphrase, but I didnt since the point here really is to not type anything during login (you still have to enter the passphrase every time you login if you provide one). This will generate two files: the private key with the name `<filename>` and the public key `<filename>.pub`.

3. Append the public key (`<filename>.pub`) to `~/.ssh/authorized_keys`.

{% highlight shell %}
cat <filename>.pub >> authorized_keys
chmod -R 600 ~/.ssh
{% endhighlight %}

4. Copy the private key to your Windows client.

### Client side

1. Install Putty. I suggest you download the installer.
2. Generate a .ppk file from the private key using PuttyGen. Load the copied private key then click Save private key.
3. Setup Putty to use the .ppk file.
4. Add auto-login username under Connection -> Data.
5. Add the .ppk file to Private key file for authentication under Connection -> SSH -> Auth.
6. Go back to Sessions, enter your servers IP address, add a session name under Saved Sessions and save.
7. Try logging in to your server using the saved session details from #3. You should be able to now without typing your server credentials.
