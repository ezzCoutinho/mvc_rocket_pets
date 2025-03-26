from flask import Blueprint, jsonify
from src.views.http_types.http_request import HttpRequest
from src.composer.pets_list_composer import pet_list_composer
from src.composer.pets_deleter_composer import pet_deleter_composer
from src.errors.error_types.error_controller import handle_errors


pet_route_bp = Blueprint("pets_routes", __name__)

@pet_route_bp.route("/pets", methods=["GET"])
def list_pets():
  http_request = HttpRequest()
  view = pet_list_composer()

  http_response = view.handle(http_request)
  return jsonify(http_response.body), http_response.status_code

@pet_route_bp.route("/pets/<string:name>", methods=["DELETE"])
def dete_pet(name: str):
  try:
    http_request = HttpRequest(param={"name": name})
    view = pet_deleter_composer()

    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code
  except Exception as exception:
    response = handle_errors(exception)
    return jsonify(response["body"]), response["status_code"]
