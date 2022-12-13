def BasicPoolEntry():
'''public BasicPoolEntry(final ClientConnectionOperator op, final HttpRoute route, final ReferenceQueue<Object> queue)
public BasicPoolEntry(final ClientConnectionOperator op, final HttpRoute route)
public BasicPoolEntry(final ClientConnectionOperator op, final HttpRoute route, final long connTTL, final TimeUnit timeunit)
'''
pass
def getCreated():
'''public long getCreated()
'''
pass
def getUpdated():
'''public long getUpdated()
'''
pass
def getExpiry():
'''public long getExpiry()
'''
pass
def getValidUntil():
'''public long getValidUntil()
'''
pass
def updateExpiry():
'''public void updateExpiry(final long time, final TimeUnit timeunit)
'''
pass
def isExpired():
'''public boolean isExpired(final long now)
'''
pass
