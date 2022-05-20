import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("plcserver-firebase-adminsdk-cfmgb-a6159b7fbb.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://plcserver-default-rtdb.firebaseio.com'
})

def pushData(ref, data):
    ref = db.reference(ref)
    ref.push(data)

