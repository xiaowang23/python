#coding: utf-8
#�� 0002 �⣺�� 0001 �����ɵ� 200 �������루�����Ż�ȯ�����浽 MySQL ��ϵ�����ݿ��С�
#Auther: wjsaya
from random import choice
import string
import os

def main():
    if os.path.exists("./activecode.code"):
        print ("�Ѿ�����activecode.code�ļ����Ѿ�ɾ��")
        os.remove("./activecode.code")
        
    dict = string.ascii_letters[:]
    #�趨�ֵ�Ϊ'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count = input("�����뼤���������")
    if count == "":
        count = "1"
    length = input("�����뼤���볤�ȣ�")
    if length == "":
        length = "8"

    get_code(dict, length, count)
        
def get_code(dict, length, count):
#���ݸ����ֵ䣬�������ó�������
    for i in range(0,int(count)):
        code = ""
    #ͨ��count���Ƽ����������ѭ������choice�����㼤����
        for i in range(0,int(length)):
            code = code+str(choice(dict))
        save_to_file(code)
    
def save_to_file(code):
#���浽�ļ�
    with open ('activecode.code', 'a') as f:
        f.write(code+'\n')
     
def save_to_mysql(id, code):
    host = ("���������ݿ�����ip��")
    user = ("���������ݿ��û�����")
    pass = ("���������ݿ��Ӧ�û������룺")
    db = ("������ִ�в��������ݿ⣺")
    mysql = pymysql.connect(host, user, pass, db)
    cursor = mysql.cursor()
    sql = """ insert into `active` (`id`, `code`) VALUES
        (`id`, `code`);"""
    
    
if __name__ == "__main__":
    main()
