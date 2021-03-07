# from flask import Flask, request, jsonify 
# from flask_sqlalchemy import SQLAlchemy 
# from flask_marshmallow import Marshmallow 
# import os 
# import strings

#  INIT APP 
# app = Flask(__name__)

# # BASIC ROUTE 
# @app.route('/', methods=['GET'])
# def get():
#     return jsonify({ 'msg': 'Hello Android'})

# SET DB
# BASE DIRECTORY 
# basedir = os.path.abspath(os.path.dirname(__file__))
# CONFIG DB 
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
# app. config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   # REMOVE WARNING

# INIT DB 
# db = SQLAlchemy(app)

# INIT MARSHMALLOW 
# marshmellow = Marshmallow(app)

# MODEL 
# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), unique=True)
#     description = db.Column(db.String(200))
#     price = db.Column(db.Float)
#     qty = db.Column(db.Integer)

#     # CONSTRUCTOR
#     def __init__(self, name, description, price, qty):
#         self.name = name
#         self.description = description 
#         self.price = price
#         self.qty = qty

# # SCHEMA
# class ProductSchema(marshmellow.Schema):
#     class Meta:
#         fields = ('id', 'name', 'description', 'price', 'qty')

# # INIT SCHEMA
# product_schema = ProductSchema()  # FOR ONE 
# products_schema = ProductSchema(many=True)  # FOR MANY

# CREATE PRODUCT ROUTE 
# @app.route('/product', methods=['POST'])
# def addProduct():
#     name = request.json['name']
#     description = request.json['description']
#     price = request.json['price']
#     qty = request.json['qty']

#     new_product = Product(name, description, price, qty)

#     db.session.add(new_product)
#     db.session.commit()

#     return product_schema.jsonify(new_product)

# # GET ALL PRODUCTS ROUTE 
# @app.route('/product', methods=['GET'])
# def getProducts():
#     all_products = Product.query.all()
#     result = products_schema.dump(all_products)

#     return jsonify(result)

# # GET SINGLE PRODUCT ROUTE 
# @app.route('/product/<id>', methods=['GET'])
# def getProduct(id):
#     product = Product.query.get(id)

#     return product_schema.jsonify(product)

# # UPDATE PRODUCT 
# @app.route('/product/<id>', methods=['PUT'])
# def updateProduct(id):
#     product = Product.query.get(id)

#     name = request.json['name']
#     description = request.json['description']
#     price = request.json['price']
#     qty = request.json['qty']

#     product.name = name
#     product.description = description 
#     product.price = price
#     product.qty = qty

#     db.session.commit()

#     return product_schema.jsonify(product)

# # DELETE PRODUCT 
# @app.route('/product/<id>', methods=['DELETE'])
# def deleteProduct(id):
#     product = Product.query.get(id)

#     db.session.delete(product)
#     db.session.commit()
    
#     return product_schema.jsonify(product)

# RUN ANOTHER FILE 
# @app.route('/run', methods=['GET']) 
# def runFile():
#     return strings.main() # run main => strings.main()

# # POST REQUEST 
# @app.route('/myPost', methods=['POST'])
# def myPostReq():
#     value = request.form['name']
#     print(value)
    
#     return (value)

# @app.route('/', methods = ['GET', 'POST'])
# def handle_request():
#     imagefile = flask.request.files['image']
#     filename = werkzeug.utils.secure_filename(imagefile.filename)
#     print("\nReceived image File name : " + imagefile.filename)
#     imagefile.save(filename)
#     return "Image Uploaded Successfully"

# RUN SERVER 
# if __name__ == '__main__':
#     # app.run(host="0.0.0.0", port=5000, debug=True)
#     # app.run(debug=True, host='0.0.0.0')
#     app.run(debug=True)

import flask
from flask import jsonify 
from test import sayHello

app = flask.Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def predict():
  sayHello('Shalitha')
  return jsonify({ 'msg': 'Hello Android'})

@app.route('/predict', methods = ['GET', 'POST'])
def predictNew():
  sayHello('Shalitha')
  return jsonify({ 'msg': 'Hello Android 2'})

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=9696, debug=True)
