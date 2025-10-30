import requests

GET_CATEG = "https://mobilebackendsimpleflask-belkessambadis2870-99jnbj3w.leapcell.dev/news.categories.get"  # 🔹 replace with your actual deployed URL
GET_NEWS = "https://mobilebackendsimpleflask-belkessambadis2870-99jnbj3w.leapcell.dev/news.all.get"

# Example GET request
r = requests.get(GET_CATEG)
print("Status:", r.status_code)
print("Response:", r.text)