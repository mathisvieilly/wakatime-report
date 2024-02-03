import pandas as pd
from file_utils import valid_wakatime_format

# Method to process the data from the file
def process_data(file):
    modified_filename = valid_wakatime_format(file)
    data = pd.read_csv(modified_filename, skiprows=2, index_col=False)

    # Sort the data by the Total column (the first line will be the total time spent on the project and for each date)
    data.sort_values(by='Total', ascending=False, inplace=True)

    return modified_filename, data
