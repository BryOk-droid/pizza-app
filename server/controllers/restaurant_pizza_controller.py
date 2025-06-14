from flask import Blueprint, request, jsonify
from server.models import RestaurantPizza, db, Restaurant, Pizza

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__)

@restaurant_pizza_bp.route('/', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()

    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    if not (1 <= price <= 30):
        return jsonify({"errors": ["Price must be between 1 and 30"]}), 400

    restaurant = Restaurant.query.get(restaurant_id)
    pizza = Pizza.query.get(pizza_id)

    if not restaurant or not pizza:
        return jsonify({"error": "Invalid restaurant or pizza ID"}), 404

    rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
    db.session.add(rp)
    db.session.commit()

    return jsonify({
        "id": pizza.id,
        "name": pizza.name,
        "ingredients": pizza.ingredients
    }), 201
