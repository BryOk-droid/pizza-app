from server.app import create_app
from server.models import db, Restaurant, Pizza, RestaurantPizza

app = create_app()

with app.app_context():
    print("Seeding database...")

    # Clear existing data
    RestaurantPizza.query.delete()
    Restaurant.query.delete()
    Pizza.query.delete()

    # Create restaurants
    r1 = Restaurant(name="Domino's", address="123 Main St")
    r2 = Restaurant(name="Pizza Hut", address="456 Elm St")

    # Create pizzas
    p1 = Pizza(name="Pepperoni", ingredients="cheese, pepperoni, sauce")
    p2 = Pizza(name="Hawaiian", ingredients="cheese, ham, pineapple")

    # Link them through RestaurantPizza
    rp1 = RestaurantPizza(price=12, restaurant=r1, pizza=p1)
    rp2 = RestaurantPizza(price=15, restaurant=r2, pizza=p2)
    rp3 = RestaurantPizza(price=10, restaurant=r1, pizza=p2)

    db.session.add_all([r1, r2, p1, p2, rp1, rp2, rp3])
    db.session.commit()

    print("Database seeded successfully.")
