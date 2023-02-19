import json


def fromJson(file_path: str)->dict:
    """
    This function will read the json file and return the data as a dictionary.
    
    Parameters:
        file_path (str): Path of the file to be read
    Returns:
        dict: Dictionary containing the data of the json file.
    
    """
    data = open(file_path, encoding='utf-8-sig')
    data = data.read()
    json_data = json.loads(data)
    
    return json_data

data = "data/result.json"
# print(fromJson(data))