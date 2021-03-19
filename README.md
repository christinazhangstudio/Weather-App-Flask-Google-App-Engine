# Weather-App-Flask-Google-App-Engine

###### Inspiration and initial tutorial credit: [Free Code Camp] (https://www.freecodecamp.org/news/how-to-build-a-web-app-using-pythons-flask-and-google-app-engine-52b1bb82b221/)


<details open>
<summary>Table of Contents</summary>

- [Prerequisites](#prereq)
- [Environment Setup and Installation](#env)
- [Local Deployment](#deploy1)
- [Google Cloud Deployment](#deploy2)
- [Contact](#contact)
</details>

- - - -
## Prerequisites <a name="prereq"/>
- Python 3
- Free API key from [Open Weather Map](https://openweathermap.org/api)
- Google account
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)

- - - -
## Environment Setup and Installation <a name="env"/>
Create the virtual environment (Windows):

``` virtualenv venv ```

Activate the virtual environment (Windows):

`call venv\Scripts\activate.bat`

Install app dependencies:

`pip install -r requirements.txt`

- - - -
## Local Deployment <a name="deploy1"/>

`python main.py`

- - - -
## Google Cloud Deployment <a name="deploy2"/>
Replicate the library's dependencies in the lib folder:

`pip install -t lib -r requirements.txt`

Deploy on Google Cloud through Google Cloud SDK shell:

`gcloud init`

`gcloud app deploy app.yaml`

## Contact <a name="contact"/>
christinazhang2013@gmail.com
