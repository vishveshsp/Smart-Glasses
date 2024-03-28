# Voice Assistant Readme

## Overview
This is a Python script implementing a simple voice assistant. The assistant can perform various tasks such as searching the web, object detection in images, converting images to text, telling jokes, and playing songs from YouTube. It utilizes speech recognition and text-to-speech libraries along with other packages for image processing and web browsing.

## Requirements
- Python 3.x
- Libraries:
  - pyttsx3
  - speech_recognition
  - webbrowser
  - wikipedia
  - requests
  - pywhatkit
  - pyjokes
  - PIL (Python Imaging Library)
  - pytesseract
  - OpenCV (cv2)
  - NumPy

## Features
1. **Voice Interaction**: The assistant interacts with the user through voice commands and responses.
2. **Time-based Greetings**: It greets the user based on the time of the day.
3. **Web Search**: Allows the user to perform web searches.
4. **Object Detection**: Performs object detection in images using YOLOv3.
5. **Image to Text**: Converts images to text using OCR (Optical Character Recognition).
6. **Jokes**: Tells jokes upon user request.
7. **Play Music**: Plays songs from YouTube based on user input.
8. **Listen Command**: Listens for commands and executes them.

## How to Use
1. Clone the repository or download the script.
2. Install the required libraries by running `pip install -r requirements.txt`.
3. Run the script using `python voice_assistant.py`.
4. Follow the voice prompts to interact with the assistant.
5. Available commands are: 
   - `search`: Perform web search
   - `object_detection`: Detect objects in an image
   - `image_to_text`: Convert image to text
   - `joke`: Listen to a joke
   - `play`: Play music
   - `listen`: Listen for user command
   - `exit`: Exit the program

## Notes
- Ensure your system has a microphone connected for voice input.
- Some functionalities may require an internet connection (e.g., web search, playing music).
- Object detection relies on pre-trained YOLOv3 weights (`yolov3.weights`) and configuration (`yolov3.cfg`), along with COCO dataset class names (`coco.names`). Ensure these files are present in the same directory as the script.
- The assistant uses Google's speech recognition service for voice recognition, which requires an internet connection.

## Author
Vishvesh Singh Pal

Feel free to reach out for any queries or contributions!
