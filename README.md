# Global Analysis of On-Campus Computer Science & IT Master's Programs
# Problem statement
This project automates the collection of Computer Science & IT Master’s program information from 35+ countries using Selenium and Undetected-Chromedriver.
It gathers key details including program name, university, tuition fee, duration, city, country, average rating, review count, and global ranking percentage. 
The final output is a clean, analysis-ready dataset sourced from the [MastersPortal](https://www.mastersportal.com/) website.<br/>

Later I used the scraped data to explore patterns and insights using an interactive Tableau dashboard. <br/>
1) Tuition Fee Heatmap across countries and rating categories (excluding Singapore)
2) Bar Chart of Average Tuition Fee by Country
3) Bar Chart of Tuition Fee vs. Rating Category, with bars colored by country
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
5) USA has the highest average tuition fee, while Italy has the lowest average tuition fee.
6) Canada is cheaper compared to some European countries.
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
   
## Analytics   
View the dashboards:

[Dashboard 1](https://public.tableau.com/app/profile/sheikh.anandee.hasan/viz/GlobalAnalysisofOn-CampusComputerScienceITMastersPrograms/TuitionComparisonDashboard)
[Dashboard 2](https://public.tableau.com/app/profile/sheikh.anandee.hasan/viz/GlobalAnalysisofOn-CampusComputerScienceITMastersPrograms_17642456408750/Dashboard2?publish=yes)
