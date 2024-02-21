# Student-placement-prediction


This is a Streamlit web application for predicting the placement of students based on their information.

## Requirements

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yash0203patil/Student-placement-prediction.git
cd Student-placement-prediction
```

2.Create a virtual environment (optional but recommended):

```bash
python -m venv env
```
3.Activate the virtual environment:

```bash
source env/bin/activate
```
4.Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage 

1.Make sure you're in the project directory and your virtual environment is activated.

2.Run the Streamlit app:
```bash
streamlit run app.py
```
 -Access the app in your web browser at http://localhost:8501.

 -Enter the student information in the input fields provided.

 -Click on the "Predict" button to see the placement prediction based on the provided information.

## Input Fields
 -Age: Enter the age of the student.
 -Gender: Select the gender of the student from the dropdown menu.
 -Stream: Select the stream of the student from the dropdown menu.
 -Internships: Enter the number of internships completed by the student.
 -CGPA: Enter the CGPA (Cumulative Grade Point Average) of the student.

## Output
-If the model predicts that the student is likely to be placed, a success message will be displayed.
-If the model predicts that the student is not likely to be placed, an error message will be displayed.

## Model
-The predictive model used in this app is stored in the placement_prediction_model.joblib file.

## Author
-Yash Patil

##License
-This project is licensed under the MIT License.
