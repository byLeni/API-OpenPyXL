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

if __name__ == "__main__":
    # search a data list
    while True:
        print('\n- - - where do you want to know ?')
        input_citys = input('\t>> ').split(" ")
        print('input_citys len >> {}'.format(len(input_citys)))
        print(input_citys)
        xy_code = search(input_citys=input_citys, city_data_list=city_data_list)
        print('xy_code >> {}'.format(xy_code))

else:
    def pyxlMain():
        print('\n- - - where do you want to know ?')
        input_citys = input('\t>> ').split(" ")
        print(input_citys)
        xy_code = search(input_citys=input_citys, city_data_list=city_data_list)
        print('xy_code >> {}'.format(xy_code))
        return xy_code
