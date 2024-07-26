# 📈 Dunhumby The complete Journey Dashboard
![banner](https://github.com/Med-Kallel/Dunhumby-The-complete-Journey-Dashboard/assets/173089953/1e6b69ab-9df3-453d-96c0-e05aeb1c6ce6)

## Table of Contents

-   [Technologies Used](#technologies-used)
-   [Description](#description)
    -   [App Overview](#app-overview)
    -   [App Screenshots](#app-screenshots)
-   [Demo](#demo)
-   [Using Docker](#using-docker)
-   [Installation](#installation)
-   [Usage](#usage)
-   [Project Structure](#project-structure)
-   [Contact me](#contact)
-   [Licence](#licence)

---

## Technologies Used

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)  ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)  ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black) ![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white) ![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white) ![JSON](https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white")
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://dunhumby-the-complete-journey-dashboard.streamlit.app/)


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
| ![Dataset Presentation](https://github.com/Medkallel/Dunhumby-The-complete-Journey-Dashboard/assets/26349357/3e724be4-ff00-4c99-85a3-08616550e70c)|

| Data Exploration|
|:----------------:|
|![Data Exploration](https://github.com/Medkallel/Dunhumby-The-complete-Journey-Dashboard/assets/26349357/32a4eb3e-30be-4452-b877-af91c08485d9)|

|Demographic Data |
|:----------------:|
|![Demographic Data](https://github.com/Medkallel/Dunhumby-The-complete-Journey-Dashboard/assets/26349357/0278e438-054b-499e-a790-e54b99ded094)|

| Product Presence |Product Sales |
|:------------:|:----------:|
| ![Product Presence](https://github.com/Medkallel/Dunhumby-The-complete-Journey-Dashboard/assets/26349357/bfd3cb6f-2bec-460b-a090-9364ad3ffd3c)|![Product Presence](https://github.com/Medkallel/Dunhumby-The-complete-Journey-Dashboard/assets/26349357/94b61eea-fdcf-4273-b46b-da2369d0fe59)|

| General Sales | Sales By Demographic  | Customer Acqiosition  |
|:----------:|:----------:|:----------:|
| ![General Sales](https://github.com/Medkallel/Dunhumby-The-complete-Journey-Dashboard/assets/26349357/4f4de4d9-cac3-4167-b0c8-b19da1c2d13b)|![Sales By Demographic](https://github.com/Medkallel/Dunhumby-The-complete-Journey-Dashboard/assets/26349357/2384f085-8c88-49dc-82ad-cba67c0c0092)| ![Customer Acquisition](https://github.com/Medkallel/Dunhumby-The-complete-Journey-Dashboard/assets/26349357/c5c14e89-8ee2-47db-a076-52b831f1ebf2)|

---
## Demo
##### The app demo is hosted & available on the following link: [Demo Link](https://dunhumby-the-complete-journey-dashboard.streamlit.app/)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://dunhumby-the-complete-journey-dashboard.streamlit.app/)


---
## Using Docker
#### 1. Pulling the Docker Image
To pull the Docker image from Docker Hub, run the following command:
```sh
# Pull the docker image
$ docker pull medkallel/dunhumby-the-complete-journey-dashboard:latest

# Or if you downloaded the .tar image
$ docker load -i dunhumby-the-complete-journey-dashboard.tar
```
#### 2. Building the Docker Image
If you prefer to build the Docker image locally, navigate to the project directory and run:

```sh
# Build the docker image
$ docker build -t dunhumby-the-complete-journey-dashboard .
```
#### 3. Running the Docker Container
To run the Docker container, use the following command:
```sh
# Run the docker container
$ docker run -p 8501:8501 dunhumby-the-complete-journey-dashboard
```
> [!TIP] 
> You can access the app on another device by following the link: ```http://<server-ip>:8501```
---
## Installation

> [!IMPORTANT]
> The project was done on Python 3.11.6

To run this project locally, follow these steps:

1. Clone the repository:
```sh
# Clone the repository
$ git clone https://github.com/Medkallel/Dunhumby-The-complete-Journey-Dashboard
# Navigate into the directory
$ cd Dunhumby-The-complete-Journey-Dashboard
```
2. Install the required dependencies:
```sh
# Install the requirements
$ pip install -r requirements.txt
```

---
## Usage 
```sh
# Run the Streamlit app
$ streamlit run Src/Streamlit/1_👋_Dataset_Presentation.py
```
> [!TIP] 
> You can access the app on another device by following the link: ```http://<server-ip>:8501```
---
## Project Structure
```
Here's a visual representation of the structure:
📦Project
 ┣ 📁.github/workflows
 ┃ ┗ 🦑github-docker-cicd.yaml # Used for the CI/CD pipeline
 ┣ 📁.streamlit/
 ┃ ┗ 📄config.toml
 ┣ 📁Assets/
 ┃ ┣ 🖼️ banner.jpg
 ┃ ┗ 🖼️ WordCloudMask.png
 ┣ 📁Data/ # Contains the dataset
 ┣ 📁Export/ # Contains the processed dataset
 ┣ 📁Doc/
 ┃ ┣ 📄dataset_description.json
 ┃ ┗ 📄dunnhumby - The Complete Journey User Guide.pdf
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
 ┣ 🐳Dockerfile
 ┣ 📄README.md
 ┗ 📄requirements.txt
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
## License
This project is under the **CC BY-NC 4.0 Licence**. Check the licence file for more info. <br/>
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

