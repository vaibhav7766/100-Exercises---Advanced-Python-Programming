def generate_sql(table_name, col_names):
    columns = ""
    for i in col_names:
        columns += i + "," + " "
    return f"CREATE TABLE {table_name} ({columns[:-2]})"

# ALTER
# def generate_sql(table_name, col_names):
#     return f"CREATE TABLE {table_name} (" + ", ".join(col_names) + ")"
