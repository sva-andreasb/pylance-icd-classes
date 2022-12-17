MODE_RESTORE_ALL = "String  \"restore all\""
MODE_RESTORE_CHANGED_ONLY = "String  \"changed only\""
MODE_RESTORE_FAST = "String  \"restore fast\""
def getPropertyDescriptor():
    '''returns PropertyDescriptor\n\n
    getPropertyDescriptor(final String s)\n
    getPropertyDescriptor(final String key)\n
    '''
def setStateValue():
    '''returns None\n\n
    setStateValue(final String s, final Object o)\n
    '''
def restoreBean():
    '''returns boolean\n\n
    restoreBean(final Object o, final boolean b)\n
    restoreBean(final Object obj, final boolean b, final boolean b2)\n
    '''
def ignoreProperty():
    '''returns boolean\n\n
    ignoreProperty(final String s)\n
    '''
def getStateValue():
    '''returns Object\n\n
    getStateValue(final String s)\n
    '''
def printState():
    '''returns None\n\n
    printState(final PrintStream printStream)\n
    '''
def getException():
    '''returns Exception\n\n
    getException()\n
    '''
def getPropertyName():
    '''returns String\n\n
    getPropertyName()\n
    '''
def getValue():
    '''returns Object\n\n
    getValue()\n
    '''
def ():
    '''returns RestoreException\n\n
    ()\n
    '''
def getExceptions():
    '''returns ExceptionContext[]\n\n
    getExceptions()\n
    '''
def fillInStackTrace():
    '''returns Throwable\n\n
    fillInStackTrace()\n
    '''
def getIndex():
    '''returns int\n\n
    getIndex(final String key)\n
    '''
