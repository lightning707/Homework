import requests
import pprint
import json

params = {
    'subreddit': 'pathofexile',
    'size': 100,
    'sort_type': 'created_utc'
}

resp = requests.get('https://api.pushshift.io/reddit/search/comment', params=params)

print(resp.status_code)
data = resp.json()['data']
# print(data)

comment_list = [comm.get('body') for comm in data]
pprint.pprint(comment_list)

with open('reddit.json', 'w') as fd:
    json.dump(comment_list, fd)
