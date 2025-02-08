import requests

check_website = "https://winbloxos.phytonanywhere.com"

response = requests.get(check_website)

def avalibality(c_avalibality):
    try:
        if response.status_code == 100 or 200:
            print("Server is working and is ready to get data.")
        else:
            print("Server is not ready.", response)
    except requests.exceptions.RequestException as e:
        print(f"Error while checking {c_avalibality}: {e}")

avalibality(check_website)