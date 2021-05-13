import pytest
import tasks
from tasks import Task


@pytest.fixture(scope='session', params=['tiny'])
def tasks_db_session(tmpdir_factory, request):
    # Setup : start db
    tmp_dir = tmpdir_factory.mktemp('temp')

    tasks.start_tasks_db(str(tmp_dir), request.param)

    yield  # this is where the testing happens

    # Teardown : stop db
    tasks.stop_tasks_db()


@pytest.fixture()
def tasks_db(tasks_db_session):
    tasks.delete_all()


@pytest.fixture()
def db_with_3_tasks(tasks_db, tasks_just_a_few):

    for task in tasks_just_a_few:
        tasks.add(task)


@pytest.fixture()
def db_with_mult_per_owner(tasks_db, tasks_mult_per_owner):

    for task in tasks_mult_per_owner:
        tasks.add(task)


@pytest.fixture(scope='session')
def tasks_just_a_few():
    """All summaries and owners are unique."""
    return (
        Task('Write some code', 'Brian', True),
        Task("Code review Brian's code", 'Katie', False),
        Task('Fix what Brian did', 'Michelle', False)
            )


@pytest.fixture(scope='session')
def tasks_mult_per_owner():
    """Several owners with several tasks each."""
    return (
        Task('Make a cookie', 'Raphael'),
        Task('Use an emoji', 'Raphael'),
        Task('Move to Berlin', 'Raphael'),
        Task('Create', 'Michelle'),
        Task('Inspire', 'Michelle'),
        Task('Encourage', 'Michelle'),
        Task('Do a handstand', 'Daniel'),
        Task('Write some books', 'Daniel')
            )
