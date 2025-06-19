from flask import request, jsonify
from models import db, Hero, Power, HeroPower

def register_routes(app):
    @app.route("/")
    def index():
        return 'Superhero API'

    @app.route("/heroes", methods=['GET'])
    def get_heroes():
        heroes = Hero.query.all()
        return jsonify([{
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name
        } for hero in heroes]), 200

    @app.route("/heroes/<int:id>", methods=["GET"])
    def get_hero_by_id(id):
        hero = Hero.query.get(id)
        if not hero:
            return jsonify({"error": "Hero not found"}), 404

        return jsonify({
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name,
            "hero_powers": [
                {
                    "id": hp.id,
                    "hero_id": hp.hero_id,
                    "power_id": hp.power_id,
                    "strength": hp.strength,
                    "power": hp.power.to_dict()
                } for hp in hero.hero_powers
            ]
        }), 200

    @app.route("/powers", methods=['GET'])
    def get_powers():
        powers = Power.query.all()
        return jsonify([power.to_dict() for power in powers]), 200

    @app.route("/powers/<int:id>", methods=['GET'])
    def get_power_by_id(id):
        power = Power.query.get(id)
        if not power:
            return jsonify({"error": "Power not found"}), 404
        return jsonify(power.to_dict()), 200

    @app.route("/powers/<int:id>", methods=['PATCH'])
    def update_power(id):
        power = Power.query.get(id)
        if not power:
            return jsonify({"error": "Power not found"}), 404

        data = request.get_json()
        new_description = data.get("description")

        if not new_description or len(new_description) < 20:
            return jsonify({"errors": ["validation errors"]}), 400

        power.description = new_description
        db.session.commit()
        return jsonify(power.to_dict()), 200

    @app.route("/hero_powers", methods=['POST'])
    def create_hero_power():
        data = request.get_json()
        strength = data.get("strength")
        power_id = data.get("power_id")
        hero_id = data.get("hero_id")

        if not strength or not power_id or not hero_id:
            return jsonify({"errors": ["validation errors"]}), 400

        try:
            hero = Hero.query.get(hero_id)
            power = Power.query.get(power_id)
            if not hero or not power:
                return jsonify({"errors": ["validation errors"]}), 400

            hero_power = HeroPower(
                strength=strength,
                hero_id=hero_id,
                power_id=power_id
            )
            db.session.add(hero_power)
            db.session.commit()

            return jsonify({
                "id": hero_power.id,
                "hero_id": hero_power.hero_id,
                "power_id": hero_power.power_id,
                "strength": hero_power.strength,
                "hero": {
                    "id": hero.id,
                    "name": hero.name,
                    "super_name": hero.super_name
                },
                "power": power.to_dict()
            }), 201

        except Exception:
            return jsonify({"errors": ["validation errors"]}), 400
