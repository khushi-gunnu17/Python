# freeapi.api

# pip install requests

import requests

def fetch_random_user_freeapi() :
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    api_data = response.json()

    if api_data["success"] and "data" in api_data :
        user_data = api_data["data"]
        username = user_data['login']['username']
        country = user_data['location']['country']
        return username, country
    else :
        raise Exception("Failed to fetch user data")
    

def main() :
    try :
        username, country = fetch_random_user_freeapi()
        print(f"Username : {username} \nCountry : {country}")

    except Exception as e : 
        print(str(e))


if __name__ == '__main__' :
    main()