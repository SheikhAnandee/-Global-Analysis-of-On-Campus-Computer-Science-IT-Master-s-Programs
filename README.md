# Global Analysis of On-Campus Computer Science & IT Master's Programs
# Problem statement
the goal of this project is to gather information of Computer Science and IT masters program worldwide from [this website.](https://www.mastersportal.com/)

Later I used the scraped data to explore patterns and insights using an interactive Tableau dashboard. <br/>

1) Tuition Fee Heatmap across countries and rating categories (excluding Singapore)
2) Bar Chart of Average Tuition Fee by Country
3) Bar Chart of Tuition Fee vs. Rating Category, with bars colored by country
4) Scatter Plot: Average Monthly Tuition vs. Program Duration (USA Only) – exploring tuition patterns in the USA
5) List of Top-Ranked Universities Offering Data Science Master’s Programs Worldwide
6) Map of European Countries Showing Universities Offering AI, Cybersecurity, and Data Analytics Programs – including number of programs, universities, maximum reviews, average ranking %, and tuition fee
7) Bar Chart of Number of Top-Ranked Universities in Affordable Countries – showing review count, average rating, and average ranking

You can visit the public Dashboard 1 [here:](https://public.tableau.com/app/profile/sheikh.anandee.hasan/viz/GlobalAnalysisofOn-CampusComputerScienceITMastersPrograms/TuitionComparisonDashboard) 
and Dashboard 2 [here:](https://public.tableau.com/app/profile/sheikh.anandee.hasan/viz/GlobalAnalysisofOn-CampusComputerScienceITMastersPrograms_17642456408750/Dashboard2?publish=yes)

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
