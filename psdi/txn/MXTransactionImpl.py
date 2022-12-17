def ():
    '''returns TransactableInfo\n\n
    (final Object id)\n
    (final Object t)\n
    (final Object t, final long s)\n
    '''
def getID():
    '''returns Object\n\n
    getID()\n
    '''
def add():
    '''returns None\n\n
    add(final Transactable txn)\n
    add(final Transactable txn, final long status)\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def commit():
    '''returns None\n\n
    commit()\n
    '''
def rollback():
    '''returns None\n\n
    rollback()\n
    '''
def validate():
    '''returns None\n\n
    validate()\n
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
def put():
    '''returns None\n\n
    put(final String keyString, final boolean value)\n
    put(final String keyString, final String value)\n
    '''
def getBoolean():
    '''returns boolean\n\n
    getBoolean(final String keyString)\n
    '''
def getInt():
    '''returns int\n\n
    getInt(final String keyString)\n
    '''
def getString():
    '''returns String\n\n
    getString(final String keyString)\n
    '''
def remove():
    '''returns boolean\n\n
    remove(final Transactable t)\n
    '''
def getTransactionStatus():
    '''returns long\n\n
    getTransactionStatus(final Transactable t)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def indexOf():
    '''returns int\n\n
    indexOf(final Transactable t)\n
    '''
def setIndexOf():
    '''returns None\n\n
    setIndexOf(final Transactable tsb, final int order)\n
    '''
def getSize():
    '''returns int\n\n
    getSize()\n
    '''
def setEventFired():
    '''returns None\n\n
    setEventFired(final boolean flag)\n
    '''
def setTxnPropertyMap():
    '''returns None\n\n
    setTxnPropertyMap(final Transactable t, final Map<Object, Object> map)\n
    '''
def clearTxnPropertyMap():
    '''returns None\n\n
    clearTxnPropertyMap()\n
    '''
def setPropertyMap():
    '''returns None\n\n
    setPropertyMap(final Map<Object, Object> map)\n
    '''
def clearPropertyMap():
    '''returns None\n\n
    clearPropertyMap()\n
    '''
