import pandas as pd
from datetime import datetime,timedelta
def process_scd2(source,target):
    today=datetime.today().strftime("%Y-%m-%d")
    yesterday=(
        datetime.today()-timedelta(days=1)
    ).strftime("%Y-%m-%d")
    changes=[]
    result=target.copy()
    result["Effective_To"]=(
        result["Effective_To"]
        .fillna("")
        .astype(str)
    )
    for _, s_row in source.iterrows():
        cid=s_row["Customer_ID"]
        current_record=result[
            (result["Customer_ID"]==cid)
            &(result["Current"]=="Y")
        ]
        if current_record.empty:
            new_row={
                "Customer_ID":cid,
                "Name":s_row["Name"],
                "City":s_row["City"],
                "Effective_From":today,
                "Effective_To": "",
                "Current":"Y"
            }
            result=pd.concat(
                [result,pd.DataFrame([new_row])],
                ignore_index=True
            )
        else:
            old=current_record.iloc[0]
            if(
                old["Name"] != s_row["Name"]
                or
                old["City"] != s_row["City"]
            ):
                idx=current_record.index[0]
                result.at[idx,"Effective_To"]=yesterday
                result.at[idx,"Current"]="N"
                new_row={
                    "Customer_ID":cid,
                    "Name":s_row["Name"],
                    "City":s_row["City"],
                    "Effective_From":today,
                    "Effective_To": "",
                    "Current":"Y"
                }
                result=pd.concat(
                    [result,pd.DataFrame([new_row])],
                    ignore_index=True
                )
                changes.append(
                    f"Customer {cid} city changed from "
                    f"{old['City']} to {s_row['City']}"
                )
    return result, changes            
