Penguin Classification App
This application classifies penguins based on various attributes such as size, weight, and species. The model was trained using the penguins_cleaned.csv dataset and deployed as a web app using Streamlit.

Project Files
penguin-app.py: The main application file that runs the Streamlit web interface.
penguins_cleaned.csv: The dataset containing information about penguins, including their species, bill length, bill depth, flipper length, and body mass.
penguin_clf.pkl: The trained machine learning model used for classifying the penguins.
Procfile: Defines the commands to start the app.
requirements.txt: Lists the dependencies for the application.
runtime.txt: Specifies the Python runtime environment.
setup.sh: Setup script for deploying the app.
Installation and Setup
Clone this repository to your local machine:

git clone https://github.com/AshutoshTiwari0/penguin-classification-app.git
cd penguin-classification-app
Create a virtual environment:

python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
Install the required dependencies:

pip install -r requirements.txt
Run the Streamlit app locally:

streamlit run penguin-app.py
Visit the app at http://localhost:8501.

Usage
The app allows users to input the following penguin features:

Bill length (mm)
Bill depth (mm)
Flipper length (mm)
Body mass (g)
Once the user submits the input, the app predicts the species of the penguin.

Deployment
You can deploy the app to cloud platforms like Heroku. Here are the steps:

Create a Heroku account and install the Heroku CLI.

Log in to Heroku:


heroku login
Initialize a Git repository (if you haven't already):


git init
heroku create
git add .
git commit -m "Initial commit"
Push the app to Heroku:

git push heroku master
Open the app in the browser:


heroku open
Dependencies
Streamlit: For the web application interface.
Scikit-learn: For the machine learning model.
Pandas: For data manipulation.
Pickle: For saving and loading the trained model.
NumPy: For numerical computations.
These dependencies are listed in the requirements.txt file.

