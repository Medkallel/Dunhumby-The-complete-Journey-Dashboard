# 📈 Dunhumby The complete Journey Dashboard
![banner](https://github.com/Med-Kallel/Dunhumby-The-complete-Journey-Dashboard/assets/173089953/1e6b69ab-9df3-453d-96c0-e05aeb1c6ce6)
## Table of Contents

-   [Description](#description)
-   [Installation](#installation)
-   [Usage](#usage)
    -   [App Overview](#app-overview)
    -   [App Screenshots](#app-screenshots)
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
    | Dataset Presentation | Data Exploration |
    |:--------------------:|:----------------:|
    | ![image](https://github.com/Med-Kallel/Dunhumby-The-complete-Journey-Dashboard/assets/173089953/950d54e1-88f1-471d-9819-8d6b4c09c4b0)| ![image](https://github.com/Med-Kallel/Dunhumby-The-complete-Journey-Dashboard/assets/173089953/e6ce60cb-7522-4b50-99bf-9ca9f2a3fe04)|

    | Demographic Data | Product Data | Sales Data |
    |:----------------:|:------------:|:----------:|
    | ![Demographic Data](Assets/demographic_data.png) | ![Product Data](Assets/product_data.png) | ![Sales Data](Assets/sales_data.png) |


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
