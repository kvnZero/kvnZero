#coding=utf-8

import requests
import json
import os

url = "https://music.163.com/weapi/v1/play/record?csrf_token="

def get_week():
    data = {
        "params": "e1Qer4IFS6TIQuUOU6cis87pNDpZCIJ1+4ESW9AiQ7kdAgP8hWIhfTsBcChN8GS2CvbGHo6DBDGenp2VldCNZXvBWc1VS1nAbqutKQ8W5bp8tDq7nmA0I2wOTQ4NQySyC4T5UIpwXFD3qWMLXv+YbXeYlZiS5K8D1FbB/P2g55NQ1y3gAZKOCMJxu/YFT/0G",
        "encSecKey": "ab1f1594074b3cacf010d2991440bb7ae79ee9419473c66ff7360c0f146a9a3fceb972a2e3b92f8190df0f312021426e9f48682c15e010103a0a2d6218361173af56d059fcaaee83e20dae4d845bf3aae7030425933865392bb4abc8bec8753020f4210b5010d369fc472182a22d478c26a244705a659be178982118d654169b"
    }

    session = requests.session()
    result = session.post(url, data).text;
    json_data = json.loads(result.encode("gbk", 'ignore').decode("gbk", "ignore"))
    weekData = json_data['weekData']
    song_data = []
    for item in weekData:
        ararr = []
        for ar in item['song']['ar']:
            ararr.append(ar['name'])
        song_data.append({"song":item['song']['name']+" - "+'/'.join(ararr), "score": item['score']})
    return song_data

def get_all():
    data = {
        "params": "mK1E/TjrYhVctq3ZDJhUCPWsDppFOFuHcugo/EgTYiSVZiGBLEc9md6df0kTZXx8KuuBJ/if8SZRuU/nk4QJ25ZnT+p1XrULkRJt0X2FUjoXHaWXZ+MoWyjFv2PF8hneqFNxqn/xiJ4h1Nm9+xfKFv+KON7hXwP1IdnNVRLWEKVLIwgDrerEe1ITiX16DUMi",
        "encSecKey": "2c9b9ece93a9fdec68f6fdea8c5793a78b8272bec589e859b610696826fae1cb6cbfb65d10cd60b8c67876ee3624e49c93c11aebe37659d75e1c37960c0d4aa8e4ed370da991d1f7c886eb1eb4388512fb16726fc30af2a1d14dee1c32cbf86cea8997f91462bbf6b399c02f2357b129336413cb1265bd639be77b7e57fbc73c"
    }
    session = requests.session()
    result = session.post(url, data).text;
    json_data = json.loads(result.encode("gbk", 'ignore').decode("gbk", "ignore"))
    allData = json_data['allData']
    song_data = []
    for item in allData:
        song_data.append({"song":item['song']['name']+" - "+item['ar'][0]['name'], "score": item['score']})
    return song_data

songs = get_week()
songs = songs[:5]
i = 0
text = ""
for song in songs:
    text += "%i. 🌈%s\n" % (i, song['song'])
    i += 1

with open('README-base.md', 'r', encoding='utf-8') as f:
    content = f.read()
    new_content = content.replace("{song_list}" , text)

    with open("README.md", 'w+', encoding='utf-8') as new_f:
        new_f.write(new_content)
