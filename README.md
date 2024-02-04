
# WakaTime Report [![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)


Generate a formatted wakatime report from a CSV file downloaded from one of your projects tracked by Wakatime.



## Installation

Clone the repository

```bash
git clone https://github.com/mathisvieilly/wakatime-report.git
```

To run the project (make sure you're using your current version of Python, mine is 3.11)

```bash
cd wakatime-report
pip3 install -r requirements.txt
python3.11 app.py
```

Navigate to the website to start uploading your files

```bash
http://127.0.0.1:5000
```


## Usage

Download a WakaTime report on one of your projects as shown below.
![On the project page](https://i.ibb.co/VwZ9vsM/Screenshot-2024-02-03-at-11-51-51.png)

Then click on the "Download" blue button.
![Download the CSV file](https://i.ibb.co/rmGWm1n/Screenshot-2024-02-03-at-11-52-04.png)



Once you've downloaded the report(s), go to the site exposed by the application at http://127.0.0.1:5000.

Upload the downloaded CSV files - you can select more than one. Enter a name for the output file, and click on "Submit".

You're there! The output file is downloaded into the same folder as the repository (wakatime-report).

