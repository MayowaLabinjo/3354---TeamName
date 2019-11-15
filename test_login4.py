# Test 4: valid on second attempt

from io import StringIO
from login import login

input4 = StringIO("insdf\ne39js\nuser2\npass2\n")
def test_login4(monkeypatch):
	monkeypatch.setattr("sys.stdin", input4)
	assert login() == True