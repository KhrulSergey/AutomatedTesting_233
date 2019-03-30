import json
import os.path
import shutil

BASE_DIR = os.path.join( os.path.dirname( __file__ ), '..' )


__author__ = 'Sergey Khrul'


with open(os.path.dirname(os.getcwd()) + "./data/config.json") as f:
    try:
        res = json.load(f)
    except ValueError as ex:
        print(ex)
        res = {}

print(res)


# //    "os": {
# //        "type":"windows",
# //        "version":"8.1"
# //    }.
# //    "browser": {
# //        "type":"chrome",
# //        "version":"56.1"
# //    }
# // ProdURL = "http://php-addressbook.sourceforge.net/demo/"
