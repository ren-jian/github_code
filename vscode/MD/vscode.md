# VScode使用笔记

![奋斗](./assets/奋斗.png)
1、vscode显示中文乱码问题
    解决方法:
    菜单栏:  文件 --> 首选项 --> 设置 --> 搜索
    修改配置"files.autoGuessEncoding": false,
    改为"files.autoGuessEncoding": true,

2、MarkDown
    （1）vscode插件
        markdownlint 语法提示
        Markdown Preview Enhanced

3、中文设置
    Ctrl+shift+P
    Configure Display Language
    zh-CN

4、插件
    Code Runner 运行bat等多种代码。可再文件-首选项-设置-扩展中打开终端窗口。输出栏右键可停止。

5、git
    在setting.json中添加 "git.path": "D:\\Software\\Git\\cmd\\git.exe"