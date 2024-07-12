def generate_sql(table_name, col_names, constraints):
    columns = ""
    for i, j in zip(col_names, constraints):
        if j:
            columns += i + " " + j + ", "
        else:
            columns += i + ", "
    columns = columns[:-2]
    return f"CREATE TABLE {table_name} ({columns})"


# ALTER
# def generate_sql(table_name, col_names, constraints):
#     cols = [
#         " ".join((col, constraint)).strip()
#         for col, constraint in zip(col_names, constraints)
#     ]
#     return f"CREATE TABLE {table_name} (" + ", ".join(cols) + ")"
