网页地址：https://branddb.wipo.int/

加密类型：AES 加密

代码运行 ：

window环境

```powershell
# 创建虚拟环境
python -m venv venv
# 激活虚拟环境
venv\Scripts\activate
# 安装依赖
pip install -r requirements.txt
```

macOS 和 Linux 环境

```bash
# 创建虚拟环境
python -m venv venv
# 激活虚拟环境
source venv/bin/activate
# 安装依赖
pip install -r requirements.txt
```

简介：代码只实现的wipo网站的快速搜索功能的接口，需要更改更高级的搜索方式同理，加密方式也是一样的。

运行结果：为对应的csv文件，里面的数据时根据json的对应数据格式，未进行数据处理。

代码日期：2024/4/10