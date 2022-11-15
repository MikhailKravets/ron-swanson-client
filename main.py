from pprint import pprint

from ron_swanson.api import RonSwanson

if __name__ == '__main__':
    ron = RonSwanson()
    pprint(ron.search("food"))
    print("Merge Me")
