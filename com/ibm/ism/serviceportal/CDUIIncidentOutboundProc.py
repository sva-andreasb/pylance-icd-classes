FILTERDOMAIN = "String  \"SSC_INCLIST\""
OBJECTNAME = "String  \"INCIDENT\""
def CDUIIncidentOutboundProc():
    '''public CDUIIncidentOutboundProc()
    '''
def search():
    '''public void search(final MboSetRemote mboSet, final String createdby, final String reportedby, final String affectedperson, final String text)
    '''
def searchByClass():
    '''public void searchByClass(final MboSetRemote mboSet, final String tkclass, final String createdby, final String reportedby, final String affectedperson, final String text)
    '''
def searchByStatus():
    '''public void searchByStatus(final MboSetRemote mboSet, final String srstatus, final String prstatus, final String incstatus, final String createdby, final String reportedby, final String affectedperson, final String text)
    '''
def searchNotStatus():
    '''public void searchNotStatus(final MboSetRemote mboSet, final String srstatus, final String prstatus, final String incstatus, final String createdby, final String reportedby, final String affectedperson, final String text)
    '''
def searchNotStatusSP():
    '''public void searchNotStatusSP(final MboSetRemote mboSet, final String srstatus, final String prstatus, final String incstatus, final String createdby, final String reportedby, final String affectedperson, final String text, final boolean isAppendRelatedIncident)
    '''
def searchRelatedIncident():
    '''public void searchRelatedIncident(final MboSetRemote mboSet, final String srstatus, final String createdby, final String reportedby, final String affectedperson, final String text, final boolean isSRAndRelInc)
    '''
def checkBusinessRules():
    '''public int checkBusinessRules(final MboRemote mbo, final MosDetailInfo mosDetInfo, final Map<String, Object> ovrdColValueMap)
    '''
