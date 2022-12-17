CONNECTION_CLOSED = "int  1"
LOCAL_TRANSACTION_STARTED = "int  2"
LOCAL_TRANSACTION_COMMITTED = "int  3"
LOCAL_TRANSACTION_ROLLEDBACK = "int  4"
CONNECTION_ERROR_OCCURRED = "int  5"
def getId():
    '''returns int\n\n
    getId()\n
    '''
def getException():
    '''returns Exception\n\n
    getException()\n
    '''
def getConnectionHandle():
    '''returns Object\n\n
    getConnectionHandle()\n
    '''
def setConnectionHandle():
    '''returns None\n\n
    setConnectionHandle(final Object connectionHandle)\n
    '''
def ():
    '''returns ConnectionEvent\n\n
    (final ManagedConnection source, final int eid)\n
    (final ManagedConnection source, final int eid, final Exception exception)\n
    '''
