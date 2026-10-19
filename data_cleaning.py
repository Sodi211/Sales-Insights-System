"""Task 2: load and clean the corner store's product and sales CSV data."""

import pandas as pd


DATE_FORMATS = ("%Y-%m-%d", "%Y/%m/%d", "%d/%m/%Y", "%d-%m-%Y")


def load_raw_data(products_path: str, sales_path: str):
    """Read both CSV files without making any cleaning changes."""
    products_df = pd.read_csv(products_path)
    sales_df = pd.read_csv(sales_path)
    return products_df, sales_df


def clean_products(products_df: "pd.DataFrame") -> "pd.DataFrame":
    """Return products with valid names/prices, consistent categories and unique IDs."""
    products = products_df.copy()
    products = products.drop_duplicates()

    # Blank text should count as missing, not as a valid product name.
    for column in ("product_id", "product_name", "category"):
        products[column] = products[column].astype("string").str.strip()
        products[column] = products[column].replace("", pd.NA)

    products["unit_price"] = pd.to_numeric(products["unit_price"], errors="coerce")
    products = products.dropna(subset=["product_id", "product_name", "category", "unit_price"])
    products = products[products["unit_price"] >= 0].copy()
    products["category"] = products["category"].str.title()

    # The database needs each product_id to be unique.
    products = products.drop_duplicates(subset=["product_id"], keep="first")
    return products.reset_index(drop=True)


def _standardise_date(value):
    """Parse known formats explicitly; ambiguous numeric dates are day-first."""
    if pd.isna(value) or not str(value).strip():
        return None
    date_text = str(value).strip()
    for date_format in DATE_FORMATS:
        try:
            return pd.to_datetime(date_text, format=date_format, errors="raise").strftime("%Y-%m-%d")
        except (ValueError, TypeError):
            continue
    return None


def clean_sales(sales_df: "pd.DataFrame", valid_product_ids) -> "pd.DataFrame":
    """Return dated, valid sales linked to cleaned products."""
    sales = sales_df.copy()
    sales = sales.drop_duplicates()

    for column in ("sale_id", "product_id", "payment_method", "customer_type"):
        sales[column] = sales[column].astype("string").str.strip().replace("", pd.NA)

    sales["quantity"] = pd.to_numeric(sales["quantity"], errors="coerce")
    sales["sale_date"] = sales["sale_date"].map(_standardise_date)

    # A sale must have a date, a product, an ID and a positive whole-number quantity.
    sales = sales.dropna(subset=["sale_id", "product_id", "quantity", "sale_date"])
    sales = sales[(sales["quantity"] > 0) & (sales["quantity"] % 1 == 0)].copy()
    sales = sales[sales["product_id"].isin(set(valid_product_ids))].copy()

    # Preserve transactions when only optional descriptive fields are missing.
    sales["payment_method"] = sales["payment_method"].fillna("Unknown")
    sales["customer_type"] = sales["customer_type"].fillna("Unknown")
    sales = sales.drop_duplicates(subset=["sale_id"], keep="first")
    sales["quantity"] = sales["quantity"].astype(int)
    return sales.reset_index(drop=True)


def cleaning_summary(raw_df: "pd.DataFrame", clean_df: "pd.DataFrame", name: str) -> str:
    """Summarise removed records; cleaned-in-place values do not change row counts."""
    removed = len(raw_df) - len(clean_df)
    return f"{name}: {len(raw_df)} raw rows -> {len(clean_df)} clean rows ({removed} removed)"

    
if __name__ == "__main__":
    # Load the original datasets
    products, sales = load_raw_data(
        "data/products.csv",
        "data/sales.csv"
    )

    # Clean the datasets
    clean_p = clean_products(products)
    clean_s = clean_sales(sales, clean_p["product_id"])

    # Save the cleaned datasets as new CSV files
    clean_p.to_csv("data/cleaned_products.csv", index=False)
    clean_s.to_csv("data/cleaned_sales.csv", index=False)

    # Display cleaning results
    print(cleaning_summary(products, clean_p, "products"))
    print(cleaning_summary(sales, clean_s, "sales"))

    print("Cleaned CSV files saved successfully!")

