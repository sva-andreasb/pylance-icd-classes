def ():
    '''returns CMXAResourceImpl\n\n
    (final XAResource XAR, final ConnectO connectO)\n
    '''
def commit():
    '''returns None\n\n
    commit(final Xid xid, final boolean onePhase)\n
    '''
def end():
    '''returns None\n\n
    end(final Xid xid, final int flags)\n
    '''
def forget():
    '''returns None\n\n
    forget(final Xid xid)\n
    '''
def getTransactionTimeout():
    '''returns int\n\n
    getTransactionTimeout()\n
    '''
def isSameRM():
    '''returns boolean\n\n
    isSameRM(final XAResource xares)\n
    '''
def prepare():
    '''returns int\n\n
    prepare(final Xid xid)\n
    '''
def recover():
    '''returns Xid[]\n\n
    recover(final int flag)\n
    '''
def rollback():
    '''returns None\n\n
    rollback(final Xid xid)\n
    '''
def setTransactionTimeout():
    '''returns boolean\n\n
    setTransactionTimeout(final int seconds)\n
    '''
def start():
    '''returns None\n\n
    start(final Xid xid, final int flags)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
