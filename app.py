from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME =  os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)

db = client[DB_NAME]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/kirimdata", methods=["GET"])
def show_data():
    datastock = list(db.DataStock.find({}, {"_id": False}))
    return jsonify({"DataServer": datastock})

@app.route("/data", methods=["POST"])
def save_data():
    KodeObat_receive = request.form.get("KodeObat_give")
    NamaGenerik_receive = request.form.get("NamaGenerik_give")
    NamaMerek_receive = request.form.get("NamaMerek_give")
    Deskripsi_receive = request.form.get("Deskripsi_give")
    Stock_receive = request.form.get("Stock_give")
    EfekSamping_receive = request.form.get("EfekSamping_give")
    Indikasi_receive = request.form.get("Indikasi_give")
    Peringatan_receive = request.form.get("Peringatan_give")
    InteraksiObat_receive = request.form.get("InteraksiObat_give")
    Produsen_receive = request.form.get("Produsen_give")
    Harga_receive = request.form.get("Harga_give")
    doc = {
        'KodeObat' : KodeObat_receive,
        'NamaGenerik' : NamaGenerik_receive,
        'NamaMerek' : NamaMerek_receive,
        'Deskripsi' : Deskripsi_receive,
        'Stock' : Stock_receive,
        'EfekSamping' : EfekSamping_receive,
        'Indikasi' : Indikasi_receive,
        'Peringatan' : Peringatan_receive,
        'InteraksiObat' : InteraksiObat_receive,
        'Produsen' : Produsen_receive,
        'Harga' : Harga_receive,
    }
    db.DataStock.insert_one(doc)
    return jsonify({"message": "POST diterima bagus!!!"})



if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)