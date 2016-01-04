#CS 115 Homework 2 
#Daniel Vinakovsky
#5 September 2013
#I pledge my honor that I have abided by the Stevens Honor System

# Implement the following functions using map and reduce.
# You will probably need to write additional functions to help.
# Even if you are familiar with recursion and for/while loops,
# do not use them.  Use map and/or reduce.

def shriek(strs):
    """Assume strs is a non-empty list of strings.  Return a list of
    the same strings but with exclamation mark (!) suffix.  See example below."""
    return None  # replace this by your code

a_list = ['I', 'am', 'learning', 'to', 'program']
sliced = a_list[start:end]
shriek_example = shriek(a_list)
print shriek_example
# should be ['I!' 'am!', 'learning!', 'to!', 'program!']   


def catenate(strs):
    """Assume strs is a list of strings.  Return a single string of their catenation"""
    return None

catenate_example = catenate(a_list) 
# should be 'Iamlearningtoprogram'


def catSpace(strs):
    """Assume strs is a list of strings.  Return their catenation, but with one space between each one."""
    return None

catSpace_example = catSpace(a_list) 
# should be 'I am learning to program'
# Hint: use map and reduce to get ' I am learning to program', and then
# use slice notation to get rid of the extra space at the beginning.


