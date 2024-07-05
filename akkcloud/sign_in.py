import lxml.etree
import requests
import os

# get subUrl from primaryUrl
# By default, choose the first href with XPath
primaryUrl = "https://akkcloud.com"
html = requests.get(primaryUrl).text
tree = lxml.etree.HTML(html)
subUrl = tree.xpath("//div[@class='content-top']//a[1]")[0].attrib["href"]

# open session
with requests.Session() as session:
    # login
    payload = {
        "email": os.environ.get("email"),
        "passwd": os.environ.get("password"),
    }
    loginUrl = subUrl + "/auth/login"
    loginRes = (
        session.post(loginUrl, data=payload).text.encode().decode("unicode_escape")
    )
    print(loginRes)

    # checkin
    checkinUrl = subUrl + "/user/checkin"
    checkinRes = session.post(checkinUrl).text.encode().decode("unicode_escape")
    print(checkinRes)
