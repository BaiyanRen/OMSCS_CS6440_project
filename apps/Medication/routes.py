from apps.Medication import blueprint, medication_service
from flask import render_template, request, jsonify
from flask_login import login_required
import json
from werkzeug.exceptions import HTTPException
from apps.Medication import medication


@blueprint.route('/allMedications', methods=['GET'])
@login_required
def api_get_medications():
    """
    Get all patients
    :return:
    """
    medications = medication_service.get_all_medications()
  #  return render_template('patient.html', title='Patient')
    return jsonify([medication.get_medication() for medication in medications])