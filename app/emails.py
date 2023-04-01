from threading import Thread
from flask_mail import Message
from flask import current_app, render_template

"""
def notificacion_compra(mail, usuario, libro):
    try:
        message = Message('Notificación de compra de libro',
                          sender=current_app.config['MAIL_SENDER'],
                          recipients=[current_app.config['MAIL_SENDER']])
        message.html = render_template('emails/notificacion_compra.html',
                                       usuario=usuario,
                                       libro=libro)
        mail.send(message)
    except Exception as ex:
        raise Exception(ex)
"""


def notificacion_compra(app, mail, usuario, libro):
    try:
        message = Message('Notificación de compra de libro',
                          sender=current_app.config['MAIL_SENDER'],
                          recipients=[current_app.config['MAIL_SENDER']])
        message.html = render_template('emails/notificacion_compra.html',
                                       usuario=usuario,
                                       libro=libro)
        thread = Thread(target=envio_email_async, args=[app, mail, message])
        thread.start()
    except Exception as ex:
        raise Exception(ex)

def envio_email_async(app, mail, message):
    with app.app_context():
        mail.send(message)