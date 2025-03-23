from flask import Blueprint, jsonify
from src.views.http_types.http_request import HttpRequest
from src.composer.pets_list_composer import pet_list_composer
from src.composer.pets_deleter_composer import pet_deleter_composer

pet_route_bp = Blueprint("pets_routes", __name__)

@pet_route_bp.route("/pets", methods=["GET"])
def list_pets():
  http_request = HttpRequest()
  view = pet_list_composer()

  http_response = view.handle(http_request)
  return jsonify(http_response.body), http_response.status_code

@pet_route_bp.route("/pets/<string:name>", methods=["DELETE"])
def dete_pet(name: str):
  http_request = HttpRequest(param={"name": name})
  view = pet_deleter_composer()

  http_response = view.handle(http_request)
  return jsonify(http_response.body), http_response.status_code
