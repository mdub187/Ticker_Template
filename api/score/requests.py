# from api import requests
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath())))
from dict import *
import http.client
from .. import dict
from dict import API_KEY
from urllib import request
from __init__ import credentials
conn = http.client.HTTPSConnection("v1.basketball.api-sports.io")
url = "https://v1.basketball.api-sports.io/leagues"

payload={}
headers = {
  #'x-rapidapi-key': API_KEY,
  'x-rapidapi-host': 'v1.basketball.api-sports.io'
}

insomnia.environment.get("api/")
console.log()
console.log(insomnia.collectionVariables.get.parameters)
console.log(insomnia.cookies.cookieJar.jarName);
#return "results"

# Get all Standings from one {league} & {season}
get("https://v1.american-football.api-sports.io/standings?league=1&season=2022&team=9"):

# Get all Standings from one {league} & {season} & {team}
#get("https://v3.football.api-sports.io/standings?league=39&team=33&season=2019");

# Get all Standings from one {team} & {season}
#get("https://v3.football.api-sports.io/standings?team=33&season=2019");

# example ping for broncos
#get("https://v1.american-football.api-sports.io/standings?league=1&season=2022&team=10");
