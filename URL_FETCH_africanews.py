from http import HTTPStatus
import requests
import time
import datetime
import csv
print("http status:", HTTPStatus.OK, "\n")

datetimestr = datetime.datetime.now()
datetimestr = str(datetimestr)
datetimestr = datetimestr.replace(" ", "-")
datetimestr = datetimestr.replace(":", "-")
datetimestr = datetimestr.replace(".", "-")
datetimestr = str(datetimestr + "-africanews")

csvfile = open("{}.csv".format(datetimestr), "a", encoding="utf-8", newline="")
writer = csv.writer(csvfile, delimiter=";")

url_suffix_list = []

start = datetime.datetime(2019,1,23)
end = datetime.datetime.today()
daterange = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

for item in daterange:
    item = str(item)
    url_str_y = item[0:4]
    url_str_m = item[5:7]
    url_str_d = item[8:10]
    url_suffix = ("{}/{}/{}/".format(url_str_y, url_str_m, url_str_d))
    url_suffix_list.append(url_suffix)

#print(url_suffix_list)

def url_fetcher(url_suffix_list):
    for urlsuffix_item in url_suffix_list:
        full_date_url = ("https://www.africanews.com/{}".format(urlsuffix_item))
        site_request = requests.get(full_date_url)
        site_str = site_request.text
        #print(urlsuffix_item, full_date_url)

        # Replace "your search string here" part below with your own search string
        stra = "<a href=\"/country/your search string here/\""
        strb = "<a href=\"/{}".format(urlsuffix_item)
        strc = "\">"

        #print(site_str)
        #exit()
        #print(len(site_str))

        if (site_str.count(stra)) == 0:
            print(urlsuffix_item, site_str.count(stra))
            continue

        else:
            istra = 0
            istrb = 0
            istrc = 0
            istrd = 0
            i = 0

            while i < (site_str.count(stra)):
                i+=1
                try:
                    istra = site_str[istra:].find(stra) + istra
                    istrb = site_str[istra:].find(strb) + istra
                    istrc = site_str[istrb:].find(strc) + istrb
                    print(urlsuffix_item, i, istra, istrb, istrc, end=" ")
                    link = str(site_str[istrb:istrc])
                    full_link = link.replace("a href=\"", "https://www.africanews.com")
                    full_link = full_link.replace("<", "")

                    print(full_link)

                    writer.writerow([urlsuffix_item[0:-1], full_link])
                    istra = site_str[istra+50:].find(stra) + istra

                except:
                    print("except break")
                    break
    return

url_fetcher(url_suffix_list)
csvfile.close()
