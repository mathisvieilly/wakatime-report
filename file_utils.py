# Method to validate the format of the wakatime file and a modified version of the file
def valid_wakatime_format(file):
    bytes_lines = file.readlines()

    if 'Total' not in bytes_lines[2].decode('utf-8'):
        line = bytes_lines[2].decode('utf-8').strip()
        line += ',Total\n'
        bytes_lines[2] = line.encode('utf-8')

    modified_filename = file.filename.replace('.csv', '_modifie.csv')

    with open(modified_filename, 'w', encoding='utf-8') as modified_file:
        modified_file.writelines([line.decode('utf-8') for line in bytes_lines])

    return modified_filename