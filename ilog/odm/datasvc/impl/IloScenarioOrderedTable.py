COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
DELETED_COLUMN_NAME = "String  \"__DELETED\""
TCN_COLUMN_NAME = "String  \"__TCN\""
EOV_COLUMN_NAME = "String  \"__EOV\""
def ():
    '''returns IloScenarioOrderedTable\n\n
    (final IloScenarioTableContainer container, final IloSchemaImpl schema)\n
    '''
def getScenarioId():
    '''returns Long\n\n
    getScenarioId()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
def addRowAtIndex():
    '''returns None\n\n
    addRowAtIndex(final int index, final IloRow row)\n
    '''
def getOrderedRows():
    '''returns List<IloRow>\n\n
    getOrderedRows()\n
    '''
def removeRowAtIndex():
    '''returns None\n\n
    removeRowAtIndex(final int index)\n
    '''
def addRow():
    '''returns None\n\n
    addRow(final IloRow row)\n
    '''
def getDifferenceWith():
    '''returns Collection<IloRowDifference>\n\n
    getDifferenceWith(final IloTable table)\n
    '''
def incContentReference():
    '''returns None\n\n
    incContentReference()\n
    '''
def decContentReference():
    '''returns None\n\n
    decContentReference()\n
    '''
def getRows():
    '''returns Collection<IloRow>\n\n
    getRows()\n
    '''
def isContentLoaded():
    '''returns boolean\n\n
    isContentLoaded()\n
    '''
def isContentUnloadable():
    '''returns boolean\n\n
    isContentUnloadable()\n
    '''
def isInSync():
    '''returns boolean\n\n
    isInSync()\n
    '''
def isKeyIndexValid():
    '''returns boolean\n\n
    isKeyIndexValid()\n
    '''
def isModified():
    '''returns boolean\n\n
    isModified()\n
    '''
def removeAllRows():
    '''returns None\n\n
    removeAllRows()\n
    '''
def removeRow():
    '''returns None\n\n
    removeRow(final IloRow row)\n
    '''
def removeRowById():
    '''returns None\n\n
    removeRowById(final Long row_id)\n
    '''
def removeRowByKey():
    '''returns None\n\n
    removeRowByKey(final IloRowKey key)\n
    '''
def removeRows():
    '''returns None\n\n
    removeRows(final Set<IloRow> rows)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def beginModifications():
    '''returns None\n\n
    beginModifications(final boolean storeEvents)\n
    '''
def endModifications():
    '''returns None\n\n
    endModifications()\n
    '''
def getDataTableId():
    '''returns Long\n\n
    getDataTableId()\n
    '''
def getDataTableTcn():
    '''returns Long\n\n
    getDataTableTcn()\n
    '''
def updateConflicts():
    '''returns None\n\n
    updateConflicts(final Collection<IloRowConcurrentChangeConflict> conflicts, final IloRowConcurrentChangeConflict.Resolution resolution)\n
    '''
def getLastModificationDate():
    '''returns Date\n\n
    getLastModificationDate()\n
    '''
def getLastModifier():
    '''returns IloUser\n\n
    getLastModifier()\n
    '''
def getLastModificationDateFromLastSync():
    '''returns Date\n\n
    getLastModificationDateFromLastSync()\n
    '''
def setLinkedList():
    '''returns None\n\n
    setLinkedList()\n
    '''
def resetLinkedList():
    '''returns None\n\n
    resetLinkedList()\n
    '''
def isMaterialized():
    '''returns boolean\n\n
    isMaterialized()\n
    '''
def setSessionAttachedMap():
    '''returns None\n\n
    setSessionAttachedMap(final Map<Long, IloPersistentRow> map)\n
    '''
