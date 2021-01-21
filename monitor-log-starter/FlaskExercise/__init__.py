import logging
from flask import Flask

app = Flask(__name__)
wsgi_app = app.wsgi_app
# TODO: Set the app's logger level to "warning"
#   and any other necessary changes
# Logging Level Doc: https://docs.python.org/3/library/logging.html
app.logger.setLevel(logging.WARNING); # log level from warning and above

streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.WARNING)
app.logger.addHandler(streamHandler) # add stream hanlder to app.logger object


import FlaskExercise.views