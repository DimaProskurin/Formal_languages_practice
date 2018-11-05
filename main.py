def merge(first_set, second_set):
    result = first_set.union(second_set)
    for word in result:
        if len(word) > WORD_LEN:
            result.remove(word)
    return result


def concat(first_set, second_set):
    result = set()
    for word_in_first_set in first_set:
        for word_in_second_set in second_set:
            if len(word_in_first_set + word_in_second_set) <= WORD_LEN:
                result.add(word_in_first_set + word_in_second_set)

    return result


def iteration_clini(input_set):
    result = set()
    result.add('')

    current_iteration = input_set
    while len(current_iteration) > 0:
        for word in current_iteration:
            result.add(word)

        current_iteration = concat(current_iteration, input_set)

    return result


def all_subwords(word):
    result = set()
    for i in range(len(word) + 1):
        for j in range(i, len(word) + 1):
            result.add(word[i: j])
    return result


def build_language(RPN):
    stack = []

    for char in RPN:
        if char in ['+', '.', '*']:
            if char == '*':
                operand = stack.pop()
                stack.append(iteration_clini(operand))
            else:
                operand_first = stack.pop()
                operand_second = stack.pop()
                if char == '+':
                    stack.append(merge(operand_first, operand_second))
                else:
                    stack.append(concat(operand_second, operand_first))
        else:
            stack.append(set(char))

    return stack[0]


def find_max_len_subword_in_language(language, word):
    max_len = -1
    subwords = all_subwords(word)
    for subword in subwords:
        if subword in language and len(subword) > max_len:
            max_len = len(subword)

    return max_len


WORD_LEN = 3  # default value for tests

if __name__ == '__main__':
    input_RPN = input()
    input_word = input()
    WORD_LEN = len(input_word)

    try:
        answer = find_max_len_subword_in_language(build_language(input_RPN), input_word)
        if answer == -1:
            print('INF')
        else:
            print(answer)
    except Exception:
        print('ERROR')
