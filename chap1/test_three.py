"""Test the Task data type."""
from collections import namedtuple

Task = namedtuple("Task", ["summary", "owner", "done", "id"])  # 第一引数がクラス名、第二引数がフィールド名のリストです。
Task.__new__.__defaults__ = (None, None, False, None)  # namedtupleはimmutableなので、初期化するときに__new__を使う必要があるhttp://nihaoshijie.hatenadiary.jp/entry/2017/12/01/140622
# dafaultsでデフォルト値を設定してる？
# __new__.__defaults__で、未指定のデフォルト値をあらかじめ指定できる。


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
    

