import pytest
import subprocess

from hr import users

password = '$6$pEP10f8j4fb3tYpZ$D82X1cT4g6B77eZAsYVgOVUmY5wbgRChzArq/W.VdOp..7ENg.UGC1qeXVeQT6RnYHMaWvABcxM90CYn3J8Xd1'

user_dict = {
    'name': 'raminder',
    'groups':['wheel', 'dev'],
    'password': password
}

def test_users_add(mocker):
    """
    Given a user dictionary. `user.add(...)` should utilize `useradd` to create a user with the password and groups.
    """
    mocker.patch('subprocess.call')
    users.add(user_dict)
    subprocess.call.assert_called_with([
        'useradd',
        '-p',
        password,
        '-G',
        'wheel,dev',
        'raminder',
    ])

def test_users_remove(mocker):
    """
    Given a user disctionary, `user.remove(...)` should utilize `userdel` to delete the user.
    """
    mocker.patch('subprocess.call')
    users.remove(user_dict)
    subprocess.call.assert_called_with([
        'userdel',
        '-r',
        'raminder',
    ])

def test_users_update(mocker):
    """
    Given a user dictionary, `users.update(...)` should utilize `usermod` to set the groups and password for the user.
    """
    mocker.patch('subprocess.call')
    users.update(user_dict)
    subprocess.call.assert_called_with([
        'usermod',
        '-p',
        password,
        '-G',
        'wheel,dev',
        'raminder'
    ])


def test_users_sync(mocker):
    """
    Given a list of user dictionaries, `user.sync(...)` should create missing users, remove extra non-system users and update existing user. A list of existing usernames can be passed in or default users will be used.
    """
    existing_user_names = ['raminder', 'bob']
    users_info = [
            user_dict,
            {
                'name': 'jose',
                'groups': ['wheel'],
                'password': password
            }
    ]
    mocker.patch('subprocess.call')
    users.sync(users_info, existing_user_names)

    subprocess.call.assert_has_calls([
        mocker.call([
            'usermod',
            '-p',
            password,
            '-G',
            'wheel,dev',
            'raminder',
        ]),
        mocker.call([
            'useradd',
            '-p',
            password,
            '-G',
            'wheel',
            'jose',
        ]),
        mocker.call([
            'userdel',
            '-r',
            'bob',
        ]),
    ])
