import requests
import json
from rich import print

def fetch_domain_data(api_key: str):
    """
    Fetches domain URL information from AlienVault's API.

    :param api_key: Your AlienVault OTX API key
    """
    # Prompt user for the domain URL
    
    domain_url = input("Enter the domain (e.g., example.com): ").strip()
    if not domain_url:
        print("Error: Domain URL cannot be empty.")
        return

    # API endpoint
    api_endpoint = f"https://otx.alienvault.com/api/v1/indicators/domain/{domain_url}/general"
   
    # Headers with API key
    headers = {
        "X-OTX-API-KEY": api_key
    }
    
    try:
        # Make the API request
        response = requests.get(api_endpoint, headers=headers)
        response.raise_for_status()  # Raise an error for HTTP error codes
        
        # Parse and display the response data
        data = response.json()
        # Displays response in red
        print("[italic red]\nResponse Data:[/italic red]", locals())
        # Formats json to be more readable
        pretty_response = json.dumps(data, indent=5, sort_keys=True )
        print(pretty_response)
        
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError:
        print("Error parsing response as JSON.")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")

if __name__ == "__main__":
    # Replace with your actual AlienVault OTX API Key
    API_KEY = "{ENTER API_KEY}"
    
    if API_KEY == "{ENTER API_KEY}":
         print("[red]Error: Please set your API_KEY in the script.[/red]")
    else:
        fetch_domain_data(API_KEY)

