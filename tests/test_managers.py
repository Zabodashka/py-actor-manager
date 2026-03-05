import pytest
import os
from app.managers import ActorManager
from app.models import Actor

TABLE_NAME = 'actors'


@pytest.fixture()
def test_db(tmp_path) -> str:
    return os.path.join(tmp_path, 'cinema.db')


@pytest.fixture()
def manager(test_db: str) -> ActorManager:
    return ActorManager(database=test_db, table_name=TABLE_NAME)
