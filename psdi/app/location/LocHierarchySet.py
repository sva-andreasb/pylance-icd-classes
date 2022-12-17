def ():
    '''returns LocHierarchySet\n\n
    (final MboServerInterface ms)\n
    '''
def isChildOfThisLocHierarchyProcessedForDeletion():
    '''returns boolean\n\n
    isChildOfThisLocHierarchyProcessedForDeletion(final String lochierarchyid)\n
    '''
def isLocAncestorAlreadyMarkedForDeletion():
    '''returns boolean\n\n
    isLocAncestorAlreadyMarkedForDeletion(final String locancestorid)\n
    '''
def getDeletionsProcessed():
    '''returns Vector<String>\n\n
    getDeletionsProcessed()\n
    '''
def getDeletedLocAncestors():
    '''returns Vector<String>\n\n
    getDeletedLocAncestors()\n
    '''
def setDeletionsProcessed():
    '''returns None\n\n
    setDeletionsProcessed(final Vector<String> deletionsProcessed)\n
    '''
def setDeletedLocAncestors():
    '''returns None\n\n
    setDeletedLocAncestors(final Vector<String> deletedLocAncestors)\n
    '''
def recordChildrenOfThisLocHierarchyProcessedForDeletion():
    '''returns None\n\n
    recordChildrenOfThisLocHierarchyProcessedForDeletion(final String lochierarchyid)\n
    '''
def recordLocAncestorAsMarkedForDeletion():
    '''returns None\n\n
    recordLocAncestorAsMarkedForDeletion(final String locancestorid)\n
    '''
def recordNewTopLevelLocHierForNetworkedLocHier():
    '''returns None\n\n
    recordNewTopLevelLocHierForNetworkedLocHier(final String newTopLevelLocHier)\n
    '''
def isTopLevelForNetworkedLocHierAdded():
    '''returns boolean\n\n
    isTopLevelForNetworkedLocHierAdded(final String newTopLevelLocHier)\n
    '''
def canAdd():
    '''returns None\n\n
    canAdd()\n
    '''
def isLocLocAncCreated():
    '''returns boolean\n\n
    isLocLocAncCreated()\n
    '''
def setLocLocAncCreated():
    '''returns None\n\n
    setLocLocAncCreated(final boolean locLocAncCreated)\n
    '''
def save():
    '''returns None\n\n
    save(final long flags)\n
    '''
def saveTransaction():
    '''returns None\n\n
    saveTransaction(final MXTransaction txn)\n
    '''
