一个能上传到github上的项目必须包含：
- `.env.example` 相当于填放环境变量（api key，vpn等）的模板，行业标准是必须有这个，可以上传github；实际操作的时候需要复制单独建立一个.env，不能上传github
- `.gitinore` 告诉 GitHub 哪些文件不要上传（包括API key、缓存文件、临时文件）
- `readme.md` 这是什么、怎么跑起来、你做了什么决策。
- `requirements.txt` 记录你的 Python 项目需要安装哪些包。

python基础代码
- `print("")` 写出""内的内容，记住一定要加""
- `python xx.py` 运行python文件（记住一定首先要cd到python文件在的文件夹），就写python 后面空格＋python文件名即可
