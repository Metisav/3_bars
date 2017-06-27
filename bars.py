import json
import sys
import os
from math import sqrt, cos


def load_json_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(data):
    return max(data, key=lambda a: a['SeatsCount'])


def get_smallest_bar(data):
    return min(data, key=lambda a: a['SeatsCount'])


def get_closest_bar(data, longitude, latitude):
    min_distance = 1000000
    json_string = ""
    earth_radius = 6371  # radius of the earth in km
    for item in data:
        # get formula from here https://stackoverflow.com/questions/15736995/how-can-i-quickly-estimate-the-distance-between-two-latitude-longitude-points
        # x = (lon2 - lon1) * cos( 0.5*(lat2+lat1) )
        coor_x = (float(item['Longitude_WGS84']) - longitude) * \
            cos(0.5 * (float(item['Latitude_WGS84']) + latitude))
        coor_y = float(item['Latitude_WGS84']) - latitude
        current_distance = earth_radius * sqrt(coor_x * coor_x + coor_y * coor_y)
        if current_distance < min_distance:
            min_distance = current_distance
            json_string = item
    return json_string


if __name__ == '__main__':
    try:
        json_data = load_json_data(sys.argv[1])
    except Exception as e:
        raise e
    biggest_bar = get_biggest_bar(json_data)
    smallest_bar = get_smallest_bar(json_data)
    print('Самый большой заведение : {0} находится по адресу {1} и вмещает {2}'.format(biggest_bar['Name'], biggest_bar['Address'], biggest_bar['SeatsCount']))
    print('Самое маленькое заведение : {0} находится по адресу {1} и вмещает {2}'.format(smallest_bar['Name'], smallest_bar['Address'], smallest_bar['SeatsCount']))
    print('Для того чтобы узнать ближайщее заведение введите координаты')
    latitude = float(input("enter latitude\n"))
    longitude = float(input("enter longitude\n"))
    closest_bar = get_closest_bar(json_data, longitude, latitude)
    print('Ближайшее заведение : {0} находится по адресу {1}'.format(closest_bar['Name'], closest_bar['Address']))
