def ():
    '''returns JsonReadContext\n\n
    (final JsonReadContext parent, final DupDetector dups, final int type, final int lineNr, final int colNr)\n
    '''
def withDupDetector():
    '''returns JsonReadContext\n\n
    withDupDetector(final DupDetector dups)\n
    '''
def getCurrentValue():
    '''returns Object\n\n
    getCurrentValue()\n
    '''
def setCurrentValue():
    '''returns None\n\n
    setCurrentValue(final Object v)\n
    '''
def createChildArrayContext():
    '''returns JsonReadContext\n\n
    createChildArrayContext(final int lineNr, final int colNr)\n
    '''
def createChildObjectContext():
    '''returns JsonReadContext\n\n
    createChildObjectContext(final int lineNr, final int colNr)\n
    '''
def getCurrentName():
    '''returns String\n\n
    getCurrentName()\n
    '''
def hasCurrentName():
    '''returns boolean\n\n
    hasCurrentName()\n
    '''
def getParent():
    '''returns JsonReadContext\n\n
    getParent()\n
    '''
def getStartLocation():
    '''returns JsonLocation\n\n
    getStartLocation(final Object srcRef)\n
    '''
def clearAndGetParent():
    '''returns JsonReadContext\n\n
    clearAndGetParent()\n
    '''
def getDupDetector():
    '''returns DupDetector\n\n
    getDupDetector()\n
    '''
def expectComma():
    '''returns boolean\n\n
    expectComma()\n
    '''
def setCurrentName():
    '''returns None\n\n
    setCurrentName(final String name)\n
    '''
