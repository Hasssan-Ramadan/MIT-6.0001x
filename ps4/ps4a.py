# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx
import unittest


def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1:
        return [sequence]
    permutations = []
    for index, char in enumerate(sequence):
        for permutation in get_permutations(sequence[:index] + sequence[index + 1:]):
            permutations += [char + permutation]
    return permutations


class TestPermutations(unittest.TestCase):

    def test_permutations(self, squence, expected):
        self.assertEqual(get_permutations(squence), expected,
                         "Actual and expected permutations are not the same")


if __name__ == '__main__':
    #    #EXAMPLE
    #    example_input = 'abc'
    #    print('Input:', example_input)
    #    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    #    print('Actual Output:', get_permutations(example_input))

    #    # Put three example test cases here (for your sanity, limit your inputs
    #    to be three characters or fewer as you will have n! permutations for a
    #    sequence of length n)
    test = TestPermutations()
    test.test_permutations('nor', ['nor', 'nro', 'onr', 'orn', 'rno', 'ron'])
