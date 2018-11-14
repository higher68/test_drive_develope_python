import pytest
import tasks  # taskディレクトリ内を全てインポート
from tasks import Task


def test_Add_1():
    """tasks.get() using id returned from add() works."""
    task = Task("breathe", "BRIAN", True)
    task_id = tasks.add(task)  # データベースにtaskを追加
    print(task_id)
    t_from_db = tasks.get(task_id)  # task_idをdbから取得使ってるのはTinyDB。細かいところは追々コード読めばいい。
    print(t_from_db)
    # ID以外は同じはず
    assert equivalent(t_from_db, task)


def equivalent(t1, t2):
    """Check two tasks for equivalence.)"""
    # id以外のフィールドを全て比較
    return ((t1.summary == t2.summary) and (t1.owner == t2.owner) and (t1.done == t2.done))


@pytest.fixture(autouse=True)  # autouseフィクスチャで、データベースへのアクセスが可能になるんだってさ
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    tasks.start_tasks_db(str(tmpdir), "tiny")
    yield
    tasks.stop_tasks_db()
    
