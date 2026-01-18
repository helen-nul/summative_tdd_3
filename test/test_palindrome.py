from main import is_pali

def test_pytest():
    assert 2+2 == 4

def test_is_pali_happy():
        assert is_pali("radar") == True
        assert is_pali("Radar") == True

def test_is_pali_unhappy():
        assert is_pali("radar1") == False
