COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def getLastModificationTimestamp():
    '''returns long\n\n
    getLastModificationTimestamp()\n
    '''
def ():
    '''returns IloDomDeleteNullifyTransaction\n\n
    (final String modelid)\n
    (final String modelid, final IloDomFactory factory)\n
    ()\n
    (final TransactionalEditingDomain domain, final List<IloDomTrigger> triggers, final Command derived)\n
    (final Class<? extends IloDomObject> entity)\n
    '''
def enableTransactionManagement():
    '''returns None\n\n
    enableTransactionManagement()\n
    '''
def disableTransactionManagement():
    '''returns None\n\n
    disableTransactionManagement()\n
    '''
def isTransactionManagementEnabled():
    '''returns boolean\n\n
    isTransactionManagementEnabled()\n
    '''
def addTransactionListener():
    '''returns None\n\n
    addTransactionListener(final IloDomTransactionListener listener)\n
    '''
def removeTransactionListener():
    '''returns None\n\n
    removeTransactionListener(final IloDomTransactionListener listener)\n
    '''
def addTriggerListener():
    '''returns None\n\n
    addTriggerListener(final IloDomTriggerListener listener)\n
    '''
def removeTriggerListener():
    '''returns None\n\n
    removeTriggerListener(final IloDomTriggerListener listener)\n
    '''
def execute():
    '''returns None\n\n
    execute(final IloDomTransaction job)\n
    execute(final String label, final IloDomTransaction job)\n
    '''
def executeReadOnly():
    '''returns None\n\n
    executeReadOnly(final IloDomTransaction job)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    '''
def canUndo():
    '''returns boolean\n\n
    canUndo()\n
    '''
def canRedo():
    '''returns boolean\n\n
    canRedo()\n
    '''
def undo():
    '''returns None\n\n
    undo()\n
    '''
def redo():
    '''returns None\n\n
    redo()\n
    '''
def getEditingDomain():
    '''returns TransactionalEditingDomainImpl\n\n
    getEditingDomain()\n
    '''
def addRecord():
    '''returns None\n\n
    addRecord(final IloDomRecord record, final int index)\n
    '''
def removeRecord():
    '''returns None\n\n
    removeRecord(final IloDomRecord record)\n
    '''
def updateRecord():
    '''returns None\n\n
    updateRecord(final IloDomRecord record, final int col)\n
    '''
def beforeReload():
    '''returns List<IloDomObject>\n\n
    beforeReload(final IloDomRecordType recordType)\n
    '''
def afterReload():
    '''returns None\n\n
    afterReload(final IloDomRecordType recordType, final List<IloDomObject> previousObjects)\n
    '''
def isSynchronizationTransaction():
    '''returns boolean\n\n
    isSynchronizationTransaction(final Transaction tr)\n
    '''
def addRecordListener():
    '''returns None\n\n
    addRecordListener(final IloDomRecordTransactionListener listener)\n
    '''
def removeRecordListener():
    '''returns None\n\n
    removeRecordListener(final IloDomRecordTransactionListener listener)\n
    '''
def recordBeginModifications():
    '''returns None\n\n
    recordBeginModifications(final String label, final IloDomModelChangeEvent event)\n
    '''
def recordAdded():
    '''returns None\n\n
    recordAdded(final IloDomRecord record, final int index, final IloDomObjectImpl obj)\n
    '''
def recordDeleted():
    '''returns None\n\n
    recordDeleted(final IloDomRecord record, final int index)\n
    '''
def tableDeleted():
    '''returns None\n\n
    tableDeleted(final IloDomRecordType type)\n
    '''
def recordChanged():
    '''returns None\n\n
    recordChanged(final IloDomRecord record, final int col)\n
    '''
def recordEndModifications():
    '''returns None\n\n
    recordEndModifications()\n
    '''
def bulkDeleteEntityObjects():
    '''returns None\n\n
    bulkDeleteEntityObjects(final Class<? extends IloDomObject> entity)\n
    '''
def bulkDeleteEntityObjectsAndReferences():
    '''returns None\n\n
    bulkDeleteEntityObjectsAndReferences(final Class<? extends IloDomObject> entity)\n
    '''
def bulkDeleteAllObjects():
    '''returns None\n\n
    bulkDeleteAllObjects()\n
    '''
def startTransaction():
    '''returns None\n\n
    startTransaction(final String label, final IloDomTransaction job)\n
    '''
def isTransactionStarted():
    '''returns boolean\n\n
    isTransactionStarted()\n
    '''
def appendToTransaction():
    '''returns None\n\n
    appendToTransaction(final IloDomTransaction job)\n
    '''
def commitTransaction():
    '''returns None\n\n
    commitTransaction()\n
    '''
def rollbackTransaction():
    '''returns None\n\n
    rollbackTransaction()\n
    '''
def withTransaction():
    '''returns None\n\n
    withTransaction(final String name, final Closure<Void> c)\n
    '''
def resourceSetChanged():
    '''returns None\n\n
    resourceSetChanged(final ResourceSetChangeEvent event)\n
    '''
def transactionAboutToCommit():
    '''returns Command\n\n
    transactionAboutToCommit(final ResourceSetChangeEvent event)\n
    '''
def canExecute():
    '''returns boolean\n\n
    canExecute()\n
    '''
def getNotifications():
    '''returns List<Notification>\n\n
    getNotifications()\n
    '''
