import requests
from bs4 import BeautifulSoup


def getLinks(url, pageno=1):
    if pageno == 101:
        return

    r = requests.get(url + str(pageno))

    soup = BeautifulSoup(r.content, "html.parser")
    linkler = soup.find_all("h2", {"itemprop": "name"})

    j = 0
    for l in linkler:
        data = l.find_all("a")
        curl = data[0].get("href")

        with open("curl.txt", "a") as dosya:
            dosya.write('"' + curl + '",')

    return getLinks(url, pageno + 1)


def getLogo(logoSource):
    if len(logoSource) == 0:
        return ""
    else:
        for l in logoSource:
            logo = l.get("src")
            break
        return logo


def getimgLinks(imgSource):
    j = 0
    im = []

    if len(imgSource) == 0:
        return ""
    else:
        for i in imgSource:
            im.append(i.get("href"))
            j += 1
        return im


def getRating(ratValue):
    if len(ratValue) == 0:
        return ""
    else:
        return ratValue[0].get("content")


def getPostalcode(postalCode):
    if len(postalCode) == 0:
        return ""
    else:
        return postalCode[0].get("content")


def getlinks(link):
    if len(link) == 0:
        return ""
    else:
        l = link.get("href")
    return l


def gettel(tel):
    if len(tel) == 0:
        return ""

    return tel[0].text.strip().replace(" ", "").replace("\n", " ", 1)


def getdata(data, a=0):
    if len(data) == 0:
        return ""
    elif a == 1 and len(data) == 1:
        return ""
    else:
        return data[a].get("href")


def getmail(data, a):
    try:
        if len(data) == 0:
            return ""
        elif a == 0:
            return data[0].get("href").replace("mailto:", "")
        else:
            return data[a].get("href").replace("mailto:", "")
    except IndexError:
        print("mail hatası")


def gethours(data):
    try:
        if len(data) == 0:
            return ""
        return data[0].text.strip()
    except IndexError:
        print("çalışma saati hatası")


def getdesc(data):
    if len(data) == 0:
        return ""
    return data[0].text


def getname(name):
    try:
        if len(name) == 0:
            return "İsim Tanımlanmadı"
        return name[3].text
    except IndexError:
        return "İsim Tanımlanmadı"


def getcat(cat):
    try:
        if len(cat) == 0:
            return "Kategori Tanımlanmadı"
        return cat[0].text.strip().replace(",", "").replace("\n", "")
    except IndexError:
        return "Kategori Tanımlanmadı"
