from random import choice as rc
from app import app
from models import db, Hero, Power, HeroPower

# This ensures the code only runs when you directly execute the file
if __name__ == '__main__':
    with app.app_context():  # Gives access to Flask app context
        print("🧹 Clearing db...")

        # Clear existing records to prevent duplicates
        HeroPower.query.delete()
        Power.query.delete()
        Hero.query.delete()

        print("🌱 Seeding powers...")
        powers = [
            Power(name="super strength", description="gives the wielder super-human strength"),
            Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed"),
            Power(name="super human senses", description="allows the wielder to use her senses at a super-human level"),
            Power(name="elasticity", description="can stretch the human body to extreme lengths"),
        ]
        db.session.add_all(powers)

        print("🌱 Seeding heroes...")
        heroes = [
            Hero(name="Kamala Khan", super_name="Ms. Marvel"),
            Hero(name="Doreen Green", super_name="Squirrel Girl"),
            Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
            Hero(name="Janet Van Dyne", super_name="The Wasp"),
            Hero(name="Wanda Maximoff", super_name="Scarlet Witch"),
            Hero(name="Carol Danvers", super_name="Captain Marvel"),
            Hero(name="Jean Grey", super_name="Dark Phoenix"),
            Hero(name="Ororo Munroe", super_name="Storm"),
            Hero(name="Kitty Pryde", super_name="Shadowcat"),
            Hero(name="Elektra Natchios", super_name="Elektra"),
        ]
        db.session.add_all(heroes)

        print("🔗 Adding powers to heroes...")
        strengths = ["Strong", "Weak", "Average"]
        hero_powers = []

        for hero in heroes:
            power = rc(powers)  # Randomly assign a power
            strength = rc(strengths)  # Random strength
            hero_powers.append(HeroPower(hero=hero, power=power, strength=strength))

        db.session.add_all(hero_powers)
        db.session.commit()

        print("✅ Done seeding!")
