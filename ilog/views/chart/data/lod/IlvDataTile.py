EMPTY = "int  0"
LOCKED = "int  1"
CACHED = "int  2"
def lock():
    '''returns None\n\n
    lock(final Object o)\n
    '''
def unlock():
    '''returns boolean\n\n
    unlock(final Object o)\n
    '''
def getLocks():
    '''returns Iterator\n\n
    getLocks()\n
    '''
def loadComplete():
    '''returns None\n\n
    loadComplete()\n
    '''
def notifyLoadError():
    '''returns None\n\n
    notifyLoadError(final Throwable t)\n
    '''
def setData():
    '''returns None\n\n
    setData(final IlvDoublePoints ilvDoublePoints)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
