import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendacerealtime-5786f-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "815610":
        {
            "name": "Nzola Kiampava",
            "major": "Robotics",
            "starting_year": 2010,
            "total_attendance": 6,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-12-03 00:55:43"
        },
    "852741":
        {
            "name": "Emilinda",
            "major": "Economics",
            "starting_year": 2020,
            "total_attendance": 6,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-12-03 00:55:43"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physis",
            "starting_year": 2010,
            "total_attendance": 6,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-12-03 00:55:43"
        }
}

for key, value in data.items():
    ref.child(key).set(value)