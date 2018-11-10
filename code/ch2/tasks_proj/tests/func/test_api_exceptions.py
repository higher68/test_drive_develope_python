import pytest
import tasks

@pytest.mark.smoke
def test_list_tasks_raises():
    """list_tasks() should raise an exception with wrong type param"""
    with pytest.raises(TypeError):
        tasks.list_tasks(owner=123)


@pytest.mark.get
@pytest.mark.smoke
def test_get_raises():
    """get() shold raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.get(task_id="123")
        
        
