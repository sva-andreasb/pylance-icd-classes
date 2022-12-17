def ():
    '''returns IdleConnectionHandler\n\n
    ()\n
    '''
def add():
    '''returns None\n\n
    add(final HttpConnection connection, final long validDuration, final TimeUnit unit)\n
    '''
def remove():
    '''returns boolean\n\n
    remove(final HttpConnection connection)\n
    '''
def removeAll():
    '''returns None\n\n
    removeAll()\n
    '''
def closeIdleConnections():
    '''returns None\n\n
    closeIdleConnections(final long idleTime)\n
    '''
def closeExpiredConnections():
    '''returns None\n\n
    closeExpiredConnections()\n
    '''
