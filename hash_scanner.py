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
print("PLEASE ENTER A FORMAT: ")
print("-----------------------------")
format = input(">>>ENTER A FORMAT / [MD5]-[SHA1]: ")

if format =="md5" or format == "MD5":

    print("-----------------------------")
    print("PLEASE ENTER A HASH: ")
    print("-----------------------------")
    md5 = input(">>>MD5 HASH: ")
    print("\n")
    question = "https://md5.gromweb.com/?string={}".format(md5)
    send_request = requests.get(question)
    sleep(3)
    soup = BeautifulSoup(send_request.content, "lxml")
    hash_info = soup.find_all("em",attrs={"class":"long-content string"})

    for hash in hash_info:

        print("SEARCH HASH: {}".format(md5))
        print("-----------------------------")
        print("HASH: ".format(hash.txt))
        print("-----------------------------")

elif format =="sha1" or format == "SHA1":

    print("-----------------------------")
    print("PLEASE ENTER A SHA1: ")
    print("-----------------------------")
    md5 = input(">>>SHA1 HASH: ")
    print("\n")
    question = "https://sha1.gromweb.com/?string={}".format("sha1")

    send_request = requests.get(question)
    sleep(3)
    soup = BeautifulSoup(send_request.content, "lxml")
    hash_info = soup.find_all("em",attrs={"class":"long-content string"})

    for hash in hash_info:

        print("SEARCH HASH: {}".format("sha1"))
        print("-----------------------------")
        print("SEARCH HASH: ".format(hash.txt))
        print("-----------------------------")


