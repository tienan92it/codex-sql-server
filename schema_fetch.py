# import psycopg2
from sqlalchemy import create_engine, inspect
from utils import convert_to_crows_foot

# # Connect to the PostgreSQL database
# conn = psycopg2.connect(
#     host="34.87.6.108",
#     database="nghenhan_dev",
#     user="postgres",
#     password="NHqpeIJAzGphSklOwL4o"
# )

# # Open a cursor to perform database operations
# cur = conn.cursor()

# # Execute a query to get the tables and columns in the database
# cur.execute("SELECT table_name, column_name, data_type FROM information_schema.columns WHERE table_schema = 'public';")

# # Fetch all the table and column information
# table_columns = cur.fetchall()

# # Group the columns by table
# table_columns_dict = {}
# for table, column, data_type in table_columns:
#     if table not in table_columns_dict:
#         table_columns_dict[table] = []
#     table_columns_dict[table].append((column, data_type))

# # Identify the primary and foreign keys for each table
# table_keys_dict = {}
# for table, columns in table_columns_dict.items():
#     pk_columns = []
#     fk_columns = []
#     for column, data_type in columns:
#         if column == 'id' or column.endswith('_id'):
#             if column == 'id':
#                 pk_columns.append(column)
#             else:
#                 fk_columns.append(column)
#     if pk_columns:
#         table_keys_dict[table] = {'pk': pk_columns, 'fk': fk_columns}
#     else:
#         table_keys_dict[table] = {'fk': fk_columns}

# # Print the schema names
# print(table_columns_dict)

# # Close the cursor and the database connection
# cur.close()
# conn.close()


def getSchema(conn):
    # Create a connection to the database
    engine = create_engine(conn)

    # Create an inspector for the database
    inspector = inspect(engine)

    # Get the list of table names
    table_names = inspector.get_table_names()

    crow_foot = []
    # Loop over the table names and print their columns and keys
    for table_name in table_names:
        # Get the columns for the table
        columns = inspector.get_columns(table_name)

        # Get the primary keys for the table
        primary_keys = inspector.get_pk_constraint(
            table_name)['constrained_columns']

        # Get the foreign keys for the table
        foreign_keys = []
        for foreign_key in inspector.get_foreign_keys(table_name):
            foreign_keys.append({
                'constrained_columns': foreign_key['constrained_columns'],
                'referred_table': foreign_key['referred_table'],
                'referred_columns': foreign_key['referred_columns']
            })

        crow_foot_text = convert_to_crows_foot(
            table_name, columns, primary_keys, foreign_keys)
        # Print the table name, columns, primary keys, and foreign keys
        # print(crow_foot_text)
        crow_foot.append(crow_foot_text);

    return crow_foot
