# REST API
from flask import Flask, render_template, request, jsonify, make_response
import requests
import json
import grpc
import booking_pb2
import booking_pb2_grpc
from google.protobuf.json_format import MessageToDict

app = Flask(__name__)

PORT = 3203
HOST = "0.0.0.0"

with open("{}/data/users.json".format("."), "r") as jsf:
    users = json.load(jsf)["users"]


# root message


@app.route("/", methods=['GET'])
def home():
   return "<h1 style='color:blue'>Welcome to the User service!</h1>"

@app.route("/users", methods=['GET'])
def get_json():
   return make_response(jsonify({"users": users}), 200)
@app.route("/users/<userid>", methods=['POST'])
def add_user(userid):
   req = request.get_json()
   for user in users:
      if str(user["id"]) == str(userid):
            return make_response(jsonify({"error":"User already exists"}),409)
   users.append(req)
   res = make_response("User added successfully",200)
   return res

@app.route("/users/<userid>", methods=['GET'])
def get_user_byid(userid):
    for user in users:
        if str(user["id"]) == str(userid):
            return make_response(jsonify(user),200)
    return make_response(jsonify({"error":"User ID not found"}),400)



# Get reservations (Bookings) by user_id and date
@app.route("/bookings/<user_id>", methods=["GET"])
def get_user_bookings(user_id):
    if request.args:
        req = request.args
        reservation_date = req["date"]
        with grpc.insecure_channel('localhost:3001') as channel :
            stub = booking_pb2_grpc.BookingStub(channel)
            all_bookings = stub.GetBookingByUserID(booking_pb2.UserID(user_id=user_id))
            bookings = []
            for reservation in all_bookings:
                for dates in reservation.dates:
                    if dates.date == reservation_date:
                        bookings.append(dates)
            channel.close()
            for item in bookings:
                res = make_response(MessageToDict(item), 200)
                return res
            return make_response(jsonify({"Error": "error in user booking request"}), 400)
    else:
        return make_response(jsonify({"error": "date not found"}), 400)

# We interact with movie service to get information about each movie.
@app.route("/bookingInfo/<user_id>", methods=["GET"])
def get_user_booking_details(user_id):
    with grpc.insecure_channel('localhost:3001') as channel :
        stub = booking_pb2_grpc.BookingStub(channel)
        all_reservations_for_user = stub.GetBookingByUserID(booking_pb2.UserID(user_id=user_id))
        details = []
        for reservation in all_reservations_for_user:
            for dates in reservation.dates:
                reservation_details = {"date": dates.date,  "movies": []}
                for movie_id in dates.movies:
                    movie_details = requests.post(
                        f"http://127.0.0.1:3100/graphql",
                        json={
                            "query": 'query{ movie_with_id(_id:"'
                            + f"{movie_id}"
                            + '"){id title director rating}}'
                        },
                    ).json()
                    reservation_details["movies"].append(movie_details["data"]["movie_with_id"])
                details.append(reservation_details)
        channel.close()
    res = make_response(jsonify(details), 200)
    return res

@app.route("/movies", methods=['GET'])
def get_movies():
    query = """
query Get_all_movies {
    get_all_movies {
        id
        title
        director
        rating
    }
}
    """
    response = requests.post("http://localhost:3100/graphql", json={'query':  query})
    return make_response(response.json(), response.status_code)

@app.route("/best_rated_movie", methods=['GET'])
def best_rated_movie():
   query = """
query Best_Rated_Movie {
    best_rated_movie {
        id
        title
        director
        rating
    }
}
    """
   response = requests.post("http://localhost:3100/graphql", json={'query':  query})
   return make_response(response.json(), response.status_code)

@app.route("/worst_rated_movie", methods=['GET'])
def worst_rated_movie():
   query = """
query Worst_Rated_Movie {
    worst_rated_movie {
        id
        title
        director
        rating
    }
}
    """
   response = requests.post("http://localhost:3100/graphql", json={'query':  query})

   return make_response(response.json(), response.status_code)

@app.route("/best_rated_movie_of_actor/<actor_id>", methods=['GET'])
def best_rated_movie_of_actor(actor_id):
   query = """
query Best_rated_movie {
    best_rated_movie_of_actor(_id:"""+ str(actor_id)+""") {
        id
        title
        director
        rating
    }
}

"""
   response = requests.post("http://localhost:3100/graphql", json={"query" : query})
   return make_response(response.json(), response.status_code)


@app.route("/worst_rated_movie_of_actor/<actor_id>", methods=['GET'])
def worst_rated_movie_of_actor(actor_id):
   query = """
query Worst_rated_movie {
    worst_rated_movie_of_actor(_id:"""+ str(actor_id)+""") {
        id
        title
        director
        rating
    }
}

"""
   response = requests.post("http://localhost:3100/graphql", json={"query" : query})
   return make_response(response.json(), response.status_code)

@app.route("/youngest_actor_in_movie/<movie_id>", methods=['GET'])
def youngest_actor_in_movie(movie_id):
   query = """
query Youngest_actor_in_movie {
    youngest_actor_in_movie(_id:"""+movie_id+""") {
        id
        firstname
        lastname
        birthyear
        films
    }
}
    """
   response = requests.post("http://localhost:3001/graphql", json={'query':  query})
   return make_response(response.json(), response.status_code)

@app.route("/oldest_actor_in_movie/<movie_id>", methods=['GET'])
def oldest_actor_in_movie(movie_id):
   query = """
query Oldest_actor_in_movie {
    oldest_actor_in_movie(_id:"""+movie_id+""") {
        id
        firstname
        lastname
        birthyear
        films
    }
}
    """
   response = requests.post("http://localhost:3001/graphql", json={'query':  query})
   return make_response(response.json(), response.status_code)

@app.route("/colaboration_of_actors/<id_actors>", methods=['GET'])
def colaboration_of_actors(id_actors):
   id_actor1 = id_actors.split('-')[0]
   id_actor2 = id_actors.split('-')[1]
   print(type(id_actor1))
   query = """
query Colaboration_of_actors {
    colaboration_of_actors(_id1: """+id_actor1+""" , _id2: """+id_actor2+""") {
        id
        title
        director
        rating
    }
}

    """
   response = requests.post("http://localhost:3001/graphql", json={'query':  query})
   return make_response(response.json(), response.status_code)


if __name__ == "__main__":
    print("Server running in port %s" % (PORT))
    app.run(host=HOST, port=PORT, debug=True)
