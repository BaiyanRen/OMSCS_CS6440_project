from apps.Patient import blueprint
from flask import render_template, request, jsonify
from flask_login import login_required
from flask import render_template
from apps.Patient import patient_service
import json
from werkzeug.exceptions import HTTPException


@blueprint.route('/allPatients', methods=['GET'])
@login_required
def api_get_patients():
    """
    Get all patients
    :return:
    """
    patients = patient_service.get_all_patient()
  #  return render_template('patient.html', title='Patient')
    return jsonify([patient.get_patient() for patient in patients])

