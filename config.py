# RUN_MODE: "DEMO" for full functionality,
#    features turned off
RUN_MODE = "DEV"

# USE_DSGE: True if the DSGE estimates as a part of the forecasts
USE_DSGE = False

DB_SETTINGS = {
    'AWS_PROD': {
        'USER_NAME': '',
        'PASSWORD' : '',
        'HOST'     : '',
        'PORT'     : 3306,
        'SCHEMA'   : ''
    },
    'AWS_DEV': {
        'USER_NAME': '',
        'PASSWORD' : '',
        'HOST'     : '',
        'PORT'     : 3306,
        'SCHEMA'   : ''
    },
    'LOCAL': {
        'USER_NAME': 'root',
        'PASSWORD' : 'password',
        'HOST'     : 'localhost',
        'PORT'     : 3306,
        'SCHEMA'   : 'worldprediction'
    }
}

# DATABASE_SOURCE: 'AWS_PROD' for production database hosted on RDS in AWS, 'LOCAL' for locally hosted mysql
#    server database
DATABASE_SOURCE = 'LOCAL'

DB_USER_NAME      = DB_SETTINGS[DATABASE_SOURCE]['USER_NAME']
DB_PASSWORD       = DB_SETTINGS[DATABASE_SOURCE]['PASSWORD']
DB_SERVER_ADDRESS = DB_SETTINGS[DATABASE_SOURCE]['HOST']
DB_PORT           = DB_SETTINGS[DATABASE_SOURCE]['PORT']
DB_NAME           = DB_SETTINGS[DATABASE_SOURCE]['SCHEMA']

# USER_DB_NAME is the same regardless of DATABASE_SOURCE; there is a single source for user data in the AWS Production
#    DB instance. (AWS_PROD DB_SETTINGS must be used directly to connect.)
USER_DB_NAME = 'gp_users'

# Support Mail Server settings
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = '465'
MAIL_USERNAME = ''
MAIL_PASSWORD = ''


# DEPLOY_READY: "True" for port 80 and 0.0.0.0 access, "False" for port 5000 and 127.0.0.1 localhost access
DEPLOY_READY = False
if DEPLOY_READY:
    HOST = "0.0.0.0"
    PORT = 80
    HOST_URL = ""
else:
    HOST = "127.0.0.1"
    PORT = 7000
    HOST_URL = "http://localhost:5000/"

# Flask login session settings
SECRET_KEY = 'a4e0a8b152c6771e462c6ab90bed7cbe825a616230095addb5ee051dcbe6a477'
