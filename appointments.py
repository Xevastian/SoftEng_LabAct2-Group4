from backend import DBModel

db = DBModel("appointments.json")

class Appointment:
    def schedule_appointment(userId,time,vaccination):
        new_appointment = {
            "appointmentId": int(db.get_last_id('appointmentId')) + 1 if db.get_last_id('appointmentId') != None else 1,
            "userId": userId,
            "time": time,
            "vaccination": vaccination,
            "status": 'Pending'
        }
        db.create_data(new_appointment)

    def getAllAppointments(filter_key = None, filter_value = None):
        return db.read_all(filter_key, filter_value)
    
    def update_appointment(appointmentId, key, new_value):
        db.update(appointmentId, key, new_value, identifier_key="appointmentId")

    def delete_appointment(appointmentId):
        db.delete(appointmentId, identifier_key="appointmentId")
    
