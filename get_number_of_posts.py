from read_data import fromJson

def get_number_of_posts(data:dict)->int:
    """
    Return the number of posts for a given dictionary

    Args:
        data (dict): a dictionary of posts

    Returns: 
        int: the number of posts for the given dictionary
    """
    number_of_msgs = 0 
    for post in data["messages"]:
        if post["type"] == "message":
            number_of_msgs += 1
    return number_of_msgs
data = fromJson('data/result.json')
# print(get_number_of_posts(data))