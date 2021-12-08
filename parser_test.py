from worker import video_link_parser, ip_info


# url = 'https://www.porntube.com/videos/steamy-babe-alix-lynx-drilled-muff_7564440'
# url = 'https://videa.hu/videok/felnott/isteni-baszni-a-tusoloban-Ww07TYmp4RN439Uk'
# url = 'https://fb.watch/9JqdvOOOh0/'
# url = 'https://www.youtube.com/watch?v=WpYLPIMxzaU&t=428s'
# url = 'ffcitRgiNDs'
# url = 'https://videa.hu/videok/zene/depeche-mode-a-question-of-OS4trhQQXIW85qjd'
url = 'https://www.youtube.com/watch?v=St552jpMbzU'

parsed = video_link_parser(url)
if len(parsed) == 3:
    print('\n', parsed['extractor'], '-', parsed['title'])
    for data in parsed['datas']:
        print(data['resolution'], ':', data['url'])     # , ',', data['original_url'])
else:
    print('\n No data - Sorry!')
