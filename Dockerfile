FROM python:3.11-slim

# Working Directory
WORKDIR /app

# Copy source code to working directory
COPY Src /app/Src/
COPY Data /app/Data/
COPY requirements.txt /app/
COPY Assets /app/Assets/
COPY Export /app/Export/
COPY .streamlit /app/.streamlit/
COPY Doc /app/Doc/

# Install packages from requirements.txt

RUN pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

CMD python -m streamlit run /app/Src/Streamlit/1_👋_Dataset_Presentation.py