from flask import flash, render_template, redirect, request
from FlaskExercise import app


@app.route('/')
def home():
    log = request.values.get('log_button')
    # TODO: Appropriately log the different button presses
    #   with the appropriate log level.
    if log:
        if log == 'info': 
            app.logger.info('Info with no error log')
        elif log == 'warning':
            app.logger.warning('Warning')
        elif log == 'error': 
            app.logger.error('Error')
        elif log == 'critical': 
            app.logger.critical('Critical')
    return render_template(
        'index.html',
        log=log
    )
