def LSNRActionHelper():
    '''public LSNRActionHelper()
    '''
def requiredFieldsExist():
    '''public boolean requiredFieldsExist(final MboRemote actionObject, final long uniqueId)
    '''
def createCommLog():
    '''public void createCommLog(final MboRemote inboundComm, final MboRemote actionObject)
    '''
def createDocLinkForCommLog():
    '''public void createDocLinkForCommLog(final MboRemote inboundComm, final MboRemote commlog)
    '''
def updateDoclinkForActionObject():
    '''public void updateDoclinkForActionObject(final MboRemote inboundComm, final MboRemote actionObject)
    '''
def updateStatusAndSendMail():
    '''public void updateStatusAndSendMail(MboRemote inboundComm, final String status, final String msgStr, final String templateName)
    '''
def convertToDate():
    '''public Date convertToDate(final int type, final String value, final UserInfo u)
    '''
def createObject():
    '''public MboRemote createObject(InboundCommRemote inboundComm, final MboRemote objectRemote)
    '''
def updateObject():
    '''public MboRemote updateObject(InboundCommRemote inboundComm, final MboRemote objectRemote)
    '''
def performSecuityCheck():
    '''public boolean performSecuityCheck(final InboundCommRemote inboundComm, final MboRemote objectMbo)
    '''
def authExistForObjectAndAction():
    '''public boolean authExistForObjectAndAction(final InboundCommRemote inboundComm, final MboRemote objectRemote, final String action, final String objectName)
    '''
def setExtraAttrValuesForInsert():
    '''public void setExtraAttrValuesForInsert(final HashMap<String, String> map)
    '''
def setExtraAttrValuesForUpdate():
    '''public void setExtraAttrValuesForUpdate(final HashMap<String, String> map)
    '''
def updateInbCommAfterAction():
    '''public void updateInbCommAfterAction(final InboundCommRemote inboundComm, final MboRemote objectRemote)
    '''
def handleException():
    '''public void handleException(final String objectName, final Exception ee, final MboRemote inboundComm, final String action)
    '''
