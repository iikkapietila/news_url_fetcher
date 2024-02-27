from http import HTTPStatus
import requests
import time
import datetime
import csv
print("http status:", HTTPStatus.OK, "\n\n")

datetimestr = datetime.datetime.now()
datetimestr = str(datetimestr)
datetimestr = datetimestr.replace(" ", "-")
datetimestr = datetimestr.replace(":", "-")
datetimestr = datetimestr.replace(".", "-")
datetimestr = str(datetimestr + "-euronews")

csvfile = open("{}.csv".format(datetimestr), "a", encoding="utf-8", newline="")
writer = csv.writer(csvfile, delimiter=";")

def url_fetcher(fi):
    # Replace placeholder text "your search string here" below with your own search string
    site_request = requests.get("https://www.euronews.com/search?query=your_search_string_here&p={}".format(fi))
    site_str = site_request.text

    #site_str.find(ur"<a class="m-object__description__link " rel="bookmark" href=")
    x = "<a rel=\"bookmark\" class=\"m-object__title__link"
    y = "article data-nid"

    stra = "m-object__img"
    strb = "a href=\""
    strc = "class=\"media__img__link\""

    #print(site_str)
    #print(len(site_str))
    #print(site_str.count(stra))

    istra = 0
    istrb = 0
    istrc = 0
    istrd = 0
    i = 1

    while i <= 17:
        try:
            istra = site_str[istra:].find(stra) + istra

            istrb = site_str[istra:istra+300].find(strb) + istra
            istrc = site_str[istrb:istrb+300].find(strc) + istrb
            #print(istra, istrb, istrc, end=" ")
            link = str(site_str[istrb:istrc])[0:-5]
            full_link = link.replace("a href=\"", "https://www.euronews.com")
            full_link = full_link.replace("\"", "")
            full_link = full_link.strip()
            print("Page:", fi, "Item n:", i, full_link)
            istra = site_str.find(link)+len(link)

            writer.writerow([full_link])

            #time.sleep(0.01)
            i+=1

        except:
            continue

fi = 1
while fi <= 92:
    url_fetcher(fi)
    fi+=1

csvfile.close()