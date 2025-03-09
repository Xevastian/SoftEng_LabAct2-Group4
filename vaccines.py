class Vaccine:
    vaccines = []
    id = 1

    def __init__(self, name, manufacturer, numOfStock):
        self.vaccineId = Vaccine.id
        Vaccine.id += 1
        self.name = name
        self.manufacturer = manufacturer
        self.numOfStock = numOfStock

    def checkStock(self):
        return self.numOfStock

    def reduceStock(self, quantity):
        if quantity > self.numOfStock:
            return "Not enough stock available"
        self.numOfStock -= quantity
        return f"Stock reduced by {quantity}, remaining: {self.numOfStock}"

    @classmethod
    def addVaccine(cls, name, manufacturer, numOfStock):
        vaccine = cls(name, manufacturer, numOfStock)
        cls.vaccines.append(vaccine)
        return vaccine

    @classmethod
    def getVaccineById(cls, vaccineId):
        for vaccine in cls.vaccines:
            if vaccine.vaccineId == vaccineId:
                return vaccine
        return None

    @classmethod
    def getAllVaccines(cls):
        return cls.vaccines


v1 = Vaccine.addVaccine("Pfizer", "Pfizer Inc.", 100)
v2 = Vaccine.addVaccine("Moderna", "Moderna Inc.", 150)

print(v1.checkStock())
print(v1.reduceStock(20))
print([vars(v) for v in Vaccine.getAllVaccines()])
