import http.client;
from optparse import Values;
# from __init__ import credentials
import pandas as pd;
import __init__;
#import ("api.dict");
API_KEY = "2f2d48ebac0ff1195cb9b3ec9cc16293"
conn = http.client.HTTPSConnection;
#GET = f"https://v1.american-football.api-sports.io/standings?league=1&season={year}&team={team}"
headers = {
    'x-rapidapi-host':  (f"{API_KEY}"),
    'x-rapidapi-key': (f"{API_KEY}"),
    'x-rapidapi-pair_key': (f"{API_KEY}"),
    }

def glueConn(conn, url, headers):
	conn.request("GET", url, headers=headers)

year = input()  # Replace with the desired year
team = input()  # Replace with the desired team name
url = f"https://v1.american-football.api-sports.io/standings?league=1&season={year}&team={team}"
glueConn(conn("v1.american-football.api-sports.io"), url, headers)
body = {
	"get": "`${team}`[-1:].score",
	"parameters": ["leagues", "season", "team"],
	"errors": {
		"endpoint": "This endpoint do not exist.",
	},
	"results": 100,
	"response": print("very nice!")
}

res = conn.getresponse()
data = res.read()
write = data
df = pd.DataFrame([data.decode("utf-8")])
df.to_csv("api/score/data.csv", sep=',', encoding='utf-8', index=False)

print(data.decode("utf-8"))
if __name__ == '__main__':
    print(__name__)
