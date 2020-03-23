# work-related

[windows安装cygwin教程](https://blog.csdn.net/chunleixiahe/article/details/55666792)

[桌面云安装Cygwin问题的解决方式](http://3ms.huawei.com/km/blogs/details/6078397)

[darknet在windows上的安装编译与使用](https://blog.csdn.net/fanhenghui/article/details/102835176)
darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
提示Couldn't open file: data/coco.names
之前是通过Git克隆的darknet项目的源码到本地文件，改为直接下载zip文件然后解压，编译之后，就可以避免之前的问题。
内存不足解决方法
My solution to run Yolov3 perfectly was to : modify the cfg/yolov3.cfg :
```
batch=1
subdivisions=1
width=416
height=416
```

[train遇到问题](http://www.luyixian.cn/news_show_20149.aspx)
使用notepad++工具，打开该文件，编辑->文档格式转换->转化为unix格式。
```
[net]
# Testing
# batch=1
# subdivisions=1
# Training
batch=64
subdivisions=16
```

遇到问题
Couldn't open file: /darknet/scripts/2007_train.txt
使用notepad++工具，打开该文件，编辑->文档格式转换->转化为unix格式。
修改路径
classes= 2
train  = scripts/2007_train.txt
valid  = scripts/2007_val.txt
names = data/voc.names
backup = backup

遇到问题
YOLOV3无法加载图片"cannot load image"
1、修改路径
2、使用notepad++工具，打开该文件，编辑->文档格式转换->转化为unix格式。

yolov3用训练过的weights文件继续训练
./darknet detector train cfg/voc.data cfg/yolov3-voc.cfg backup/yolov3-voc_100.weights

[解决sudo apt-get install libprotobuf-dev
is to be installed
E: Unable to correct problems, you have held broken packages.](https://www.cnblogs.com/aaron-agu/p/8862624.html)
