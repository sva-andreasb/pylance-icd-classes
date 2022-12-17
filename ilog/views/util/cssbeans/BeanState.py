def ():
    '''returns BeanState\n\n
    (final Object o)\n
    ()\n
    '''
def copy():
    '''returns BeanState\n\n
    copy()\n
    '''
def saveState():
    '''returns BeanState\n\n
    saveState(final Object o)\n
    '''
def getPropertyDescriptor():
    '''returns PropertyDescriptor\n\n
    getPropertyDescriptor(final String anObject)\n
    '''
def updateState():
    '''returns BeanState\n\n
    updateState(final Object o, final PropertyDescriptor e, final int value)\n
    '''
def restoreBean():
    '''returns boolean\n\n
    restoreBean(final Object o, final boolean b)\n
    restoreBean(final Object obj, final String s, final boolean b)\n
    '''
def restoreBeanUncaught():
    '''returns boolean\n\n
    restoreBeanUncaught(final Object o, final boolean b, final boolean b2)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def propertyIterator():
    '''returns Iterator\n\n
    propertyIterator()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns Object\n\n
    next()\n
    '''
def remove():
    '''returns boolean\n\n
    remove()\n
    remove(final String s)\n
    remove(final int n, final String s)\n
    '''
def getValue():
    '''returns Object\n\n
    getValue(final String s)\n
    getValue(final int n, final String s)\n
    '''
def printState():
    '''returns None\n\n
    printState(final PrintStream printStream)\n
    '''
