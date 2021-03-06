'''调用返回自己IP信息的API，其Url如下：http://whois.pconline.com.cn/ipJson.jsp'''

if __name__ == '__main__':
    import requests

    payload = {'key1': 'value1', 'key2': 'value2'}
    web = requests.get("http://whois.pconline.com.cn/ipJson.jsp", params=payload)
    print(web.status_code)
    print(web.text)

    '''请求豆瓣电影中《肖申克的救赎》页面，并在控制台输出请求结果，
    其Url如下：:https://movie.douban.com/subject/1292052/'''

    url = 'https://movie.douban.com/subject/1292052/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}  # 请求表头
    response = requests.get(url, headers=headers)  # 获取请求状态码 200为正常
    if (response.status_code == 200):
        print(response.text)  # 获取输出相应内容
    else:
        print("请求失败!")
