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


class Galaxy(Base):
    __tablename__ = "galaxies"

    galaxy_number = Column("gnumber", Integer, nullable=False)
    galaxy_name = Column("gname", String, primary_key=True, nullable=False)

    systems = relationship("StarSystem", back_populates="galaxy")

    def __init__(self, number, name):
        self.galaxy_number = number
        self.galaxy_name = name


class StarSystem(Base):
    __tablename__ = "systems"

    member_galaxy = Column("host", String, nullable=False)
    star_class = Column("sclass", String)
    system_name = Column("sname", String, primary_key=True)
    region_name = Column("rname", String)
    core_distance = Column("cdistance", Integer)

    planet_count = Column("pcount", Integer)
    # TODO: Get list of planet names from Planets table and assign here
    # planet_names = Column("pnames", List)

    # Will be a list of ["Unavailable", "Gek", "Vykeen", "Korvax", "Abandoned"]
    native_population = Column("npop", String)

    # 0 == 'regular', 1 == 'outlaw'
    outlaw_status = Column("outlaw_status", Integer)

    # 1 == low, 2 == moderate, 3 == high
    economy_rating = Column("econ_rate", Integer)

    # Will be list of econ types
    economy_type = Column("econ_type", String)

    # 1 == low, 2 == moderate, 3 == high
    conflict_level = Column("conflict", Integer)

    galaxy = relationship("Galaxy", back_populates="systems")

    def __init__(
        self,
        galaxy,
        sclass,
        sys_name,
        reg_name,
        cdist,
        pcnt,
        natpop,
        status,
        erating,
        etype,
        clevel,
    ):
        self.member_galaxy = galaxy
        self.star_class = sclass
        self.system_name = sys_name
        self.region_name = reg_name
        self.core_distance = cdist
        self.planet_count = pcnt
        self.native_population = natpop
        self.outlaw_status = status
        self.economy_rating = erating
        self.economy_type = etype
        self.conflict_level = clevel


engine = create_engine("sqlite:///data/mysample.db", echo=True)
Base.metadata.create_all(bind=engine, checkfirst=True)

Session = sessionmaker(bind=engine)
session = Session()

# galaxy = Galaxy(1, "Euclid")
# galaxy2 = Galaxy(2, "Hilbert Dimension")

galaxy_x = session.query(Galaxy).filter_by(galaxy_name="Euclid").one()
# # galaxy_x = "foo"

new_system = StarSystem(
    galaxy_x.galaxy_name,
    "G8pf",
    "Urbajave2",
    "Bitoug Terminus",
    714556,
    3,
    "Gek",
    0,
    3,
    "High Tech",
    1,
)

# session.add(galaxy)
# session.add(galaxy2)
session.add(new_system)
session.commit()


results = session.query(Galaxy).all()
results2 = session.query(StarSystem).all()

for r in results:
    print(r.galaxy_name)

for r in results2:
    print(r.member_galaxy, r.system_name)
