# Test 5: valid on third attempt

from io import StringIO
from login import login

input5 = StringIO("oiensdf\n33920d\nfieoiwd\neg8e\nuser3\npass3\n")
def test_login5(monkeypatch):
	monkeypatch.setattr("sys.stdin", input5)
	assert login() == True