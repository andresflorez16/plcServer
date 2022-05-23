import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("proyecto-plc-fc319-firebase-adminsdk-n91zc-2b95fbd049.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://proyecto-plc-fc319-default-rtdb.firebaseio.com/'
})

def pushData(ref, data):
    ref = db.reference(ref)
    ref.push(data)

