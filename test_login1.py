# Test 1: valid username, valid password, first attempt

from io import StringIO
from login import login

input1 = StringIO("user1\npass1\n")
def test_login1(monkeypatch):
	monkeypatch.setattr("sys.stdin", input1)
	assert login() == True
