'''
structures.py

Simple functions performing operations on basic Python data structures.  
'''

# Lists

# write a function that returns a list containig the first and the last element
# of "the_list". 
def first_and_last(the_list):
    newlist = [the_list[0],the_list[-1]]
    return newlist


# write a function that returns part of "the_list" between indices given by the
# second and third parameter, respectively. The returned part should be in
# reverse order than in the original "the_list". 
# If "end" is greater then "beginning" or any og the indices is out of the
# list, raise a "ValueError" exception. 
def part_reverse(the_list, beginning, end):
    if beginning > end:
        raise(ValueError)
    elif len(the_list) < beginning:
        raise(ValueError)
    elif len(the_list) < end:
        raise(ValueError)
    else:
        secondlist = the_list[beginning:end]
        return secondlist.reverse() # hint this is incomplete


# write a function that at the "index" of "the_list" inserts three times the
# same value. For example if the_list = [0,1,2,3,4] and index = 3 the function
# will return [0,1,2,3,3,3,4]. 
def repeat_at_index(the_list, index):
    for i in range(2):
        the_list.insert(index,the_list[index])
        i = i+1
    return the_list


# Strings

# write a function that checks whether the word is a palindrome, i.e. it reads
# the same forward and backwards
def palindrome_word(word):
    wordrev = word[::-1]
    return word == wordrev

# write a function that checks whether the sentence is a palindrome, i.e. it
# read the same forward and backward. Ignore all spaces and other characters
# like fullstops, commas, etc. Also do not consider whether the letter is
# capital or not. 
def palindrome_sentence(sentence):
    import string
    sentence2 = ''.join(i.lower() for i in sentence if i in string.ascii_letters)
    sentencerev = sentence2[::-1]
    return sentence2 == sentencerev

# write a function that concatenates two sentences. First the function checks
# whether the sentence meets the following criteria: it starts with a capital
# letter and it ends with a full stop, question mark, or an exclamation point.
# Keep in mind, that the sentence might have whitespace at the beginning or at
# the end.  The concatenated sentence must have no white space at the beginning
# or at the end and the must be exactly one space after the end of the first
# sentence. 
def concatenate_sentences(sentence1, sentence2):
    import string
    if sentence1[0] == ' ':
        sentence1 = sentence1.replace(' ','',1)
    if sentence1[-1] == ' ':
        sentence1 = sentence1[:len(sentence1) - 1]
    if sentence2[0] == ' ':
        sentence2 = sentence2.replace(' ','',1)
    if sentence2[-1] == ' ':
        sentence2 = sentence2[:len(sentence2) - 1]
    if sentence1[0].islower():
        return 'sentence 1 start upper case'
    if sentence2[0].islower():
        return 'sentence 2 start upper case'
    if sentence1[-1] not in string.punctuation:
        return 'sentence 1 finish right'
    if sentence2[-1] not in string.punctuation:
        return 'sentence 2 finish right'
    return sentence1 + ' ' + sentence2



# Dictionaries

# write a function that checks whether there is a record with given key in the
# dictionary. Return True or False.
def index_exists(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False
    

# write a function which checks whether given value is stored in the
# dictionary. Return True or False.
def value_exists(dictionary, value):
    if value in dictionary.values():
        return True
    else:
        return False

# write a function that returns a new dictionary which contains all the values
# from dictionary1 and dictionary2.
def merge_dictionaries(dictionary1, dictionary2):
    dictionary1.update(dictionary2)
    return dictionary1
