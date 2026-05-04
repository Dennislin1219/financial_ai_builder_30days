## 文件读写

1. 文件读写基础
`open()` 是Python读写文件的函数，`with` 是自动管理文件开关的语法。在AI开发里用来**保存对话记录、读取财报数据、存储API结果**，任何需要持久化数据的场景都会用到。聊天机器人需要把对话历史保存到文件，下次启动还能接着聊。这就需要文件读写。
- 基础用法，需注意
	- open前基本都要跟with：加了with会open操作完后自动关闭文件，即使发生异常也不会出现文件被锁住的问题
	- 会自动创建portfolio.txt在python文件的所在文件夹
	- 一定要加encoding='utf-8'，这样中文不会出现乱码（还有其他标准比如ASCII美国标准，只支持英文），但utf-8用的是最多的国际标准
	- 这里只能读写.csv, .md, .txt等纯文本文件，docx / pdf等文件需要二进制专门的库
```
# 写入文件（'w'模式，覆盖写）
with open('portfolio.txt', 'w', encoding='utf-8') as f:   # 打开文件，自动关闭
    f.write('AAPL, 185.5, 买入\n')                        # 写入一行，\n是换行
    f.write('NVDA, 875.3, 买入\n')                        # 再写一行
    f.write('TSLA, 175.0, 观望\n')                        # 再写一行

# 一次写入writelines()
lines = ['AAPL, 185.5, 买入\n', 'NVDA, 875.3, 买入\n', 'TSLA, 175.0, 观望\n'] 
with open('portfolio.txt', 'w', encoding='utf-8') as f: 
	f.writelines(lines) # 一次写入整个列表

# 'a'：追加写（在文件末尾继续写，不清空原内容）
with open('portfolio.txt', 'a', encoding='utf-8') as f:
    f.write('MSFT, 415.2, 买入\n')    # AAPL那行还在，MSFT加在后面

# 'r'：读取（三种读法）
with open('portfolio.txt', 'r', encoding='utf-8') as f:
    content = f.read()                # 读取全部内容，返回字符串

with open('portfolio.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()             # 读取所有行，返回列表
    print(lines)                      # → ['AAPL, 185.5, 买入\n', 'MSFT, 415.2, 买入\n']

with open('portfolio.txt', 'r', encoding='utf-8') as f:
    for line in f:                    # 逐行读取，大文件时省内存
        print(line.strip())           # strip()去掉每行末尾的\n
```

| 模式     | 文件存在 | 文件不存在 | 能读  | 能写  |
| ------ | ---- | ----- | --- | --- |
| `'r'`  | 正常打开 | 报错    | ✅   | ❌   |
| `'w'`  | 清空重写 | 新建    | ❌   | ✅   |
| `'a'`  | 追加内容 | 新建    | ❌   | ✅   |
| `'r+'` | 正常打开 | 报错    | ✅   | ✅   |
2. JSON文档读写
JSON是**数据交换的通用格式**，长得像Python字典但是**字符串**。JSON文档存在的原因是1）JSON专门给所有语言和系统之间互相传数据用（任何计算机语言，包括Java，python都能看懂），如果没有JSON，直接用python调用Claude API，Anthropic的服务器可能是用Java/Go写的，它不认识Python字典；2）JSON文档有结构，有明确的key和value，但txt和md就没有，所以只能用JSON作为API数据传输的文件。在AI开发里，API返回的所有数据都是JSON格式，发给API的参数也是JSON，理解JSON等于理解AI应用的数据流。
- JSON基础操作
	- `json` 是Python内置标准库，不用安装但必须import
	- 用json.dumps转化成的字符串，和python自带的str，格式会些许不一样。比如json.dumps的字符串习惯用双引号（vs. python字符串用单引号），json用true（vs. python用True）。`str()` 只是Python自己的文字表示，发给其他系统会报错。`json.dumps()` 输出的是**标准JSON格式**，全世界所有语言都能读。
```
import json

# ===== 字符串相关 =====

# json.dumps()：Python对象 → JSON字符串
data = {"ticker": "AAPL", "price": 185.5, "tags": ["科技", "买入"]}
json_str = json.dumps(data, ensure_ascii=False, indent=2) # `ensure_ascii=False` 支持中文，`indent=2` 让格式好看
print(json_str)           # 打印出来是字符串，长得像字典但不是
print(type(json_str))     # → <class 'str'>

# json.loads()：JSON字符串 → Python对象
back = json.loads(json_str)
print(back["price"])      # → 185.5（float，可以做计算）
print(type(back))         # → <class 'dict'>

# ===== 文件相关 =====

# json.dump()：Python对象 → 直接写入JSON文件
with open("stock.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# json.load()：JSON文件 → 直接读成Python对象
with open("stock.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
print(loaded["ticker"])   # → AAPL
```

| 操作场景       | 使用函数           |
| :--------- | :------------- |
| API返回的是字符串 | `json.loads()` |
| 从本地文件读     | `json.load()`  |
| 存到本地文件     | `json.dump()`  |
| 发给API前转字符串 | `json.dumps()` |

## 报错处理

1. try / except相关
`try/except` 是Python的错误处理机制，让程序出错时不崩溃而是优雅地处理。在AI开发里调用API随时可能失败（网络断了、参数错了、余额不足），AI Agent项目必须要有报错处理。
- 基础应用
	- try下面必须要return值，如果没有错误就会返回try下面的值
	- 两个except的意思是出了不同的错，分别怎么处理
	- `e` 就是错误信息本身，`as e` 是把错误信息存进变量 `e`，方便打印出来看
```
import json

data = '{"ticker": "AAPL", "price": 185.5}'   # 正常JSON字符串

try:
    result = json.loads(data)                  # 尝试解析JSON
    print(result["ticker"])                    # 尝试取key
except json.JSONDecodeError as e:             # JSON格式错误
    print(f"JSON解析失败：{e}")
except KeyError as e:                         # key不存在
    print(f"找不到key：{e}")
```

```
# json库特有的错误，要加json.前缀
json.JSONDecodeError    # JSON格式错误，属于json库

# Python内置的错误，直接用，不需要前缀
KeyError                # 字典key不存在，Python内置
ValueError              # 值类型错误，Python内置
FileNotFoundError       # 文件不存在，Python内置
TypeError               # 类型错误，Python内置
ZeroDivisionError       # 除以零，Python内置
```
- 同时捕获多个日常
```
# 同时捕获多个异常 
try: 
	price = float("abc") 
except (ValueError, KeyError) as e: # 两种错误用括号括起来 
	print(f"出错了：{e}")
```
- finally：无论成功失败都执行
```
try: 
	result = 100 / 0 # ZeroDivisionError 
except ZeroDivisionError as e: 
	print(f"除零错误：{e}") 
finally: 
	print("无论如何都执行这里") # 一定会跑到这行
```
- raise：自己在定义函数的时候，主动触发一个错误，必须要配合if（而非python或JSON内置错误）
```
# raise：主动抛出异常 
def check_price(price): 
	if price < 0: 
		raise ValueError(f"股价不能为负数：{price}") # 主动报错 
	return f"股价正常：{price}" 

try: 
	print(check_price(-10)) # 传入负数，触发raise 
except ValueError as e: 
	print(f"捕获到错误：{e}")
```
