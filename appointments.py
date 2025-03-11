import datetime

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

    def updateStatus(self, new_status):
        self.status = new_status

    @classmethod
    def schedule(cls, userId, time, location):
        appointment = cls(userId, time, location, status="Scheduled")
        cls.appointments.append(appointment)
        return appointment

    @classmethod
    def getAppointment(cls, appointmentId):
        for appt in cls.appointments:
            if appt.appointmentId == appointmentId:
                return appt
        return None

    @classmethod
    def reschedule(cls, appointmentId, new_time, new_location):
        appointment = cls.get_appointment(appointmentId)
        if appointment:
            appointment.time = new_time
            appointment.location = new_location
            appointment.status = "Rescheduled"
            return appointment
        return None

    @classmethod
    def cancel(cls, appointmentId):
        appointment = cls.get_appointment(appointmentId)
        if appointment:
            appointment.status = "Canceled"
            return appointment
        return None

    @classmethod
    def getAllAppointments(cls):
        return cls.appointments

a1 = Appointment.schedule(101, "2025-03-15 14:00:00", "Hospital A")
a2 = Appointment.schedule(102, "2025-03-16 09:30:00", "Clinic B")

a1.updateStatus("Completed")

Appointment.reschedule(2, "2025-03-17 10:00:00", "Clinic C")

Appointment.cancel(1)

print([vars(appt) for appt in Appointment.get_all_appointments()])
