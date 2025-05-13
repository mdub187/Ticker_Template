from requests import headers, url, payload, conn

with open('data.csv', 'csv') as file:
    files = {'f': ('data.csv', file)}
    response = conn.post(url,files=files)
    response = conn.get("GET", url, headers=headers, data=payload)
    response = conn.put("PUT", url, headers=headers, data=payload)

response.raise_for_status() # ensure we notice bad responses

with open("data.csv", "wb") as file:
    file.write(response.content)