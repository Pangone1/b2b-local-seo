import requests
import urllib.parse

print("--- Termux Local SEO Auditor ---")
api_key = input("Enter your SerpApi Key: ")
business = input("Enter Business Name and City (e.g., Joe's Plumbing Las Vegas): ")

# Encode the search query for the URL
query = urllib.parse.quote_plus(business)
url = f"https://serpapi.com/search.json?engine=google_maps&q={query}&api_key={api_key}"

print(f"\nScanning Google Maps data for {business}...\n")

try:
    response = requests.get(url)
    data = response.json()

    if "local_results" in data and len(data["local_results"]) > 0:
        result = data["local_results"][0]
        title = result.get('title', 'N/A')
        rating = result.get('rating', '0')
        reviews = result.get('reviews', '0')
        category = result.get('type', 'N/A')
        website = result.get('website')
        
        print("=== GOOGLE BUSINESS PROFILE AUDIT ===")
        print(f"Name: {title}")
        print(f"Primary Category: {category}")
        print(f"Score: {rating} Stars across {reviews} Reviews")
        
        if website:
            print(f"Website: {website}")
        else:
            print("Website: NONE DETECTED (High-Value Pitch Target)")
            
        print("=====================================\n")
    else:
        print("=== RESULT ===")
        print("No Google Maps profile found. This business is invisible on Local Search!")
        print("=====================================\n")
except Exception as e:
    print(f"Error fetching data. Check your API key and internet connection.\nDetails: {e}")
