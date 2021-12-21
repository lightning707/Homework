import requests
import pprint

params = {
    'subreddit': 'pathofexile',
    'size': 100
}

resp = requests.get('https://api.pushshift.io/reddit/search/comment', params=params)

print(resp.status_code)
data = resp.json()['data']
# print(data)

comment_list = sorted(list(set([comm.get('body') for comm in data])))
pprint.pprint(comment_list)
