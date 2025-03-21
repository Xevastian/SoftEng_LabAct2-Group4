from backend import DBModel

class Vaccine:
    db = DBModel("vaccines.json")
    id_counter = 1

    def __init__(self, name, manufacturer, numOfStock):
        self.vaccineId = Vaccine.id_counter
        Vaccine.id_counter += 1
        self.name = name
        self.manufacturer = manufacturer
        self.numOfStock = numOfStock

    def check_stock(self):
        return self.numOfStock

    def reduce_stock(self, quantity):
        if quantity > self.numOfStock:
            return "Not enough stock available"
        self.numOfStock -= quantity
        Vaccine.db.update(self.vaccineId, "numOfStock", self.numOfStock, "vaccineId")
        return f"Stock reduced by {quantity}, remaining: {self.numOfStock}"

    def save_to_db(self):
        new_vaccine = {
            "vaccineId": self.vaccineId,
            "name": self.name,
            "manufacturer": self.manufacturer,
            "numOfStock": self.numOfStock
        }
        Vaccine.db.create(new_vaccine, "vaccineId")

    @classmethod
    def add_vaccine(cls, name, manufacturer, numOfStock):
        vaccine = cls(name, manufacturer, numOfStock)
        vaccine.save_to_db()
        return vaccine

    @classmethod
    def get_vaccine_by_id(cls, vaccineId):
        return cls.db.get(vaccineId, "vaccineId")

    @classmethod
    def get_all_vaccines(cls):
        return cls.db.get_all()
