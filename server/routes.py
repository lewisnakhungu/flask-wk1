from flask import request, jsonify
from models import Hero

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
