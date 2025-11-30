# Global Analysis of On-Campus Computer Science & IT Master's Programs
# Problem statement
the goal of this project is to gather information of Computer Science and IT masters program from [this website.](https://www.mastersportal.com/)

Later I used the scraped data to explore patterns and insights using an interactive Tableau dashboard.

You can visit the public Dashboard 1 [here:](https://public.tableau.com/app/profile/sheikh.anandee.hasan/viz/GlobalAnalysisofOn-CampusComputerScienceITMastersPrograms/TuitionComparisonDashboard) 
and Dashboard 2 [here:](https://public.tableau.com/app/profile/sheikh.anandee.hasan/viz/GlobalAnalysisofOn-CampusComputerScienceITMastersPrograms_17642456408750/Dashboard2?publish=yes)

# Build from sources and run the selenium scrapper
1) Clone the repository
 ```bash

   git clone:https://github.com/SheikhAnandee/-Global-Analysis-of-On-Campus-Computer-Science-IT-Master-s-Programs.git

  ```
2) Initialize and activate virtual environment
   For windows:
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

  python Capstone_Project_1/scrapper1.py--chromedriver_path

 ```
 
6) After running, you will get a file named "CS_master_program_details_Top35_Countries.csv" containing all the required details
   Alternatively:
   Check our scraped data here:
   
## Analytics   
View the dashboards:

[Dashboard 1](https://public.tableau.com/app/profile/sheikh.anandee.hasan/viz/GlobalAnalysisofOn-CampusComputerScienceITMastersPrograms/TuitionComparisonDashboard)
[Dashboard 2](https://public.tableau.com/app/profile/sheikh.anandee.hasan/viz/GlobalAnalysisofOn-CampusComputerScienceITMastersPrograms_17642456408750/Dashboard2?publish=yes)
