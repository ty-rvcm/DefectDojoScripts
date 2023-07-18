import requests

# declare API key constant here
API_KEY = "c66c5dad-395c-4ec6-afdf-7b78eb94166a"

proxies = {"http":"http://127.0.0.1:8080", "https":"http://127.0.0.1:8080"} #dictionary / dict

# Get company info by name
def getCompanyByName():
    requestURL = "https://api.orb-intelligence.com/3/match/?api_key={API_KEY}&name=nike&country=us"

    try:

        # Object built right here
        r = requests.get(requestURL, proxies=proxies)
        # Checks if the request was successful
        if r.status_code == 200: 
            data=r.json()

            response_data = data["results"]

            found_match = False
            
            # Extract relevant information based on condition
            for result in response_data:
                address1 = result.get('address1')
                city = result.get('city')
                state = result.get('state')

                if address1 == '1 BOWERMAN DR' and city == 'Beaverton' and state == 'OR':
                    orb_number = result.get('orb_number')
                    company_name = result.get('name')
                    print(f"ORB Number: {orb_number}")
                    print(f"Company Name: {company_name}")
                    found_match = True
            
            if not found_match:
                print("No matching company found.")
        else:
            print("Request failed with status code:", r.status_code)
    except requests.RequestException as e:
        print("An error has occured during the request:", e)

    if __name__ == "__main__":
        getCompanyByName()

    
    """ 
    The task:
    1. Create the request object to pull down the information from the request URL - DONE
        - How do you know the request was successful? 
            - 200 OK response
    2. Use the API_KEY parameter in the request in place of the hardcoded key in the URL -  concatenation of strings/paramaters
    3. Print out the orb number and company name only if the address1 field = "1 BOWERMAN DR" in Beaverton, OR

    Objectives: Understand common processing logic and working with JSON objects in Python
    """