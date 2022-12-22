class User:
    table_name = "user_details"
    sql_specification = {
        "id": {
            "data_type": "SERIAL PRIMARY KEY",
            "type_extra": "NOT NULL",
            "index": None,
            "foreign_key": None,
            "primary_key": "ix_user_id"
        },
        "role_id": {
            "data_type": "INT",
            "type_extra": "",
            "index": None,
            "foreign_key": "role.id",
            "primary_key": None
        },
        "user_name": {
            "data_type": "VARCHAR(50)",
            "type_extra": "NOT NULL",
            "index": None,
            "foreign_key": None,
            "primary_key": None
        },
        "first_name": {
            "data_type": "VARCHAR(50)",
            "type_extra": "NOT NULL",
            "index": None,
            "foreign_key": None,
            "primary_key": None
        },
        "surname": {
            "data_type": "VARCHAR(50)",
            "type_extra": "NOT NULL",
            "index": None,
            "foreign_key": None,
            "primary_key": None
        },
        "email": {
            "data_type": "VARCHAR(50)",
            "type_extra": "NOT NULL",
            "index": None,
            "foreign_key": None,
            "primary_key": None
        },
        "password": {
            "data_type": "VARCHAR(50)",
            "type_extra": "",
            "index": None,
            "foreign_key": None,
            "primary_key": None
        },
        "session_id": {
            "data_type": "UUID",
            "type_extra": "",
            "index": None,
            "foreign_key": None,
            "primary_key": None
        },
    }

    def __init__(self, id, role_id, user_name, first_name, surname, email, password, session_id) -> None:
        self.values = {
            "id": id,
            "role_id": role_id,
            "user_name": user_name,
            "first_name": first_name,
            "surname": surname,
            "email": email,
            "password": password,
            "session_id": session_id,
        }

    def set_id(self, value):
        self.values["id"] = value

    def set_role_id(self, value):
        self.values["role_id"] = value

    def set_user_name(self, value):
        self.values["user_name"] = value

    def set_first_name(self, value):
        self.values["first_name"] = value

    def set_surname(self, value):
        self.values["surname"] = value

    def set_email(self, value):
        self.values["email"] = value

    def set_password(self, value):
        self.values["password"] = value

    def set_session_id(self, value):
        self.values["session_id"] = value

    def get_id(self):
        return self.values["id"]

    def get_role_id(self):
        return self.values["role_id"]

    def get_user_name(self):
        return self.values["user_name"]

    def get_first_name(self):
        return self.values["first_name"]

    def get_surname(self):
        return self.values["surname"]

    def get_email(self):
        return self.values["email"]

    def get_password(self):
        return self.values["password"]

    def get_session_id(self):
        return self.values["session_id"]

