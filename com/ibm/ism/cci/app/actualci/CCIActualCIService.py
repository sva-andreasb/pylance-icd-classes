FETCHLIMIT = "String  \"mxe.db.fetchResultStopLimit\""
ITIC_NOT_COMPLETE = "String  \"NO\""
ITIC_COMPLETE = "String  \"YES\""
ITIC_COMPLETE_VARNAME = "String  \"CCIITICCOMPLETE\""
def ():
    '''returns CCIActualCIService\n\n
    ()\n
    (final MXServer mxServer)\n
    '''
def deleteActualCIs():
    '''returns None\n\n
    deleteActualCIs(final MboRemote mbo)\n
    '''
def updateDeletedActCI():
    '''returns None\n\n
    updateDeletedActCI(final CCIDeletedActualCIRemote deletedActCI, final MboRemote actci, final Date systemDate)\n
    '''
def getActualCIsToDelete():
    '''returns CCIDeletedActualCISet\n\n
    getActualCIsToDelete(final MboRemote mbo)\n
    '''
def setITICAsNotComplete():
    '''returns None\n\n
    setITICAsNotComplete(final MboRemote mbo)\n
    '''
def setITICAsComplete():
    '''returns None\n\n
    setITICAsComplete(final MboRemote mbo)\n
    '''
def getITICCompleteValue():
    '''returns String\n\n
    getITICCompleteValue(final MboRemote mbo)\n
    '''
def addCustomerAssociations():
    '''returns String\n\n
    addCustomerAssociations(final MboSetRemote actCISet, final String primaryCustomer, final ArrayList<String> customers, final boolean continueOnError)\n
    addCustomerAssociations(final MboRemote actCI, final String primaryCustomer, final ArrayList<String> customers, final boolean continueOnError)\n
    '''
