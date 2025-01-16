import sqlite3

def initialize_database():
    connection = sqlite3.connect("database/bridge_costs.db")
    cursor = connection.cursor()

    # Create table for material cost data
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bridge_costs (
        material TEXT PRIMARY KEY,
        base_rate REAL,
        maintenance_rate REAL,
        repair_rate REAL,
        demolition_rate REAL,
        environmental_factor REAL,
        social_factor REAL,
        delay_factor REAL
    )
    """)

    # Prepopulate with data
    cursor.executemany("""
    INSERT OR IGNORE INTO bridge_costs VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, [
        ("Steel", 3000, 50, 200, 100, 10, 0.5, 0.3),
        ("Concrete", 2500, 75, 150, 80, 8, 0.6, 0.2),
    ])

    connection.commit()
    connection.close()
    print("Database initialized successfully!")

if __name__ == "__main__":
    initialize_database()
