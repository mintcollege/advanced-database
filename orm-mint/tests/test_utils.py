import pytest
from pytest import mark
from typing import Union

def get_fullname(first: str | None = '', last: str | None = '') -> Union[str, None]:
    if first is None and last is None:
        # return None
        raise ValueError('No data')
    if first is None and last is not None:
        return last
    if last is None and first is not None:
        return first

    if first and last:
        # Both must have a value
        return f'{first} {last}'.strip()
    else:
        # One of them has a value
        if not first:
            return last
        if not last:
            return first


class TestUtils:
    @mark.skip
    def test_fullname(self):
        assert get_fullname('aaa', 'bbb') == 'aaa bbb'
        assert get_fullname(first='aaa') == 'aaa'
        assert get_fullname(last='bbb') == 'bbb'
        assert get_fullname('', '') == ''
        assert get_fullname() == ''
        # assert get_fullname(None, None) == None
        assert get_fullname(first='aaa', last=None) == 'aaa'
        assert get_fullname(first=None, last='bbb') == 'bbb'
        assert get_fullname(first=None, last='') == ''
        assert get_fullname(first='', last=None) == ''

        with pytest.raises(ValueError):
            get_fullname(None, None)



class TestUserAccount:
    def test_signin(self):
        pass


    @mark.focus
    def test_signup(self):
        pass


    @mark.focus
    def test_logout(self):
        pass


    # def test_profile(self):
    #     dbdata = update_db()
    #     cachedata = update_cache()
    #     assert dbdata == cachedata

