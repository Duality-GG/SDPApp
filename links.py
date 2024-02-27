import requests
from bs4 import BeautifulSoup

# as a reminder, this is can integrated into presets and constellations.
#
#

def fetch_astro_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the div with class 'keyinfobox'
        key_info_boxes = soup.find_all('div', class_='keyinfobox')

        right_ascension = None
        declination = None

        for box in key_info_boxes:
            label = box.find('label')
            if label:
                label_text = label.get_text().strip()
                if 'Right Ascension J2000' in label_text:
                    right_ascension = label.find_next_sibling().get_text().strip()
                elif 'Declination J2000' in label_text:
                    declination = label.find_next_sibling().get_text().strip()

        return right_ascension, declination

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from the website: {e}")

def main():
    # Prompt user to paste the URL
    url = input("Please paste the URL here: ")

    print(f"Fetching data from: {url}")
    ra, dec = fetch_astro_data(url)

    if ra and dec:
        print(f"Right Ascension: {ra}, Declination: {dec}")
    else:
        print("Data not found or the website structure has changed.")

if __name__ == "__main__":
    main()
