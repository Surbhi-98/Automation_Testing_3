import pytest

#----------------------------TestCases for ping command---------------------
@pytest.mark.parametrize("host", [("www.google.com"), ("www.foo.com")])
def test_ping(host, myping):
  #host = "www.google.com"
  assert myping.hostname(host) == 0, "Test Failed for test_ping"
  