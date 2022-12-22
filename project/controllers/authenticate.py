from project.utility.validation import validate
from project.models.user import User


class Authenticate:

    def __init__(self) -> None:
        pass

    def signup(self, form, db):

        user = User(
            id=None,
            role_id=validate(form['role']),
            user_name=validate(form['user_name']),
            first_name=validate(form['first_name']),
            surname=validate(form['surname']),
            email=validate(form['email']),
            password=validate(form['password']),
            session_id=None
        )

        db.insert_object(user)

    def update_user(self, form, db, id):
        user_data = db.get_objects(User.table_name, filter=f'id = {id}')[0]
        user = User(
            id=user_data[0],
            role_id=user_data[1],
            user_name=user_data[2],
            first_name=user_data[3],
            surname=user_data[4],
            email=user_data[5],
            password=user_data[6],
            session_id=user_data[7]
        )

        user.set_role_id(validate(form['role']))
        user.set_user_name(validate(form['user_name']))
        user.set_first_name(validate(form['first_name']))
        user.set_surname(validate(form['surname']))
        user.set_email(validate(form['email']))
        user.set_password(validate(form['password']))

        db.update_object(user)
