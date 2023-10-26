from typing import Union

from fastapi import FastAPI
from exponent_server_sdk import PushClient
from exponent_server_sdk import PushMessage
from pydantic import BaseModel

deep_link = 'com.yourApp.app://'
NOTIFICATION_TOKEN = 'ExponentPushToken[NoDNqBKFbdAo2x-XND8COjm]'

app = FastAPI()

class NotificationModel(BaseModel):
    route: str
    title: str
    body: str
    userId: int
    userName: str


def token_message(notification_item: NotificationModel):
  message = PushMessage(
    to=NOTIFICATION_TOKEN,
    title=notification_item.title,
    body=notification_item.body,
    data={'deepLink': deep_link + notification_item.route, 'userId': notification_item.userId, 'userName': notification_item.userName}
  )
  
  try:
    response = PushClient().publish(message)
    return response
  except Exception as e:
    print("Error al enviar el mensaje:", e)


@app.post("/sendNotification")
def send_notification(notification_item: NotificationModel):
  print(notification_item)
  message = token_message(notification_item)
  return {"data": message}
