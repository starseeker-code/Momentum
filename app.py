from flask import Flask, request

app = Flask(__name__)

# TODO: Connect with Mongo

@app.route("/get-test-list/", methods=["GET"])
def get_all_test():
    return "all tests"

@app.route("/post-test", methods=["POST"])
def post_test():
    json = request.get_json()
    return json  # TODO: Full CRUD

@app.route("/get-test/<string:date>", methods=["GET"])
def get_test():
    return "There's no post"

@app.route("/patch-test/<string:date>", methods=["PATCH"])
def patch_test():
    json = request.get_json()
    return "test"

@app.route("/delete-test/<string:date>", methods=["DELETE"])
def delete_test():
    return "test"

# TODO: Update and delete