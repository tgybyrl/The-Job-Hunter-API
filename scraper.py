import requests
from bs4 import BeautifulSoup

def scrape_job_description(url):
    """
    Fetches the web page from the given URL and extracts paragraph/list text.
    """
    try:
        # A User-Agent header makes our script look like a normal web browser.
        # This helps prevent websites from blocking us immediately.
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }
        
        # 1. Send the GET request to download the page HTML
        response = requests.get(url, headers=headers, timeout=10)
        
        # 2. Raise an exception if the response was bad (e.g., 404 Not Found)
        response.raise_for_status()

        # 3. Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # 4. Find the most relevant elements containing text.
        # Job descriptions are usually in <p> (paragraphs) or <li> (list items) tags.
        # By targeting these, we mostly skip navbars, scripts, and footers.
        text_elements = soup.find_all(['p', 'li'])
        
        # Extract the text chunks and clean up the extra spaces
        extracted_text = []
        for element in text_elements:
            clean_text = element.get_text(strip=True)
            if clean_text:
                extracted_text.append(clean_text)
                
        # Join into a single large string separated by spaces
        final_text = ' '.join(extracted_text)
        
        return final_text

    except Exception as e:
        # If the request fails (e.g. timeout, invalid URL), return an error message
        return f"Error scraping the URL: {str(e)}"

if __name__ == "__main__":
    # This block only runs if you run `python scraper.py` directly.
    print("Testing the scraper...")
    test_url = input("Enter a valid URL (e.g., a Wikipedia page or a job posting): ")
    if test_url:
        result = scrape_job_description(test_url)
        print("\n--- Extracted Text (First 500 characters) ---")
        # Print only the first 500 characters so we don't spam the terminal
        print(result[:500] if len(result) > 500 else result)
        print("---------------------------------------------")
