def ():
    '''returns MaxMessageCache\n\n
    ()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def reload():
    '''returns None\n\n
    reload()\n
    reload(final String hashKey)\n
    reload(final String group, final String key, final String langCode)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getMaxMessage():
    '''returns MaxMessage\n\n
    getMaxMessage(final String group, final String key, final UserInfo ui)\n
    getMaxMessage(final String group, final String key, final String langCode)\n
    getMaxMessage(final String group, final String key)\n
    '''
def getMessage():
    '''returns Message\n\n
    getMessage(final String group, final String key, final UserInfo ui)\n
    getMessage(final String group, final String key)\n
    '''
def getTaggedMessage():
    '''returns Message\n\n
    getTaggedMessage(final String group, final String key, final UserInfo ui)\n
    getTaggedMessage(final String group, final String key, final String langCode)\n
    getTaggedMessage(final String group, final String key)\n
    '''
def loadMsgGroup():
    '''returns None\n\n
    loadMsgGroup(final String group, final UserInfo ui)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def addElement():
    '''returns None\n\n
    addElement(String group, final String key, final String langCode, final MaxMessage msgRef)\n
    '''
def getElement():
    '''returns MaxMessage\n\n
    getElement(String group, final String key, final String langCode)\n
    '''
def getElementInAnyLanguage():
    '''returns MaxMessage\n\n
    getElementInAnyLanguage(String group, final String key)\n
    '''
def isGroupLoaded():
    '''returns boolean\n\n
    isGroupLoaded(String group, final String langCode)\n
    '''
def clearGroupForAllLanguage():
    '''returns None\n\n
    clearGroupForAllLanguage(final String group)\n
    '''
def clearMessageForAllLanguage():
    '''returns None\n\n
    clearMessageForAllLanguage(String group, final String key)\n
    '''
def getLoadedLanguages():
    '''returns String[]\n\n
    getLoadedLanguages(String group, final String key)\n
    '''
def clearMessage():
    '''returns None\n\n
    clearMessage(String group, final String key, final String langCode)\n
    '''
