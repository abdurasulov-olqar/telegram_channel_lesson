from read_data import fromJson
import datetime


def get_post_month(data:dict,month:int)->int:
    """
    Return the number of posts for a given month

    Args:
        data (dict): a dictionary of posts
        month (int): as number between 1 and 12

    Returns: 
        int: the number of posts for the given month
    """
    number_of_month_msg: int = 0
    for post in data["messages"]:

        if post["type"] == "message":
            i = int(post["date_unixtime"])
            time = datetime.datetime.fromtimestamp(i)
            m = int(time.strftime("%m"))
            
            if m == month:
                number_of_month_msg += 1

    return number_of_month_msg

data = fromJson('data/result.json')
# print(get_post_month(data, 10))