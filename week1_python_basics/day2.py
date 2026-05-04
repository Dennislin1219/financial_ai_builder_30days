# 1. 计算复利

def compound(principal, r, years):
        return round(principal * (1 + r) ** years, 0)

print(compound(10,0.1,4))

# 2. 判断一个数是否是质数 

def prime(input_num):
    if input_num == 1:
        print('否')
    else:   
        for i in range(2, input_num):
            if input_num % i == 0:
                print('否')
                break
        else:
            print('是')

num = int(input('请输入整数：'))
prime(num)
            
# 3. 返回列表的最大值和最小值

def maxmin(numbers:list):
    return f'最大值是{max(numbers)},最小值是{min(numbers)}'


portfolio = ["AAPL", "TSLA", "NVDA"]   # 定义一个股票列表
portfolio.append("MSFT")               # 在末尾加一只股票
portfolio.remove("TSLA")               # 删除指定股票
print(portfolio)                       # 打印当前列表
print(len(portfolio))                  # 打印列表长度


stocks = ["AAPL", "TSLA", "NVDA", "MSFT", "GOOG"]
prices = [185.5, 175.0, 875.3, 415.2, 142.8]
pe_ratios = [28, 65, 45, 32, 22]
shares = [100, 50, 80, 60, 120]

# 生成所有股票的市值列表 values
values = [share * price for share, price in zip(shares, prices)]
print(values)
# 筛选出PE低于35的股票名称列表 value_stocks

value_stocks = [stock for stock, pe in zip(stocks, pe_ratios) if pe < 35]
print(value_stocks)


database = {
    "AAPL": {"price": 185.5, "pe": 28, "rating": "买入"},
    "TSLA": {"price": 175.0, "pe": 65, "rating": "观望"},
    "NVDA": {"price": 875.3, "pe": 45, "rating": "买入"},
}

# 查询 NVDA 的股价和评级
NVDA_dict = database["NVDA"]
NVDA_price = NVDA_dict['price']
NVDA_rating = NVDA_dict.get('rating','noun')

print(NVDA_price)
print(NVDA_rating)

# 把 TSLA 的评级改成 "卖出"
TSLA_dict = database["TSLA"]
TSLA_dict['rating'] = '卖出'

# 新增一只股票 MSFT：股价415.2，PE32，评级买入
MSFT_dict = {}
MSFT_dict['price'] = 415.2
MSFT_dict['pe'] = 32
MSFT_dict['rating'] = '买入'
database['MSFT'] = MSFT_dict

# 删除 TSLA
del database['TSLA']
print(database)

# 遍历整个数据库，打印：