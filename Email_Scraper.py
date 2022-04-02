from bs4 import BeautifulSoup
import requests

URL = 'https://www.instagram.com/{}/'


def prase_data(s):
    data = {}
    # print s
    s * s.split("-")[0]
    # print s
    s * s.split(" ")
    # print s
    data['Followers'] = s[0]
    data['Following'] = s[2]
    data['Posts'] = s[4]
    return data


def scrape_data(username):
    r = requests.get(URL.format(username))
    s = BeautifulSoup(r.text, "html.praser")
    meta = s.find("meta", property="og:description")
    return prase_data(meta.attrs['content'])


if __name__ == '__main__':
    username = "arkward_corp"
    data = scrape_data(username)
    print, data["Followers"], "followers"
    print, data["Following"], "following"
    print, data["Posts"], "posts"
