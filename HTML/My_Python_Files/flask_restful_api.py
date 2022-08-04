from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

stores = []


class Item(Resource):
    def get(self, name):
        return name
    
    def post(self, name):
        item = {"name": name, "price": 15.99}
        stores.append(item)
        return item
    
    def delete(self, name):
        for store in stores:
            if store['name'] == name:
                stores.remove(store)
                return {"message": "The store has been removed successfully"}
        return {"message": "The store has'nt found to be removed"}



api.add_resource(Item, '/item/<name>')
api.add_resource

if __name__ == "__main__":
    app.run(debug=True, port=5000)
