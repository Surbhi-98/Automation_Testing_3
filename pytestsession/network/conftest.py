import pytest
import os
#----------------------------Fixture for ping command---------------------
class network_config:
  def hostname(host):
    return os.system("ping " + host)
  
@pytest.fixture
def myping():
  #response = os.system("ping " + host)
  yield network_config