NAME_KEY = "String  \"name\""
CASE_KEY = "String  \"casesensitive\""
NEGATE_KEY = "String  \"negate\""
REGEX_KEY = "String  \"regex\""
def ():
    '''returns FilenameSelector\n\n
    ()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def setName():
    '''returns None\n\n
    setName(String pattern)\n
    '''
def setRegex():
    '''returns None\n\n
    setRegex(final String pattern)\n
    '''
def setCasesensitive():
    '''returns None\n\n
    setCasesensitive(final boolean casesensitive)\n
    '''
def setNegate():
    '''returns None\n\n
    setNegate(final boolean negated)\n
    '''
def setParameters():
    '''returns None\n\n
    setParameters(final Parameter[] parameters)\n
    '''
def verifySettings():
    '''returns None\n\n
    verifySettings()\n
    '''
def isSelected():
    '''returns boolean\n\n
    isSelected(final File basedir, final String filename, final File file)\n
    '''
