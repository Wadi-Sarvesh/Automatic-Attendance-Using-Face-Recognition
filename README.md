# Automatic-Attendance-Using-Face-Recognition
An automatic attendance application that takes attendance through face recognition, appends attendance on excel sheet and uploads it on firebase server

Face Recognition technology is gradually evolving to a universal biometric solution since it requires virtually zero effort from the users end while compared with other biometric options. It is accurate and allows high enrolment and verification rates. This project is based on face detection and recognition algorithms. It proposes an effective solution for automatic attendance and it is capable to mark the attendance by recognizing the face of a person. Haar Cascade Algorithm has been used for face detection. Project is based on python and android, the python program takes in the dataset, trains it and appends attendance sheet with attendance through face recognition. This excel sheet is uploaded on a firebase server and can be managed: read, updated by students and professors to track attendance.

To get started just clone the project! For the firebase part create a new project on firebase update its credentials in face_recognition/ServiceAccoutKey.json, furthermore update the values.xml file in the android application with your own credentials.