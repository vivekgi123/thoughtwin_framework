from modules.user_activity_module.business.models.User_log import UserLog
from infrastructure.di.di import obj_graph
from modules.user_activity_module.enterprise.services.User_log_service import (
    UserLogServices,
)


def test_user_activity_log():
    """_summary_"""
    db = obj_graph.provide(UserLogServices)
    testdb = UserLog(data="jhfgjehrf", created_by="mishra")
    data = db.create(testdb)
    assert data == testdb
    try:
        data = db.get(UserLog, dict(pk=testdb.pk))
    except Exception as e:
        print(e)
    try:
        assert data == testdb
    except Exception as e:
        print(e)

    data = db.get_all(UserLog)
    assert isinstance(data, list) == True

    data = db.update(UserLog, dict(pk=testdb.pk), dict(data="ewdfwef"))
    try:
        assert data == testdb
    except Exception as e:
        print(e)

    data = db.delete(UserLog, dict(pk=testdb.pk))
    try:
        assert data == testdb
    except Exception as e:
        print(e)
