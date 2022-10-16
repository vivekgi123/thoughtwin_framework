import pytest
from adaptors.redis_nosql.manager import DataBaseManager
from infrastructure.di.di import obj_graph
from modules.user.business.models.User import User


def test_db_adaptor():
    db = obj_graph.provide(DataBaseManager)
    testdb = User(
        first_name="t3est",
        last_name="re67d",
        email="t@t.T7.com",
        password="dfddfd",
        created_at="2022-10-14T12:04:35.719123",
    )
    data = db.create(testdb)
    assert data == testdb
