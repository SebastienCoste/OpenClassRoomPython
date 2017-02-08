'''
Created on Feb 8, 2017

@author: Static
'''
from roboc.connector import Messages as m

class Translator(object):
    '''
    It will be used to translate messages, and actions from the user
    '''


    def __init__(self, userLan):
        self.lan = userLan
        
    def getMessage(self, key):
        try:
            return m.LanguageToMessages[self.lan][key]
        except KeyError:
            return key
        
    def getTechMatcher(self, matcherName):
        return m.LanguageToTech[self.lan][matcherName]