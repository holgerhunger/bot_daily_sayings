from typing import Optional
from datetime import datetime
from sqlmodel import Field, Session, SQLModel, create_engine, select
from pydantic import EmailStr
from dotenv import load_dotenv
import os

# TODO: Role in Users zufügen, und admin Email laden, und Fehler nach Admin Email schicken

# Load mariadb-url
load_dotenv()
MARIADB_URL = os.getenv("MARIADB_URL")


class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: EmailStr
    password_hash: str
    name: str
    confirmed: bool
    last_access: datetime
    weekdays: str


mariadb_url = MARIADB_URL
engine = create_engine(mariadb_url, echo=True)


def select_users():
    with Session(engine) as session:
        statement = select(Users)
        results = session.exec(statement)
        for user in results:
            print(type(user))
            print(user.name)
            print(user.email)
            print(user.last_access)
            print(user)


# select_users()


# create email list depending on weekday
# Datenbank öffnen
def get_mail_list(day_of_week):
    email_list = []
    with Session(engine) as session:
        statement = select(Users)
        results = session.exec(statement)
        for user in results:
            # Nur wenn bestätigt und korrekter Wochentag aktiviert, E-Mail Empfänger in Liste aufnehmen
            if user.confirmed and str(day_of_week) in user.weekdays:
                email_list.append(user.email)
    return email_list
