'''
res = requests.get('https://123-179-85-204.mcdn.bilivideo.cn:480/upgcxcode/02/53/268735302/268735302_nb2-1-30080.m4s?expires=1608782204&platform=pc&ssig=FM4K_ly6XK0tXus7jF5xiw&oi=1940629332&trid=33e6de5e2f1d47bebc7e08071ce74fc2u&nfc=1&nfb=maPYqpoel5MI3qOUX6YpRA==&mcdnid=1000890&mid=0&orderid=1,3&agrr=0&logo=60000001","https://cn-jstz-dx-v-01.bilivideo.com/upgcxcode/02/53/268735302/268735302_nb2-1-30080.m4s?expires=1608782204&platform=pc&ssig=FM4K_ly6XK0tXus7jF5xiw&oi=1940629332&trid=33e6de5e2f1d47bebc7e08071ce74fc2u&nfc=1&nfb=maPYqpoel5MI3qOUX6YpRA==&cdnid=4965&mid=0&orderid=2,3&agrr=0&logo=40000000')


path='abc.mp4'
with open (path,'wb') as f:
    f.write(res.content)
    f.close()
'''
