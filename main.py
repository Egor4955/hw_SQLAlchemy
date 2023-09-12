import sqlalchemy
from sqlalchemy.orm import sessionmaker, declarative_base
from models import Publisher, Shop, Book, Stock, Sale, create_tables

Base = declarative_base()

login = 'postgres'
password = 1234
db_name = 'hw_book'
DSN = f'postgresql://{login}:{password}@localhost:5432/{db_name}'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)


Session = sessionmaker(bind=engine)
session = Session()

publisher_1 = Publisher(1,'Пушкин')
publisher_2 = Publisher(2,'Толстой')
publisher_3 = Publisher(3, 'Чехов')
publisher_4 = Publisher(4, 'Гоголь')

session.add(publisher_1)
session.add(publisher_2)
session.add(publisher_3)
session.add(publisher_4)
session.commit()

book_1 = Book(1, 'Капитанская дочь', 1)
book_2 = Book(2, 'Руслан и Людмида', 1)
book_3 = Book(3, 'Война и Мир', 2)
book_4 = Book(4, 'Чайка', 3)
book_5 = Book(5, 'Мёртвые души', 4)

session.add(book_1)
session.add(book_2)
session.add(book_3)
session.add(book_4)
session.add(book_5)
session.commit()

shop_1 = Shop(1, 'Буквоед')
shop_2 = Shop(2, 'Книги и Книжечки')
shop_3 = Shop(3, 'Лабиринт')

session.add(shop_1)
session.add(shop_2)
session.add(shop_3)

session.commit()

stock_1 = Stock(1, 1, 1, 1)
stock_2 = Stock(2, 2, 1, 1)
stock_3 = Stock(3, 3, 3, 1)
stock_4 = Stock(4, 4, 2, 1)
stock_5 = Stock(5, 5, 1, 1)

session.add(stock_1)
session.add(stock_2)
session.add(stock_3)
session.add(stock_4)
session.add(stock_5)

session.commit()

sale_1 = Sale(1, 300, '07.09.2023', 1, 1)
sale_2 = Sale(2, 200, '08.09.2023', 2, 1)
sale_3 = Sale(3, 100, '09.09.2023', 3, 1)
sale_4 = Sale(4, 150, '10.09.2023', 4, 1)
sale_5 = Sale(5, 150, '09.09.2023', 5, 1)

session.add(sale_1)
session.add(sale_2)
session.add(sale_3)
session.add(sale_4)
session.add(sale_5)

session.commit()

def get_shops(info): #Функция принимает обязательный параметр
    result = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).select_from(Shop).\
    join(Stock).\
    join(Book).\
    join(Publisher).\
    join(Sale)
    if info.isdigit(): 
        result_info = result.filter(Publisher.id == info).all()
    else:
        result_info = result.filter(Publisher.name == info).all()
    for book, shop, sale, stock in result_info:
        print(f"{book: <40} | {shop: <10} | {sale: <8} | {stock.strftime('%d-%m-%Y')}")

if __name__ == '__main__':
    info = input("Введите данные: ")
    get_shops(info) 
session.close()
