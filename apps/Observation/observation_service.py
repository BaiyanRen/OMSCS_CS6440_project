from apps.Observation.observation import Observation


def get_all_observation():
    """
    Get all patients
    :return:
    """
    return Observation.query.all()