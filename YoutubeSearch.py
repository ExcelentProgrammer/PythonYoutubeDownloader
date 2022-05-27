from youtube_search import YoutubeSearch
from pprint import pprint
from json import *
def videosearch(check):
    results = YoutubeSearch(check, max_results=50).to_json()
    results = results.split(" ")
    qidiruv = []
    start = 1
    for t in results:
        if t.startswith("\"/watch?v="):
            t = t.split("/")
            t = t[1]
            t = t.split("\"}")
            t = t[0]
            qidiruv.append(f"http://www.youtube.com/{t}")
            start += 1
    print(qidiruv)
    return qidiruv
