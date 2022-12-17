def ():
    '''returns MicTransactable\n\n
    ()\n
    '''
def setMboSet():
    '''returns None\n\n
    setMboSet(final MboSetRemote set)\n
    '''
def getMboSet():
    '''returns MboSetRemote\n\n
    getMboSet()\n
    '''
def saveTransaction():
    '''returns None\n\n
    saveTransaction(final MXTransaction txn)\n
    '''
def commitTransaction():
    '''returns None\n\n
    commitTransaction(final MXTransaction txn)\n
    '''
def rollbackTransaction():
    '''returns None\n\n
    rollbackTransaction(final MXTransaction txn)\n
    '''
def undoTransaction():
    '''returns None\n\n
    undoTransaction(final MXTransaction txn)\n
    '''
def validateTransaction():
    '''returns boolean\n\n
    validateTransaction(final MXTransaction txn)\n
    '''
def fireEventsBeforeDB():
    '''returns None\n\n
    fireEventsBeforeDB(final MXTransaction txn)\n
    '''
def fireEventsAfterDB():
    '''returns None\n\n
    fireEventsAfterDB(final MXTransaction txn)\n
    '''
def fireEventsAfterDBCommit():
    '''returns None\n\n
    fireEventsAfterDBCommit(final MXTransaction txn)\n
    '''
