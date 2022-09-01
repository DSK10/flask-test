######################################################################
from flask import Flask, request, jsonify, Response
from gevent.pywsgi import WSGIServer
import traceback


######################################################################

class Hailstorm_main:

    def __init__(self, details):
        
        self.host_api = "0.0.0.0"
        self.port = 9000


        app = self.initialise_apis()

        app.debug = True
        http_server = WSGIServer((self.host_api, self.port), app)
        http_server.serve_forever()

    def initialise_apis(self):
        
        # Initialize the Flask application
        app = Flask(__name__)

        @app.route('/', methods=['GET', 'POST'])
        def home():
            try:
                return Response('Server is active!', status=200)
            except:
                traceback.print_exc()
                return Response(status=500)

        
   
        print("[INFO] Hailstorm Running..")
        return app



def main():

    Hailstorm_main({"a":"b"})

if __name__ == "__main__":
    
    main()