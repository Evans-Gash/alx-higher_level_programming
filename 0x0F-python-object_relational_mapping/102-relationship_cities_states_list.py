#!/usr/bin/env python3
"""Lists all City objects from the database with their linked State objects."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create the connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, db_name))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve and print the cities and their linked states
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        state_name = city.state.name
        print("{}: {} -> {}".format(city.id, city.name, state_name))

    session.close()
