from flask import Flask, request, jsonify

app = Flask(__name__)


class Item:
    def __init__(self, name, description=None, price=0.0, tax=None):
        self.name = name
        self.description = description
        self.price = price
        self.tax = tax

    def to_dict(self):
        item_dict = {
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "tax": self.tax,
        }
        if self.tax is not None:
            item_dict["price_with_tax"] = self.price + self.tax
        return item_dict


@app.route("/items/", methods=["POST"])
def create_item():
    data = request.get_json()
    item = Item(**data)
    return jsonify(item.to_dict())


# GET /api/hello
@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello, World!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
