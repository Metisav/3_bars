import json


def load_data(filepath):
    data = open(filepath, 'r').read()
    json_data = json.loads(''.join(data))
    return json_data

def get_biggest_bar(data):
    max = 0
    for i in data:
        if i['SeatsCount'] > max:
            max = i['SeatsCount']
    return max


def get_smallest_bar(data):
    min = 9999
    for i in data:
        if i['SeatsCount']<min:
            min = i['SeatsCount']
    return min


def get_closest_bar(data, longitude, latitude):
    pass


if __name__ == '__main__':
    data = load_data('data-2897-2016-11-23.json')
    print(get_biggest_bar(data))
    print(get_smallest_bar(data))
