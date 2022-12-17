def ():
    '''returns BasicMessageLogger\n\n
    ()\n
    '''
def progressMsg():
    '''returns None\n\n
    progressMsg(String msg)\n
    progressMsg(String msg, final String[] params)\n
    '''
def message():
    '''returns None\n\n
    message(String msg)\n
    message(String msg, final String[] params)\n
    '''
def warning():
    '''returns None\n\n
    warning(String msg)\n
    warning(String msg, final String[] params)\n
    '''
def error():
    '''returns None\n\n
    error(String msg)\n
    error(String msg, final String[] params)\n
    '''
def exception():
    '''returns None\n\n
    exception(final Throwable t)\n
    exception(final String pageName, final String itemName, final Throwable t)\n
    exception(final String pageName, final String itemName, final String fieldName, final Throwable t)\n
    '''
def dataIntegrityMessage():
    '''returns None\n\n
    dataIntegrityMessage(String msg)\n
    dataIntegrityMessage(String msg, final String[] params)\n
    '''
def get():
    '''returns String\n\n
    get(final String key)\n
    get(final String key, final String[] params)\n
    '''
def getErrorCount():
    '''returns int\n\n
    getErrorCount()\n
    '''
