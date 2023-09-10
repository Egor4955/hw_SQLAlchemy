import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = "publisher"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40))

    def __init__(self, id_publisher, name):
        self.id = id_publisher
        self.name = name

    def __str__(self):
        return f'({self.id}) {self.name}'
    

class Book(Base):
    __tablename__ = "book"
    
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=40))
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey(Publisher.id))

    def __init__(self, id_book, title, id_publisher):
        self.id = id_book
        self.title = title
        self.id_publisher = id_publisher

    def __str__(self):
        return f'{self.title}'


class Shop(Base):
    __tablename__ = "shop"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40))

    def __init__(self, id_shop, name):
        self.id = id_shop
        self.name = name
    
    def __str__(self):
        return f'{self.name}'


class Stock(Base):
    __tablename__ = "stock"

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey(Book.id))
    id_shop = sq.Column(sq.Integer, sq.ForeignKey(Shop.id))
    count = sq.Column(sq.Integer)

    def __init__(self, id_stok, id_book, id_shop, count):
            self.id = id_stok
            self.id_book = id_book
            self.id_shop = id_shop
            self.count = count
    

class Sale(Base):
    __tablename__ = "sale"

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer)
    date_sale = sq.Column(sq.Date)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey(Stock.id))
    count = sq.Column(sq.Integer)

    def __init__(self, id_price, price, date_sale, id_stock, count):
        self.id = id_price
        self.price = price
        self.date_sale = date_sale
        self.id_stock = id_stock
        self.count = count

    def __str__(self):
        return f'{self.price} | {self.date_sale}'



def create_tables(engine):
    Base.metadata.drop_all(engine)
    print("Данные удалены")
    Base.metadata.create_all(engine)
    print("Данные созданы")