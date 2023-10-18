import firebase_admin
from firebase_admin import credentials
import pyrebase
from configs.firebase_config_example import firebaseConfig

if not firebase_admin._apps:
    cred = credentials.Certificate("configs/fastshopapi-firebase-adminsdk-hndzj-bb3a7be7b2.json")
    # cred = credentials.Certificate("path/to/serviceAccountKey.json")
    firebase_admin.initialize_app(cred) 
    
    # firebase_admin.initialize_app(cred)

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
auth = firebase.auth()