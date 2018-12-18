"""
공공데이터포털: (신)동네예보정보조회서비스 API
공공데이터포털: (신)생활기상지수조회 API
xlsx 파일 분석 후 해당 값을 python 데이터로 변환.

The latest modify day: Thu, December 18, 2018
- from Leni
"""


def search(city_data_list):
    print('where do you want to know ?')
    input_city = input('\t>> ')
    city_level = [None, None, None]

    for level1 in city_data_list.keys():
        print(level1)
        if level1.find(input_city) != -1:
            print('hear')
            city_level[0] = level1
            input_city.replace(input_city, "")

    print('input level 1 {}'.format(input_city))
