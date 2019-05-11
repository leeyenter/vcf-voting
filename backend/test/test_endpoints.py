import requests
import json

url = "http://localhost:8080"
session = requests.Session()

#POST to /login
print("POST incorrectly to /login")
data = {"username": "thisiswrong", "password": "obviously"}
r = session.post(url= url + "/login", json = data)
print(r.content, end="\n\n")

#POST to /login
print("POST correctly to /login")
data = {"username": "admin", "password": "password"}
r = session.post(url= url + "/login", json = data)
print(r.content, end="\n\n")

#POST maxVotes = -1 to /admin/ballots
print("POST maxVotes = -1 to /admin/ballots")
data = {
    "position": "Chairman",
    "names": ["Xiao Ming", "Xiao Bai", "Andy Tan"],
    "maxVotes": -1 }
r = session.post(url = url + "/admin/ballots", json = data)
print(r.content, end="\n\n")

#POST names = string to /admin/ballots
print("POST names = string to /admin/ballots")
data = {
    "position": "Chairman",
    "names": "Xiao Ming",
    "maxVotes": 1 }
r = session.post(url = url + "/admin/ballots", json = data)
print(r.content, end="\n\n")

#POST correctly to /admin/ballots
print("POST correctly to /admin/ballots")
data = {
    "position": "Chairman",
    "names": ["Xiao Ming", "Xiao Bai", "Andy Tan"],
    "maxVotes": 1 }
r = session.post(url = url + "/admin/ballots", json = data)
print(r.content, end="\n\n")

#GET from /admin/ballots/id
ballotId = json.loads(r.content)["id"]
print("GET from /admin/ballots/" + ballotId)
r = session.get(url = url + "/admin/ballots/" + ballotId)
print(r.content, end="\n\n")

#GET from /admin/ballots/id
data = {
    "position": "Treasurer",
    "names": ["Xiao Ming", "Xiao Bai", "Andy Tan"],
    "maxVotes": 1 }
r = session.post(url = url + "/admin/ballots", json = data)
print("GET from /admin/ballots/")
r = session.get(url = url + "/admin/ballots")
print(json.loads(r.content), end="\n\n")