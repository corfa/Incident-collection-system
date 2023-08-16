
from app import App
import os
from dotenv import load_dotenv

load_dotenv()


if __name__ == "__main__":
    host_app = os.getenv('HOST_APP', '0.0.0.0')
    port_app = os.getenv('PORT_APP', '5454')
    app = App(host=host_app, port=int(port_app))
    app.run()
