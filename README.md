# Global Analysis of IT Master's Programs
## Quick Links
- **Live Dashboard:** [View on Tableau Public](https://public.tableau.com/views/GlobalITMastersProgramsAnanlysis/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
- **Dataset (CSV):** [View Dataset](data/CS_master_program_details_top35_countries.csv)
- **Scraper Code:** [View Scraper](src/scraper.py)
- **Data Source:** [Mastersportal website](https://www.mastersportal.com/)
- **Full Repository:** [GitHub Repo](https://github.com/SheikhAnandee/Global-IT-Masters-Program-Analysis.git)
- **Contact:** anandeehasan24@gmail.com
## Objective
Build a centralized dataset and interactive dashboard to compare global Computer Science & IT Master’s programs across 35+ countries.
## Project Background
Comparing Computer Science and IT master’s programs across countries is challenging due to fragmented and inconsistent information spread across multiple university websites. This project addresses that problem by automating the collection of standardized program data from 35+ countries.
Using Selenium with Undetected-Chromedriver, the project scrapes on-campus CS & IT master’s program information from the [MastersPortal](https://www.mastersportal.com/) website.The resulting dataset is structured, consistent, and ready for analysis, enabling efficient cross-country comparisons of tuition, rankings, duration, and availability.
## Data Scraping & Preprocessing
### Data Collection
Program data is automatically scraped from paginated search results on [MastersPortal](https://www.mastersportal.com/)  using Selenium and Undetected-Chromedriver to bypass anti-bot protections. 
Key attributes collected include:
- Program Name
- University
- City
- Country
- Tuition Fee
- Duration
- Average Rating
- Review Count
- Global Ranking Percentage
- Program Links

### Data Cleaning
- Parsed location strings into separate city & country
- Cleaned review counts (removed extra characters)
- Handled missing values safely
- Converted tuition fields to numeric format
- Exported clean, analysis-ready dataset using Pandas

The final output is stored as a clean, analysis-ready [CSV file](data/CS_master_program_details_top35_countries.csv) using Pandas.

## Data Analysis & Visualization
### Dashboard 1: Tuition Analysis
<p align="center"> <img src="visualizations/tuition-dashboard-1.png" width="900"> </p>

### Visualizations: 
1. **Scatter Plot: Average Tuition Fee vs. Average Rating**
   - Explores whether higher tuition fees correlate with better program ratings.
   - Points are color-coded by country and sized by Top-Ranked Count, making it easy to spot which countries offer strong  ratings without the highest price tag.

2. **Bar Chart: Average Tuition Fee by Country**
   - Highlights countries with the highest and lowest average tuition costs
   - Clicking a bar filters the other two visualizations by that country.
   
3. **Scatter Plot: Monthly Average Tuition vs. Program Duration**
   - Breaks down cost efficiency by program length, with point color showing the average monthly tuition (green = low, red = high).
   - Dynamically updates based on the country selected via the bar chart filter — defaults to showing all countries when nothing is selected.

### Dashboard 2: Ranking & Geographic Distribution
<p align="center"> <img src="visualizations/ranking-dashboard-2.png" width="900"> </p>

### Visualizations: 

1. **Scatter Plot: Rating vs. Review Volume ("Hidden Gems" Quadrant Analysis)**
   - Plots average rating against review count, split into quadrants (Proven Favorites, Popular but Polarizing, Hidden Gems, Watch List) to surface well-rated but under-the-radar programs.
   - Points are color-coded by country using the dashboard-wide country filter.

2. **Global Map: Geographic Distribution of Top-Ranked Programs**
    - Choropleth map shading countries by concentration of top-ranked programs.

3. **Table: Top Universities for Data Science**
   - Lists university name, country, and program, with a percentage indicator bar per row.
     
4. **Country Filter Legend**
   - Interactive multi-country selector that drives both the scatter plot and the map.




You can visit the public [Dashboard](https://public.tableau.com/views/GlobalITMastersProgramsAnanlysis/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link) 

## Interesting Findings 

- **The UK has the highest average tuition fee ($33,377), while Italy has the lowest ($6,255)**, creating a substantial gap in the cost of pursuing a CS & IT master's program across countries.

- **Programs with similar ratings (≈4.0–4.5) span a wide tuition range**, indicating that **higher tuition does not necessarily guarantee higher student satisfaction**.

- **The USA shows a strong concentration of 12-month master's programs**, suggesting that the **one-year format is particularly common among US-based CS & IT programs** in the dataset.

- **Program duration does not always translate into higher monthly cost**, as some **24-month programs have lower monthly tuition than certain 10–12 month programs**, showing that longer programs can offer better cost efficiency when normalized by duration.

- **The "Hidden Gems" quadrant highlights programs with high ratings but relatively low review volume**, identifying **well-rated programs that may have strong student satisfaction but lower visibility or a smaller review base**.

- **Top-ranked CS & IT programs are geographically concentrated**, with a noticeable **cluster across European countries on the global map**, alongside a few standout education hubs in other regions.

- **Tuition and student ratings show no clear positive relationship**, with **highly rated programs appearing across both lower- and higher-tuition categories**, suggesting that cost alone is not a reliable indicator of perceived program quality.

- **Several lower-tuition destinations still contain highly rated programs**, indicating that students can potentially find **stronger value-for-money options outside traditionally expensive study destinations**.

    
## Build from sources and run the selenium scrapper
1) Clone the repository
 ```bash

   git clone:https://github.com/SheikhAnandee/Global-IT-Masters-Program-Analysis.git

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

  python python src/scraper.py--chromedriver_path <path_to_chromedriver>

 ```
 
6) After running, you will get a file named "CS_master_program_details_Top35_Countries.csv" containing all the required details
   Alternatively:
   Check our scraped data here: https://github.com/SheikhAnandee/Global-IT-Masters-Program-Analysis/tree/main/data/CS_master_program_details_top35_countries.csv
   
##  Analytics & Interactive Dashboard

Explore the full interactive Tableau dashboard to analyze tuition trends, rankings, program distribution, and cross-country comparisons in detail.

 **Live Dashboard:**  
 [View on Tableau Public](https://public.tableau.com/views/GlobalITMastersProgramsAnanlysis/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)


## License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute this project with proper attribution.

## Acknowledgments

- **MastersPortal** – For providing structured access to global master’s program information.
- **Tableau Public** – For enabling interactive data visualization and dashboard publishing.
- **Selenium & Undetected-Chromedriver Community** – For automation tools used in large-scale data scraping.
- **Open Source Community** – For the Python libraries and ecosystem that made this project possible.

## Feedback & Contact
If you have suggestions, questions, or ideas to improve the dataset or dashboard, feel free to reach out. Feedback and discussions are always welcome.
<br/>
Email: anandeehasan24@gmail.com
