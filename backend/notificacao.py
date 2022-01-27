from datetime import datetime
from flask_socketio import emit
from flask import Blueprint, jsonify, request, make_response
from sqlalchemy import text,and_

notificacao_blueprint = Blueprint('notificacao_blueprint', __name__)


from __init__ import db, app, socketio
from models import Notification


@notificacao_blueprint.route('/updateVisto/<int:id>', methods=['POST'])
def updateNotoficacao(id):

    notificacao = Notification.query.get(id)

    if notificacao:
        setattr(notificacao,'visto',1)

        db.session.commit()

        return make_response('Notificação atualizado com sucesso', 200)  

    else:
        return make_response('Notificação não existe', 404)    



@notificacao_blueprint.route('/todos/<string:id>', methods=['GET'])
def getAllNotiUser(id):

    output=[]

    notificacoes= Notification.query.filter(Notification.fk_Utilizador_username==id).all()

    for noti in notificacoes:
        # appending the user data json
        # to the response list
        output.append({
            'idNot' :noti.idNot,
            'fk_Utilizador_username' :noti.fk_Utilizador_username,
            'sent' : noti.sent,
            'visto' : noti.visto,
            'titulo' : noti.titulo,
            'mensagem' : noti.mensagem
        })

    
    response = jsonify({'Notificacoes': output})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


   
@socketio.on("messageInstant")
def messageIntant(data):

    socketio.emit('messageInstant', data ,room="user_" + data.get('userDestino'))
         
    
     


@socketio.on("message")
def create_user_notification_mensagem(data):#, title, message):
    """
    Create a User Notification
    :param user: User object to send the notification to
    :param action: Action being performed
    :param title: The message title
    :param message: Message
    """
    notification = Notification(titulo=data.get('titulo'),
                                mensagem=data.get('mensagem'),
                                sent=datetime.now(),
                                visto=0,
                                fk_Utilizador_username=data.get('userDestino'))
            

    db.session.add(notification)
    db.session.commit()

    
    
    socketio.emit('message', data ,room="user_" + data.get('userDestino'))
         #namespace='/notifs')
   
    #push_user_notification(userD)  




@socketio.on("viagem")
def create_user_notification_viagem(data):#, title, message):
    """
    Create a User Notification
    :param user: User object to send the notification to
    :param action: Action being performed
    :param title: The message title
    :param message: Message
    """
    notification = Notification(titulo=data.get('titulo'),
                                mensagem=data.get('mensagem'),
                                sent=datetime.now(),
                                visto=0,
                                fk_Utilizador_username=data.get('userDestino'))
            

    db.session.add(notification)
    db.session.commit()

    
    
    socketio.emit('viagem', data ,room="user_" + data.get('userDestino'))
         
    
     


@socketio.on("pedido")
def create_user_notification_pedido(data):#, title, message):
    """
    Create a User Notification
    :param user: User object to send the notification to
    :param action: Action being performed
    :param title: The message title
    :param message: Message
    """
    notification = Notification(titulo=data.get('titulo'),
                                mensagem=data.get('mensagem'),
                                sent=datetime.now(),
                                visto=0,
                                fk_Utilizador_username=data.get('userDestino'))
            

    db.session.add(notification)
    db.session.commit()

    
    
    socketio.emit('pedido', data ,room="user_" + data.get('userDestino'))
     
