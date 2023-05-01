import requests
from time import sleep
from bs4 import BeautifulSoup

banner = """    
┬ ┬┌─┐┌─┐┬ ┬  ┌─┐┌─┐┌─┐┌┐┌┌┐┌┌─┐┬─┐
├─┤├─┤└─┐├─┤  └─┐│  ├─┤││││││├┤ ├┬┘
┴ ┴┴ ┴└─┘┴ ┴  └─┘└─┘┴ ┴┘└┘┘└┘└─┘┴└─                                                                                                
"""
print("[md5-sha1]")
print("-----------------------------")
print("[?]LUTFEN BIR FORMAT GIRINIZ: ")
print("-----------------------------")
format = input(">>>[+]FORMAT GIRINIZ / [MD5]-[SHA1]: ")

if format =="md5" or format == "MD5":

    print("-----------------------------")
    print("[?]LUTFEN BIR HASH GIRINIZ: ")
    print("-----------------------------")
    md5 = input(">>>[+]MD5 HASH: ")
    print("\n")
    sorgula = "https://md5.gromweb.com/?string={}".format(md5)
    istek_yolla = requests.get(sorgula)
    sleep(3)
    soup = BeautifulSoup(istek_yolla.content, "lxml")
    hash_bilgisi = soup.find_all("em",attrs={"class":"long-content string"})

    for hash in hash_bilgisi:

        print("[?]SEARCH HASH: {}".format(md5))
        print("-----------------------------")
        print("[%]HASH: ".format(hash.txt))
        print("-----------------------------")

elif format =="sha1" or format == "SHA1":

    print("-----------------------------")
    print("[?]LUTFEN BIR SHA1 GIRINIZ: ")
    print("-----------------------------")
    md5 = input(">>>[+]SHA1 HASH: ")
    print("\n")
    sorgula = "https://sha1.gromweb.com/?string={}".format("sha1")

    istek_yolla = requests.get(sorgula)
    sleep(3)
    soup = BeautifulSoup(istek_yolla.content, "lxml")
    hash_bilgisi = soup.find_all("em",attrs={"class":"long-content string"})

    for hash in hash_bilgisi:

        print("[?]SEARCH HASH: {}".format("sha1"))
        print("-----------------------------")
        print("[%]HASH: ".format(hash.txt))
        print("-----------------------------")


