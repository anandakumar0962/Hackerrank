'''A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

For example, "Hello World 1", "HELLO 0", and "hello world hello world 2" are all sentences. You are given a sentence containing an integer . You want to truncate sentence such that it contains only the first for the given integer words followed by it should not contains any duplicate words and any alphanumeric characters. Return sentence after truncating it.

Input Format

'Hello how are are you # Contestant 6'

Constraints

truncating integer should be less than the length of the spaced words in a sentence(includes alphanumeric and integer)

Output Format

'Hello how are you'  '''

def truncate_sentence(sentence):
        corrected_sentence = []
        for word in sentence:
            if word.isalpha() and len(corrected_sentence) < (int(sentence[-1])-1) and word not in corrected_sentence:
                corrected_sentence.append(word)
                
        return corrected_sentence
        
given_sentence = input().split(' ')
result = truncate_sentence(given_sentence)
print(' '.join(result))
        