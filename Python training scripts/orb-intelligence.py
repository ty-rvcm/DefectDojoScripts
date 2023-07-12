import requests

# declare API key constant here
API_KEY = "c66c5dad-395c-4ec6-afdf-7b78eb94166a"

proxies = {"http":"http://127.0.0.1:8080", "https":"http://127.0.0.1:8080"} #dictionary / dict

# Get company info by name
def getCompanyByName():
    requestURL = "https://api.orb-intelligence.com/3/match/?api_key=c66c5dad-395c-4ec6-afdf-7b78eb94166a&name=nike&country=us"

    # build request object here
    # request methods:
    # GET, POST, PUT, DELETE, TRACE, PATCH, UPDATE, etc...
    r = requests.get(requestURL)

    if r.status_code == 200: 
        data=r.json()
        
        response_data = data["results"]
        
    
        
        
    
    """
    request_fields
    results_count
    results
    """
    
    """ 
    The task:
    1. Create the request object to pull down the information from the request URL - DONE
        - How do you know the request was successful? - 200 OK response
    2. Use the API_KEY parameter in the request in place of the hardcoded key in the URL -  concatenation of strings/paramaters
    3. Print out the orb number and company name only if the address1 field = "1 BOWERMAN DR" in Beaverton, OR

    Data types:
    1. character: 'a'
    2. integer: 123
    3. long: 23423.12
    4. "This is a string"
    5. dictionary
    6. array : fruit=["apple","pear"]
    7. booleans
    8. list = ArrayList

    Objectives: Understand common processing logic and working with JSON objects in Python
    """

if __name__ == "__main__":
    getCompanyByName()