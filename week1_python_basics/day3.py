import json

good_data = '{"ticker": "AAPL", "price": 185.5, "pe": 28}'
bad_json = '这不是JSON'
missing_key = '{"ticker": "TSLA"}'
negative_price = '{"ticker": "NVDA", "price": -100}'

def safe_parse(json_str):
    try:
        data = json.loads(json_str)           # 填：解析哪个变量
        
        if data["price"] < 0:          # 填：判断条件
            raise ValueError(f"股价不能为负数：{data['price']}")        # 填：错误信息
            
        return data                      # 成功返回字典
        
    except json.JSONDecodeError as e:
        print(f"JSON格式错误：{e}")
    except KeyError as e:                     # 填：缺少key是什么错误
        print(f"缺少price字段：{e}")
    except ValueError as e:                     # 填：捕获ValueError
        print(f"股价不能为负数：{e}")
    finally:
        print('解析完成')                              # 填：打印"解析完成"
    
    return None                          # 失败返回None

# 测试四种情况
for data in [good_data, bad_json, missing_key, negative_price]:
    print(safe_parse(data))