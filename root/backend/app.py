from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Users(Resource):
    """ Classe de recurso de URL/API """

    def get(self):
        """ Metodo que recebe o path e query/params como argumentos da função """
        return {"message": "All users"}


class User(Resource):
    """ Classe de recurso de URL/API """

    def get(self, cpf):
        """ Metodo que recebe o path e query/params como argumentos da função """
        return {'message': f"{cpf}"}

    def post(self):
        """ Metodo post que recebe apenas o parametro e os dados vai via json no 
        corpo do cabeçalho da requisição http"""
        return {'message': 'POST'}


api.add_resource(Users, '/users')
api.add_resource(User, '/user', '/user/<string:cpf>')


if __name__ == '__main__':
    app.run(debug=True)
