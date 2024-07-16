import requests

# Colors for console output
class color:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

# URL where XSS payloads are hosted
payloads_url = 'https://raw.githubusercontent.com/payloadbox/xss-payload-list/master/Intruder/xss-payload-list.txt'

# Input the base URL to test
base_url = input("Enter the URL to test (e.g., http://www.example.com/search.php?query=): ").strip()

# Function to fetch XSS payloads from a given URL
def get_xss_payloads(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Split payloads, each on a new line
            payloads = response.text.strip().split('\n')
            return payloads
        else:
            print(color.YELLOW + f"Error: Unable to fetch payloads from GitHub. Status Code: {response.status_code}" + color.END)
            return None
    except Exception as e:
        print(color.YELLOW + f"Error: An error occurred while fetching payloads from GitHub: {str(e)}" + color.END)
        return None

# Fetch XSS payloads
xss_payloads = get_xss_payloads(payloads_url)

if xss_payloads:
    print(color.BLUE + f"Successfully retrieved {len(xss_payloads)} XSS payloads from GitHub." + color.END)

    # Test the URL with all payloads
    for payload in xss_payloads:
        full_url = base_url + payload
        response = requests.get(full_url)
        
        # Check the response to determine if XSS vulnerability exists
        if payload in response.text:
            print(color.GREEN + f"XSS vulnerability found! Payload: {payload}" + color.END)
        else:
            print(color.RED + f"No XSS vulnerability found. Payload: {payload}" + color.END)

else:
    print(color.YELLOW + "Unable to fetch XSS payloads. Please try again or check the GitHub URL." + color.END)
