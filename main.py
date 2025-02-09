import requests

check_website = input("enter the website link you want to check :")

response = requests.get(f"https://{check_website}")

def avalibality(c_avalibality):
    try:
        if response.status_code == 100 or 200:
            print("Server is working and is ready to get data.")
        else:
            print("Server is not ready.", response)
    except requests.exceptions.RequestException as e:
        print(f"Error while checking {c_avalibality}: {e}")

avalibality(response)
