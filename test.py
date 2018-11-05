import unittest
from main import merge, concat, iteration_clini
from main import all_subwords
from main import build_language, find_max_len_subword_in_language


class TestLanguageMethods(unittest.TestCase):
    def test_merge(self):
        self.assertEqual(merge({'a', 'b'}, {'b', 'c'}), {'a', 'b', 'c'})
        self.assertEqual(merge({'a', 'b'}, {'c', 'd'}), {'a', 'b', 'c', 'd'})
        self.assertEqual(merge({''}, {'ba', 'cd'}), {'', 'ba', 'cd'})

    def test_concat(self):
        self.assertEqual(concat({'a'}, {'b', 'c'}), {'ab', 'ac'})
        self.assertEqual(concat({'ab', 'ba'}, {'b', 'c'}), {'abb', 'abc', 'bab', 'bac'})
        self.assertEqual(concat({''}, {'bab', 'cba'}), {'bab', 'cba'})

    def test_iteration_clini(self):
        self.assertEqual(iteration_clini({'a'}), {'', 'a', 'aa', 'aaa'})
        self.assertEqual(iteration_clini({'a', 'b'}), {'', 'a', 'b', 'aa', 'ab', 'ba', 'bb',
                                                       'aaa', 'aab', 'aba', 'abb', 'baa', 'bab',
                                                       'bba', 'bbb'})


class TestAdditionMethods(unittest.TestCase):
    def test_all_subwords(self):
        self.assertEqual(all_subwords('ab'), {'', 'a', 'b', 'ab'})
        self.assertEqual(all_subwords(''), {''})
        self.assertEqual(all_subwords('a'), {'', 'a'})
        self.assertEqual(all_subwords('aba'), {'', 'a', 'ab', 'aba', 'b', 'ba'})


class TestTaskMethods(unittest.TestCase):
    def test_build_language(self):
        self.assertEqual(build_language('ab+bc+.'), {'ab', 'ac', 'bb', 'bc'})
        self.assertEqual(build_language('ab+*'), {'', 'a', 'b', 'aa', 'ab', 'ba', 'bb',
                                                  'aaa', 'aab', 'aba', 'abb', 'baa',
                                                  'bab', 'bba', 'bbb'})
        self.assertEqual(build_language('a'), {'a'})

    def test_find_max_len_subword_in_language(self):
        self.assertEqual(find_max_len_subword_in_language({'ab', 'ac', 'bb', 'bc'}, 'ab'), 2)
        self.assertEqual(find_max_len_subword_in_language({'ab', 'aa', 'ba', 'bb'}, 'cc'), -1)
        self.assertEqual(find_max_len_subword_in_language({'a'}, 'abcd'), 1)
        self.assertEqual(find_max_len_subword_in_language({'', 'bab', 'cab'}, 'a'), 0)


if __name__ == '__main__':
    unittest.main()
