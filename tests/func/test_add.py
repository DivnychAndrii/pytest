import pytest
import tasks.api as tasks

from tasks import Task


def test_add_increases_count(db_with_3_tasks):

    tasks.add(Task('Party'))

    assert tasks.count() == 4


@pytest.mark.skip
def test_add_returns_valid_id(tasks_db):

    new_task = Task('do snth')
    task_id = tasks.add(new_task)

    assert isinstance(task_id, int)


@pytest.mark.skip
@pytest.mark.smoke
def test_added_task_has_id_set():

    new_task = Task('sit', owner='me', done=True)
    task_id = tasks.add(new_task)

    task_from_db = tasks.get(task_id)

    assert task_from_db.id == task_id
