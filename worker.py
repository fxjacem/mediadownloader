import pyshorteners
import requests
import yt_dlp as yt
from flask import request
from urllib.request import urlopen
from json import load


def link_shorter(long_url):
    url_shortener = pyshorteners.Shortener()
    short_url = url_shortener.tinyurl.short(long_url)

    return short_url


def url_decoder(url):
    # headers.update({'Access-Control-Allow-Origin': '*'})
    # headers = requests.get(url).headers
    # headers.update({'Cross-Origin-Resource-Policy': 'cross-site'})
    # headers.pop('Cross-Origin-Resource-Policy')
    # headers.update({'Access-Control-Allow-Origin': '*'})
    # print('url', req.url, '\nheader:', headers)
    # response = requests.get(url, headers=headers)

    req = requests.get(url)
    print(req.url)

    return req.url


def video_link_parser(input_link):
    ydl = yt.YoutubeDL({'outtmpl': '%(id)s%(ext)s', 'quiet': True, 'warning': False})

    with ydl:
        full_data = dict()
        try:
            result = ydl.extract_info(input_link,
                                      download=False,   # We just want to extract the info
                                      )

            if result['extractor_key'] != '':
                full_data['extractor'] = '[' + result['extractor_key'] + ']'
                full_data['title'] = result['title']

                restore = []
                for data in result['formats']:
                    if (result['extractor_key'] == 'Youtube' and data['ext'] == 'mp4' and data['asr'] is not None) or\
                            (result['extractor_key'] != 'Youtube' and data['ext'] == 'mp4'):
                        resolution = data['resolution']

                        url = data['url']
                        url = url_decoder(url)
                        short_url = url     # link_shorter(url)

                        restore.append({'resolution': resolution,
                                        'url': short_url,
                                        'original_url': url})

                full_data['datas'] = restore
        except:
            pass

    return full_data


def ip_info(addr=''):
    if addr == '':
        url = 'https://ipinfo.io/json'
    else:
        url = 'https://ipinfo.io/' + addr + '/json'
    res = urlopen(url)
    # response from url(if res==None then check connection)
    data = load(res)
    if '192.168.' not in request.remote_addr:
        response = {'ip': data['ip'],
                    'city': data['city'],
                    'country': data['country'],
                    'location': data['loc']}
    else:
        response = ""
    return response
"""
        else:
            idx = [key for key, format in enumerate(result['formats']) if result['format_id'] in format['format_id']]
            restore = result['formats'][idx[0]]['url']
"""