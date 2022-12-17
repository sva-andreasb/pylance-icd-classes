def getLimit():
    '''returns int\n\n
    getLimit()\n
    '''
def setLimit():
    '''returns None\n\n
    setLimit(final int limit)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def getLevel():
    '''returns Level\n\n
    getLevel(final Category category)\n
    '''
def getEffectiveLevel():
    '''returns Level\n\n
    getEffectiveLevel(final Category category)\n
    '''
def isEnabled():
    '''returns boolean\n\n
    isEnabled(final Level level, final Category category)\n
    '''
def setLevel():
    '''returns None\n\n
    setLevel(final Category category, final Level level)\n
    '''
def clearLevel():
    '''returns None\n\n
    clearLevel(final Category category)\n
    '''
def log():
    '''returns None\n\n
    log(final Level level, final Throwable t)\n
    log(final Level level, final Category category, final Throwable t)\n
    log(final Level level, final Category category, final String message)\n
    log(final Level level, final Category category, final String message, final String detail)\n
    log(final Level level, final Category category, final String message, final Throwable t)\n
    '''
def getEntries():
    '''returns LogEntry[]\n\n
    getEntries()\n
    '''
