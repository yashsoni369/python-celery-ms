import logging

from flask import Flask, request, jsonify
from flask_cors import CORS

from user.services.user_tasks import add_t


app = Flask(__name__)

CORS(
    app,
    resources={
        r"/*": {
            "origins": [
                "*"
            ]
        }
    },
)

@app.route("/add/<num_1>/<num_2>", methods=["GET"])
def add(num_1, num_2):
    # Schedule an add task

    # Wait for the task to complete and return the result
    # Convert the input to integers
    num_1 = int(num_1)
    num_2 = int(num_2)
    print("Adding %d + %d" % (num_1, num_2))
    add_result = add_t.delay(num_1, num_2)
    add_result.wait()
    logging.info("Result: %s", add_result.get())
    return str(add_result.get())

if __name__ == "__main__":
    # Step I: Run the application.
    app.run(host="0.0.0.0", port=8081, debug=True)
