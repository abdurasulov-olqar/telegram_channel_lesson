from read_data import fromJson
import datetime

def get_post_per_month(data:dict)->dict:
    """
    Return the number of posts for each month

    Args:
        data (dict): a dictionary of posts
        
    Returns: 
        dict: a dictionary with the number of posts for each month
    """
    number_of_month_msg: int = 0
    month_msgs_number: dict = {}
    
    for month in range(1, 13):
        for post in data["messages"]:
            if post["type"] == "message":
                i = int(post["date_unixtime"])
                time = datetime.datetime.fromtimestamp(i)
                m = int(time.strftime("%m"))
            
                if m == month:
                    number_of_month_msg += 1

        month_msgs_number.update({month: number_of_month_msg})
    return month_msgs_number

data = fromJson('data/result.json')
# print(get_post_per_month(data))

