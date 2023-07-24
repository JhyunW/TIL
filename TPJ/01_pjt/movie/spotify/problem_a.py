import json
from pprint import pprint


def artist_info(artist):
      {
    "id": 178,
    "name": "Jimin",
    "type": "artist",
    "uri": "spotify:artist:1oSPZhvZMIrWW5I41kPkkY",
    "images": [
        {
            "height": 640,
            "url": "https://i.scdn.co/image/ab6761610000e5eb59f8cfc8e71dcaf8c6ec4bde",
            "width": 640
        },
        {
            "height": 320,
            "url": "https://i.scdn.co/image/ab6761610000517459f8cfc8e71dcaf8c6ec4bde",
            "width": 320
        },
        {
            "height": 160,
            "url": "https://i.scdn.co/image/ab6761610000f17859f8cfc8e71dcaf8c6ec4bde",
            "width": 160
        }
    ],
    "external_urls": {
        "spotify": "https://open.spotify.com/artist/1oSPZhvZMIrWW5I41kPkkY"
    },
    "genres_ids": [
        651,
        816
    ]
}
      pass


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artist_json = open('data/artist.json', encoding='utf-8')
    artist_dict = json.load(artist_json)
    
    pprint(artist_info(artist_dict))
