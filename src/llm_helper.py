def explain_changes(changes):
    explanation="\n".join(changes)
    return f"""
SCD2 processing summary
{explanation}
Historical records preserved successfuly.
"""