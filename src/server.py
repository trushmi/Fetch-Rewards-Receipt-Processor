from flask import Flask, request, jsonify
import uuid
from utils import get_total_receipt_points
from validations import validate_receipt
from validations import is_receipt_id_valid
from validations import ValidationResult

server = Flask(__name__)

receipts_data = {}


@server.route("/receipts/process", methods=["POST"])
def process_receipts():
    """
    Function is responsible for handling POST requests to /receipts/process. 
    It retrieves the JSON payload, generates a unique ID using uuid, calculates 
    points based on the receipt and stores the points with the ID as the key.
    Returns the ID in the JSON response.
    
    Parameters:
        None: The function retrieves data from the request object.
    
    Returns:
        JSON: A JSON response containing either an error message (if the receipt 
        is invalid) or the unique receipt ID along with a corresponding HTTP status code.
    """
    receipt = request.get_json()
    validation_result = validate_receipt(receipt)
    if not validation_result.is_valid:
        return jsonify(error="The receipt is invalid", message=validation_result.message), 400
    receipt_id = str(uuid.uuid4())
    points = get_total_receipt_points(receipt)
    receipts_data[receipt_id] = points
    return jsonify(id=receipt_id), 201

@server.route("/receipts/<id>/points", methods=["GET"])
def get_points(id: str):
    """
    Function is responsible for handling GET requests to /receipts/{id}/points. 
    It retrieves the points using the ID provided in the path, and returns the 
    points in the JSON response. If the ID is not found, it returns a 404 error 
    with an appropriate message.
    
    Parameters:
        id (str): The unique identifier of the receipt whose points are to be retrieved.
    
    Returns:
        JSON: A JSON response containing either the points associated with the provided 
        ID or an error message along with a corresponding HTTP status code (either 200 or 404).
    """
    
    points_id = receipts_data.get(id)
    print(points_id,id)
    validation_points_id_result = is_receipt_id_valid(id)
    if not validation_points_id_result.is_valid or receipts_data.get(id) is None: 
        return jsonify(error="No receipt found for that id", message=validation_points_id_result.message), 404
    return jsonify(points=points_id)


if __name__ == "__main__":
   server.run(host='0.0.0.0')