from apps.Patient.patient import Patient


def get_all_patient():
    """
    Get all patients
    :return:
    """
    return Patient.query.all()


