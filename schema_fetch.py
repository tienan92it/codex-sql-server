# import psycopg2
from sqlalchemy import create_engine, inspect
from utils import convert_to_crows_foot


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
