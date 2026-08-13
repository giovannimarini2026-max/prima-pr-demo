from greet import greet, shout


def test_greet_with_name():
    assert greet("Giovanni") == "Hello, Giovanni!"


def test_shout():
    assert shout("ciao") == "CIAO!"
