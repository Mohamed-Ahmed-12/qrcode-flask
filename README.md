# QR Code Generator

A Flask-based web application to generate QR codes based on user-provided input. This application accepts a URL or text, generates a QR code for it, and displays the QR code on the page.

---

## Features
- Accepts user input via a form.
- Generates QR codes dynamically.
- Displays the generated QR code on the same page.
- Provides an easy-to-use interface.

---

## Requirements

Ensure you have the following installed on your system:
- Python 3.7 or above
- Flask
- Python libraries: `qrcode`, `pillow`

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Mohamed-Ahmed-12/qrcode-flask.git
   cd qrcode-flask
2. Set Up a Virtual Environment:
   ```bash
   python -m venv myvenv
   source myvenv/bin/activate  # On Windows: myvenv\Scripts\activate

3. Install Dependencies:
   ```bash
   pip install flask qrcode pillow

4. Run the Application:
   ```bash
   python -m flask --app Project run --port 8000 --debug
The app will be available at http://127.0.0.1:8000.

## Project Structure

qrcode_generator/
├── Project/
│   ├── __init__.py         # Flask app initialization
│   ├── views.py            # Blueprint for QR code generation
│   ├── templates/
│   │   └── scan.html       # HTML template for user interface
│   └── static/             # (Optional) Static files like CSS/JS
├── README.md               # Project documentation
└── myvenv/                 # Virtual environment (not included in the repo)

## Usage

    Start the application using the instructions above.
    Navigate to http://127.0.0.1:8000/api/qrcode.
    Enter the URL or text you want to convert into a QR code.
    Submit the form to generate and view the QR code.

## Examples
Input:

A user inputs the following link in the form:

https://www.example.com

Output:

A QR code is displayed that links to the URL.
Contributing

## Contributions are welcome! To contribute:

    Fork the repository.
    Create a new branch for your feature or bugfix.
    Commit your changes and create a pull request.
## Demo
![Screenshot 2025-01-14 at 17-44-04 Qr Code](https://github.com/user-attachments/assets/6bce495b-674e-4cdd-89f3-1a926c375f33)
\
Downloaded Qrcode
![qrcode(1)](https://github.com/user-attachments/assets/b7dc278c-5e50-4df3-8710-dd75da9bee0f)
