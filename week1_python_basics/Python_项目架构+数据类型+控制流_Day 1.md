
## python项目架构
- 一个能上传到github上的项目必须包含：
	- `.env.example` 相当于填放环境变量（api key，vpn等）的模板，行业标准是必须有这个，可以上传github；实际操作的时候需要复制单独建立一个.env，不能上传github
	- `.gitinore` 告诉 GitHub 哪些文件不要上传（包括API key、缓存文件、临时文件）
	- `readme.md` 这是什么、怎么跑起来、你做了什么决策。
	- `requirements.txt` 记录你的 Python 项目需要安装哪些包。

## python数据类型

1. **字符串str**
str就是文字内容，必须用引号包起来。在AI开发里，发给大模型的每一条prompt、收到的每一条回复，全都是字符串形式，因此这是最核心的数据类型。以下为常见引申应用：
- **f"{变量名}"
```
# 字符串拼凑整合（拼凑prompt和response）
analyst = "苹果" 
summary = f"{analyst}公司代码是{stock}" # f-string：花括号里直接放变量 
print(summary) # 打印f-string结果,注意print后只能跟返回值的，放改变原对象的方法只会得到None（比如print后放list.append这个动作就是noun）
```
- **len**
```
# 获取字符串长度（统计财报标题字数） 
title = "苹果公司2024年年度财报" 
print(len(title)) # 输出：11
```
- **replace**
```
# 字符串替换（批量替换报告里的旧股票代码） 
old = "持仓：FB 100股" 
new = old.replace("FB", "META") # 把FB替换成META 
print(new) # 输出：持仓：META 100股
```
- **split**
``` 
# 字符串分割（把逗号分隔的持仓列表拆开）
portfolio = "AAPL,TSLA,NVDA,MSFT" 
stocks = portfolio.split(",") # 按逗号(也可按空格、|切割等)切割，变成列表 
print(stocks) # 输出：['AAPL', 'TSLA', 'NVDA', 'MSFT']列表
```
- upper() / lower()
```
# upper() / lower()：股票代码统一大小写（用户输入aapl也能识别） 
code = "aapl" 
print(code.upper()) # → AAPL（全大写） 
print(code.lower()) # → aapl（全小写）
```
- strip()
```
# strip()：清除两端空格（处理从Excel粘贴过来的脏数据） 
messy = " TSLA " 
print(messy.strip()) # → TSLA（去掉两端空格）
```

2. **int和float（整数和小数）**
`int` 是整数（没有小数点），`float` 是小数（有小数点）。在AI开发里，处理股价、仓位、收益率这些金融数据时会大量用到，也会用来做prompt里的动态数字填充。
- 特殊计算符号
```
# int和float运算结果自动变float
/ # 除/
// # 整除//
% # 取余%
abs() # 取绝对值
round(变量，2) # 保留变量的两外小数
== #数学符号的等于
>= & <= #大于等于和小于等于
+= #累加，在for循环里最常见，比如a += 1 等价于a = a + 1,另外-=就是累减，*=和/=是一个道理
** # ^的意思（如2 ** 2 = 4）
sum(列表名)，sum可以求列表数字的综合
```
- int / float和str转换
```
# int()和float()强制转换（处理用户输入或LLLM API返回的数据） 
user_input = "100" # 用户输入的是字符串"100" 
shares = int(user_input) # 转成整数才能做计算 
print(shares * 249.5) # → 24950.0

# 数字必须转成字符串才能拼进prompt（f-string自动帮你转） 
prompt = f"我持有{shares}股NVDA，买入价{price}美元，今日涨跌{change}%，总市值{total}美元，请给出操作建议。"
```

3. bool（布尔值）
布尔值（bool）只有两个值：`True` 和 `False`，就是"是"和"否"。在AI开发里，用来做条件判断，比如判断股票是否值得买入、用户输入是否合法、API返回是否成功。
- 比较运算符（注意等于 / 不等于的符号）
```
# 比较运算符（筛选股票） 
pe_ratio = 25 
print(pe_ratio < 30) # → True（PE低于30，估值合理） 
print(pe_ratio == 25) # → True（注意：判断相等用==，不是=） 
print(pe_ratio != 30) # → True（不等于）
```
- and / or / not多条件筛选（我的量化回测项目里一定需要用到）
```
# and / or / not（多条件筛选） 
price = 150.0 
volume = 8000000 
print(price < 200 and volume > 5000000) # → True（价格低且成交量大，两个都要满足） print(price > 200 or volume > 5000000) # → True（或者，满足一个就行） 
print(not price > 200) # → True（取反，价格不高于200）
```
 - 判断返回数据是否为空（比如LLM返回数据）
```
# bool()转换（判断数据是否为空） 
data = "" # 空字符串，代表没有收到财报数据 
print(bool(data)) # → False（空字符串=False，有内容才是True） 
data = "营收增长20%" 
print(bool(data)) # → True
```

4. 列表list
列表（list）是有序的数据集合，可以**随时增删改查里面的元素（相对应tuple元组不能删改）**。在AI开发里，存对话历史、存批量处理结果、存股票池，全都用列表。==列表在LLM代码里最常见的场景是**存对话历史**，因为chatgpt的history memory其实就是一个列表，并在这个空列表上不断append。==
- 基础操作
```
portfolio = ["AAPL", "TSLA", "NVDA", "MSFT"]

# remove：删除指定元素
portfolio.remove("TSLA")

# append：在末尾加元素
portfolio.append("GOOG")              # → ["AAPL", "TSLA", "NVDA", "MSFT", "GOOG"]

# insert：在指定位置插入（注意先位置再值）
portfolio.insert(0, "BRK")            # 在第0位插入 → ["BRK", "AAPL", ...]

# pop：删除并返回指定位置的元素（默认最后一个）
removed = portfolio.pop()             # 删除最后一个，返回"GOOG"
removed2 = portfolio.pop(0)          # 删除第0个，返回"BRK"

# index：找元素的位置
print(portfolio.index("NVDA"))        # → 2

# in：判断元素是否存在
print("AAPL" in portfolio)            # → True
print("TSLA" in portfolio)            # → True

# sort：排序
prices = [185.5, 875.3, 175.0, 415.2]
prices.sort()                         # 从小到大排序（如果是字母，就是由a到z），直接改变原列表
print(prices)                         # → [175.0, 185.5, 415.2, 875.3]

prices.sort(reverse=True)             # 从大到小
print(prices)                         # → [875.3, 415.2, 185.5, 175.0]

new_prices = sorted(prices)           # 不改prices，返回新列表
```
- 列表切片，规律是`[start:end:step]`，其中end如果是3，则取到第二个，包头不包尾，和range同理。负数从末尾数（最后一个是-1）。另外如果step是负数，默认第一个最后一个，从右往左。
```
prices = [185.5, 175.0, 875.3, 415.2, 210.0, 320.5]

print(prices[0:3])      # 取第0,1,2个 → [185.5, 175.0, 875.3]
print(prices[2:])       # 从第2个取到末尾 → [875.3, 415.2, 210.0, 320.5]
print(prices[:3])       # 从开头取到第2个 → [185.5, 175.0, 875.3]
print(prices[-1])       # 最后一个 → 320.5
print(prices[-3:])      # 最后3个 → [415.2, 210.0, 320.5]
print(prices[::2])      # 每隔一个取一个 → [185.5, 875.3, 210.0]
print(prices[::-1])     # 倒序 → [320.5, 210.0, 415.2, 875.3, 175.0, 185.5]
prices[::2]    # 从左往右，每隔一个 → [185.5, 875.3, 210.0]
prices[::-1]   # 从右往左，每一个  → [320.5, 210.0, 415.2, 875.3, 175.0, 185.5]
prices[::-2]   # 从右往左，每隔一个 → [320.5, 415.2, 175.0]
```
- zip()，把多个列表配对，可快速解决多列表问题
```
stocks = ["AAPL", "TSLA", "NVDA", "MSFT"]
prices = [185.5, 175.0, 875.3, 415.2]
shares = [100, 50, 80, 60]

# zip两个列表
for stock, price in zip(stocks, prices):
    print(f"{stock}：{price}美元")

# zip三个列表
for stock, price, share in zip(stocks, prices, shares):
    value = price * share
    print(f"{stock} | 股价:{price} | 持股:{share} | 市值:{value}")

# zip打印结果
print(list(zip(stocks, prices, values)))
[('AAPL', 185.5, 18550.0), ('TSLA', 175.0, 8750.0), ('NVDA', 875.3, 70024.0), ('MSFT', 415.2, 24912.0), ('GOOG', 142.8, 17136.0), ('META', 505.0, 45450.0)]

# zip转成字典（非常实用！）
stock_dict = dict(zip(stocks, prices))
print(stock_dict)   # → {'AAPL': 185.5, 'TSLA': 175.0, 'NVDA': 875.3, 'MSFT': 415.2}
```
- ==列表推导式（重要！）==
```
[  price  |  for price in prices  |  if price > 200  ]
#  ①取什么  |  ②从哪里取           |  ③过滤条件（可选）
`for` 后面的变量名是当前元素的临时名字，①取什么里必须用到它

prices = [185.5, 175.0, 875.3, 415.2, 142.8, 505.0]
stocks = ["AAPL", "TSLA", "NVDA", "MSFT", "GOOG", "META"]

# 对每个元素做计算（所有股价转港币，汇率7.8）
hkd_prices = [round(price * 7.8, 1) for price in prices]
print(hkd_prices)       # → [1446.9, 1365.0, 6827.3, 3238.6, 1113.8, 3939.0]

# 同时处理两个列表（zip配对生成prompt）
prompts = [f"分析{stock}当前股价{price}美元" for stock, price in zip(stocks, prices)]
print(prompts)          # → ["分析AAPL当前股价185.5美元", ...]

# 嵌套条件（多个过滤条件）
values = [price * share for price, share in zip(prices, [100,50,80,60,120,90])]
big_positions = [v for v in values if v > 20000]   # 只要市值超过2万的
print(big_positions)    # → [70024.0, 24912.0, 45450.0]
```

5. 字典dict
字典（dict）是**键值对**的集合，用`key`找`value`，就像用股票代码查股票信息。**在AI开发里，API返回的JSON数据、对话历史、配置参数，全都是字典格式**。
- 基础操作
```
stock = {                              # 用{}定义字典
    "ticker": "NVDA",                  # key: value，用冒号分隔
    "price": 875.3,
    "pe": 45,
    "rating": "买入"
}

print(stock["ticker"])                 # 用key取value → NVDA
print(stock["price"])                  # → 875.3,但如果无该key会报错
print(stock.get("pe", 0))             # get()取值，找不到key时返回默认值0
print(stock.get("revenue", "无数据")) # key不存在 → 返回"无数据"，不报错
```
- 增加、修改（用update最好！）和删除key
```
stock = {"ticker": "NVDA", "price": 875.3, "pe": 45} 
# 增加/修改key
stock["rating"] = "买入"       # 新增key 
stock["price"] = 900.0        # 修改已有key 
print(stock) 

# update()：批量更新/新增多个key（最常用！）
stock.update({"price": 900.0, "rating": "买入"}) # 改price，新增
rating print(stock) # → {"ticker": "NVDA", "price": 900.0, "pe": 45, "rating": "买入"}

# 嵌套字典可层层取值：
database["NVDA"]["price"]

# 删除key（pop是删除并返回指定key的value）
del stock["pe"]               # 删除pe print(stock)

removed = stock.pop("pe") # 删除pe，返回45 
print(removed) # → 45 
print(stock) # pe已经不在了

```
- 用items / key / value来讲字典转化为list
```
# 遍历字典 
for key, value in stock.items(): # .items()同时取key和value 
	print(f"{key}：{value}") 

# 取所有key和value 
print(stock.keys()) # → dict_keys(['ticker', 'price', 'rating']) print(stock.values()) # → dict_values(['NVDA', 900.0, '买入'])
```
- 字典和列表的合用
```
# 用字典存股票分析结果 
results = {} # 空字典 
stocks = ["AAPL", "TSLA", "NVDA"] 

for stock in stocks: 
	results[stock] = f"{stock}的分析结果" # 股票代码做key，分析结果做value 

print(results["NVDA"]) # → NVDA的分析结果 
print(results.get("MSFT", "未分析")) # → 未分析
```
- 合并两个字典
```
# 合并两个字典（Python 3.9+） 
extra = {"revenue": "600亿", "sector": "科技"} 
merged = stock | extra # 用|合并，返回新字典 
print(merged)
```
- 字典推导式（和列表推导式一样的逻辑）
```
字典推导式（和列表推导式一样的逻辑） 
prices = {"AAPL": 185.5, "TSLA": 175.0, "NVDA": 875.3} 
hkd = {stock: round(price * 7.8, 1) for stock, price in prices.items()} 
print(hkd) # → {"AAPL": 1446.9, "TSLA": 1365.0, "NVDA": 6827.3}
```
## python控制流

1. if / elif / else
`if/elif/else` 是条件判断，让程序根据不同情况走不同的路。在AI开发里用来控制Agent的决策逻辑，比如根据股票评分决定买入、持有还是卖出，或者根据API返回结果决定下一步动作。
- 基础应用（注意每行后加:，每个条件句后用tab空格来区分）
```
price = 150.0                        # 当前股价
target = 200.0                       # 目标价

if price < target * 0.8:             # 如果价格低于目标价80%
    print("强烈买入")                 # 满足条件执行这里
elif price < target:                 # 否则如果价格低于目标价
    print("买入")                     # 满足条件执行这里
else:                                # 以上条件都不满足
    print("观望")                     # 执行这里
```
- if里嵌套if（大条件和小条件）
```
# if里嵌套if（先看大条件，再看小条件） 
price = 150.0 
volume = 3000000 
if price < 160: 
	if volume > 5000000: # 价格低且成交量大，更有把握 
		print("高信心买入") 
	else: 
		print("低信心买入") # 价格低但成交量不足
```
- 多条件判断（结合not, or, and）
```
# if结合and/or（多条件一起判断） 
pe = 25 
debt = 0.3 
if pe < 30 and debt < 0.5: # 两个条件同时满足 
	print("基本面健康，可以买入")
```
- if除了判断数字，也可以判断str和bool
```
# if判断字符串（根据用户输入决定动作） 
user_cmd = "买入" 
if user_cmd == "买入": 
	print("执行买入指令") 
elif user_cmd == "卖出": 
	print("执行卖出指令") 
else: 
	print("无效指令，请重新输入")
```

2. for循环
`for` 循环是让程序自动重复执行一段代码，每次处理**列表里一个元素**。在AI开发里用来批量处理数据，比如遍历10只股票逐个分析、批量发送API请求、逐条处理财报数据。
- for循环基础应用（必须包含变量名，列表）
```
portfolio = ["AAPL", "TSLA", "NVDA", "MSFT"]  # 定义一个股票列表

for stock in portfolio:                         # 依次取出每只股票(stock可以是任何其他符号，for后面的变量名默认是列表里的所有因素，依次取出)
    print(f"正在分析：{stock}")                  # 每次循环打印一只股票
```
- for循环和if结合
```
# 循环里加if判断（筛选出涨幅超过5%的股票） 
changes = [2.3, -1.5, 6.8, 0.4, 5.2] # 每只股票今日涨跌幅 
stocks = ["AAPL", "TSLA", "NVDA", "MSFT", "GOOG"] 

for i in range(len(stocks)): # range(5)→0,1,2,3,4，range是一个输出列表函数，注意包头不包围，比如range(2，3)只输出2，不包含3！range(2,2)是空的！用索引同时取两个列表 
	if changes[i] > 5: 
		print(f"{stocks[i]} 涨幅超过5%：{changes[i]}%")
```
- for循环用于累加（一定要在for外赋予total初始值）
```
# 循环累加（计算投资组合总市值） 
prices = [185.5, 175.0, 875.3, 415.2] # 四只股票价格 
shares = [100, 50, 80, 60] # 对应持股数量 

total = 0 # 初始化总市值为0 
for i in range(len(prices)): 
	total += prices[i] * shares[i] # += 每次累加到total 
	print(f"投资组合总市值：{total}美元")
```
- enumerate函数（可以同时拿编号和值，很有用），如果print就需要搭配list强制展开
```
# enumerate同时获取序号和值（生成带编号的报告） 
portfolio = ["AAPL", "TSLA", "NVDA"] 
for index, stock in enumerate(portfolio): # enumerate自动给每个元素加编号 
	print(f"{index+1}. {stock}") # index从0开始所以+1

portfolio = ["AAPL", "TSLA", "NVDA"] 
print(list(enumerate(portfolio))) # 强制展开 # → [(0, 'AAPL'), (1, 'TSLA'), (2, 'NVDA')]

# 从1开始编号（不用index+1）
for index, stock in enumerate(portfolio, start=1):   # start=1直接从1开始
    print(f"{index}. {stock}")
```
- ==for else，循环没被break打断才执行else，专门处理跑完没触发的情况，while else也一样==

3. while循环
`while` 循环是**满足条件就一直执行**（因此需要在while下用+=等累计符号让变量变化），直到条件变成 `False` 才停下来。和 `for` 循环不同，`for` 是知道要循环几次，`while` 是不知道要循环几次，在AI开发里常用来**持续等待用户输入、重试失败的API请求、持续监控股价直到触发条件**。**while循环==必须有退出条件==，否则死循环**。
- 基础应用
```
price = 100.0                        # 当前股价
target = 150.0                       # 目标价

while price < target:                # 只要股价低于目标价就一直循环
    print(f"当前股价：{price}，未到目标价，继续持有")
    price += 10                      # 每次循环股价涨10（模拟价格上涨）

print(f"目标价达到！当前股价：{price}") # 循环结束后执行
```
- break强制退出循环（常用于while True，如果不break它会一直循环），用于量化止损机制
```
# break强制退出循环（股价暴跌时止损） 
price = 100.0 

while True: # 永远为True，必须靠break退出 
	price -= 5 # 模拟每天下跌5元 
	print(f"当前股价：{price}") 
	if price <= 80: # 跌到80元触发止损 
		print("触发止损，强制卖出！") 
		break # 立刻退出循环
```
- continue跳过当次循环（跳过某些不处理的情况）
```
stocks = ["AAPL", "TSLA", "", "NVDA"] # 数据里有空字符串 
for stock in stocks: 
	if stock == "": # 遇到空数据 
		continue # 跳过这次，直接进入下一次循环 
	print(f"处理股票：{stock}") # 只处理有效数据
```
- 计数器+while
```
attempts = 0 
max_attempts = 3 
while attempts < max_attempts: 
	print(f"第{attempts+1}次尝试调用API...") 
	attempts += 1 # 每次循环计数器+1 
print("重试结束")
```
- try和except是预防报错功能，把可能出错的代码放进 `try`，出错了就跳到 `except` 处理，程序不会崩溃。
```
# try/except/else/finally（完整版，AI开发最常用） 
try: 
	response = "API返回结果" # 模拟API调用 
except Exception as e: # e是错误信息，打印出来方便调试 
	print(f"API调用失败：{e}") 
else: 
	print("API调用成功，处理结果") # try成功才执行 
finally:
	print("无论成功失败都执行，比如关闭连接") # 一定执行
```

## python交互函数
1. input（返回的永远是str）
```
num = input("请输入一个数字：")   # 程序暂停，等你在键盘输入，回车确认
print(num)
print(type(num))                  # 注意：input()返回的永远是字符串！
```
