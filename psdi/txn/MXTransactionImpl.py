def MXTransactionImpl():
'''public MXTransactionImpl(final Object id)
'''
pass
def getID():
'''public Object getID()
'''
pass
def add():
'''public void add(final Transactable txn)
public void add(final Transactable txn, final long status)
'''
pass
def save():
'''public void save()
'''
pass
def commit():
'''public void commit()
'''
pass
def rollback():
'''public void rollback()
'''
pass
def validate():
'''public void validate()
'''
pass
def saveTransaction():
'''public void saveTransaction(final MXTransaction txn)
'''
pass
def commitTransaction():
'''public void commitTransaction(final MXTransaction txn)
'''
pass
def rollbackTransaction():
'''public void rollbackTransaction(final MXTransaction txn)
'''
pass
def undoTransaction():
'''public void undoTransaction(final MXTransaction txn)
'''
pass
def validateTransaction():
'''public boolean validateTransaction(final MXTransaction txn)
'''
pass
def fireEventsBeforeDB():
'''public void fireEventsBeforeDB(final MXTransaction txn)
'''
pass
def fireEventsAfterDB():
'''public void fireEventsAfterDB(final MXTransaction txn)
'''
pass
def fireEventsAfterDBCommit():
'''public void fireEventsAfterDBCommit(final MXTransaction txn)
'''
pass
def put():
'''public void put(final String keyString, final boolean value)
public void put(final String keyString, final String value)
'''
pass
def getBoolean():
'''public boolean getBoolean(final String keyString)
'''
pass
def getInt():
'''public int getInt(final String keyString)
'''
pass
def getString():
'''public String getString(final String keyString)
'''
pass
def remove():
'''public boolean remove(final Transactable t)
'''
pass
def getTransactionStatus():
'''public long getTransactionStatus(final Transactable t)
'''
pass
def clear():
'''public void clear()
'''
pass
def indexOf():
'''public int indexOf(final Transactable t)
'''
pass
def setIndexOf():
'''public void setIndexOf(final Transactable tsb, final int order)
'''
pass
def getSize():
'''public int getSize()
'''
pass
def setEventFired():
'''public void setEventFired(final boolean flag)
'''
pass
def getTxnPropertyMap():
'''public Map<Object, Object> getTxnPropertyMap(final Transactable t)
'''
pass
def setTxnPropertyMap():
'''public void setTxnPropertyMap(final Transactable t, final Map<Object, Object> map)
'''
pass
def clearTxnPropertyMap():
'''public void clearTxnPropertyMap()
'''
pass
def TransactableInfo():
'''public TransactableInfo(final Object t)
public TransactableInfo(final Object t, final long s)
'''
pass
def getPropertyMap():
'''public Map<Object, Object> getPropertyMap()
'''
pass
def setPropertyMap():
'''public void setPropertyMap(final Map<Object, Object> map)
'''
pass
def clearPropertyMap():
'''public void clearPropertyMap()
'''
pass
