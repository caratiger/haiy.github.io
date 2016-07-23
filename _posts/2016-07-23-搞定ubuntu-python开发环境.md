---
layout: post
---

{{page.title}}
================
<p class = "meta">July 23 2016</p>

在ubuntu下玩python要充分便利好用才不枉折腾。
我的python开发环境主要由tmux+vim+jedi组成,先看一张结果图：

<a href="http://haiy.github.io/images/python_dev_ide.png"  target="_blank"><img alt="右键看大图" src="{{site.url}}/images/python_dev_ide.png"  height="225px" width="400px"> </a>

**1 安装基本的几个东西**

```bash
sudo apt-get install tmux 

#jedi是个代码自动补全的库
pip install jedi
sudo apt install vim-nox-py2
```

**2 git clone 配置**

```
#这个是我的vim配置
git clone https://github.com/haiy/vim.git

#这个是我写的安装脚本install.sh
chmod +x install.sh
./install.sh
cp vimrc ~/.vimrc
```
安装好插件后基本上打开vim会是下面的样子:

<a href="http://haiy.github.io/images/vim_theme.png" target="_blank"><img alt="右键看大图" src="{{site.url}}/images/vim_theme.png"  height="275px" width="389px"></a>

好了，差不多ok了，可以愉快的玩耍了。
这时候python的自动补全应该也是ok的。
至于具体的键位映射看下vimrc.


参考:    
[jedi-vim](https://github.com/davidhalter/jedi-vim)   
[Automatically_add_Python_paths_to_Vim_path](http://vim.wikia.com/wiki/Automatically_add_Python_paths_to_Vim_path)    
[ubuntu-16-04-vim-without-python-support](http://askubuntu.com/questions/764882/ubuntu-16-04-vim-without-python-support)   
