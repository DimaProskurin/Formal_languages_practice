import unittest
from main import Matrix, WORD_LEN
from main import merge, concat, iteration_clini
from main import build_subwords_matrix, find_max_len_subword_in_subwords_matrix


class TestLanguageMethods(unittest.TestCase):
    def test_merge(self):
        matrix_first = Matrix(WORD_LEN)
        matrix_first.empty_word = True
        matrix_first.subwords[0][0] = 1

        matrix_second = Matrix(WORD_LEN)
        matrix_second.empty_word = False
        matrix_second.subwords[1][1] = 1

        matrix = merge(matrix_first, matrix_second)

        self.assertEqual(matrix.empty_word, True)
        self.assertEqual(matrix.subwords[0][0], 1)
        self.assertEqual(matrix.subwords[1][1], 1)
        self.assertEqual(matrix.subwords[0][1], 0)

    def test_concat(self):
        word = 'ab'
        matrix_first = Matrix(len(word))
        matrix_second = Matrix(len(word))
        matrix_first.subwords[0][0] = 1
        matrix_second.subwords[1][1] = 1

        matrix = concat(matrix_first, matrix_second, word)

        self.assertEqual(matrix.empty_word, False)
        self.assertEqual(matrix.subwords[0][0], 0)
        self.assertEqual(matrix.subwords[0][1], 1)

    def test_iteration_clini(self):
        word = 'ab'
        matrix = Matrix(len(word))
        matrix.subwords[0][0] = 1

        matrix = iteration_clini(matrix, word)

        self.assertEqual(matrix.empty_word, True)
        self.assertEqual(matrix.subwords[0][0], 1)
        self.assertEqual(matrix.subwords[1][1], 0)


class TestTaskMethods(unittest.TestCase):
    def test_build_subwords_matrix(self):
        word = 'ab'
        rpn = 'ab+ab+.'
        matrix = build_subwords_matrix(rpn, word)

        self.assertEqual(matrix.empty_word, False)
        self.assertEqual(matrix.subwords[0][1], 1)
        self.assertEqual(matrix.subwords[0][0], 0)

    def test_find_max_len_subword_in_subwords_matrix(self):
        matrix = Matrix(WORD_LEN)
        matrix.empty_word = True

        self.assertEqual(find_max_len_subword_in_subwords_matrix(matrix), 0)


class TestErrorsMethods(unittest.TestCase):
    def test_build_language(self):
        try:
            build_subwords_matrix('++++', 'word')
            build_subwords_matrix('abacaba', 'word')
            build_subwords_matrix('a*a+b.c+', 'word')
        except Exception:
            self.assertEqual(1, 1)
            return

        self.assertEqual(1, 0)


if __name__ == '__main__':
    unittest.main()
