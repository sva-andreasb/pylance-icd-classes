def MXTransactionImpl():
    '''public MXTransactionImpl(final Object id)
    '''
def getID():
    '''public Object getID()
    '''
def add():
    '''public void add(final Transactable txn)
    public void add(final Transactable txn, final long status)
    '''
def save():
    '''public void save()
    '''
def commit():
    '''public void commit()
    '''
def rollback():
    '''public void rollback()
    '''
def validate():
    '''public void validate()
    '''
def saveTransaction():
    '''public void saveTransaction(final MXTransaction txn)
    '''
def commitTransaction():
    '''public void commitTransaction(final MXTransaction txn)
    '''
def rollbackTransaction():
    '''public void rollbackTransaction(final MXTransaction txn)
    '''
def undoTransaction():
    '''public void undoTransaction(final MXTransaction txn)
    '''
def validateTransaction():
    '''public boolean validateTransaction(final MXTransaction txn)
    '''
def fireEventsBeforeDB():
    '''public void fireEventsBeforeDB(final MXTransaction txn)
    '''
def fireEventsAfterDB():
    '''public void fireEventsAfterDB(final MXTransaction txn)
    '''
def fireEventsAfterDBCommit():
    '''public void fireEventsAfterDBCommit(final MXTransaction txn)
    '''
def put():
    '''public void put(final String keyString, final boolean value)
    public void put(final String keyString, final String value)
    '''
def getBoolean():
    '''public boolean getBoolean(final String keyString)
    '''
def getInt():
    '''public int getInt(final String keyString)
    '''
def getString():
    '''public String getString(final String keyString)
    '''
def remove():
    '''public boolean remove(final Transactable t)
    '''
def getTransactionStatus():
    '''public long getTransactionStatus(final Transactable t)
    '''
def clear():
    '''public void clear()
    '''
def indexOf():
    '''public int indexOf(final Transactable t)
    '''
def setIndexOf():
    '''public void setIndexOf(final Transactable tsb, final int order)
    '''
def getSize():
    '''public int getSize()
    '''
def setEventFired():
    '''public void setEventFired(final boolean flag)
    '''
def getTxnPropertyMap():
    '''public Map<Object, Object> getTxnPropertyMap(final Transactable t)
    '''
def setTxnPropertyMap():
    '''public void setTxnPropertyMap(final Transactable t, final Map<Object, Object> map)
    '''
def clearTxnPropertyMap():
    '''public void clearTxnPropertyMap()
    '''
def TransactableInfo():
    '''public TransactableInfo(final Object t)
    public TransactableInfo(final Object t, final long s)
    '''
def getPropertyMap():
    '''public Map<Object, Object> getPropertyMap()
    '''
def setPropertyMap():
    '''public void setPropertyMap(final Map<Object, Object> map)
    '''
def clearPropertyMap():
    '''public void clearPropertyMap()
    '''
