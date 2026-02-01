import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':""
})
ref = db.reference("students")
data = {
    "27_CS_21":
        {
            "Name": "Harvendra",
            "Major": "CSE",
            "Starting_Year": 2021,
            "Total_Attendance": 6,
            "Standing": "M",
            "Year": 3,
            "Last_Attendance": "2023-12-12 02:23:12"
        },
    "19_CS_21":
        {
            "Name": "Astha",
            "Major": "CSE",
            "Starting_Year": 2021,
            "Total_Attendance": 6,
            "Standing": "G",
            "Year": 3,
            "Last_Attendance": "2023-12-12 02:23:12"
        },
    "30_CS_21":
        {
            "Name": "Krishna",
            "Major": "CSE",
            "Starting_Year": 2021,
            "Total_Attendance": 9,
            "Standing": "M",
            "Year": 3,
            "Last_Attendance": "2023-12-12 02:23:12"
        },
    "48_CS_21":
        {
            "Name": "Sagar",
            "Major": "CSE",
            "Starting_Year": 2021,
            "Total_Attendance": 11,
            "Standing": "M",
            "Year": 3,
            "Last_Attendance": "2023-12-12 02:23:12"
        },
    "852741":
        {
            "Name": "Emily",
            "Major": "CSE",
            "Starting_Year": 2020,
            "Total_Attendance": 8,
            "Standing": "G",
            "Year": 3,
            "Last_Attendance": "2023-12-12 02:23:12"
        },
    "963852":
        {
            "Name": "Elon Musk",
            "Major": "CSE",
            "Starting_Year": 2019,
            "Total_Attendance": 7,
            "Standing": "M",
            "Year": 4,
            "Last_Attendance": "2023-12-12 02:23:12"
        }
}
for key, value in data.items():
    ref.child(key).set(value)
