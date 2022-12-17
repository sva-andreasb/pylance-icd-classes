def ():
    '''returns CharJoin\n\n
    (final int charBufSize)\n
    (final Object srcLeft, final int offLeft, final int cchLeft, final Object srcRight, final int offRight)\n
    '''
def getCharIterator():
    '''returns CharIterator\n\n
    getCharIterator(final Object src, final int off, final int cch)\n
    getCharIterator(final Object src, final int off, final int cch, final int start)\n
    '''
def stripLeft():
    '''returns Object\n\n
    stripLeft(final Object src, int off, int cch)\n
    '''
def stripRight():
    '''returns Object\n\n
    stripRight(final Object src, final int off, int cch)\n
    '''
def insertChars():
    '''returns Object\n\n
    insertChars(final int posInsert, final Object src, final int off, final int cch, final Object srcInsert, final int offInsert, final int cchInsert)\n
    '''
def removeChars():
    '''returns Object\n\n
    removeChars(final int posRemove, final int cchRemove, final Object src, final int off, final int cch)\n
    '''
def saveChars():
    '''returns Object\n\n
    saveChars(final Object srcSave, final int offSave, final int cchSave)\n
    saveChars(final Object srcSave, final int offSave, final int cchSave, final Object srcPrev, final int offPrev, final int cchPrev)\n
    '''
def depth():
    '''returns int\n\n
    depth()\n
    '''
def isValid():
    '''returns boolean\n\n
    isValid(final int off, final int cch)\n
    '''
def init():
    '''returns None\n\n
    init(final Object src, final int off, final int cch)\n
    init(final Object src, final int off, final int cch, final int startPos)\n
    '''
def release():
    '''returns None\n\n
    release()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def hasPrev():
    '''returns boolean\n\n
    hasPrev()\n
    '''
def next():
    '''returns char\n\n
    next()\n
    '''
def prev():
    '''returns char\n\n
    prev()\n
    '''
def movePos():
    '''returns None\n\n
    movePos(final int newPos)\n
    '''
