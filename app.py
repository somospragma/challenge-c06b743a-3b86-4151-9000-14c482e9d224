app = Flask(__name__)
api = Api(app)

observability_service = ObservabilityService()

class ObservabilityResource(Resource):
    def get(self):
        return jsonify(observability_service.evaluate_system())

    def post(self):
        data = request.get_json()
        return jsonify(observability_service.propose_improvement())

    def put(self):
        data = request.get_json()
        return jsonify(observability_service.justify_and_communicate())

api.add_resource(ObservabilityResource, '/observability')

if __name__ == '__main__':
    app.run(debug=True)