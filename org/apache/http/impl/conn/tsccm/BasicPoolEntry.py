def ():
    '''returns BasicPoolEntry\n\n
    (final ClientConnectionOperator op, final HttpRoute route, final ReferenceQueue<Object> queue)\n
    (final ClientConnectionOperator op, final HttpRoute route)\n
    (final ClientConnectionOperator op, final HttpRoute route, final long connTTL, final TimeUnit timeunit)\n
    '''
def getCreated():
    '''returns long\n\n
    getCreated()\n
    '''
def getUpdated():
    '''returns long\n\n
    getUpdated()\n
    '''
def getExpiry():
    '''returns long\n\n
    getExpiry()\n
    '''
def getValidUntil():
    '''returns long\n\n
    getValidUntil()\n
    '''
def updateExpiry():
    '''returns None\n\n
    updateExpiry(final long time, final TimeUnit timeunit)\n
    '''
def isExpired():
    '''returns boolean\n\n
    isExpired(final long now)\n
    '''
