def ():
    '''returns RouteSpecificPool\n\n
    (final HttpRoute route, final int maxEntries)\n
    (final HttpRoute route, final ConnPerRoute connPerRoute)\n
    '''
def getMaxForRoute():
    '''returns int\n\n
    getMaxForRoute(final HttpRoute unused)\n
    '''
def isUnused():
    '''returns boolean\n\n
    isUnused()\n
    '''
def getCapacity():
    '''returns int\n\n
    getCapacity()\n
    '''
def allocEntry():
    '''returns BasicPoolEntry\n\n
    allocEntry(final Object state)\n
    '''
def freeEntry():
    '''returns None\n\n
    freeEntry(final BasicPoolEntry entry)\n
    '''
def createdEntry():
    '''returns None\n\n
    createdEntry(final BasicPoolEntry entry)\n
    '''
def deleteEntry():
    '''returns boolean\n\n
    deleteEntry(final BasicPoolEntry entry)\n
    '''
def dropEntry():
    '''returns None\n\n
    dropEntry()\n
    '''
def queueThread():
    '''returns None\n\n
    queueThread(final WaitingThread wt)\n
    '''
def hasThread():
    '''returns boolean\n\n
    hasThread()\n
    '''
def nextThread():
    '''returns WaitingThread\n\n
    nextThread()\n
    '''
def removeThread():
    '''returns None\n\n
    removeThread(final WaitingThread wt)\n
    '''
