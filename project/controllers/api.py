from datetime import datetime
from math import ceil

from flask import Flask, request, render_template, redirect

from project.db.access_database import AccessDataBase
from project.utility.validation import validate
from project.controllers.authenticate import Authenticate

from project.models.user import User
from project.models.role import Role


def init_app(app: Flask):
    db_object = AccessDataBase()
    db_object.initialise_db_structure()

    @app.route('/', methods=['GET'])
    def home():
        return render_template('home.jinja2')

    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        auth_object = Authenticate()
        if request.method == 'POST':
            auth_object.signup(request.form, db_object)
            return redirect('/signup')
        else:
            return render_template('signup.jinja2')

    @app.route('/admin', methods=['GET'])
    def admin():
        kwargs = {
            'users': db_object.get_objects(User.table_name),
            'title': 'Admin'
        }
        return render_template('admin.jinja2', **kwargs)

    @app.route('/user/delete/<int:user_id>/', methods=['POST'])
    def delete_user(user_id):
        db_object.delete_object(User, user_id)
        return redirect('/admin')

    @app.route('/user/update/<int:user_id>/', methods=['GET', 'POST'])
    def update_user(user_id):
        if request.method == 'POST':
            auth_object = Authenticate()
            auth_object.update_user(request.form, db_object, user_id)
            return redirect('/admin')
        else:
            users = db_object.get_objects(User.table_name, filter=f'id = {user_id}')
            kwargs = {
                'user': users[0],
                'title': 'Admin'
            }
            return render_template('update_user.jinja2', **kwargs)

    @app.errorhandler(404)
    def not_found(error):
        return render_template('error.jinja2', title='TEMPLATE | NOT FOUND', warning=error), 404
    
    
    @app.errorhandler(500)
    def server_error(error):
        return render_template('error.jinja2', title='TEMPLATE | NOT FOUND', warning=error), 500
