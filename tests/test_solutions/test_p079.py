from solutions.p079 import PasscodeSearch, load_logins


def test_generate_short_passcode() -> None:
    logins = load_logins()
    assert PasscodeSearch().generate_short_passcode(logins) == 73162890
