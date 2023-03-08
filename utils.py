def convert_to_crows_foot(table_name, columns, primary_keys, foreign_keys):
    # Start with the table name
    crow_text = f"Table: {table_name}\n"
    
    # Create a list of column names with their types
    column_text = []
    for col in columns:
        col_name = col['name']
        col_type = str(col['type'])
        column_text.append(f"{col_name} ({col_type})")
        
    # Add the column list to the output
    crow_text += "Columns: [" + ", ".join(column_text) + "]\n"
    
    # Add primary keys, if any
    if primary_keys:
        pk_text = ", ".join(primary_keys)
        crow_text += f"Primary key(s): [{pk_text}]\n"
    
    # Add foreign keys, if any
    if foreign_keys:
        fk_text = []
        for fk in foreign_keys:
            fk_cols = fk['constrained_columns']
            ref_table = fk['referred_table']
            ref_cols = fk['referred_columns']
            fk_text.append(f"{', '.join(fk_cols)} -> {ref_table} ({', '.join(ref_cols)})")
        crow_text += "Foreign key(s): [" + ", ".join(fk_text) + "]\n"
        
    # Return the complete Crow's Foot notation
    return crow_text