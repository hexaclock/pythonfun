#CS 115 Homework 2 
#Daniel Vinakovsky
#5 September 2013
#I pledge my honor that I have abided by the Stevens Honor System

def shriek(strs):
    return map(appendExclaim,strs) 

def catenate(strs):
    """Assume strs is a list of strings.  Return a single string of their catenation"""
    return reduce(concatenate,strs)

def catSpace(strs):
    """Assume strs is a list of strings.  Return their catenation, but with one space between each one."""
    return reduce(concatSpace,strs)

#extra functions

#appends exclamation point to any string passed in, and returns string!
def appendExclaim(strg):
        return strg + '!'
    
#returns concatenation of stra+strb (strings that are passed into function)
def concatenate(stra,strb):
        return stra+strb

#returns conatenation of stra+_space_+strb
def concatSpace(stra,strb):
        return stra + ' ' + strb

