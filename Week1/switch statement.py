# Match case statements
from random import randint

status_codes = [200, 201, 400, 404, 500, 501]
index = randint(0,5)
http_status = status_codes[index]

match http_status:
    case 200 | 201:
        print(f'{http_status} Success')
    case 400:
        print(f'{http_status} Bad request')
    case 404:
        print(f'{http_status} Not Found')
    case 500 | 501:
        print(f'{http_status} Server Error')
    case _:
        print(f'{http_status} Unknown')