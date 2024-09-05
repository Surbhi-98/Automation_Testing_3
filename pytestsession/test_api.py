import pytest

# API Testing Function
# test_payload={
#         "Player_id":4
#     }
@pytest.mark.parametrize("test_payload",[(4), (3), (5)])
def test_get_player(get_player, test_payload):
    response=get_player.get(test_payload)
    assert response.get("Code")==200, "Test Failed for test_get_player"