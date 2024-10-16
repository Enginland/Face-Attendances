import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://facerecognitionattendanc-d1da9-default-rtdb.firebaseio.com/"
})

# refference
ref = db.reference('Peoples')
# add data
data ={
"136257":
        {
            "name": "MAO SMITH",
            "major": "Software Engineer",
            "starting_year": 2018,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-01-01 00:54:34"
        },
"852741":
        {
            "name": "Chem Bunna",
            "major": "Financial",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-01-01 00:54:34"
        },
"452741":
        {
            "name": "Leang Panha",
            "major": "Financial Analyst",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-01-01 00:54:34"
        },
"952742":
        {
            "name": "Chon Bunham",
            "major": "Financial Analyst",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,  
            "last_attendance_time": "2024-01-01 00:54:34"
        },
    "252741":
{
            "name": "Korn Souty",
            "major": "Networker",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-01-01 00:54:34"
        }

}
# execute the data to send to the database
for key, value in data.items():
    ref.child(key).set(value)