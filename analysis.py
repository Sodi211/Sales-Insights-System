"""
analysis.py
------------
Task 4: Programming logic — functions, loops, conditionals and arrays.

This module covers KM-05 topics: Programming Basics (data types,
conditionals, loops, arrays/lists, functions) and Introduction to
Algorithms.

IMPORTANT: For this file, use plain Python (for-loops, if/else,
lists and dictionaries) even where pandas could do it in one line.
The point of this section is to demonstrate the programming
fundamentals from KM-05, not just pandas shortcuts.
"""


from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE_STATUS_RESPONSE, ALERT_DESCRIPTION_INSUFFICIENT_SECURITY


def total_sales_records(sales_rows: list) -> int:
    """
    Count how many sales records there are, using a loop (not len()
    directly on the list — practise the loop!).

    Args:
        sales_rows: a list of dictionaries, one per sale, e.g.
            [{"product_id": "P001", "quantity": 2, ...}, ...]

    Returns:
        the total number of records, as an integer, counted with a loop.
    """
    # TODO: Count sales records one at a time using a for loop.
    count = 0
    for row in sales_rows:
        count += 1
    return count
    raise NotImplementedError



def low_stock_alert(products_rows: list, threshold: int = 5) -> list:
    """
    Return a list of product names that are out of stock
    or have a stock quantity below the threshold.

    TODO: Use a for loop and if statements to identify
    products that need restocking.
    """

    alerts = []

    for product in products_rows:
        name = product.get("product_name", "Unknown product")
        in_stock = product.get("in_stock")
        stock_quantity = product.get("stock_quantity")

        # TODO: Check whether the product is out of stock.
        out_of_stock = False

        if in_stock is False:
            out_of_stock = True
        elif isinstance(in_stock, str):
            if in_stock.strip().lower() == "false":
                out_of_stock = True

        # TODO: Check whether the stock quantity is low.
        low_stock = False

        if stock_quantity is not None:
            try:
                if float(stock_quantity) <= threshold:
                    low_stock = True
            except (ValueError, TypeError):
                pass

        # TODO: Add products that need restocking.
        if out_of_stock or low_stock:
            alerts.append(name)

    return alerts



def monthly_sales_trend(sales_rows: list) -> dict:
    """
    Calculate the total quantity of products sold each month.

    TODO:
        Use a for loop to go through the sales records.
        Extract the year and month from each sale_date.
        Add up the quantities sold for each month.
        Return the monthly totals as a dictionary.
    """

    trend = {}

    for row in sales_rows:
        # TODO: Extract the year and month.
        month = str(row["sale_date"])[:7]

        # TODO: Get the quantity sold.
        quantity = int(row["quantity"])

        # TODO: Add the quantity to the correct month.
        if month in trend:
            trend[month] += quantity
        else:
            trend[month] = quantity

    return trend



def classify_transaction_size(quantity: int) -> str:
    """
    A small function that demonstrates if / elif / else.

    Rules:
        quantity >= 5   -> "Bulk"
        quantity >= 2   -> "Multiple"
        quantity == 1   -> "Single"
        anything else   -> "Invalid"

    TODO: implement the if / elif / else chain above.
    """
    if quantity >=5:
        return "Bulk"
    elif quantity >=2:
        return "Multiple"
    elif quantity == 1:
        return "Single"
    else:
        return "Invalid"
    raise NotImplementedError


def average_basket_size(sales_rows: list) -> float:
    """
    Calculate the average quantity per sale across ALL sales, using a
    loop to sum quantities and a loop (or len()) to count records.

    Returns:
        a float rounded to 2 decimal places."""

    # TODO: Calculate the average number of itemscount records per sale record.
    Total_quantity = 0
    Count = 0
    for row in sales_rows:
            Total_quantity += row["quantity"]
            Count += 1
    return round(Total_quantity / Count, 2)
    
    raise NotImplementedError
