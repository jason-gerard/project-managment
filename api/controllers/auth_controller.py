from flask import request, session, jsonify
from werkzeug.security import check_password_hash
import services.company_service as company_service


def sign_in():
    username = request.form.get('username')
    password = request.form.get('password')

    selected_user = company_service.get_company_by_username(username)

    if selected_user:
        is_authenticated = (check_password_hash(selected_user.get('password'), password) and
                            selected_user.get('username') == username)

        if is_authenticated:
            session['company_id'] = selected_user.get('id')
            return {
                'msg': f'{username} is now signed in'
            }

    return {
        'error': 'user is not authenticated'
    }


def sign_out(company_id):
    session.pop('company_id', None)

    return jsonify({'message': f'User of id -> {company_id} is signed out'})
