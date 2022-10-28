import traceback

import requests
import config

if __name__ == '__main__':
    try:

        img = requests.get('https://static.escolakids.uol.com.br/2021/05/golfinho.jpg')
        print(img)

        with open('golfinho.jpg', 'wb') as f:
            f.write(img.content)

    except:
        traceback.print_exc()