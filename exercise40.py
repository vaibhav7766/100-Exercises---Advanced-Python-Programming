def generate_sql(table_name, col_names, constraints):
    cols = [
        " ".join((col, constraint)).strip()
        for col, constraint in zip(col_names, constraints)
    ]
    for i in range(len(cols)):
        temp = "\n\t" + cols[i]
        cols[i], temp = temp, cols[i]
    cols[-1] = cols[-1] + "\n"
    return f"CREATE TABLE {table_name} (" + ",".join(cols) + ")"


# ALTER
# def generate_sql(table_name, col_names, constraints):
#     cols = [
#         " ".join((col, constraint)).strip()
#         for col, constraint in zip(col_names, constraints)
#     ]
#     return f"CREATE TABLE {table_name} (\n\t" + ",\n\t".join(cols) + "\n)"
