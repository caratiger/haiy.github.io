---
layout: post
title: hack ssh
---

{{page.title}}
=============

<p class="meta">2 Oct 2016</p>

### Target  

There are three hosts，A with many NAT layers at home ，B public IP host，C host from anyhere.Now I want to build 
web apps on A, and access the urls from C.

### Methods：

** 1. build a reverse ssh tunnel **

```bash
#on A, reverse tunnel
apt-get install autossh
autossh -N -f -R 2222:localhost:22 userB@B

#on C, try to connect A directly
ssh -f -N -L 3333:localhost:2222 userB@B
ssh -L 3333 userA@localhost
```

** 2. dig web holes on B for web apps **

#on B,








[reverse-ssh-port-forwarding](https://toic.org/blog/2009/reverse-ssh-port-forwarding/) 
[direct-ssh-tunnel-through-a-reverse-ssh-tunnel](http://askubuntu.com/questions/598626/direct-ssh-tunnel-through-a-reverse-ssh-tunnel)
