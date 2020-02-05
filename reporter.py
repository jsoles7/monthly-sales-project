
#function in order to convert to price
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

print("GENERATING SALES REPORT FOR MONTH OF OCTOBER 2013...")
print("")
print("")


#beginning of the exercise code

import pandas as pd

#read in CSV
csv_filepath = "data/sales-201804.csv"
financial_figures = pd.read_csv(csv_filepath)

#convert CSV to dictionary
financial_figures.to_dict()

print(financial_figures)


