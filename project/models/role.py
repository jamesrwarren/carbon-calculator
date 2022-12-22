class Role:
    table_name = "role_details"
    sql_specification = {
        "id": {
            "data_type": "SERIAL PRIMARY KEY",
            "type_extra": "NOT NULL",
            "index": None,
            "foreign_key": None,
            "primary_key": "ix_user_id"
        },
        "role_name": {
            "data_type": "VARCHAR(50)",
            "type_extra": "NOT NULL UNIQUE",
            "index": None,
            "foreign_key": None,
            "primary_key": None
        }
    }

    def __init__(self, role_name) -> None:
        self.values = {
            "id": None,
            "role_name": role_name,
        }

    def set_id(self, value):
        self.values["id"] = value

    def set_role_name(self, value):
        self.values["role_name"] = value

    def get_id(self):
        return self.values["id"]

    def get_role_name(self):
        return self.values["role_name"]
