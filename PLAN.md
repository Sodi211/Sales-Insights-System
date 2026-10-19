Thabo's Corner Store - Project Plan 
Task 1: Plan Before Coding (Computational Thinking) 
Project: Sales Insights System   Modules: KM-04 Data & Databases and KM-05 
Programming & Python 
1. Decomposition - Breaking the problem into smaller tasks 
My goal is to help Thabo understand his store's sales using a simple Python system. Instead 
of trying to build everything at once, I will divide the work into smaller parts: clean the CSV 
files, save the correct information in an SQLite database, analyse sales, create charts, and 
protect reports with a password. I will test each part before connecting everything through 
main.py. 
2. Pattern Recognition - Finding possible data problems 
After looking at the supplied files, I noticed that some product prices and names are missing, 
a product ID is repeated, and the category "Beverages" is not always written with the same 
capitalisation. The sales file also contains blank quantities, dates and payment methods, a 
repeated sale ID, and different date formats. I will check whether every sale is a valid 
product. For ambiguous dates such as 05-01-2026, I plan to use day-month-year when 
interpreting that format, then store valid dates as YYYY-MM-DD. I will record any 
assumptions and rejected rows rather than silently guessing. 
3. Abstraction - Keeping only what is needed 
I will focus on fields that answer Thabo's business questions. Product IDs will connect sales 
to products, while prices, quantities, and dates will help calculate revenue and sales trends. 
The in_stock field tells me whether an item is available, but it does not give an exact stock 
quantity, so I will not pretend it can measure how many items are left. 
4. Algorithm Design - Order of work 
1. data_cleaning.py: Load both CSV files with pandas, check for missing or duplicate 
values, standardise categories and dates, and prepare valid rows. 
2. database.py: Create linked products and sales tables in SQLite, insert cleaned records, 
and write SQL queries using JOIN, GROUP BY and SUM. 
3. analysis.py: Use Python functions, loops and conditions to identify best sellers, 
transaction sizes and monthly trends. 
4. visualize.py: Create and save a bar chart for product revenue and a line chart for 
monthly sales trends. 
5. security.py: Hash a password, check login attempts, and restrict access to sales 
reports. 
Finally, I will run main.py to test the full system, explain my cleaning decisions and security 
limitations in README.md, and commit my work to GitHub as I complete each stage.