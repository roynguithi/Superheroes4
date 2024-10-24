from flask import Flask, jsonify, request, abort
from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'  # Update with your database URI
db.init_app(app)

@app.route('/')
def home():
    return "Welcome to the Superheroes API!"

# Route to get all heroes
@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes])

# Route to get a hero by ID
@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    hero_powers = HeroPower.query.filter_by(hero_id=id).all()
    return jsonify(hero.to_dict(hero_powers=hero_powers))

# Route to get all powers
@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers])

# Route to get a power by ID
@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify(power.to_dict())

# Route to update a power
@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    data = request.get_json()
    if "description" in data:
        power.description = data["description"]
        db.session.commit()
        return jsonify(power.to_dict())
    return jsonify({"errors": ["validation errors"]}), 400

# Route to create a new HeroPower
@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    new_hero_power = HeroPower(
        strength=data.get("strength"),
        power_id=data.get("power_id"),
        hero_id=data.get("hero_id")
    )
    db.session.add(new_hero_power)
    db.session.commit()
    return jsonify(new_hero_power.to_dict()), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure all tables are created
    app.run(debug=True)
