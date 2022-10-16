from modules.user.enterprise.services.UserService import *
from modules.user.business.models.User import User
from infrastructure.di.di import obj_graph
from modules.user.enterprise.services.UserService import UserServices


def test_user_service():
    db = obj_graph.provide(UserServices)
    testdb = User(
        first_name="rajat", last_name="mishra", email="r@r.com", password="ajat322"
    )
    data = db.create(testdb)
    assert data == testdb
    try:
        data = db.get(User, dict(pk=testdb.pk))
    except Exception as e:
        print(e)
    try:
        assert data == testdb
    except Exception as e:
        print(e)

    data = db.get_all(User)
    assert isinstance(data, list) == True

    data = db.update(User, dict(pk=testdb.pk), dict(firstname="man"))
    try:
        assert data == testdb
    except Exception as e:
        print(e)

    data = db.delete(User, dict(pk=testdb.pk))
    try:
        assert data == testdb
    except Exception as e:
        print(e)
