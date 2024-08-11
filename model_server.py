from flask import Flask, request, render_template, redirect, url_for
import joblib
import pandas as pd

app = Flask(__name__)

# Load the model from the .joblib file
model = joblib.load(r'C:\Users\ISRAEL\Downloads\Diabetes_Model\Diabetes_Model\_GRC_model.joblib')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the POST request has the file part
        if 'file' not in request.files:
            return 'No file part', 400

        file = request.files['file']

        # If no file is selected
        if file.filename == '':
            return 'No selected file', 400

        # Check if the file is of the allowed type (e.g., CSV)
        if file and file.filename.endswith('.csv'):
            # Read the CSV file into a DataFrame
            data = pd.read_csv(file)

            # Process the data using your loaded model
            predictions = model.predict(data)

            # Convert predictions to a string and return
            return str(predictions)

        return 'Unsupported file type. Please upload a CSV file.', 400

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
