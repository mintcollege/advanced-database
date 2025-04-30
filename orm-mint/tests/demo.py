from collections import Counter

class TestFoo:

    @staticmethod
    def calculate(a: int, b: int):
        return a + b


    @staticmethod
    def split_fullname(fullname: str | None, default: str = '',
                       prefix: str | list | tuple | None = None,
                       suffix: str | list | tuple | None = None) -> tuple:
        """
        Splits a fullname into their respective first_name and last_name fields.
        If only one name is given, that becomes the first_name
        :param fullname:    The name to split
        :param default:     The value if only one name is given
        :param prefix:      Custom prefixes to append to the default list
        :param suffix:      Custom suffixes to append to the default list
        :return:            tuple
        """
        # TODO: Fails: Alberto Guzman Jr. PhD
        if not fullname:
            return '', ''

        if prefix and not isinstance(prefix, (str, list, tuple)):
            raise TypeError('`prefix` must be a list/str for multi/single values.')

        if suffix and not isinstance(suffix, (str, list, tuple)):
            raise TypeError('`suffix` must be a list/str for multi/single values.')

        prefix = isinstance(prefix, str) and [prefix] or prefix or []
        suffix = isinstance(suffix, str) and [suffix] or suffix or []
        prefix_lastname = ['dos', 'de', 'delos', 'san', 'dela', 'dona', 'van', 'von', 'der', 'de la', 'bin', 'ben',
                           'al',
                           'Mc', 'O\'', 'Le', 'Mac', 'St.', 'St', 'La', 'L\'', 'L', 'Da', 'D\'', 'D', 'Te', 'Ibn', 'I',
                           *prefix]
        suffix_lastname = ['phd', 'md', 'rn', 'jr', 'sr', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x', 'esq',
                           *suffix]

        list_ = fullname.split()
        lastname_idx = None
        if len(list_) > 2:
            for idx, val in enumerate(list_):
                if val.lower() in prefix_lastname:
                    lastname_idx = idx
                    break
                elif val.lower().replace('.', '') in suffix_lastname:
                    lastname_idx = idx - 1
                else:
                    if idx == len(list_) - 1:
                        lastname_idx = idx
                    else:
                        continue
            list_[:lastname_idx] = [' '.join(list_[:lastname_idx])]
            list_[1:] = [' '.join(list_[1:])]
        try:
            first, last = list_
        except ValueError:
            first, last = [*list_, default]
        return first, last


    @staticmethod
    def reduce_permissions(permissions: list[str]) -> list[str]:
        """
        Merge permissions by removing any items which start with '-'. For use in collating permissions.
        Duplicates are removed in the process.
        :param permissions: List of permissions
        :return:            Filtered permissions list
        """
        include = set()
        exclude = set()

        for perm in permissions:
            perm = perm.strip()
            if perm.startswith('-'):
                exclude.add(perm.strip()[1:])
            else:
                include.add(perm.strip())  # noqa
        resultlist = include - exclude
        return list(resultlist)


    def test_calculate(self):
        assert TestFoo.calculate(1, 2) == 3
        assert TestFoo.calculate(5, 5) == 10


    # print(split_fullname('Alberto Guzman Jr. PhD'))
    def test_split_fullname(self):
        assert TestFoo.split_fullname('Jake Johnson') == ('Jake', 'Johnson')
        assert TestFoo.split_fullname('Jake Guzman III') == ('Jake', 'Guzman III')
        # print('Something happened')
        # assert TestFoo.split_fullname('Alberto Guzman Jr PhD') == ('Alberto', 'Guzman Jr PhD')


    def test_check_perms(self):
        perms1 = ['account.signin', 'account.upload', 'account.update']
        perms2 = ['account.signin', 'account.upload', 'account.update', '-account.upload']

        assert Counter(TestFoo.reduce_permissions(perms1)) == Counter(perms1)
        assert Counter(TestFoo.reduce_permissions(perms2)) == Counter(['account.signin', 'account.update'])
        assert Counter(TestFoo.reduce_permissions([])) == Counter([])
        assert Counter(TestFoo.reduce_permissions(['account.foo', '-account.foo'])) == Counter([])
        assert Counter(TestFoo.reduce_permissions(['account.foo', '-account.foo', 'account.foo'])) == Counter([])

