from backend import DBModel

db = DBModel("appointments.json")

class Appointment:
    appointments = []
    id = 1

    def __init__(self, userId, time, location, status="Pending"):
        self.appointmentId = Appointment.id
        Appointment.id += 1
        self.userId = userId
        self.time = time
        self.location = location
        self.status = status

    def save_to_db(self):
        new_appointment = {
            "appointmentId": self.appointmentId,
            "userId": self.userId,
            "time": self.time,
            "location": self.location,
            "status": self.status
        }
        db.create(new_appointment)  # Save to the JSON file immediately

    @classmethod
    def schedule(cls, userId, time, location):
        appointment = cls(userId, time, location, status="Scheduled")
        cls.appointments.append(appointment)
        appointment.save_to_db()  # Save the appointment to JSON
        return appointment

    @classmethod
    def getAllAppointments(cls):
        return cls.appointments
