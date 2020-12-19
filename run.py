""" Main module. """
# Project files.
from main import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
