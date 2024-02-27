import csv
import datetime

datetimestr = datetime.datetime.now()
datetimestr = str(datetimestr)
datetimestr = datetimestr.replace(" ", "-")
datetimestr = datetimestr.replace(":", "-")
datetimestr = datetimestr.replace(".", "-")
datetimestr = str(datetimestr + "-newsapi")

my_api_key = #"your newsapi api key here"

from newsapi import NewsApiClient
url = "https://newsapi.org/v2/everything&apiKey={}".format(my_api_key)
print("url =", url)

newsapi = NewsApiClient (api_key = my_api_key)
sources = newsapi.get_sources()

"""
for item in sources["sources"]:
    print(item)
exit()
"""

csvfile = open("{}.csv".format(datetimestr), "a", encoding="utf-8", newline="")
writer = csv.writer(csvfile, delimiter=";")

def get_articles(page_n):
    all_articles = newsapi.get_everything(q='your search string here',
                                          exclude_domains="marketwatch.com, businessinsider.com, investors.com, "
                                                          "biztoc.com, nfl.com, nhl.com, thesportbible.com,"
                                                          "news.vice.com, bleacherreport.com, zacjohnson.com, "
                                                          "marketscreener.com, christianitytoday.com, investing.com,"
                                                          "sabah.com, naturalnews.com, guernicamag.com, dodbuzz.com,"
                                                          "nakedcapitalism.com, techxplore.com, moneycontrol.com, "
                                                          "wnd.com, metropoles.com, sabah.com.tr, patronlardunyasi.com,"
                                                          "yazaroku.com, patheos.com, ibtimes.com, lawyersgunsmoneyblog.com,"
                                                          "vg.no, odatv4.com, removed.com, catholicnewsagency.com ",
                                          #sources="abc-news, al-jazeera-english, associated-press, bbc-news,"
                                          #        "cbs-news, cnn, google-news, independent, nbc-news, newsweek,"
                                          #        "politico, reuters, spiegel-online, the-huffington-post, "
                                          #        "the-washington-post, time, the-times-of-india, national-geographic,"
                                          #        "die-tagesspiegel, cbc-news",
                                          #page_size=100,
                                          sort_by='relevancy',
                                          from_param="2024-01-27",
                                          to="2024-02-27",
                                          page=page_n
                                          #language="en"
                                          )

    print(all_articles["totalResults"])

    for i in all_articles["articles"]:
        row_to_csv_temp = [i["publishedAt"],
                           i["source"]["name"],
                           i["title"],
                           i["url"],
                           i["description"],
                           i["content"]]
        row_to_csv = []

        for i in row_to_csv_temp:
            i = str(i)
            #i = i.replace("\n", "")
            row_to_csv.append(str(i+";"))

        print(row_to_csv)
        writer.writerow(row_to_csv)

counter=1
for counter in range(1,10):
    get_articles(counter)
    counter+=1

csvfile.close()