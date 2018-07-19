#coding=gb2312

import requests



def sqli_exploit(url):
    payload = {1:"/C6/Jhsoft.Web.login/newview.aspx?id=1"}
    for a in payload:
        res = requests.get(url + payload[a])
        if "<script>" not in res.text and res.status_code is 200:
            print("[*]:" + url + " | 存在漏洞页面")
            return
        else:
            print("[*]:" + url + " | 不存在漏洞页面")
            return

def run(url):
    sqli_exploit(url)


if __name__ == '__main__':

    while True:
        go = input("(1) 单个检测 (2) 批量检测 (exit) 退出程序：")
        if go == 'exit':
            break
        elif go == 1:
            url = raw_input("Please enter url:")
            if url[:4] != 'http':
                url = 'http://' + url
            run(url)
        elif go == 2:
            filepath = raw_input("FilePath:")
            url_list = open(filepath)
            new_url_list = url_list.readlines()
            for url in new_url_list:
                url = url.strip()
                try:
                    run(url)
                except Exception as e:
                    print(e)
                    pass
        else:
            print("别特么瞎几把输入")
