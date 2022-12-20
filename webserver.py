import logging

from flasgger import Swagger
from flask import Flask, request, render_template, Response

from room import Room

app = Flask(__name__)
swagger = Swagger(app)

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

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
    log.info("Returning view with all rooms: %s", rooms)
    return render_template('room.html', rooms=rooms)


@app.route('/temperature', methods=['POST'])
def create_temperature():
    """
    This endpoint adds a temperature to the current room.
    ---
    responses:
      200:
        description: Temperature successfully added.
    """
    if not rooms:
        log.debug("Rooms list is empty!")
        rooms.append(Room())

    temp = request.json['temperature']
    rooms[-1].add_temperature(temp)
    log.info("Added temperature to the last object of the rooms list: %s", temp)
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
    log.info("Added a new Object Room to the rooms list")
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
    rooms.clear()
    log.info("Cleared all objects from the rooms list")
    return Response(status=200)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    rooms.append(Room([21, 22]))
    rooms.append(Room([23, 25]))
    rooms.append(Room([19, 18]))
    rooms.append(Room([20, 21]))
    app.run(host="0.0.0.0", port=8080)
