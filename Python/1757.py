# Note: double brackets will return one dataframe column, whereas singles just return a series
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[(products.low_fats == "Y") & (products.recyclable == "Y")][["product_id"]]