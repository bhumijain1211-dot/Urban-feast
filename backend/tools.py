import pandas as pd

import os
CSV_PATH = os.path.join(os.path.dirname(__file__), "data", "bookings.csv")

def get_bookings() -> dict:
    df = pd.read_csv(CSV_PATH)
    return df.to_dict(orient="records")

def book_table(name: str, time: str, party_size: int) -> dict:
    df = pd.read_csv(CSV_PATH)
    
    if party_size <= 2:
        table_cols = ["table1_2p", "table2_2p", "table3_2p", "table4_2p"]
    else:
        table_cols = ["table5_4p", "table6_4p", "table7_4p", "table8_4p"]
    
    time_row = df[df["time"] == time]
    
    if time_row.empty:
        return {"success": False, "message": f"Time slot {time} not available."}
    
    row_index = time_row.index[0]
    
    for col in table_cols:
        if pd.isna(df.at[row_index, col]) or df.at[row_index, col] == "":
            df.at[row_index, col] = name
            df.to_csv(CSV_PATH, index=False)
            return {
                "success": True,
                "message": f"Table booked for {name} at {time} for {party_size} people. Table: {col}"
            }
    
    return {
        "success": False,
        "message": f"No tables available for {party_size} people at {time}."
    }