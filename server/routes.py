from flask import request, jsonify
from models import db, Hero, Power, HeroPower

def register_routes(app):

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
        return jsonify(hero.to_dict()), 200

    @app.route('/heroes/<int:id>', methods=['DELETE'])
    def delete_hero(id):
        hero = Hero.query.get(id)
        if not hero:
            return jsonify({"error": "Hero not found"}), 404
        db.session.delete(hero)
        db.session.commit()
        return jsonify({"message": "Hero deleted"}), 200

    @app.route('/heroes/<int:id>', methods=['PUT'])
    def update_hero(id):
        hero = Hero.query.get(id)
        if not hero:
            return jsonify({"error": "Hero not found"}), 404
        data = request.get_json()
        hero.name = data.get('name', hero.name)
        hero.super_name = data.get('super_name', hero.super_name)
        db.session.commit()
        return jsonify(hero.to_dict()), 200

    @app.route('/powers', methods=['POST'])
    def create_power():
        data = request.get_json()
        try:
            new_power = Power(name=data['name'], description=data['description'])
            db.session.add(new_power)
            db.session.commit()
            return jsonify(new_power.to_dict()), 201
        except Exception:
            return jsonify({"errors": ["validation errors"]}), 400

    @app.route('/powers/<int:id>', methods=['DELETE'])
    def delete_power(id):
        power = Power.query.get(id)
        if not power:
            return jsonify({"error": "Power not found"}), 404
        db.session.delete(power)
        db.session.commit()
        return jsonify({"message": "Power deleted"}), 200

    @app.route('/powers/<int:id>/heroes', methods=['GET'])
    def get_heroes_by_power(id):
        power = Power.query.get(id)
        if not power:
            return jsonify({"error": "Power not found"}), 404
        heroes = [hp.hero.to_dict() for hp in power.hero_powers]
        return jsonify(heroes), 200

    @app.route('/hero_powers/<int:id>', methods=['DELETE'])
    def delete_hero_power(id):
        hero_power = HeroPower.query.get(id)
        if not hero_power:
            return jsonify({"error": "HeroPower not found"}), 404
        db.session.delete(hero_power)
        db.session.commit()
        return jsonify({"message": "HeroPower deleted"}), 200
