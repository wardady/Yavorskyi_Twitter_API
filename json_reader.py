import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def read_json(par, amount):
    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1):
        print("Please input username!")
        return -1
    users_d = {}
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': str(amount)})
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    js = json.loads(data)
    for u in js['users']:
        users_d[u['screen_name']] = u[par]
    return users_d


friends = read_json('status', 5)
for k in friends:
    print(k, '\n' + friends[k]['text'])
    print("10")
