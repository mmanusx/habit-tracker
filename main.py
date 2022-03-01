import requests
from datetime import datetime

TOKEN = "****"   # burada kendi oluşturduğum şifre görevi görüyor
USERNAME = "mmanus"
GRAPH_ID = "graph1"

############ Step 1 Creating User account https://pixe.la/
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,                       # kendim oluşturdum
    "username": USERNAME,                 # kendim oluşturdum
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)     # şuan json ile işimiz olmadığından text olarak başarılı olup olmadığına baktık


########### Step 2 Creating a graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,                     #id'yi kendim oluşturuyorum
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

headers = {                             # dcumantasyonda graph oluşturma kısmında token ı parametre olarak  vermiyoruz, bunun yerine header da belirtmemizi istiyor
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers) #headers kwargs olduğundan oto çıkmıyor
# print(response.text)

####### Step 3 find path https://pixe.la/v1/users/mmanus/graphs/graph1 and add html end of it https://pixe.la/v1/users/mmanus/graphs/graph1.html
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()   # datetime(year=2022, month=7, day=23)
today_formated= today.strftime("%Y%m%d")
pixel_data = {
    "date":today_formated , # https://www.w3schools.com/python/python_datetime.asp
    "quantity": "9.55"
}
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)


#### put() method for updating inputs
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_formated}"
update_data = {
    "quantity":"100"
}

# response = requests.put(url=update_endpoint, json=update_data, headers=headers)

####headers delete todays data

response = requests.delete(url=update_endpoint,headers=headers)