import csv
def read_csv_file(file_path, dtypes:dict):
    """
    Read a CSV file and convert each column to the specified data type.

    Args:
        file_path (str): Path to the CSV data file.
        dtypes (dict): Dictionary mapping column names to data types ('int', 'float', 'string').

    Returns:
        dict: A dictionary where keys are column names and values are lists of column values.
              Missing values (empty strings) are replaced with None.
    
    """
    with open(file_path, mode = 'r') as file :
      rows = file.readlines()
      values = [row.split(',') for row in rows[1:]]
    output = {col:[] for col in dtypes.keys()}
    for row in values :
      for dt , key , value in zip(dtypes.values() , dtypes.keys() , row):
        if value.strip()=='':
          output[key].append(None)
          continue
        if dt=='string':
          output[key].append(str(value).replace('"' , '').strip())
        elif dt=='float':
          output[key].append(float(value))
        elif dt=='int':
          output[key].append(int(value))
    return output








def read_dtype(file_path):
    """
    Read a CSV file containing column names and their data types.

    Args:
        file_path (str): Path to the CSV file containing column names and types.

    Returns:
        dict: A dictionary where keys are column names and values are data types ('int', 'float', 'string').
    """
    with open(file_path, mode='r') as file:
        rows = file.readlines()[1:]
        output = {row.split(',')[0].strip(): row.split(',')[1].strip() for row in rows}


    return output
            
def write_file(file_path, data:dict):
    """
    Write a data dictionary to a CSV file.

    Args:
        file_path (str): Path to the output CSV file.
        data (dict): Dictionary where keys are column names and values are lists of column values.

    Returns:
        None
    """


    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)


        writer.writerow(data.keys())

        if not data:
            return

        num_rows = len(list(data.values())[0])

        for i in range(num_rows):
            row_values = [data[key][i] for key in data.keys()]
            writer.writerow(row_values)
