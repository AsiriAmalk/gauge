# Gauge Chert with Drop Down
# Please change the data.csv file (Not data.xlsx convert Excel file to CSV)

Here is an example of graph visualization app using Dash and Flask
# This app was made with Flask 
#### Prerequisites: Python 3.6 or later

#### 1. Installing virtualenv
* On macOS and Linux:\
`python3 -m pip install --user virtualenv`
* On Windows \
 `py -m pip install --user virtualenv`
 
#### 2. Creating a virtual environment
* On macOS and Linux:\
`python3 -m venv env`
* On Windows:\
`py -m venv env`

The second argument is the location to create the virtual environment. Generally, you can just create this in your project and call it `env`.

venv will create a virtual Python installation in the `env` folder.

#### 3. Activating a virtual environment

* On macOS and Linux:\
`source env/bin/activate`

* On Windows:
`.\env\Scripts\activate`


###### You can confirm you’re in the virtual environment by checking the location of your Python interpreter, it should point to the env directory.

* On macOS and Linux:`which python`\
.../env/bin/python

* On Windows:`where python`\
.../env/bin/python.exe

#### Installing packages

`pip install -r requirements.txt`

#### Update / Create requirements.txt
`pip freeze > requirements.txt`

#### Flask Debug mode enable

* On macOS and Linux:\
`$ export FLASK_ENV=development`

* On Windows:\
`$ set FLASK_ENV=development`\
`$ flask run`

##### Launch in local host
`$ flask run` or 
`$ python app.py`

###### The app will run on the default port `http://127.0.0.1:5000/` 

##### Launch in public host / custom host
`$ flask run --host=0.0.0.0 --port=80`
