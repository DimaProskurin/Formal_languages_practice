class Matrix:
    def __init__(self, word_len):
        self.subwords = [[0] * word_len for i in range(word_len)]
        self.empty_word = False


def merge(matrix_first, matrix_second):
    matrix_result = Matrix(len(matrix_first.subwords))
    for i in range(len(matrix_first.subwords)):
        for j in range(len(matrix_first.subwords[i])):
            matrix_result.subwords[i][j] = (matrix_first.subwords[i][j]
                                            + matrix_second.subwords[i][j]) % 2

    matrix_result.empty_word = True if matrix_first.empty_word or matrix_second.empty_word else False
    return matrix_result


def concat(matrix_first, matrix_second, word):
    matrix_result = Matrix(len(matrix_first.subwords))

    for first_word_start in range(len(matrix_first.subwords)):
        for first_word_end in range(len(matrix_first.subwords[first_word_start])):
            for second_word_start in range(len(matrix_second.subwords)):
                for second_word_end in range(len(matrix_second.subwords[second_word_start])):
                    if matrix_first.subwords[first_word_start][first_word_end] == 1 and \
                            matrix_second.subwords[second_word_start][second_word_end] == 1:
                        first_word = word[first_word_start:first_word_end + 1]
                        second_word = word[second_word_start:second_word_end + 1]
                        new_word = first_word + second_word
                        if new_word in word:
                            new_word_start = word.find(new_word)
                            new_word_end = new_word_start + len(new_word) - 1
                            matrix_result.subwords[new_word_start][new_word_end] = 1

    if matrix_first.empty_word:
        for second_word_start in range(len(matrix_second.subwords)):
            for second_word_end in range(len(matrix_second.subwords[second_word_start])):
                if matrix_second.subwords[second_word_start][second_word_end] == 1:
                    second_word = word[second_word_start:second_word_end + 1]
                    new_word = second_word
                    if new_word in word:
                        new_word_start = word.find(new_word)
                        new_word_end = new_word_start + len(new_word) - 1
                        matrix_result.subwords[new_word_start][new_word_end] = 1

        if matrix_second.empty_word:
            matrix_result.empty_word = True

    if matrix_second.empty_word:
        for first_word_start in range(len(matrix_first.subwords)):
            for first_word_end in range(len(matrix_first.subwords[first_word_start])):
                if matrix_first.subwords[first_word_start][first_word_end] == 1:
                    first_word = word[first_word_start:first_word_end + 1]
                    new_word = first_word
                    if new_word in word:
                        new_word_start = word.find(new_word)
                        new_word_end = new_word_start + len(new_word) - 1
                        matrix_result.subwords[new_word_start][new_word_end] = 1

    return matrix_result


def iteration_clini(input_matrix, word):
    matrix_result = Matrix(len(input_matrix.subwords))
    matrix_result.empty_word = True

    current_matrix = input_matrix
    # n iterations
    for i in range(len(input_matrix.subwords)):
        matrix_result = merge(matrix_result, current_matrix)
        current_matrix = concat(current_matrix, input_matrix, word)

    return matrix_result


def build_subwords_matrix(rpn, word):
    stack = []

    for char in rpn:
        if char in ['+', '.', '*']:
            if char == '*':
                operand = stack.pop()
                stack.append(iteration_clini(operand, word))
            else:
                operand_first = stack.pop()
                operand_second = stack.pop()
                if char == '+':
                    stack.append(merge(operand_first, operand_second))
                else:
                    stack.append(concat(operand_second, operand_first, word))
        else:
            matrix = Matrix(WORD_LEN)

            if char == '1':
                matrix.empty_word = True
            else:
                index_start = word.find(char)
                index_end = index_start
                matrix.subwords[index_start][index_end] = 1

            stack.append(matrix)

    return stack[0]


def find_max_len_subword_in_subwords_matrix(matrix):
    max_len = -1
    if matrix.empty_word:
        max_len = 0

    for word_start in range(len(matrix.subwords)):
        for word_end in range(len(matrix.subwords[word_start])):
            if matrix.subwords[word_start][word_end] == 1 and word_end - word_start + 1 > max_len:
                max_len = word_end - word_start + 1

    return max_len


WORD_LEN = 2  # default value for tests

if __name__ == '__main__':
    input_RPN = input()
    input_word = input()
    WORD_LEN = len(input_word)

    try:
        answer = find_max_len_subword_in_subwords_matrix(build_subwords_matrix(input_RPN, input_word))
        if answer == -1:
            print('INF')
        else:
            print(answer)
    except Exception:
        print('ERROR')
