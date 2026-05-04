
1. def定义函数
`def` 是定义函数的关键字，函数就是把一段代码打包起来，需要的时候直接调用，不用重复写（类似于AI Agent可以复用的skill，需要input，然后通过一段特定的代码输出output）。在AI开发里，你调用的每一个工具、每一个API请求，底层都是函数。函数最需要的两个因素就是input参数（自变量）和output参数（因变量）。
- 基础应用（注意，函数只有返回值才用return，如果是全部print，就不需要return了）
```
def analyze_stock(stock, price, target):   # def定义函数，括号里是参数（输入）
    rate = (target - price) / price * 100  # 计算上涨空间
    result = f"{stock} 当前价：{price} 目标价：{target} 上涨空间：{round(rate,2)}%"
    return result                          # return把结果返回给调用者

output = analyze_stock("NVDA", 875, 900)  # 调用函数，传入三个参数
print(output)                             # 打印返回值
```
- 默认参数（可以用=）+ return不同结果（和if条件合用）
```
# 默认参数（不传参数时用默认值） 
def get_rating(stock, pe, threshold=30): # threshold默认值是30 
if pe < threshold: 
	return f"{stock}：估值合理" 
else: 
	return f"{stock}：估值偏高" 

print(get_rating("AAPL", 28)) # 不传threshold，用默认值30 
print(get_rating("NVDA", 45, 50)) # 传入50，覆盖默认值
```
- 函数调用函数（函数可以组合使用）
```
# 函数调用函数（组合使用） 
def calc_value(price, shares): # 计算市值 
	return price * shares 

def gen_report(stock, price, shares): # 生成报告，内部调用
	calc_value value = calc_value(price, shares) # 调用上面的函数 
	return f"{stock} 持仓市值：{value}美元" print(gen_report("NVDA", 875, 80)) # → NVDA 持仓市值：70000美元
```
- 关键字参数
```
def analyze_stock(ticker, price, period):
    return f"分析{ticker} | 价格:{price} | 周期:{period}"

# 普通调用：必须按顺序
analyze_stock("AAPL", 185.5, "5y")

# 关键字参数调用：写名字，顺序随意
analyze_stock(ticker="AAPL", period="5y", price=185.5)   # 顺序乱了也没关系
analyze_stock("AAPL", period="5y", price=185.5)          # 混用也行，位置参数要放前面
```
- `*args`和`**kwargs` ：args为不知道几个参数，全部装进tuple；awargs是不知道几个关键字参数，全部装进字典dict，实际开发中 `**kwargs` 比 `*args` 用得多得多
```
# *args：不知道要传几个位置参数时用（打包成tuple）
def calc_total(*args):                   # *args接收任意数量的参数
    print(args)                          # → ('AAPL', 'TSLA', 'NVDA') 打包成tuple
    return sum(args)                     # sum()直接求和

print(calc_total(100, 200, 300))         # → 600，传几个都行
print(calc_total(100, 200))             # → 300，传两个也行

# **kwargs：不知道要传几个关键字参数时用（打包成dict字典）
def stock_info(**kwargs):                # **kwargs接收任意数量的关键字参数
    print(kwargs)                        # → {'ticker': 'AAPL', 'price': 185.5}
    for key, value in kwargs.items():    # 像字典一样遍历
        print(f"{key}：{value}")

stock_info(ticker="AAPL", price=185.5, pe=28)   # 传几个关键字都行

# LangChain/Agent框架源码里经常看到这种写法
def run_agent(prompt, **kwargs):          # 固定参数+不定关键字参数
    model = kwargs.get("model", "claude-sonnet-4-20250514")  # 有就用，没有用默认值
    temperature = kwargs.get("temperature", 0.7)
    max_tokens = kwargs.get("max_tokens", 1000)
    # ... 调用API

# 调用时想传什么就传什么
run_agent("分析NVDA", model="claude-opus-4-20250514", temperature=0.5)
run_agent("分析AAPL")                     # 不传kwargs也行，全用默认值
``` 
- 真实Agent工具中，每个功能 / tool / skill底层都是封装成一个函数
