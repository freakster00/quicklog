Quicklog

This Flask application captures frames from an ESP32 stream and performs people counting using YOLO object detection.
Features

    Captures frames from an ESP32 stream.
    Performs people counting using YOLO object detection.
    RESTful API endpoint (/count) to trigger frame capture and people counting.

Prerequisites

Before running the application, make sure you have the following dependencies installed:

    Python 3.x
    Flask
    Flask-SQLAlchemy
    OpenCV (cv2)
    ultralytics
    PIL (Python Imaging Library)
    numpy

Install the dependencies using pip:

pip install -r requirements.txt

Usage

    Start the Flask server:

python app.py

    Navigate to http://localhost:5000/count in your web browser or use a REST client like Postman to trigger frame capture and people counting.

Configuration

    Update the stream_url variable in app.py with the URL of the ESP32 stream address.

Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or create a pull request.
License

This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgements

    This project utilizes the YOLO object detection model from Ultralytics.
