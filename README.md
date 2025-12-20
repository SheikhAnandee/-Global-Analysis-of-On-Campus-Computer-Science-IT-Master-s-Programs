# Global Analysis of On-Campus Computer Science & IT Master's Programs
# Objective
To build a centralized dataset and interactive dashboard comparing global CS & IT master’s programs.
# Project Background
Comparing Computer Science and IT master’s programs across countries is challenging due to fragmented and inconsistent information spread across multiple university websites. This project addresses that problem by automating the collection of standardized program data from 35+ countries.
Using Selenium with Undetected-Chromedriver, the project scrapes on-campus CS & IT master’s program information from the [MastersPortal](https://www.mastersportal.com/) website.The resulting dataset is structured, consistent, and ready for analysis, enabling efficient cross-country comparisons of tuition, rankings, duration, and availability.
# Data Scraping & Preprocessing
Program data is automatically scraped from paginated search results on [MastersPortal](https://www.mastersportal.com/)  using Selenium and Undetected-Chromedriver to bypass anti-bot protections. Key attributes collected include program name, university, city, country, tuition fee, duration, average rating, review count, global ranking percentage, and program links.

To ensure data quality, missing elements are safely handled, location strings are parsed into separate city and country fields, and review counts are cleaned by removing extra characters. The final output is stored as a clean, analysis-ready CSV file using Pandas.

# Data Analysis & Visualization
The scraped dataset is analyzed and visualized using an interactive Tableau dashboard to uncover patterns and insights across global study destinations. The dashboard includes: <br/>
1) Tuition Fee Heatmap across countries and rating categories (excluding Singapore)
2) Bar Chart of Average Tuition Fee by Country
3) Tuition Fee vs Program Rating (Scatter Plot)
4) Scatter Plot: Average Monthly Tuition vs. Program Duration (USA Only) – exploring tuition patterns in the USA
5) List of Top-Ranked Universities Offering Data Science Master’s Programs Worldwide
6) Map of European Countries Showing Universities Offering AI, Cybersecurity, and Data Analytics Programs – including number of programs, universities, maximum reviews, average ranking %, and tuition fee
7) Bar Chart of Number of Top-Ranked Universities in Affordable Countries – showing review count, average rating, and average ranking

You can visit the public [Dashboard 1](https://public.tableau.com/app/profile/sheikh.anandee.hasan/viz/GlobalAnalysisofOn-CampusComputerScienceITMastersPrograms/TuitionComparisonDashboard) and [Dashboard 2](https://public.tableau.com/app/profile/sheikh.anandee.hasan/viz/GlobalAnalysisofOn-CampusComputerScienceITMastersPrograms_17642456408750/Dashboard2?publish=yes) 
# Some interesting findings from both dashboards
1) Universities with Excellent ratings (≥4.5) are slightly cheaper than those with Very Good ratings (≥4).
2) Most countries fall under the Very Good rating category.
3) Most programs in the USA are 12 months long.
4) Some 24-month programs are cheaper than certain 8-, 10-, or 12-month programs, which is unusual.
5) USA has the highest average tuition fee, while Italy has the lowest average tuition fee
6) Programs with similar ratings (≈4.0–4.5) appear across a wide tuition range
7) Europe offers the best balance of affordability, high-quality education, and strong global rankings.
8) Program duration varies widely: Europe leans toward 2-year programs, while the USA and UK generally offer 1-year programs.
9) The UK offers 261 programs in Cybersecurity, AI, and Data Analytics across 108 universities, making it one of the largest contributors in Europe.
    
# Build from sources and run the selenium scrapper
1) Clone the repository
 ```bash

   git clone:https://github.com/SheikhAnandee/-Global-Analysis-of-On-Campus-Computer-Science-IT-Master-s-Programs.git

  ```
2) Initialize and activate virtual environment <br/> 
For Windows:
 ```bash
    python -m venv venv
    venv\Scripts\activate
 ```
For Linux / macOS:
 ```bash

   python3 -m venv venv
   source venv/bin/activate

 ```
3) Install dependencies
 ```bash

    pip install -r requirements.txt

 ```
4) Download the correct version of Chrome WebDriver that matches your browser version:https://developer.chrome.com/docs/chromedriver/downloads

5) Run the scrapper
 ```bash

  python Capstone_Project_1/scrapper1.py--chromedriver_path <path_to_chromedriver>

 ```
 
6) After running, you will get a file named "CS_master_program_details_Top35_Countries.csv" containing all the required details
   Alternatively:
   Check our scraped data here: https://github.com/SheikhAnandee/-Global-Analysis-of-On-Campus-Computer-Science-IT-Master-s-Programs/blob/main/Capstone_Project_1/CS_master_program_details_top35_countries.csv
   
# Analytics   
View the dashboards:

[Dashboard 1](https://public.tableau.com/app/profile/sheikh.anandee.hasan/viz/GlobalAnalysisofOn-CampusComputerScienceITMastersPrograms/TuitionComparisonDashboard)
[Dashboard 2](https://public.tableau.com/app/profile/sheikh.anandee.hasan/viz/GlobalAnalysisofOn-CampusComputerScienceITMastersPrograms_17642456408750/Dashboard2?publish=yes)

# Feedback & Contact
If you have suggestions, questions, or ideas to improve the dataset or dashboard, feel free to reach out. Feedback and discussions are always welcome.
📧 Email: anandeehasan24@gmail.com
