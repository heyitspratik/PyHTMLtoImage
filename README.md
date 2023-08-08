# HTML to Image Converter with Flask

This is a simple Flask application that converts an HTML template into an image using the imgkit library.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python installed on your system.
- [imgkit](https://github.com/jarrekk/imgkit) library installed. You can install it using `pip install imgkit`.

## Getting Started

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/html-to-image-flask.git

2. Navigate to the project directory:
   
   ```bash
   cd html-to-image-flask

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt

5. Run the Flask application:

   ```bash
   python app.py

6. Access the converter in your browser by navigating to
   
   http://localhost:5000/convert_certificate

## Usage

1. Modify the participation_certificate.html template in the templates folder to match your desired certificate format.
2. Adjust the context variables in the convert_certificate function to customize the certificate content.
3. Run the Flask application as mentioned above.
4. Access the certificate conversion by navigating to http://localhost:5000/convert_certificate
