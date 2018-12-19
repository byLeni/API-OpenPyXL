"""
공공데이터포털: (신)동네예보정보조회서비스 API
공공데이터포털: (신)생활기상지수조회 API
xlsx 파일 분석 후 해당 값을 python 데이터로 변환.

The latest modify day: Thu, December 18, 2018
- from Leni
"""


def search(city_data_list):
    print('\n- - - where do you want to know ?')
    input_citys = input('\t>> ').split(" ")
    print('input_citys len >> {}'.format(len(input_citys)))
    print(input_citys)
    city_level = [None, None, None]
    level = 1

    for input_city in input_citys:
        if city_level[0] is None:
            city_level[0] = search_city(input_city, city_data_list)
            if city_level[0] is not None:
                continue

        if city_level[0] is None and city_level[1] is None:
            for small_city in city_data_list.keys():
                city_level[1] = search_city(input_city, city_data_list[small_city][1])
                if city_level[1] is not None:
                    city_level[0] =small_city
                    break

        elif city_level[1] is None:
                temp_data_list = city_data_list[city_level[0]][1]
                city_level[1] = search_city(input_city, temp_data_list)

        if city_level[0] is None and city_level[1] is None and city_level[2] is None:
            for small_city in city_data_list.keys():
                for dong in city_data_list[small_city][1].keys():
                    city_level[2] = search_city(input_city, city_data_list[small_city][1][dong][1])
                    if city_level[2] is not None:
                        city_level[0] = small_city
                        city_level[1] = dong
                        break
                if city_level[2] is not None:
                    break

        elif city_level[1] is None and city_level[2] is None:
            temp_data_list = city_data_list[city_level[0]][1]
            for dong in temp_data_list.keys():
                city_level[2] = search_city(input_city, temp_data_list[dong][1])
                if city_level[2] is not None:
                    city_level[1] = dong
                    break

        elif city_level[2] is None:
            temp_data_list = city_data_list[city_level[0]][1][city_level[1]][1]
            city_level[2] = search_city(input_city, temp_data_list)

    print(city_level)
    get_city_xyCode(city_level=city_level, city_data_list=city_data_list)

def get_city_xyCode(city_level, city_data_list):
    xy_code = None
    for level in range(len(city_level)-1):
        if city_level[level+1] is not None:
            city_data_list = city_data_list.get(city_level[level])[1]
        else:
            xy_code = city_data_list.get(city_level[level])[0]
            break
    if xy_code is None:
        xy_code = city_data_list.get(city_level[2])

    print('xy_code >> {}'.format(xy_code))

def search_city(input_city, city_data_list):
    for city in city_data_list.keys():
        # print(city)
        if input_city in city:
            return city
        else:
            continue

    return None
