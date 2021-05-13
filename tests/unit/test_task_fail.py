import pytest
from tasks.api import Task


@pytest.mark.xfail
def test_task_equality():

    t1 = Task('sit', 'brian')
    t2 = Task('do', 'okken')

    assert t1 == t2


@pytest.mark.xfail
def test_dict_equality():

    t1_dict = Task('Make sandwich', 'okken')._asdict()
    t2_dict = Task('Make sandwich', 'okkem')._asdict()

    assert t1_dict == t2_dict