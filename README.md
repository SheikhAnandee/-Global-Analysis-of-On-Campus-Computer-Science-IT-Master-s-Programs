# Global Analysis of On-Campus Computer Science & IT Master's Programs
# Problem statement
the goal of this project is to gather information of Computer Science and IT masters program from [this website.](https://www.mastersportal.com/)

Later we used the scraped data to understand the demographics and correlations using Tableau Dashboard.

You can visit the public Dashboard 1 [here:](https://public.tableau.com/app/profile/sheikh.anandee.hasan/viz/GlobalAnalysisofOn-CampusComputerScienceITMastersPrograms/TuitionComparisonDashboard) 
and Dashboard 2 [here:](https://public.tableau.com/app/profile/sheikh.anandee.hasan/viz/GlobalAnalysisofOn-CampusComputerScienceITMastersPrograms_17642456408750/Dashboard2?publish=yes)

# Build from sources and run the selenium scrapper
1) Clone the repo
 '''bash
 git clone:https://github.com/SheikhAnandee/-Global-Analysis-of-On-Campus-Computer-Science-IT-Master-s-Programs.git
 '''
2) Initialize and activate virtual environment
  '''bash
       virtualenv --no-site-packages venv
       source venv/bin/activate
  '''
3) Install dependencies
   '''bash
   pip install -r requirements.txt
   '''
4) Download Chrome Webdriver from https://developer.chrome.com/docs/chromedriver/downloads
5) Run the scrapper
   '''bash
    python Capstone_Project_1/scrapper1.py--chromedriver_path
   '''
6) You will get a file named "CS_master_program_details_Top35_Countries.csv.csv" containing all the required details.
   Alternatively,
   Check our scrape data here https://github.com/SheikhAnandee/-Global-Analysis-of-On-Campus-Computer-Science-IT-Master-s-Programs/blob/main/Capstone_Project_1/CS_master_program_details_Top30_Countries%20-%20CS_master_program_details_Top30_Countries.csv.csv

## Analytics   
View the dashboards:

[Dashboard 1](https://public.tableau.com/app/profile/sheikh.anandee.hasan/viz/GlobalAnalysisofOn-CampusComputerScienceITMastersPrograms/TuitionComparisonDashboard)
[Dashboard 2](https://public.tableau.com/app/profile/sheikh.anandee.hasan/viz/GlobalAnalysisofOn-CampusComputerScienceITMastersPrograms_17642456408750/Dashboard2?publish=yes)
