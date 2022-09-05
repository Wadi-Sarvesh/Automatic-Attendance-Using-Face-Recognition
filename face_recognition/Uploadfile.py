from firebase import firebase
import pyrebase
import datetime
config = {"apiKey" : "AIzaSyCrVM-AUjkxdUxWcvAwF8o-xV0pj-FuNbo",
    "authDomain": "attendance-system-e15b2.firebaseapp.com",
    "databaseURL": "https://attendance-system-e15b2.firebaseio.com",
    "projectId": "attendance-system-e15b2",
    "storageBucket": "attendance-system-e15b2.appspot.com",
    "messagingSenderId": "575898501088",
    "appId": "1:575898501088:web:5cff59c3112b558865b585",
    "measurementId": "G-BG9Z80XHW5"}

pyrebase=pyrebase.initialize_app(config)
storage= pyrebase.storage()
filename="Attendance_"+str(datetime.date.today())
path_on_cloud= "uploads/" + "Attendance_" + str(datetime.date.today()) +".xls"
path_local= "Output_attendance.xls"
storage.child(path_on_cloud).put(path_local)

url= storage.child(path_on_cloud).get_url(None);
data ={
    'name': filename,
    'url': url
}


firebase=firebase.FirebaseApplication("https://attendance-system-e15b2.firebaseio.com/",None)
result = firebase.post("/uploads",data)
