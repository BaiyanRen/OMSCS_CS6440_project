from apps.Medication.medication import Medication


def get_all_medications():
    """
    Get all patients
    :return:
    """
    return Medication.query.all()

