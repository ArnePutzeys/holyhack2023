# holyhack2023
## Structure
The project consists of a backend and a frontend, which are connected through a Django REST API. The backend is written in Python, the frontend in React.

### Backend + API
The Django API is located in the *holyhack2023/api* folder. The *api_interface* folder represents the actual API application, and the *pocket_api* folder contains Django's configuration files.

The backend files are also located in the api_interface folder. Below you can find a short description of each:
- *classification.py*: this file takes a dataset of reviews (in English) as input. Using Linear Discriminant Analysis it comes up with keywords that appear in groups together, indicating a trend in the data. Then it connects to openAI's text-davinci-002 to find a word that most accurately describes the subject of these keywords. A dictionary with these subjects as keys and the keywords as values is returned.
- *classification_dutch.py*: same as *classification.py*, but for dutch data. These two files could easily be merged together to save space.
- *sentiment_analysis.py*: this file performs sentiment analysis on the data: it calculates polarity (is the review positive or negative) and subjectivity (is the review objective or subjective?) for one individual review. This file is called in the data_count.py file to calculate the average sentiment for a specific keyword.
- *sentiment_dutch.py*: similar to the file above for Dutch reviews, but it cannot determine subjectivity since the underlying model (a Dutch one) does not support it. 
- *views.py*: this file defines the API's functions. The frontend can request data for a given keyword, receive data based on AI-inferred keywords (with the classification files), and request data that compares their company's reviews to their direct competitors. 
- *synonyms.py*: this file is currently not used in our implementation, but it is functional. It takes in a keyword and finds synonyms for it, which can then be passed to the *data_count.py* file to furthen the user's capabilities of "occurance analysis", in the end this only ended up working for english words since free Dutch synonyms apis are basically non existant
- *data_load.py*: 
- *data_count.py*:

In the scripts folder you can find additional scripts we developed during the hackathon:
- *reviewscraping.py*: used to scrape the Apple app store to collect data for our "competition analysis" functionality.
- *cv_to_json.py*: used (together with an online tool) to convert the spotify *.csv* data to an usable *.json* format.

### Frontend (React)
The frontend contains the following files and directories:
- */src/assets*: Assets of this project: this includes css, images and svg's.

- */src/backend*: JSON processors to contact the API from the backend.
- */src/chartsapi*: uses the backend data to create charts to display on the website.

- */src/components*: uomponents provided by the template Horizon Free.
- */src/layouts*: auth and admin are the 2 pages on this site, there are their base template.
- */src/theme*: themes provided by the template Horizon Free.
- */src/types*: typescript types used by the template Horizon Free.
- */src/variables*: variables for charts.
- */src/views*: the layout of each page inside "www.website.com/admin/page" "www.website.com/auth/page".
- */src/index.tsx*: main render function with routes from routes.tsx.
- *LICENSE*: a LICENSE from the template is provided.

## Run the project
### Backend
Run the backend by navigating to the */api/* folder and running the command `python manage.py runserver 80`. This will run the backend Django server on port 80.
### Frontend
After running `npm install`, you can launch the web application by running `npm start`. The page is hosted on *http://localhost:3000*.
