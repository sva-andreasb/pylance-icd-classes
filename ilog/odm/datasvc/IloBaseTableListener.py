COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloBaseTableListener\n\n
    ()\n
    '''
def notifyRowAdded():
    '''returns None\n\n
    notifyRowAdded(final IloRowAddedEvent evt)\n
    '''
def notifyRowDeleted():
    '''returns None\n\n
    notifyRowDeleted(final IloRowDeletedEvent evt)\n
    '''
def notifyRowChanged():
    '''returns None\n\n
    notifyRowChanged(final IloRowChangedEvent evt)\n
    '''
def notifyContentChanged():
    '''returns None\n\n
    notifyContentChanged(final IloTableEvent evt)\n
    '''
def notifyStateChanged():
    '''returns None\n\n
    notifyStateChanged(final IloTableEvent evt)\n
    '''
def notifyContentLoaded():
    '''returns None\n\n
    notifyContentLoaded(final IloTableEvent evt)\n
    '''
def setMultiEventsThreshold():
    '''returns None\n\n
    setMultiEventsThreshold(final int nbEvents)\n
    '''
def getMultiEventsThreshold():
    '''returns int\n\n
    getMultiEventsThreshold()\n
    '''
def notifyChanges():
    '''returns None\n\n
    notifyChanges(final List<IloTableEvent> events)\n
    '''
