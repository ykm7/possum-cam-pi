import pyrebase
from camera-script import start_camera_system

config = {
  "apiKey": "AIzaSyDIqGnrv-p0FN65MOwbqBNQuY1AMZ4SLO4",
  "authDomain": "possum-cam.firebaseapp.com",
  "databaseURL": "https://possum-cam.firebaseio.com",
  "storageBucket": "possum-cam.appspot.com",
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()

deviceNumber = 1

pi_db_path = "pi/" + str(deviceNumber) + "/db/" + str(deviceNumber) + "/"
pi_storage_path = "pi" + str(deviceNumber) + "/storage/" + str(deviceNumber) + "/"

def auth_refresh_loop(user):
    global auth

    user = auth.refresh(user['refreshToken'])
    return user

def init():
    pass

def storeImage(file_path, )

if __name__ == "__main__":
    main()