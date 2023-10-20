import math

  
def get_points_for_retailer_name(receipt):
    """
    Calculates points based on the alphanumeric characters in the retailer's name from the receipt.
    
    Each alphanumeric character in the retailer's name awards one point.
    
    Parameters:
    receipt (dict): A dictionary containing the retailer's name with the key "retailer", 
                    where the value is a string.
    
    Returns:
    int: The total points calculated based on the alphanumeric characters in the retailer's name.
    """
    points = 0
    retailer_name =  receipt.get("retailer")
   
    if retailer_name is None:
        return points

    for char in retailer_name:
        if char.isalnum():
            points += 1
    return points

def get_purchase_day_points(receipt):
    """
    Awards points based on the parity of the purchase day.

    Parameters:
    receipt (dict): A dictionary containing the purchase date with the key "purchaseDate" 
                    in the format "YYYY-MM-DD".

    Returns:
    int: 6 if the purchase day is odd, 0 otherwise.
    """

    points = 0
    purchase_date_str = receipt.get("purchaseDate")
    
    if purchase_date_str is None:
        return points
    
    purchase_day= int(purchase_date_str[-2:])
    if purchase_day % 2 !=0:
        points += 6
    return points 


def get_purchase_hour_points(receipt):
    """
    Awards 10 points if the purchase time is after 2:00pm and before 4:00pm, otherwise returns 0.

    Parameters:
    receipt (dict): A dictionary containing the time of purchase with the key "purchaseTime",
                    formatted as "HH:mm".
    Returns:
    int: 10 if the purchase time is within the specified range, 0 otherwise.
    """

    points = 0
    purchase_time_str =  receipt.get("purchaseTime")

    if purchase_time_str is None or len(purchase_time_str) == 0:
        return points

    purchase_hour, purchase_minute = map(int, purchase_time_str.split(':'))
    
    if (purchase_hour == 14 and purchase_minute > 0) or (15 <= purchase_hour < 16):
        points += 10
    
    return points 
    

def is_total_multiple_points(receipt):
    """
    Awards 25 points if the total amount in the receipt is a multiple of 0.25.
    
    Parameters:
    receipt (dict): A dictionary containing the total amount with the key "total", 
                    where the value is a string.
    
    Returns:
    int: 25 if the total is a multiple of 0.25, 0 otherwise.
    """
    points = 0
    total_str =  receipt.get("total")
    
    if total_str is None:
        return points
    
    total = float(total_str)
    if total % 0.25 == 0:
        points += 25
    return points 

def is_total_round_dollar_amount_points(receipt):
    """
    Awards 50 points if the total amount in the receipt is a round dollar amount with no cents.
    
    Parameters:
    receipt (dict): A dictionary containing the total amount with the key "total", 
                    where the value is a string representing a floating-point number.
    
    Returns:
    int: 50 if the total amount meets the specified condition, 0 otherwise.
    """

    points = 0
    total_str =  receipt.get("total")

    if total_str is None:
        return points
    
    total = float(total_str)
    if total % 1 == 0:
        points += 50
    return points 

def get_points_for_items_in_receipt(receipt):
    """
    Calculates and returns the total points earned based on the number of items on the receipt.
    Points are awarded at a rate of 5 points for every pair of items.

    Parameters:
    receipt (dict): A dictionary containing a list of items under the key "items".

    Returns:
    int: The total points earned based on given criteria.
    """
    
    points = 0
    receipt_items = receipt.get("items")
    
    if receipt_items is None:
        return points
    
    pair_receipt_items = len(receipt_items) // 2
    points = pair_receipt_items * 5
    return points 

def trimmed_length_item_description_points(receipt):
    """
    Calculates points based on item descriptions and prices.
    
    If the trimmed length of an item description is a multiple of 3,
    the points earned are the item's price multiplied by 0.2,
    rounded up to the nearest integer.
    
    Parameters:
    receipt (dict): A dictionary containing a list of items with the key "items",
                    where each item is a dictionary with a "shortDescription" (str)
                    and a "price" (str) key.
    
    Returns:
    int: The total points earned based on given criteria.
    """

    points = 0
    receipt_items = receipt.get("items")

    if receipt_items is None:
        return points
    
    for item in receipt_items:
        description = item.get("shortDescription","")
        trimmed_description = description.strip()
        price = item.get("price","0")
        price = float(price)
        if(len(trimmed_description) % 3 == 0 and len(description) > 0):
            points += math.ceil(price*0.2)
    
    return points 


def get_total_receipt_points(receipt):
    """
    Calculate the total points awarded for a given receipt based on defined criteria.

    The function aggregates points from various criteria including retailer name, 
    purchase date and time, total amount, and item descriptions among others.

    Parameters:
    receipt (dict): A dictionary with keys such as 'retailer', 'purchaseDate',
                    'purchaseTime', 'total', and 'items'.

    Returns:
    int: The total points awarded for the receipt.
    """
    points = 0
    processors = [get_points_for_retailer_name, 
                get_purchase_day_points,
                get_purchase_hour_points,
                is_total_multiple_points,
                is_total_round_dollar_amount_points,
                get_points_for_items_in_receipt,
                trimmed_length_item_description_points
                ]
    for processor in processors:
        points += processor(receipt)

    return points
    