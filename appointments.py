class Appointments:
    appointments = [] 
    id = 1 

    def __init__(self, userId, location, status="Pending"):
        self.appointmentId = Appointments.id
        Appointments.id += 1  
        self.userId = userId
        self.location = location
        self.status = status

    def updateStatus(self, new_status):
        self.status = new_status

    @classmethod
    def schedule(cls, userId, location):
        appointment = cls(userId, location, status="Scheduled")
        cls.appointments.append(appointment)
        return appointment

    @classmethod
    def get_appointment(cls, appointmentId):
        for appt in cls.appointments:
            if appt.appointmentId == appointmentId:
                return appt
        return None 

    @classmethod
    def reschedule(cls, appointmentId, new_location):
        appointment = cls.get_appointment(appointmentId)
        if appointment:
            appointment.location = new_location
            appointment.status = "Rescheduled"
            return appointment
        return None 

    @classmethod
    def cancel(cls, appointmentId):
        """Cancels an appointment."""
        appointment = cls.get_appointment(appointmentId)
        if appointment:
            appointment.status = "Canceled"
            return appointment
        return None 

    @classmethod
    def get_all_appointments(cls):
        """Returns all appointments."""
        return cls.appointments
