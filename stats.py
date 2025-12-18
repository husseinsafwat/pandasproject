def get_col_max(col:list):
    """
    Compute the maximum value of a numerical column.

    Args:
        col (list): A list of numerical values. `None` values are ignored.

    Returns:
        The maximum value in the column (numeric type).
    """
    col = [value for value in col if value is not None]
    try:
        element = col[0]

        for value in col :
            if value>element:
                element = value
        return element
    except TypeError as e :
        print(e)

def get_col_min(col:list):
    """
    Compute the minimum value of a numerical column.

    Args:
        col (list): A list of numerical values. `None` values are ignored.

    Returns:
        The minimum value in the column (numeric type).
    """
    col = [value for value in col if value is not None]

    element = col[0]
    try:
        for value in col :
            if value<element:
                element = value
        return element
    except TypeError as  e:
        print(e)

def get_col_mean(col:list):
    """
    Compute the mean (average) value of a numerical column.

    Args:
        col (list): A list of numerical values. `None` values are ignored.

    Returns:
        The mean value of the column (float).
    """
    sum_col = 0
    col = [value for value in col if value is not None]
    try:
        for value in col :
            if type(value)=='str' or type(value)=='object':
                print("mean is only performed on numeric data")
        for value in col:
            sum_col+=value

        return sum_col/len(col)
    except TypeError as e :
        print(e)




def get_col_median(col:list):
    """
    Compute the median value of a numerical column.

    Args:
        col (list): A list of numerical values. `None` values are ignored.

    Returns:
        The median value of the column (numeric type).
    """
    col = [value for value in col if value is not None]
    try:
        for value in col :
            if type(value)=='str' or type(value)=='object':
                print("median is only performed on numeric data")
        col = sorted(col)
        n = len(col)
        if n%2==0:
            n = len(col)
            med = (col[(n//2)]+col[(n//2)-1])*1.0*.5
        else:
            med = col[n//2]

        return med
    except TypeError as e :
        print(e)


    
def get_col_mode(col:list):
    """
    Compute the mode (most frequent value) of a column.

    Args:
        col (list): A list of values. `None` values are ignored.

    Returns:
        The mode value of the column. If multiple values have the same
        frequency, the first encountered is returned.
    """
    freq = {}
    max_freq = 0
    max_element = ''
    col = [value for value in col if value is not None]
    for value in col:
        if freq.get(value , -1 )>0:
            freq[value]+=1
        else :
            freq[value] = 1

        if freq[value] > max_freq:
            max_freq = freq[value]
            max_element = value


    return max_element



        
def get_stat(data:dict, dtypes:dict, function:str):
    """
    Apply a statistical function to all numerical columns in a dataset.

    Args:
        data (dict): Dictionary where keys are column names and values are lists of column values.
        dtypes (dict): Dictionary where keys are column names and values are data types ('int', 'float', 'string').
        function (function): A function to apply to each numerical column (e.g., get_col_max, get_col_mean).

    Returns:
        dict: A dictionary where keys are column names and values are the result
        of applying the function to that column. Only numerical columns are processed.
    """
    stats = {}
    if function == 'median':
        for col,dtype in dtypes.items():
            if dtype!='string':
                stats[function+'_'+col] = get_col_median(data[col])

    elif function == 'min':
        for col,dtype in dtypes.items():
            if dtype!='string':
                stats[function+'_'+col] = get_col_min(data[col])

    elif function == 'max':
        for col,dtype in dtypes.items():
            if dtype!='string':
                stats[function+'_'+col] = get_col_max(data[col])

    elif function == 'mode':
        for col,dtype in dtypes.items():
            stats[function+'_'+col] = get_col_mode(data[col])

    elif function == 'mean':
        for col,dtype in dtypes.items():
            if dtype!='string':
                stats[function+'_'+col] = get_col_mean(data[col])


    else:
        print("function not found")
        return {}

    return stats




