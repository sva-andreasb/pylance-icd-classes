def ():
    '''returns SessionHolder\n\n
    (final Session session)\n
    (final Object key, final Session session)\n
    '''
def getSession():
    '''returns Session\n\n
    getSession()\n
    getSession(final Object key)\n
    '''
def getAnySession():
    '''returns Session\n\n
    getAnySession()\n
    '''
def addSession():
    '''returns None\n\n
    addSession(final Session session)\n
    addSession(final Object key, final Session session)\n
    '''
def removeSession():
    '''returns Session\n\n
    removeSession(final Object key)\n
    '''
def containsSession():
    '''returns boolean\n\n
    containsSession(final Session session)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def doesNotHoldNonDefaultSession():
    '''returns boolean\n\n
    doesNotHoldNonDefaultSession()\n
    '''
def setTransaction():
    '''returns None\n\n
    setTransaction(final Transaction transaction)\n
    '''
def getTransaction():
    '''returns Transaction\n\n
    getTransaction()\n
    '''
def setPreviousFlushMode():
    '''returns None\n\n
    setPreviousFlushMode(final FlushMode previousFlushMode)\n
    '''
def getPreviousFlushMode():
    '''returns FlushMode\n\n
    getPreviousFlushMode()\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
