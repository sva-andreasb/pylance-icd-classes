FETCHLIMIT = "String  \"mxe.db.fetchResultStopLimit\""
ITIC_NOT_COMPLETE = "String  \"NO\""
ITIC_COMPLETE = "String  \"YES\""
ITIC_COMPLETE_VARNAME = "String  \"CCIITICCOMPLETE\""
def CCIActualCIService():
    '''public CCIActualCIService()
    public CCIActualCIService(final MXServer mxServer)
    '''
def deleteActualCIs():
    '''public void deleteActualCIs(final MboRemote mbo)
    '''
def updateDeletedActCI():
    '''public void updateDeletedActCI(final CCIDeletedActualCIRemote deletedActCI, final MboRemote actci, final Date systemDate)
    '''
def getActualCIsToDelete():
    '''public CCIDeletedActualCISet getActualCIsToDelete(final MboRemote mbo)
    '''
def setITICAsNotComplete():
    '''public void setITICAsNotComplete(final MboRemote mbo)
    '''
def setITICAsComplete():
    '''public void setITICAsComplete(final MboRemote mbo)
    '''
def getITICCompleteValue():
    '''public String getITICCompleteValue(final MboRemote mbo)
    '''
def addCustomerAssociations():
    '''public ArrayList<String> addCustomerAssociations(final MboSetRemote actCISet, final String primaryCustomer, final ArrayList<String> customers, final boolean continueOnError)
    public String addCustomerAssociations(final MboRemote actCI, final String primaryCustomer, final ArrayList<String> customers, final boolean continueOnError)
    '''
