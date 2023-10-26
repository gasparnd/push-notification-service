# Get started

## Install fastapi

```
pip install fastapi

or

pip3 install fastapi
```

```
pip install "uvicorn[standard]"

or

pip3 install "uvicorn[standard]"
```

## Install dependencies

```
pip install pydantic

or

pip3 install pydantic
```

```
pip install exponent_server_sdk

or

pip3 install exponent_server_sdk
```

## Start server

Run this command in your console, in the root of the project

```
$ uvicorn main:app --reload
```

## How to use it

1. Update the notification token to your device

```
NOTIFICATION_TOKEN = "YOUR NOTIFICATION TOKEN HERE"
```

2. Use the post method _*send_notification*_ . It revice the next values to send a notification:

```
{
    "route": "your app route",
    "title": "Title of the notification",
    "body": "Body of the notification",
    "userId": 234,
    "userName": "Gaspar"
}
```

## How to send diferent data?

Update the "NotifactionModel", and "PushMessage" method.

```

class NotificationModel(BaseModel):
    ...
    newValue: str

message = PushMessage(
  to=NOTIFICATION_TOKEN,
  title=notification_item.title,
  body=notification_item.body,
  data={
    ...
    'userName': notification_item.userName, 'newValue': notification_item.newValue
  }
  )
```

Post method:

```
{
    "route": "your app route",
    "title": "Title of the notification",
    "body": "Body of the notification",
    "userId": 234,
    "userName": "Gaspar",
    "newValue": "Fuu"
}
```
