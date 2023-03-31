from flask_mail import Message
from flask import current_app, render_template

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