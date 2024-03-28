import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia 
import datetime
import requests
import pywhatkit as kit
import pyjokes
from PIL import Image
from pytesseract import pytesseract
import cv2
import numpy as np
import sys

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning! How can I assist you?")
    elif 12 <= hour < 17:
        speak("Good afternoon! How can I assist you?")
    elif 17 <= hour < 21:
        speak("Good evening! How can I assist you?")
    else:
        speak("Hello! How can I assist you?")

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print("You said:", query)
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return ""
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return ""

def capture_image(image_path):
    camera = cv2.VideoCapture(0)
    while True:
        _, img = camera.read()
        cv2.imshow('Capture Image', img)
        key = cv2.waitKey(1)
        if key == ord('s'):
            cv2.imwrite(image_path, img)
            camera.release()
            cv2.destroyAllWindows()
            break
        elif key == ord('q'):
            camera.release()
            cv2.destroyAllWindows()
            return None

def image_to_text(image_path):
    text = pytesseract.image_to_string(Image.open(image_path))
    return text

def object_detection(image_path):
    net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
    classes = []
    with open("coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]


    img = cv2.imread(image_path)
    img = cv2.resize(img, None, fx=0.4, fy=0.4)
    height, width, channels = img.shape
    # obj detection
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)
    # display info
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                # Obj detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                # coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, label, (x, y + 30), font, 3, (0, 255, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    while True:
        print("Enter the function name ('search', 'object_detection', 'image_to_text', 'joke', 'play', 'exit'): ")
        function_name = input().strip().lower()

        if function_name == 'exit':
            speak("Goodbye!")
            break

        if function_name == 'search':
            speak("Enter the search query: ")
            query = input().strip()
            speak("Searching the web. Please wait.")
            query = query.replace("webbrowser", " ")
            webbrowser.open(query)

        elif function_name == 'object_detection':
            speak("Please show the object to the camera.")
            capture_image('object_detection.jpg')
            object_detection('object_detection.jpg')

        elif function_name == 'image_to_text':
            speak("Please show the image to the camera.")
            capture_image('image_to_text.jpg')
            text = image_to_text('image_to_text.jpg')
            speak("The text in the image is:")
            speak(text)

        elif function_name == 'joke':
            joke = pyjokes.get_joke()
            speak(joke)

        elif function_name == 'play':
            speak("Enter the song name or URL: ")
            query = input().strip()
            query = query.replace("play", "")
            kit.playonyt(query)
            speak("Playing on YouTube. Please wait.")
        
        elif function_name == 'listen':
            speak("Listening for command...")
            query = listen_command()
            if query:
                speak("You said: " + query)

        else:
            speak("Invalid function name. Please try again.")

if __name__ == "__main__":
    main()
