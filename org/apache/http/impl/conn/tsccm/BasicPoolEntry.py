def BasicPoolEntry():
    '''public BasicPoolEntry(final ClientConnectionOperator op, final HttpRoute route, final ReferenceQueue<Object> queue)
    public BasicPoolEntry(final ClientConnectionOperator op, final HttpRoute route)
    public BasicPoolEntry(final ClientConnectionOperator op, final HttpRoute route, final long connTTL, final TimeUnit timeunit)
    '''
def getCreated():
    '''public long getCreated()
    '''
def getUpdated():
    '''public long getUpdated()
    '''
def getExpiry():
    '''public long getExpiry()
    '''
def getValidUntil():
    '''public long getValidUntil()
    '''
def updateExpiry():
    '''public void updateExpiry(final long time, final TimeUnit timeunit)
    '''
def isExpired():
    '''public boolean isExpired(final long now)
    '''
