from apps.Observation import blueprint, observation_service
from flask import render_template, request, jsonify
from flask_login import login_required
import json
from werkzeug.exceptions import HTTPException


@blueprint.route('/allObservations', methods=['GET'])
@login_required
def api_get_observations():
    """
    Get all patients
    :return:
    """
    observations = observation_service.get_all_observation()
  #  return render_template('patient.html', title='Patient')
    return jsonify([observation.get_observation() for observation in observations])