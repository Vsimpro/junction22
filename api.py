import flask, requests

from modules.sql import main
from modules.sql import *

from flask_cors import CORS, cross_origin
from flask import Flask, render_template, jsonify

app = Flask(__name__, static_folder="")
cors = CORS(app)


class Api:
    
    merchant_id = "6364e0008018ce361efafc85" 
    api_token_key = 'Bearer l9B2nDnGgcc8eilUx-tlw0qG26kqPesiZFH-Qs8nFTw'

    base_endpoint = f"/merchants/{merchant_id}/"

    fee_endpoint = f"/merchants/{merchant_id}/delivery-fee"
    order_endpoint = f"/merchants/{merchant_id}/delivery-order"

    api_gateway = "https://daas-public-api.development.dev.woltapi.com/"

    header = {
        "Authorization": "Bearer l9B2nDnGgcc8eilUx-tlw0qG26kqPesiZFH-Qs8nFTw"
    }

@app.route("/",  methods=['GET'])
def index(): 
    Database()
    main()
    return "index.html :)"


@app.route("/deliveries",  methods=['GET'])
def a_file(): 
    return Nodes.delivery_list

@app.route("/deliveries/add",  methods=['GET'])
def add_delivery(): 
    create_node("Rälssitie 20")
    find_pairs("Rälssitie 20")
    return Nodes.delivery_list


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8123)   