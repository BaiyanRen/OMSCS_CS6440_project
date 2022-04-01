from apps.Appointment.appointment import Appointment


def get_all_appointments():
    """
    Get all patients
    :return:
    """
    return Appointment.query.all()
