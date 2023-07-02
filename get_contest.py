import requests, json
import time

def get_contest():

    req = requests.get("https://codeforces.com/api/contest.list")
    response = req.text
    contest_list = json.loads(response)['result']
    contest_list.sort(key = lambda x: x['id'], reverse=True)
    contest_list = contest_list[:10]

    secs = abs(int(contest_list[0]['relativeTimeSeconds']))
    name = contest_list[0]['name']
    remaining_time = secs
    return (name, remaining_time)

def get_rank():
    nick = open("nickname.txt").read()
    req = requests.get(f"https://codeforces.com/api/user.rating?handle={nick}")
    response = req.text
    rg = json.loads(response)['result']
    rg = rg[-1]["newRating"]

    return (nick, rg)
