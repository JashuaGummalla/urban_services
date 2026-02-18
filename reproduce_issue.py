
import os
import django

# Set env vars to ensure settings load correctly for testing
os.environ['ALLOWED_HOSTS'] = 'testserver,localhost,127.0.0.1'
os.environ['DEBUG'] = 'True'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'urban_services.settings')

django.setup()

from django.test import Client
from django.urls import reverse

def test_search_functionality():
    client = Client()
    
    # 1. Inspect Home Page Form
    print("Fetching Home Page...")
    try:
        response = client.get(reverse('home'))
        print(f"Home page status: {response.status_code}")
        
        if response.status_code == 200:
            content = response.content.decode('utf-8')
            if 'action="/services/"' in content:
                print("Found correct form action '/services/' in home page.")
            else:
                 # Check what is there using regex
                import re
                match = re.search(r'action="([^"]*)"', content)
                if match:
                    print(f"Found action: {match.group(1)}")
                else:
                    print("No action attribute found or form not found.")
        else:
            print("Failed to fetch home page.")
            
    except Exception as e:
        print(f"Error fetching home page: {e}")

    # 2. Submit Search Query
    print("\nSubmitting Search Query 'Cleaning'...")
    try:
        search_url = reverse('service_list')
        response = client.get(search_url, {'q': 'Cleaning'})
        
        print(f"Search response status: {response.status_code}")
        if response.status_code == 200:
            content = response.content.decode('utf-8')
            if 'Search results for "Cleaning"' in content:
                print("SUCCESS: Search results header found.")
            else:
                print("FAILURE: Search results header NOT found.")
                
                # Debug print
                if 'Cleaning' in content:
                     print("However, the word 'Cleaning' appears in the response.")
        else:
            print("Search request failed.")
            
    except Exception as e:
         print(f"Error searching: {e}")

if __name__ == "__main__":
    test_search_functionality()
