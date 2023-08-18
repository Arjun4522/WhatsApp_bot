FROM python:3


WORKDIR /app

COPY . /app


RUN pip install pywhatkit selenium chromedriver-autoinstaller


CMD ["python", "your_script.py"]
