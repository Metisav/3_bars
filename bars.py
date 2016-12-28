import json
from math import sqrt, cos


def load_data(filepath):
    data = open(filepath, 'r').read()
    json_data = json.loads(''.join(data))
    return json_data


def get_biggest_bar(data):
    max = 0
    json_string = ""
    for i in data:
        if i['SeatsCount'] > max:
            max = i['SeatsCount']
            json_string = i

    return json_string['Name'], json_string['Address']


def get_smallest_bar(data):
    min = 9999
    json_string = ""
    for i in data:
        if (i['SeatsCount'] < min) & (i['SeatsCount'] != 0):
            min = i['SeatsCount']
            json_string = i
    return json_string['Name'], json_string['Address']


def get_closest_bar(data, longitude, latitude):
    min_distance = 1000000
    json_string = ""
    R = 6371  # radius of the earth in km
    for i in data:
        # x = (lon2 - lon1) * cos( 0.5*(lat2+lat1) )
        x = (float(i['Longitude_WGS84']) - longitude) * \
            cos(0.5 * (float(i['Latitude_WGS84']) + latitude))
        y = float(i['Latitude_WGS84']) - latitude
        d = R * sqrt(x * x + y * y)
        if d < min_distance:
            min_distance = d
            json_string = i
    return json_string['Name'], json_string['Address']


if __name__ == '__main__':
    data = load_data('c.json')
    print(' '.join(get_biggest_bar(data))+" самое большое заведение")
    print(' '.join(get_smallest_bar(data))+" самое маленькое заведение")
    latitude = float(input("enter latitude\n"))
    longitude = float(input("enter longitude\n"))
    print(' '.join(get_closest_bar(data, longitude, latitude)) +
          " ближайшее заведение")
