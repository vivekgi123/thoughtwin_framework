import pytest
from infrastructure.di.di import obj_graph
from adaptors.redis_nosql.manager import DataBaseManager


def test_di():
    obj = obj_graph.provide(DataBaseManager)
    assert isinstance(obj, DataBaseManager) == True
