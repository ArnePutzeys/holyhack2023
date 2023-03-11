# holyhack2023
## Structure
The project consists of a backend and a frontend, which are connected through a Django REST API. The backend is written in Python, the frontend in React.

### Backend + API
The Django API is located in the *holyhack2023/api* folder. The api_interface folder represents the actual API application, and the *pocket_api* folder contains Django's configuration files.

The backend files are also located in the api_interface folder. Below you can find a short description of each:
- *classification.py*: this file takes a dataset of reviews (in English) as input. Using Linear Discriminant Analysis it comes up with keywords that appear in groups together, indicating a trend in the data. Then it connects to openAI's text-davinci-002 to find a word that most accurately describes the subject of these keywords. A dictionary with these subjects as keys and the keywords as values is returned.
- *classification_dutch.py*: same as *classification.py*, but for dutch data. These two files could easily be merged together to save space.
- *sentiment_analysis.py*: this file performs sentiment analysis on the data: it calculates polarity (is the review positive or negative) and subjectivity (is the review objective or subjective?) for one individual review. This file is called in the data_count.py file to calculate the average sentiment for a specific keyword.
- *sentiment_dutch.py*: similar to the file above for Dutch reviews, but it cannot determine subjectivity since the underlying model (a Dutch one) does not support it. 
- *views.py*: this file defines the API's functions. The frontend can request data for a given keyword, receive data based on AI-inferred keywords (with the classification files), and request data that compares their company's reviews to their direct competitors. 
- *synonyms.py*: this file is currently not used in our implementation, but it is functional. It takes in a keyword and finds synonyms for it, which can then be passed to the *data_count.py* file to furthen the user's capabilities of "occurance analysis", in the end this only ended up working for english words since free Dutch synonyms apis are basically non existant
- *data_load.py*: This file defines some functions to load the data from the *.json* files into 4 lists: *output*, *score*, *iterations*, *graph_values*. These lists are used in the *data_count.py* file to get the data in the right format to be easy accessible for the data processing in *data_count.py*. Also the graph_values are displayed which are x and y values of how many times a keyword appears on a certain date in the reviews. Score is the total score that the keyword has gotten in all the reviews and is normalized later. We have 3 different data_load functions which all have their own purpose, data_load is a primitive function to extract data for the classification api. Data_load2 is used when there is a start and enddate between whom we want to extract the data. Data_load3 was a prototype and is deleted. Data_load4 is used to extract all the data from the whole dataset (enormous) as efficiënt as possible.
- *data_count.py*: The count function is used to count the amount of times a keyword appears in the reviews. It also calculates the average sentiment for the keyword. The count function is called in the *views.py* file to get the data for the API. All the data are the keywords and for every keyword the total amount of times it appears in the reviews, the percentage of how frequent it appears in the reviews, the polarity and subjectivity of a keyword, the average score of the keyword and the graph_values (x_values and y_values) for the graph. The data is returned in a nested list.


In the scripts folder you can find additional scripts we developed during the hackathon:
- reviewscraping.py was used to scrape the Apple app store to collect data for our "competition analysis" functionality
- *cv_to_json.py* was used (together with an online tool) to convert the spotify *.csv* data to an usable *.json* format

### Frontend (React)
The frontend contains the following files and directories:
- */src/assets*: Assets of this project: this includes css, images and svg's.

- */src/backend*: JSON processors to contact the API from the backend.
- /src/chartsapi: Uses the backend data to create charts to display on the website.

- */src/components*: Components provided by the template Horizon Free.
- */src/layouts*: Auth and admin are the 2 pages on this site, there are their base template.
- */src/theme*: Themes provided by the template Horizon Free.
- */src/types*: Typescript types used by the template Horizon Free.
- */src/variables*: Variables for charts.
- */src/views*: The layout of each page inside "www.website.com/admin/page" "www.website.com/auth/page".
- */src/index.tsx*: Main render function with routes from routes.tsx.
- *LICENSE*: A LICENSE from the template is provided.
