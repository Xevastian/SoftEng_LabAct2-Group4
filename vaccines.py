from backend import DBModel

db = DBModel("vaccines.json")

class Vaccine:

    def check_stock(id):
        vaccine = db.get(id, "vaccineId")
        if vaccine and vaccine["stock"] > 0:
            return vaccine["stock"]
        return None  # Do not print if stock is 0 or less

    
    def reduce_stock(id, amount=1):
        vaccine = db.get(id, "vaccineId")
        if not vaccine or vaccine["stock"] <= 0 and amount > vaccine['stock']:
            print('\n Unable to decrease stock due to limited or non existent supply.')
            return  # Do nothing if stock is already 0 or vaccine doesn't exist

        new_stock = max(0, vaccine["stock"] - amount)  # Ensure stock doesn't go negative
        db.update(id, "stock", new_stock, identifier_key="vaccineId")

    
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

    
    def getVaccineInfo(id):
        """Return the name and manufacturer of a vaccine by its ID."""
        vaccine = db.get(id, "vaccineId")
        if vaccine:
            return {"name": vaccine["name"], "manufacturer": vaccine["manufacturer"]}
        return None  # No print statement if not found

    def get_available_vaccines():
        """Return a list of all vaccine names, including those with stock 0 or less."""
        all_vaccines = db.read_all()
        vaccine_names = [vaccine["name"] for vaccine in all_vaccines]

        # Print the list in the desired format
        print("\nAvailable Vaccines:")
        print("-" * 40)
        print(f"{'ID':<10}{'Vaccine':<20}")
        print("-" * 40)

        for index, name in enumerate(vaccine_names, 1):
            print(f"{index:<10}{name:<20}")


    def get_all_vaccines():
        """Return all vaccines from the database, excluding those with stock 0 or less."""
        all_vaccines = db.read_all()
        return [vaccine for vaccine in all_vaccines if vaccine["stock"] > 0]