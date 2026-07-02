def get_employee_data(df, employee_id):
    return df[df["id"] == employee_id]