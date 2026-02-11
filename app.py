from flask import Flask, Response, render_template
import cv2

app_test = Flask(__name__)

camera = cv2.VideoCapture(0)
# helps accessing the default built-in webcam of the computer

@app_test.route('/')
def index1():
    return render_template('index1.html')

# Loading the Haar cascade classifiers for face and eyes
face_cascade=cv2.CascadeClassifier("Haarcascades/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("Haarcascades/haarcascade_eye.xml")

def generate_frames():
# success is a boolean value and frame is a numpy array of the image
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # convert to grayscale to reduce noise and focus on intensity
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # detects faces at multiple sizes
            faces= face_cascade.detectMultiScale(gray, 1.1, 7)
            for (x,y,w,h) in faces:
                # draw a rectangle around each detected face
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                # extracting region of interest - face region
                roi_gray = gray[y:y+h,x:x+w]
                roi_color = frame[y:y+h,x:x+w]
                # detects eye within the face region
                eyes = eye_cascade.detectMultiScale(roi_gray,1.1,3)
                # iterates over each eye in the face
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                    
            ret, buffer = cv2.imencode('.jpg',frame)
            frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            
@app_test.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')
# the function continuously sends images to be displayed and mime type specifies there are multiple images and the old ones are to be replaced by the new ones


if __name__=="__main__":
    app_test.run(debug=True)
# debug=True is only used in production