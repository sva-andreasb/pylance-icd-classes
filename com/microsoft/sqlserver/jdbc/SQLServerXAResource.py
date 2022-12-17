SSTRANSTIGHTLYCPLD = "int  32768"
def toString():
    '''returns String\n\n
    toString()\n
    '''
def start():
    '''returns None\n\n
    start(final Xid xid, final int flags)\n
    '''
def end():
    '''returns None\n\n
    end(final Xid xid, final int flags)\n
    '''
def prepare():
    '''returns int\n\n
    prepare(final Xid xid)\n
    '''
def commit():
    '''returns None\n\n
    commit(final Xid xid, final boolean onePhase)\n
    '''
def rollback():
    '''returns None\n\n
    rollback(final Xid xid)\n
    '''
def forget():
    '''returns None\n\n
    forget(final Xid xid)\n
    '''
def recover():
    '''returns Xid[]\n\n
    recover(final int flags)\n
    '''
def isSameRM():
    '''returns boolean\n\n
    isSameRM(final XAResource xares)\n
    '''
def setTransactionTimeout():
    '''returns boolean\n\n
    setTransactionTimeout(final int seconds)\n
    '''
def getTransactionTimeout():
    '''returns int\n\n
    getTransactionTimeout()\n
    '''
