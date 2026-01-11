import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import pandas as pd
import argparse
import time


columns = [
    "Program Name", "University Name", "City", "Country",
    "Tuition Fee", "Duration", "Average Rating", "Review Count",
    "Ranking_Percentage", "Program Link"
]

def safe_find(row, by, value):
    try:
        return row.find_element(by, value).text.strip()
    except:
        return ""

def extract_city_country(location):
    if not location:
        return "", ""
    parts = [p.strip() for p in location.split(",")]
    if len(parts) == 1:
        return "N/A", parts[0]
    if len(parts) == 2:
        return parts[0], parts[1]
    return parts[-2], parts[-1]

def get_program_details(row):
    contents = {}
    contents["Program Name"] = safe_find(row, By.CLASS_NAME, "StudyName")
    contents["University Name"] = safe_find(row, By.CLASS_NAME, "OrganisationName")

    loc = safe_find(row, By.CLASS_NAME, "OrganisationLocation")
    city, country = extract_city_country(loc)
    contents["City"], contents["Country"] = city, country

    contents["Tuition Fee"] = safe_find(row, By.CLASS_NAME, "TuitionValue")
    contents["Duration"] = safe_find(row, By.CLASS_NAME, "DurationValue")
    contents["Average Rating"] = safe_find(row, By.CLASS_NAME, "AverageStarRating")

    r = safe_find(row, By.CLASS_NAME, "ReviewQuantity")
    contents["Review Count"] = r.replace("(", "").replace(")", "")

    contents["Ranking_Percentage"] = safe_find(row, By.CLASS_NAME, "GlobalPositionPercentageValue")

    try:
        contents["Program Link"] = row.find_element(By.TAG_NAME, "a").get_attribute("href")
    except:
        contents["Program Link"] = ""

    return contents


def main():
    # Parse optional ChromeDriver path
    parser = argparse.ArgumentParser()
    parser.add_argument("--chromedriver_path", help="Path to ChromeDriver", required=False)
    args = parser.parse_args()

    # Initialize undetected Chrome
    if args.chromedriver_path:
        driver = uc.Chrome(driver_executable_path=args.chromedriver_path, headless=False)
    else:
        driver = uc.Chrome(headless=False)


    program_data = []

    for page_id in range(1, 214):

        url = f"https://www.mastersportal.com/search/master/msc/computer-science-it?mh=face2face&rg=12,11,10,9,1&page={page_id}"

        driver.get(url)
        time.sleep(4)  # allow Cloudflare bypass

        # If Cloudflare still shows
        if "cloudflare" in driver.page_source.lower():
            print(f"Cloudflare detected on page {page_id}, waiting...")
            time.sleep(8)
            driver.get(url)

        try:
            rows = driver.find_elements(By.CLASS_NAME, "SearchResultItem")
        except:
            print(f"FAILED page {page_id}")
            continue

        for row in rows:
            program_data.append(get_program_details(row))

        print(f"Page {page_id} OK — {len(rows)} items")

        time.sleep(2)

    driver.quit()

    df = pd.DataFrame(program_data)
    df.to_csv("CS_master_program_details.csv", index=False)
    print("CSV saved successfully!")


if __name__ == "__main__":
    main()
