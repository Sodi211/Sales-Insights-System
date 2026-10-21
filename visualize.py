"""
visualize.py
-------------
Task 5: Turn your analysis into charts.

This module covers KM-04 KT07: Visualising Data with AI-assisted tools.
We use matplotlib here, one of the most common Python charting
libraries (conceptually similar to the ggplot2 example from the
KM-04 slides).

You must produce AT LEAST TWO charts:
  1. A bar chart of total revenue per product (or per category)
  2. A line chart of the monthly sales trend

Save both charts as .png files — you will include them as evidence
in your submission.
"""

import matplotlib.pyplot as plt



def bar_chart_revenue_per_product(names, revenues):
    """
    Create a bar chart showing total revenue per product.

    TODO:
        Use matplotlib to create a bar chart.
        Label the axes and add a title.
    """

    import matplotlib.pyplot as plt

    # TODO: Create the bar chart.
    plt.figure(figsize=(12, 6))
    plt.bar(names, revenues)

    # TODO: Add the title and axis labels.
    plt.title("Total Revenue per Product")
    plt.xlabel("Product Name")
    plt.ylabel("Revenue (R)")

    # TODO: Make product names readable.
    plt.xticks(rotation=45, ha="right")

    # TODO: Adjust the layout and display the chart.
    plt.tight_layout()
    plt.show()




def line_chart_monthly_trend(trend):
    """
    Create a line chart showing monthly sales trends.

    TODO:
        Extract the months and sales quantities.
        Plot the monthly trend using matplotlib.
        Add a title and axis labels.
    """

    import matplotlib.pyplot as plt

    # TODO: Extract the months and quantities.
    months = sorted(trend.keys())
    quantities = [trend[month] for month in months]

    # TODO: Create the line chart.
    plt.figure(figsize=(10, 6))
    plt.plot(months, quantities, marker="o", linestyle="-")

    # TODO: Add chart title and labels.
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Quantity Sold")

    # TODO: Display the sales values.
    for month, quantity in zip(months, quantities):
        plt.annotate(
            str(quantity),
            (month, quantity),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center"
        )

    # TODO: Adjust layout and display chart.
    plt.tight_layout()
    plt.show()
