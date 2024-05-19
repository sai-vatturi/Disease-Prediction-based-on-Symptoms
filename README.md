# Disease Prediction Based on Symptoms

This repository contains a web application for predicting diseases based on symptoms using a Decision Tree algorithm. The application is built with Flask, a lightweight WSGI web application framework in Python.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Features
- User-friendly web interface for symptom input
- Predicts possible diseases based on the entered symptoms
- Displays the most probable disease with confidence level
- Provides information about the predicted diseases

## Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Steps
1. Clone the repository:
    ```sh
    git clone https://github.com/sai-vatturi/Disease-Prediction-based-on-Symptoms.git
    cd Disease-Prediction-based-on-Symptoms
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the application:
    ```sh
    flask run
    ```

5. Open your web browser and navigate to `http://127.0.0.1:5000`

## Usage
1. Open the application in your web browser.
2. Enter the symptoms you are experiencing in the input fields.
3. Click on the "Predict" button to get the prediction.
4. The application will display the predicted disease along with a confidence score.

## Technologies Used
- Python
- Flask
- scikit-learn (for Decision Tree implementation)
- HTML/CSS/JavaScript (for the front-end)


## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
- The Flask framework documentation
- scikit-learn for providing the machine learning tools
- Everyone who contributed to improving this project

