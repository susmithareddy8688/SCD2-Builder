from src.scd2_processor import process_scd2
import pandas as pd

def test_scd2_change():
    source = pd.DataFrame({
        "Customer_ID":[101],
        "Name":["Ravi"],
        "City":["Bangalore"]
    })

    target = pd.DataFrame({
        "Customer_ID":[101],
        "Name":["Ravi"],
        "City":["Hyderabad"],
        "Effective_From":["2026-06-01"],
        "Effective_To":[""],
        "Current":["Y"]
    })

    result, changes = process_scd2(source, target)

    assert len(changes) > 0