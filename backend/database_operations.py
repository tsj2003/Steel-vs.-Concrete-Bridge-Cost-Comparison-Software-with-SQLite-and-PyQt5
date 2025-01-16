import sqlite3

def get_material_data(material):
    """
    Fetch cost data for the specified material from the database.
    :param material: 'Steel' or 'Concrete'
    :return: Dictionary containing cost data for the material.
    """
    connection = sqlite3.connect("database/bridge_costs.db")
    cursor = connection.cursor()

    query = "SELECT * FROM bridge_costs WHERE material = ?"
    cursor.execute(query, (material,))
    result = cursor.fetchone()
    connection.close()

    if result:
        return {
            "material": result[0],
            "base_rate": result[1],
            "maintenance_rate": result[2],
            "repair_rate": result[3],
            "demolition_rate": result[4],
            "environmental_factor": result[5],
            "social_factor": result[6],
            "delay_factor": result[7],
        }
    else:
        raise ValueError(f"Material '{material}' not found in the database.")
