from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Animal, Product, Customer, Order, OrderDetail

# Підключення до бази даних через зазначену конект-стрічку
DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_hyEK_ZTRmq86zeLCAa4@mysql-32c408f5-ladbsbd.g.aivencloud.com:27163/Zooshop"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Функція для створення таблиць у БД
def create_database():
    Base.metadata.create_all(engine)
    print("База даних створена або оновлена.")

# Функція для виведення даних з усіх таблиць
def display_table_data():
    while True:
        print("\nМеню:")
        print("1. Вивести всі таблиці")
        print("2. Вивести тварин")
        print("3. Вивести продукти")
        print("4. Вивести користувачів")
        print("5. Вивести замовлення")
        print("6. Вивести деталі замовлення")
        print("0. Вихід")
        
        choice = input("Оберіть опцію: ")
        
        if choice == "1":
            # Вивести всі таблиці за один запит
            animals = session.query(Animal).all()
            products = session.query(Product).all()
            customers = session.query(Customer).all()
            orders = session.query(Order).all()
            order_details = session.query(OrderDetail).all()

            # Виведення всіх таблиць
            print("\nТварини:")
            for animal in animals:
                print(f"ID: {animal.AnimalID}, Name: {animal.Name}, Type: {animal.Type}, Age: {animal.Age}, Price: {animal.Price}")
            
            print("\nПродукти:")
            for product in products:
                print(f"ID: {product.ProductID}, Name: {product.Name}, Category: {product.Category}, Quantity: {product.Quantity}, Price: {product.Price}")
            
            print("\nКористувачі:")
            for customer in customers:
                print(f"ID: {customer.CustomerID}, Name: {customer.Name}, Phone: {customer.Phone}, Email: {customer.Email}, City: {customer.City}")
            
            print("\nЗамовлення:")
            for order in orders:
                print(f"Order ID: {order.OrderID}, Customer ID: {order.CustomerID}, Order Date: {order.OrderDate}, Total Amount: {order.TotalAmount}")
            
            print("\nДеталі замовлення:")
            for detail in order_details:
                print(f"OrderDetailID: {detail.OrderDetailID}, OrderID: {detail.OrderID}, ProductID: {detail.ProductID}, Quantity: {detail.Quantity}, Price: {detail.Price}")

        elif choice == "2":
            animals = session.query(Animal).all()
            for animal in animals:
                print(f"ID: {animal.AnimalID}, Name: {animal.Name}, Type: {animal.Type}, Age: {animal.Age}, Price: {animal.Price}")
        elif choice == "3":
            products = session.query(Product).all()
            for product in products:
                print(f"ID: {product.ProductID}, Name: {product.Name}, Category: {product.Category}, Quantity: {product.Quantity}, Price: {product.Price}")
        elif choice == "4":
            customers = session.query(Customer).all()
            for customer in customers:
                print(f"ID: {customer.CustomerID}, Name: {customer.Name}, Phone: {customer.Phone}, Email: {customer.Email}, City: {customer.City}")
        elif choice == "5":
            orders = session.query(Order).all()
            for order in orders:
                print(f"Order ID: {order.OrderID}, Customer ID: {order.CustomerID}, Order Date: {order.OrderDate}, Total Amount: {order.TotalAmount}")
        elif choice == "6":
            order_details = session.query(OrderDetail).all()
            for detail in order_details:
                print(f"OrderDetailID: {detail.OrderDetailID}, OrderID: {detail.OrderID}, ProductID: {detail.ProductID}, Quantity: {detail.Quantity}, Price: {detail.Price}")
        elif choice == "0":
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

# Основна частина програми
if __name__ == "__main__":
    create_database()  
    display_table_data()
