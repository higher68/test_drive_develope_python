from tasks import Task


def test_asdict():
    """_asdict() should return a dictionary."""
    t_task = Task("do something", "okken", True, 21)
    t_dict = t_task._asdict()
    expected = {"summary": "do something",
                "owner": "okken",
                "done": True,
                "id":21}
    assert t_dict == expected

    
def test_replace():
    """__replace() should change passed in fields."""
    t_before = Task("finish book", "brian", False)
    t_after = t_before._replace(id=10, done=True)  # _replacenamedtupleのフィールドの値を入れ替える
    t_expected= Task("finish book", "brian", True, 10)
    assert t_after == t_expected

    
def test_defaults():
    """Using no parameters should invoke defaults."""
    t1 = Task()
    t2 = Task(None, None, False,None)
    assert t1 == t2  # falseのとき、例外を吐く

    
def test_member_access():
    """Check .field functionality of namedtuple."""
    t = Task("buy milk", "brian")  # namedtupleは値に名前でアクセスできるのよ
    assert t.summary == "buy milk"
    assert t.owner == "brian"
    assert (t.done, t.id) == (False, None)

                
