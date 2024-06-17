# 📈 Dunhumby The complete Journey Dashboard
![banner](https://github.com/Med-Kallel/Dunhumby-The-complete-Journey-Dashboard/assets/173089953/1e6b69ab-9df3-453d-96c0-e05aeb1c6ce6)
## Table of Contents

-   [Description](#description)
    -   [App Overview](#app-overview)
    -   [App Screenshots](#app-screenshots)
-   [Demo](#demo)
-   [Installation](#installation)
-   [Usage](#usage)
-   [Project Structure](#project-structure)
-   [Contact me](#contact)
-   [Licence](#licence)
---
## Description
 This dataset contains household level transactions over two years from a group of 2,500 households who are frequent shoppers at a retailer. For certain households, demographic information as well as direct marketing contact history are included. The objective of this dashboard is to present relevant metrics about the financials of the stores, the demographic distribution of the customers and other key metrics. Multiple updates could be made to study the results of several marketing campaigns and product displays.
- #### App Overview
    - A python Notebook for the data management and creation of new metrics/columns
    - The streamlit app has **5 pages**: 
        - 👋 Dataset Presentation
        - 🔍 Data Exploration
        - 🏠 Demographic Data
        - 📦 Product_Data
        - 🧮 Sales Data  
- #### App Screenshots

|Dataset Presentation |
|:--------------------:|
| ![Dataset Presentation](https://github.com/Med-Kallel/Dunhumby-The-complete-Journey-Dashboard/assets/173089953/b39dcf96-d916-4a17-9dea-2f82b20b36be)|

| Data Exploration|
|:----------------:|
|![Data Exploration](https://github.com/Med-Kallel/Dunhumby-The-complete-Journey-Dashboard/assets/173089953/c9e7585b-a539-4bfc-9fbd-b356e0edccb9)|

|Demographic Data |
|:----------------:|
|![Demographic Data](https://github.com/Med-Kallel/Dunhumby-The-complete-Journey-Dashboard/assets/173089953/5e1abe36-b641-4a43-b9f4-0ce24f76f652)|

| Product Presence |Product Sales |
|:------------:|:----------:|
| ![Product Presence](https://github.com/Med-Kallel/Dunhumby-The-complete-Journey-Dashboard/assets/173089953/55080946-cbbf-4f2f-82de-8d4dcfc9d687)|![Product Sales](https://github.com/Med-Kallel/Dunhumby-The-complete-Journey-Dashboard/assets/173089953/d546cf6d-075b-44d0-9e8b-8e63f773cb6a)|

| General Sales | Sales By Demographic  | Customer Acqiosition  |
|:----------:|:----------:|:----------:|
| ![General Sales](https://github.com/Med-Kallel/Dunhumby-The-complete-Journey-Dashboard/assets/173089953/4f6788e4-6e9e-4d78-9fca-2769589e77b5)|![Sales By Demographic](https://github.com/Med-Kallel/Dunhumby-The-complete-Journey-Dashboard/assets/173089953/58acb585-e298-48f9-ba40-a699b71e119e)| ![Customer Acqiosition](https://github.com/Med-Kallel/Dunhumby-The-complete-Journey-Dashboard/assets/173089953/09d32935-8b6e-45d5-813b-0407453b71bd)|

---
## Demo
##### The app demo is hosted & available on the following link: [Demo Link](https://dunhumby-the-complete-journey-dashboard.streamlit.app/)
---
## Installation

> [!IMPORTANT]
> The project was done on Python 3.11.6

To run this project locally, follow these steps:

1. Clone the repository:
```sh
# Clone the repository
git clone https://github.com/Medkallel/The-complete-journey-Data-Management.git
# Navigate into the directory
cd The-complete-journey-Data-Management
```
2. Install the required dependencies:
```
# Install the requirements
pip install -r requirements.txt
```

---
## Usage 
```
# Run the Streamlit app
streamlit run Src/Streamlit/1_👋_Dataset_Presentation.py
```
> [!TIP] 
> You can access the app on another device by following the link: ```http://<server-ip>:8501```

---
## Project Structure
```
Here's a visual representation of the structure:
📦Project
 ┣ 📁.streamlit/
 ┃ ┗ 📜config.toml
 ┣ 📁Assets/
 ┃ ┣ 🖼️ banner.jpg
 ┃ ┗ 🖼️ WordCloudMask.png
 ┣ 📁Data/
 ┣ 📁Export/
 ┣ 📁Doc/
 ┃ ┣ 📜dataset_description.json
 ┃ ┗ 📜dunnhumby - The Complete Journey User Guide.pdf
 ┣ 📁Src/
 ┃ ┣ 🐍Data_Exploration-Preprocessing.ipynb
 ┃ ┗ 📁Streamlit/
 ┃   ┣ 🐍1_👋_Dataset_Presentation.py
 ┃   ┣ 🐍config.py
 ┃   ┣ 🐍display_graph.py
 ┃   ┣📁pages/
 ┃    ┣ 🐍2_🔍_Data Exploration.py
 ┃    ┣ 🐍3_🏠_Demographic Data.py
 ┃    ┣ 🐍4_📦_Product_Data.py
 ┃    ┗ 🐍5_🧮_Sales_Data.py
 ┣ 📜README.md
 ┗ 📜requirements.txt
```
---
## 📫 Contact me
<p>
<a href="https://www.linkedin.com/in/mohamed-kallel/">
<img alt="LinkedIn" src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white"/>
</a> 
<br>
</p>

---
## Licence
This project is under the **MIT Licence**. Check the licence file for more info.
