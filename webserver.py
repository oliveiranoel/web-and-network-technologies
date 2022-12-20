from flasgger import Swagger
from flask import Flask, request, render_template, Response

from room import Room

app = Flask(__name__)
swagger = Swagger(app)

rooms = []


@app.route('/', methods=['GET'])
def get_measurements():
    """
    This endpoint returns the UI for all the measurements done.
    ---
    responses:
      200:
        description: UI is successfully displayed.
    """
    return render_template('room.html', rooms=rooms)


@app.route('/temperature', methods=['POST'])
def create_temperature():
    """
    This endpoint adds a temperature to the current room.
    ---
    responses:
      200:
        description: Temperature sucessfully added.
    """
    if not rooms:
        rooms.append(Room())

    rooms[-1].add_temperature(request.json['temperature'])
    return Response(status=200)


@app.route('/room', methods=['POST'])
def create_room():
    """
    This endpoint adds a new room and sets is to current.
    ---
    responses:
      200:
        description: Room successfully added.
    """
    rooms.append(Room())
    return Response(status=201)


@app.route('/rooms', methods=['DELETE'])
def delete_rooms():
    """
    This endpoint deletes all the rooms and correlated data.
    ---
    responses:
      200:
        description: Room successfully added.
    """
    rooms = []
    return Response(status=200)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    rooms.append(Room([21, 22]))
    rooms.append(Room([23, 25]))
    rooms.append(Room([19, 18]))
    rooms.append(Room([20, 21]))
    app.run(port=8080)
