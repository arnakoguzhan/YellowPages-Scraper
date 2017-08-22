import requests
from bs4 import BeautifulSoup
import YPClass
import sqlite3
import time
import datetime
import getvalue

j = 1

con = sqlite3.connect("companydata.db")
cursor = con.cursor()


def addtodb(id , n, d, a, l, ln, lo, t, w, m, c, r, rp, rn, i, cr, sh, fh, fb, tw, yo, lnk, ig, pl, pc):
    cursor.execute(
        "INSERT INTO stores (storeId, storeName, storeDesc, storeAddress, lat, lng, logoUrl, tel, web, mail, catName, rating, ratePozitif, rateNegatif, isFeatured, crLink, startHour, finishHour, fbUrl, twUrl, yoUrl, lnUrl, igUrl, plusUrl, postalCode) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (id,n, d, a, l, ln, lo, t, w, m, c, r, rp, rn, i, cr, sh, fh, fb, tw, yo, lnk, ig, pl, pc))


def addtodbimg(u, t, id, ca, ua):
    cursor.execute("INSERT INTO photos (imgUrl, imgThumb, storeId, createdAt, updatedAt) VALUES (?,?,?,?,?)", (u, t, id, ca, ua))






for i in getvalue.data:
    curl = "https://yellowpages.com.tr" + i
    req = requests.get(curl)
    soup = BeautifulSoup(req.content, "html.parser")

    # get name of company
    cName = soup.find_all("span", {"itemprop": "name"})
    cName = YPClass.getname(cName)

    # get company Logo
    cLogo = soup.find_all("img")
    cLogo = YPClass.getLogo(cLogo)

    # get company images and url
    cImages = soup.find_all("a", {"class": "fancybox-thumb"})
    cImages = YPClass.getimgLinks(cImages)

    # get company categories
    cCat = soup.find_all("span", {"class": "categories"})
    cCat = YPClass.getcat(cCat)

    # get company rating
    cRatV = soup.find_all("meta", {"itemprop": "ratingValue"})
    cRatV = YPClass.getRating(cRatV)

    # cRatC = soup.find_all("meta", {"itemprop": "reviewCount"})
    # cRatC = YPClass.getRating(cRatC)

    cRatWR = soup.find_all("meta", {"itemprop": "worstRating"})
    cRatWR = YPClass.getRating(cRatWR)

    cRatBR = soup.find_all("meta", {"itemprop": "bestRating"})
    cRatBR = YPClass.getRating(cRatBR)

    # get Company Address
    cAddress = soup.find_all("div", {"class": "col-sm-8 col-xs-12"})
    cAddress = cAddress[0].text.strip().replace("\n", "")

    cPostalCode = soup.find_all("meta", {"itemprop": "postalCode"})
    cPostalCode = YPClass.getPostalcode(cPostalCode)

    # get company information and social links
    cTel = soup.find_all("div", {"class", "dropdown-menu phone-dropdown"})
    cTel = YPClass.gettel(cTel).splitlines()
    tel = cTel[0]

    cWM = soup.find_all("ul", {"class", "list-inline list-unstyled"})
    cWMurl = cWM[0].find_all("a", {"itemprop": "url"})
    cWebsite = YPClass.getdata(cWMurl)

    cWMmail = cWM[0].find_all("a", {"rel": "nofollow"})
    cMail = YPClass.getmail(cWMmail, len(cTel))


    cFB = soup.find_all("a", {"class", "fb"})
    cFB = YPClass.getdata(cFB, 1)

    cTW = soup.find_all("a", {"class", "tw"})
    cTW = YPClass.getdata(cTW, 1)

    cINST = soup.find_all("a", {"class", "inst"})
    cINST = YPClass.getdata(cINST)

    cIN = soup.find_all("a", {"class", "in"})
    cIN = YPClass.getdata(cIN)

    cGP = soup.find_all("a", {"class", "gp"})
    cGP = YPClass.getdata(cGP)

    cYT = soup.find_all("a", {"class", "yt"})
    cYT = YPClass.getdata(cYT)

    # Get Company description
    cDesc = soup.find_all("div", {"class", "company-overview"})
    cDesc = YPClass.getdesc(cDesc)

    cWorkTime = soup.find_all("div", {"class", "col-md-9 col-sm-9"})
    cWorkTime = YPClass.gethours(cWorkTime)

    cLat = soup.find_all("meta", {"property": "place:location:latitude"})
    cLat = YPClass.getRating(cLat)

    cLng = soup.find_all("meta", {"property": "place:location:longitude"})
    cLng = YPClass.getRating(cLng)

    zaman = time.time()
    tarih = str(datetime.datetime.fromtimestamp(zaman).strftime('%Y-%m-%d %H:%M:%S'))

    addtodb(j, cName, cDesc, cAddress, cLat, cLng, cLogo, tel, cWebsite, cMail, cCat, cRatV, cRatBR, cRatWR, 0, curl, cWorkTime, cWorkTime, cFB, cTW, cYT, cIN, cINST, cGP, cPostalCode)

    for im in cImages:
        addtodbimg(im, im, j, tarih, tarih)


    print("db'ye bir kayıt daha eklendi")
    j += 1
    con.commit()

con.close()
print("program sonlandı")