CONTEXT_INITIALIZE = "short  -1"
CONTEXT_INCLUDE = "short  0"
CONTEXT_REDEFINE = "short  1"
CONTEXT_IMPORT = "short  2"
CONTEXT_PREPARSE = "short  3"
CONTEXT_INSTANCE = "short  4"
CONTEXT_ELEMENT = "short  5"
CONTEXT_ATTRIBUTE = "short  6"
CONTEXT_XSITYPE = "short  7"
def getGrammarType():
    '''returns String\n\n
    getGrammarType()\n
    '''
def getContextType():
    '''returns short\n\n
    getContextType()\n
    '''
def getTargetNamespace():
    '''returns String\n\n
    getTargetNamespace()\n
    '''
def getLocationHints():
    '''returns String[]\n\n
    getLocationHints()\n
    '''
def getTriggeringComponent():
    '''returns QName\n\n
    getTriggeringComponent()\n
    '''
def getEnclosingElementName():
    '''returns QName\n\n
    getEnclosingElementName()\n
    '''
def getAttributes():
    '''returns XMLAttributes\n\n
    getAttributes()\n
    '''
def fromInstance():
    '''returns boolean\n\n
    fromInstance()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def setContextType():
    '''returns None\n\n
    setContextType(final short fContextType)\n
    '''
def setTargetNamespace():
    '''returns None\n\n
    setTargetNamespace(final String fNamespace)\n
    '''
def setLocationHints():
    '''returns None\n\n
    setLocationHints(final String[] array)\n
    '''
def setTriggeringComponent():
    '''returns None\n\n
    setTriggeringComponent(final QName fTriggeringComponent)\n
    '''
def setEnclosingElementName():
    '''returns None\n\n
    setEnclosingElementName(final QName fEnclosedElementName)\n
    '''
def setAttributes():
    '''returns None\n\n
    setAttributes(final XMLAttributes fAttributes)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def makeClone():
    '''returns XSDDescription\n\n
    makeClone()\n
    '''
