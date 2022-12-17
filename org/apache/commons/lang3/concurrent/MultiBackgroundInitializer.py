def ():
    '''returns MultiBackgroundInitializer\n\n
    ()\n
    (final ExecutorService exec)\n
    '''
def addInitializer():
    '''returns None\n\n
    addInitializer(final String name, final BackgroundInitializer<?> init)\n
    '''
def getResultObject():
    '''returns Object\n\n
    getResultObject(final String name)\n
    '''
def isException():
    '''returns boolean\n\n
    isException(final String name)\n
    '''
def getException():
    '''returns ConcurrentException\n\n
    getException(final String name)\n
    '''
def initializerNames():
    '''returns Set<String>\n\n
    initializerNames()\n
    '''
def isSuccessful():
    '''returns boolean\n\n
    isSuccessful()\n
    '''
