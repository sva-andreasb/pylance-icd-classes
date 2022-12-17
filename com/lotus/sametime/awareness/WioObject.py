def ():
    '''returns WioObject\n\n
    (final STWatchedObject watchedObject, final short type)\n
    (final STWatchedObject watchedObject, final STGroup stGroup)\n
    '''
def setStatus():
    '''returns None\n\n
    setStatus(final short n, final String s)\n
    '''
def addWatch():
    '''returns None\n\n
    addWatch(final Integer n)\n
    addWatch(final STGroup stGroup)\n
    '''
def removeWatch():
    '''returns None\n\n
    removeWatch(final Integer key)\n
    removeWatch(final STGroup key)\n
    '''
def isWatched():
    '''returns boolean\n\n
    isWatched(final Integer key)\n
    isWatched(final Object key)\n
    isWatched()\n
    '''
def getWatchingSessions():
    '''returns Enumeration\n\n
    getWatchingSessions()\n
    '''
def getWatchingGroups():
    '''returns Enumeration\n\n
    getWatchingGroups()\n
    '''
def dumpToStream():
    '''returns None\n\n
    dumpToStream(final NdrOutputStream ndrOutputStream)\n
    '''
def isWatchedBySession():
    '''returns boolean\n\n
    isWatchedBySession()\n
    '''
def getWatchedObject():
    '''returns STWatchedObject\n\n
    getWatchedObject()\n
    '''
