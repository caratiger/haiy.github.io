---
layout: post
---

{{page.title}}
========

<p class="meta">July 18 2016</p>

kaggle上的talking data数据分析要想好好玩呢，开发环境越舒服越好啦。我这采用的环境是
mysql+sublimt+tmux+sql_terminal+ipython+matplotlib。简单说下这么选型的原因:

 - 1 mysql存储，数据量不是很大查询高效，数据初步探索分析很方便
 - 2 sublime + tmux, sublime的多点选择非常有用，这点比vim好用；tmux界面切换方便 
 - 3 ipython + matplotlib, 直接读入mysql数据，和matplotlib无缝衔接
 

**1 基本安装**

```
sudo apt-get install ipython python-mysqldb tmux python-matplotlib


**2 数据分析**

 - 2.1 数据分布分析
 


参考:

[MySQLdb doc](http://mysql-python.sourceforge.net/MySQLdb.html)   
[Simple python mysql example](http://stackoverflow.com/questions/372885/how-do-i-connect-to-a-mysql-database-in-python)   
[matplotlib](http://matplotlib.org/)
