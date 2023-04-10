# 弹幕热点分析器-DanmuPeak：分析弹幕数据，快速找到视频亮点

面向社科研究者、代码小白的零门槛的分析弹幕文件的 Python 脚本。该脚本会读取指定文件夹内的弹幕文件，并输出一个包含视频名称和弹幕高峰时间戳的 Excel 文件。

社科学习者、研究者可以据此分析在弹幕高峰时，up主采取了什么激发互动的策略，分析为什么这能成为视频亮点、互动的最高峰。

它还适用于内容创作者、数据分析师和研究员，帮助他们深入了解观众的互动和兴趣点。

# 亮点
1. 简单易用：只需将弹幕文件放入指定文件夹，运行脚本即可得到分析结果。
2. 多文件同时分析：一次性分析文件夹内所有弹幕文件，节省时间和精力。
3. 直观的输出结果：生成包含视频名称和弹幕高峰时间戳的 Excel 文件，方便查看和进一步分析。
4. 弹性选择：输出最高峰、次高峰和第三高峰时间戳，以确保找到真正的热点时刻。

## 输入与输出
1.弹幕爬取如果不想用爬虫的话，可以尝试Chrome扩展程序“B站bilibil弹幕下载生成ASS字幕”，将最大弹幕数限制设成“99999”，就能确保下载到全部弹幕。

2.将下载的弹幕文件后缀名由“.ass”修改为".txt",文件内容样式就是ass的格式，具体请参照danmusample.txt。

3.请将input_folder替换为您的弹幕文件所在的文件夹路径，请确保该文件夹下只有弹幕文件

4.可以在“输出数据表.xlsx”处修改输出文件名，默认输出文件夹为代码文件所存放的文件夹

注意：文件路径用 / 连接，而不是 \。

## 依赖库
在运行此代码之前，请确保已经安装了pandas库。如果没有安装，可以使用以下命令安装：pip install pandas

os、re库通常已默认安装。

## 关于输出结果
1. 时间“0:0:50”指的是 0:0:50.00 - 0:0:50.99，即这一秒的开始到结束。原始数据有毫秒，程序直接去掉了毫秒，而非进行四舍五入，因此会和 WPS Excel 统计结果不相符。

2. 程序会输出最高峰时间戳、次高峰时间戳、第三高峰时间戳三个时间戳，若最高峰无任何互动激发（比如是视频的最开始，最开始是弹幕的高峰的情况很常见），则选次高峰，再不行选第三高峰用于研究。
