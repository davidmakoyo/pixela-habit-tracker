import requests

USERNAME = "davidmakoyo"
TOKEN = "189027348901272390847019234"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph",
    "name": "Habit Graph",
    "unit": "Km",
    "type": "float",
    "color": "ichou",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph"

pixel_params = {
    "date": "20230615",
    "quantity": "25"
}

# response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)


pixel_edit_endpoint = f"{pixel_endpoint}/{pixel_params['date']}"

pixel_update_params = {
    "quantity": "9",
}

# response = requests.put(url=pixel_edit_endpoint, json=pixel_update_params, headers=headers)
# print(response.text)

response = requests.delete(url=pixel_edit_endpoint, headers=headers)
