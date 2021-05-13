import pytest
import tasks.api as tasks

from tasks import Task


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):

    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield

    tasks.stop_tasks_db()


@pytest.mark.xfail(reason='test')
def test_unique_id():

    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()

    assert id_1 != id_2


@pytest.mark.xfail()
def test_unique_id_is_a_duck():
    """Demonstrate xfail."""
    uid = tasks.unique_id()
    assert uid == 'a duck'


@pytest.mark.xfail()
def test_unique_id_not_a_duck():
    """Demonstrate xpass."""
    uid = tasks.unique_id()
    assert uid != 'a duck'
