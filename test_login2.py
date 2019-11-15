# Test 2: valid usernames, invalid passwords, max attempts

from io import StringIO
from login import login

input2 = StringIO("user1\n\nuser2\noijis\nuser3\nsdofijie\n")
def test_login2(monkeypatch):
	monkeypatch.setattr("sys.stdin", input2)
	assert login() == False