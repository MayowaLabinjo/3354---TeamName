# Test 3: invalid usernames, invalid passwords, max attempts

from io import StringIO
from login import login

input3 = StringIO("\n\nasodif93js\nidfdfs dfs\nfeiisdn\nfoije\n")
def test_login3(monkeypatch):
	monkeypatch.setattr("sys.stdin", input3)
	assert login() == False