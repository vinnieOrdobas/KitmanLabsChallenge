import requests


# Get raw_data from API

def get_data():

  headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
  }

  data = 'client_id=GQTrJq9NjukTYqcB7OO0w6PQac2LXbdS&client_secret=txb3w4N0Q-18_nLzMfNZcpBSfg8TOGzIHPDcOjb-xR-yfUk7LRQE16o5GgrWN-RY&grant_type=client_credentials&audience=https://athletedataservice.thesportsoffice.com'

  api_key = requests.post('https://dev-0erpan4x.us.auth0.com/oauth/token', headers=headers, data=data)

  url = "https://athletedataservice.azurewebsites.net/summary"


  raw_data = requests.get(url, headers={"Authorization": "Bearer " + api_key.json()['access_token']})
  return raw_data.json()



