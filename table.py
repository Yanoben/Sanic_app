from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey


metadata = MetaData()

users = Table('users',
              metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('fullname', String),
              )
checkes = Table('checkes',
                metadata,
                Column('id', Integer, primary_key=True),
                Column('user_id', None, ForeignKey('users.id')),
                Column('balance', Integer, nullable=False)
                )
products = Table('addresses',
                 metadata,
                 Column('id', Integer, primary_key=True),
                 Column('title', String(100), nullable=False),
                 Column('description', String(100), nullable=False),
                 Column('price', Integer, nullable=False)
                 )


# from sqlalchemy import Column, ForeignKey, Integer, String
# from sqlalchemy.orm import declarative_base, relationship

# Base = declarative_base()


# class User(Base):
#     __tablename__ = "user"
#     id = Column(Integer, primary_key=True)
#     first_name = Column(String(100), nullable=False)
#     last_name = Column(String(100), nullable=False)
#     checks = relationship("Check")


# class Check(Base):
#     __tablename__ = "check"
#     id = Column(Integer, primary_key=True)
#     parent_id = Column(Integer, ForeignKey("user_table.id"))


# class Products(Base):
#     __tablename__ = "products"
#     id = Column(Integer, primary_key=True)
#     title = Column(String(100), nullable=False)
#     description = Column(String(100), nullable=False)
#     price = Column(Integer, nullable=False)
