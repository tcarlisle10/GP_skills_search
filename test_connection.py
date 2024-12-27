from sqlalchemy import create_engine

# MySQL connection string
engine = create_engine("mysql+mysqlconnector://root:Migmaster10!@localhost/skill_x_change")

# Test the connection
try:
    with engine.connect() as connection:
        print("Connected to the database successfully!")
except Exception as e:
    print(f"Error: {e}")
