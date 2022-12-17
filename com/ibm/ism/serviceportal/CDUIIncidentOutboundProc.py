FILTERDOMAIN = "String  \"SSC_INCLIST\""
OBJECTNAME = "String  \"INCIDENT\""
def ():
    '''returns CDUIIncidentOutboundProc\n\n
    ()\n
    '''
def search():
    '''returns None\n\n
    search(final MboSetRemote mboSet, final String createdby, final String reportedby, final String affectedperson, final String text)\n
    '''
def searchByClass():
    '''returns None\n\n
    searchByClass(final MboSetRemote mboSet, final String tkclass, final String createdby, final String reportedby, final String affectedperson, final String text)\n
    '''
def searchByStatus():
    '''returns None\n\n
    searchByStatus(final MboSetRemote mboSet, final String srstatus, final String prstatus, final String incstatus, final String createdby, final String reportedby, final String affectedperson, final String text)\n
    '''
def searchNotStatus():
    '''returns None\n\n
    searchNotStatus(final MboSetRemote mboSet, final String srstatus, final String prstatus, final String incstatus, final String createdby, final String reportedby, final String affectedperson, final String text)\n
    '''
def searchNotStatusSP():
    '''returns None\n\n
    searchNotStatusSP(final MboSetRemote mboSet, final String srstatus, final String prstatus, final String incstatus, final String createdby, final String reportedby, final String affectedperson, final String text, final boolean isAppendRelatedIncident)\n
    '''
def searchRelatedIncident():
    '''returns None\n\n
    searchRelatedIncident(final MboSetRemote mboSet, final String srstatus, final String createdby, final String reportedby, final String affectedperson, final String text, final boolean isSRAndRelInc)\n
    '''
def checkBusinessRules():
    '''returns int\n\n
    checkBusinessRules(final MboRemote mbo, final MosDetailInfo mosDetInfo, final Map<String, Object> ovrdColValueMap)\n
    '''
