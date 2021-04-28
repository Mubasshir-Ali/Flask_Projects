from flask import Flask, render_template, jsonify

# create user class
class User:

    def signup(self):

        user = {
            "_id": "",
            "name": "",
            "email": "",
            "password": ""
        }

        return jsonify(user), 200
