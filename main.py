"""
공공데이터포털: (신)동네예보정보조회서비스 API
공공데이터포털: (신)생활기상지수조회 API
xlsx 파일 분석 후 해당 값을 python 데이터로 변환.

The latest modify day: Thu, December 18, 2018
- from Leni
"""
from function.control import search
from function.make import make_data

# make a data list
city_data_list = make_data()
# print(city_data_list)

# search a data list
search(city_data_list)
