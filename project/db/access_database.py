from typing import Dict, List, Union
from project.models.user import User
from project.models.role import Role
import psycopg2

from project.db.config_database import ConfigDatabase


class AccessDataBase(ConfigDatabase):
    def __init__(self) -> None:
        self.logger.debug('Initialise Class AccessDataBase')
        self.conn = psycopg2.connect(**self.postgres_access)
        self.auto_gen_data_types = ['SERIAL PRIMARY KEY', 'UUID']

    def generate_create_table_sql(self, table_name, sql_spec):
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} "
        cols = []
        for column, spec in sql_spec.items():
            col_spec = column
            if len(spec["data_type"]) > 0:
                col_spec = col_spec + f' {spec["data_type"]}'
            if len(spec["type_extra"]) > 0:
                col_spec = col_spec + f' {spec["type_extra"]}'
            cols.append(col_spec)
        sql = sql + '(' + ', '.join(cols) + ');'

        return sql

    def initialise_db_structure(self):
        entities = [User, Role]
        sql_statements = []
        for entity in entities:
            sql_spec = entity.sql_specification
            table_name = entity.table_name
            sql = self.generate_create_table_sql(table_name, sql_spec)
            sql_statements.append(sql)
        cursor = self.conn.cursor()
        for sql_statement in sql_statements:
            cursor.execute(sql_statement)
            self.logger.debug(f'Initialising: {sql_statement}')
        cursor.close()
        self.conn.commit()

    def insert_object(self, object):
        sql = f"INSERT INTO {object.table_name} "
        cols = []
        for column, spec in object.sql_specification.items():
            if spec["data_type"] not in self.auto_gen_data_types:
                cols.append(column)
        if len(cols) > 0:
            sql = sql + '(' + ', '.join(cols) + ')'
        values = []
        for key, value in object.values.items():
            self.logger.debug(object.sql_specification[key])
            if object.sql_specification[key]["data_type"] not in self.auto_gen_data_types:
                value = "'" + str(value) + "'"
                values.append(value)
        sql = sql + ' VALUES ' + '(' + ', '.join(values) + ');'
        if self.run_sql(sql):
           self.log_success(object.table_name, values[0], 'insert')

    def get_objects(self, object, filter=None, order_by=None):
        self.logger.debug(f'Getting {object} from DB')
        cursor = self.conn.cursor()
        select_query = f"SELECT * FROM {object}"
        if filter:
            select_query = select_query + f" WHERE {filter}"
        if order_by:
            select_query = select_query + f" ORDER BY {order_by} DESC"
        select_query = select_query + ';'
        cursor.execute(select_query)
        self.logger.debug(f'Executed: {select_query}')
        results = cursor.fetchall()
        cursor.close()
        self.conn.commit()
        return results

    def update_object(self, object):
        updates_strings = []
        for key, value in object.values.items():
            if object.sql_specification[key]["data_type"] not in self.auto_gen_data_types:
                update_string = f"{key} = '{value}'"
                updates_strings.append(update_string)
        pk = self.get_pk(object)
        pk_value = object.values[pk]
        sql = f"UPDATE {object.table_name} SET {', '.join(updates_strings)} WHERE {pk} = '{pk_value}'"
        if self.run_sql(sql):
           self.log_success(object.table_name, pk_value, 'update')

    def delete_object(self, object, identifier, where_col=None):
        if not where_col:
            where_col = self.get_pk(object)
        sql = f"DELETE FROM {object.table_name} WHERE {where_col} = {identifier} "
        if self.run_sql(sql):
           self.log_success(object.table_name, identifier, 'delete')
        return True

    def get_pk(self, object):
        value = None
        for k, v in object.sql_specification.items():
            if v["data_type"] == 'SERIAL PRIMARY KEY':
                value = str(k)

        return value

    def log_success(self, table, id, statement_type):
        self.logger.debug(f'Successfully performed: {statement_type} on id: {id} from table: {table}')

    def run_sql(self, sql):
        cursor = self.conn.cursor()
        try:
            self.logger.debug(f'Running SQL: {sql}')
            cursor.execute(sql)
            cursor.close()
            self.conn.commit()
            return True
        except Exception:
            self.logger.error(f'SQL statement failure: {sql}')
            cursor.close()
            self.conn.rollback()
            return False
