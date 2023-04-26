from sqlalchemy import (
    create_engine,
    ForeignKey,
    Column,
    String,
    Integer,
    CHAR,
    ForeignKeyConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


Base = declarative_base()

engine = create_engine("sqlite:///data/mysample.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

galaxy = Galaxy(1, "Euclid")
galaxy2 = Galaxy(2, "Hilbert Dimension")

new_system = StarSystem(
    "Foo2",
    "G8pf",
    "Urbajave",
    "Bitoug Terminus",
    714556,
    3,
    "Gek",
    0,
    3,
    "High Tech",
    1,
)

session.add(galaxy)
session.add(galaxy2)
session.add(new_system)
session.commit()


results = session.query(Galaxy).all()
results2 = session.query(StarSystem).all()

for r in results:
    print(r.galaxy_name)

for r in results2:
    print(r.system_name)
