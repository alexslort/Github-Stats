#Alex Slort

import json
from flask import Flask
from github import Github

#pip install flask
#pip install PyGithub

#calls github and flask
#may need github access token if doing multiple request in a row
git = Github()
app = Flask(__name__)

@app.route("/")
def home():
    return "please add '/<user>' to search bar. Ex: '/seantomburke'"

#creates an endpoint for inputed user
@app.route("/<user>")
def get_userData(user):
    totalFork = 0
    totalStar = 0
    totalSize = 0
    avgSize = 0

    #gets user data from github
    user = git.get_user(user)
    userRep = user.get_repos()
    totalRep = userRep.totalCount
    output = []
    langList = []

    #gathers the total values in all user repos
    for repo in userRep:
        totalFork += repo.forks
        totalStar += repo.stargazers_count
        totalSize += repo.size

        #adds languages specified that are not null to a list
        lang = repo.language
        if lang is not None:
            langList.append(lang)

    #counts the amount of times each language is used and sorts them
    cnt = {i:langList.count(i) for i in langList}
    sort = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
    langCnt = str(sort)

    #presents the data in JSON format
    avgSize = round((totalSize / totalRep), 2)
    st = str(avgSize) + "KB"
    userData = {"total repositories": totalRep, "total forks": totalFork, "total stars": totalStar, "average size": st}
    output.append(userData)
   
    return json.dumps({"user data": output, "languages": langCnt})

#route when called will return the stats for repositories that are not forked
@app.route("/<user>/forked")
def get_forked(user):
    totalFork = 0
    totalStar = 0
    totalSize = 0
    avgSize = 0
    repCnt = 0

    #gets user data from github
    user = git.get_user(user)
    userRep = user.get_repos()
    output = []
    langList = []

    #gathers the total values in repos that have no forks
    for repo in userRep:
        if repo.forks_count < 1:
            totalFork += repo.forks
            totalStar += repo.stargazers_count
            totalSize += repo.size
            repCnt += 1

            lang = repo.language
            if lang is not None:
                langList.append(lang)

    cnt = {i:langList.count(i) for i in langList}
    sort = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
    langCnt = str(sort)

    #presents the data in JSON format
    avgSize = round((totalSize / repCnt), 3)
    st = str(avgSize) + "KB"
    userData = {"total repo": repCnt, "total forks": totalFork, "total stars": totalStar, "average size": st}
    output.append(userData)
   
    return json.dumps({"user data": output, "languages": langCnt})


    

    