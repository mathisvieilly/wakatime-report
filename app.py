from flask import Flask, request, render_template
import os
from excel_utils import write_to_excel
from process_data import process_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    # Get the filename and the files from the request
    uploaded_files = request.files.getlist("file[]")
    final_filename = request.form['filename'] + '.xlsx'

    csv_arrays = {}
    for file in uploaded_files:
        if file and file.filename.endswith('.csv'):
            # Process the file and get the data (the method will perform the necessary checks to ensure the file is valid)
            modified_filename,data = process_data(file)

            # Add the data to the dictionary with the filename as the key
            csv_arrays[modified_filename] = data
    
    # Write the data to an Excel file
    write_to_excel(csv_arrays, final_filename)

    # Delete the files
    delete_files = [file for file in csv_arrays.keys()]
    for file in delete_files:
        os.remove(file)
    
    return "Files downloaded and WakaTime reports generated successfully!"

if __name__ == '__main__':
    app.run(debug=True)
