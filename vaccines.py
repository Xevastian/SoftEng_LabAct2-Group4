from backend import DBModel

db = DBModel("vaccines.json")

class Vaccine:
    @staticmethod
    def check_stock(id):
        """Check the stock of a vaccine by its ID. Returns None if stock is 0 or less."""
        vaccine = db.get(id, "vaccineId")
        if vaccine and vaccine["stock"] > 0:
            return vaccine["stock"]
        return None  # Do not print if stock is 0 or less

    @staticmethod
    def reduce_stock(id, amount=1):
        """Reduce the stock of a vaccine by a given amount, ensuring it doesn't go below zero."""
        vaccine = db.get(id, "vaccineId")
        if not vaccine or vaccine["stock"] <= 0 and amount > vaccine['stock']:
            print('\n Unable to decrease stock due to limited or non existent supply.')
            return  # Do nothing if stock is already 0 or vaccine doesn't exist

        new_stock = max(0, vaccine["stock"] - amount)  # Ensure stock doesn't go negative
        db.update(id, "stock", new_stock, identifier_key="vaccineId")

    @staticmethod
    def add_vaccine(name, manufacturer, count):
        """If a vaccine with the same name & manufacturer exists, increase stock. Otherwise, add a new entry."""
        all_vaccines = db.read_all()
        
        for vaccine in all_vaccines:
            if vaccine["name"] == name and vaccine["manufacturer"] == manufacturer:
                # If found, increase stock instead of creating a new entry
                new_stock = vaccine["stock"] + count
                db.update(vaccine["vaccineId"], "stock", new_stock, identifier_key="vaccineId")
                return

        # If no existing vaccine found, create a new one
        new_vaccine = {
            "vaccineId": int(db.get_last_id("vaccineId")) + 1 if db.get_last_id("vaccineId") is not None else 1,
            "name": name,
            "manufacturer": manufacturer,
            "stock": count
        }
        db.create_data(new_vaccine)

    @staticmethod
    def getVaccineInfo(id):
        """Return the name and manufacturer of a vaccine by its ID."""
        vaccine = db.get(id, "vaccineId")
        if vaccine:
            return {"name": vaccine["name"], "manufacturer": vaccine["manufacturer"]}
        return None  # No print statement if not found

    @staticmethod
    def get_all_vaccines():
        """Return all vaccines from the database, excluding those with stock 0 or less."""
        all_vaccines = db.read_all()
        return [vaccine for vaccine in all_vaccines if vaccine["stock"] > 0]