---
layout: post
---

{{page.title}}
==========
<p class="meta">July 13 2016</p>

###Method 1

用核显(集成显卡)安装，然后安装好驱动方法。[Ref 1:](http://superuser.com/questions/1095597/linux-install-monitor-out-of-range)

Run the following commands after you booted up to Ubuntu using your integrated graphics or the already supported dedicated graphics card.

```
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt-get update
sudo apt-get install nvidia-367
```

After the installation succeed, shutdown your machine. Now you can use GTX 1070/1080 without worrying the "out of range" error again.

Monitoring

You can use the nvidia-smi script to do real-time monitoring of your GTX 1070/1080. It has temperature reading, GPU usage, power usage, fan speed and memory usage (per application). You can leverage the watch command combined with nvidia-smi to get realtime monitoring. Run this command in your terminal to get realtime monitoring

watch -n0 nvidia-smi


###Method 2
 
install ubuntu failed with monitor out of range error. 
[Ref 2](http://superuser.com/questions/1095597/linux-install-monitor-out-of-range)

Remove vt.handoff=7 [Ref 3](http://ubuntuforums.org/showthread.php?t=1751950)

