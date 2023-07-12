import requests

# declare API key constant here
API_KEY = "c66c5dad-395c-4ec6-afdf-7b78eb94166a"

proxies = {"http":"http://127.0.0.1:8080", "https":"http://127.0.0.1:8080"}

# Get company info by name
def getCompanyByName():
    r = requests.get("https://api.orb-intelligence.com/3/match/?api_key=c66c5dad-395c-4ec6-afdf-7b78eb94166a&name=nike&country=us", proxies=proxies, verify=False)

    """ 
    Additional logic goes here
    Challenge: Print out the orb number and company name only if the address1 field = "1 BOWERMAN DR" in Beaverton, OR
    """

if __name__ == "__main__":
    getCompanyByName()