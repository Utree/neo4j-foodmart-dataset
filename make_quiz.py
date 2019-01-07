import numpy as np
import numpy.random as random
from pandas import Series,DataFrame
import pandas as pd
import os

# このファイルがある場所
THIS_FILE_PATH = os.getcwd()

# sales_dataset
sales_ds = pd.read_csv(THIS_FILE_PATH + "/data/sales.csv")
# product_dataset
product_ds = pd.read_csv(THIS_FILE_PATH + "/data/product.csv")
# time_by_day_dataset
time_by_day_ds = pd.read_csv(THIS_FILE_PATH + "/data/time_by_day.csv")
# store_dataset
store_ds = pd.read_csv(THIS_FILE_PATH + "/data/store.csv")
# product_class_dataset
product_class_ds = pd.read_csv(THIS_FILE_PATH + "/data/product_class.csv")
# customer_dataset
customer_ds = pd.read_csv(THIS_FILE_PATH + "/data/customer.csv")

sales_data = []
# sales と product を内部結合
sales_data = pd.merge(sales_ds, product_ds)
# time_by_day を内部結合
sales_data = pd.merge(sales_data, time_by_day_ds)
# store を内部結合
sales_data = pd.merge(sales_data, store_ds)
# product_class を内部結合
sales_data = pd.merge(sales_data, product_class_ds)
# product_class を内部結合
sales_data = pd.merge(sales_data, customer_ds)

# カリフォルニア州で売られたOnionのデータを選択
something = sales_data[(sales_data["store_state"] == "CA") & (sales_data["product_name"].str.contains("Onions"))]


# カラムを絞る
'''
the_year    	: 購入した年
the_month   	: 購入した月
day_of_month	: 購入した日
the_day	        : 購入した曜日
store_country	: お店の場所(国)
store_state  	: お店の場所(州)
store_type  	: お店の規模
yearly_income	: 顧客の年収
gender      	: 性別
total_children	: 子供の数
education   	: 最終学歴
member_card  	: メンバーカードのグレード
num_cars_owned	: 所有車数
'''
something = something[["the_year", "the_month", "day_of_month", "the_day","store_country", "store_state", "store_type", "yearly_income", "gender", "total_children", "education", "member_card", "num_cars_owned"]]

# csv形式で出力
something.to_csv(THIS_FILE_PATH + 'something.csv')
