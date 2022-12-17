def ():
    '''returns LSNRActionHelper\n\n
    ()\n
    '''
def requiredFieldsExist():
    '''returns boolean\n\n
    requiredFieldsExist(final MboRemote actionObject, final long uniqueId)\n
    '''
def createCommLog():
    '''returns None\n\n
    createCommLog(final MboRemote inboundComm, final MboRemote actionObject)\n
    '''
def createDocLinkForCommLog():
    '''returns None\n\n
    createDocLinkForCommLog(final MboRemote inboundComm, final MboRemote commlog)\n
    '''
def updateDoclinkForActionObject():
    '''returns None\n\n
    updateDoclinkForActionObject(final MboRemote inboundComm, final MboRemote actionObject)\n
    '''
def updateStatusAndSendMail():
    '''returns None\n\n
    updateStatusAndSendMail(MboRemote inboundComm, final String status, final String msgStr, final String templateName)\n
    '''
def convertToDate():
    '''returns Date\n\n
    convertToDate(final int type, final String value, final UserInfo u)\n
    '''
def createObject():
    '''returns MboRemote\n\n
    createObject(InboundCommRemote inboundComm, final MboRemote objectRemote)\n
    '''
def updateObject():
    '''returns MboRemote\n\n
    updateObject(InboundCommRemote inboundComm, final MboRemote objectRemote)\n
    '''
def performSecuityCheck():
    '''returns boolean\n\n
    performSecuityCheck(final InboundCommRemote inboundComm, final MboRemote objectMbo)\n
    '''
def authExistForObjectAndAction():
    '''returns boolean\n\n
    authExistForObjectAndAction(final InboundCommRemote inboundComm, final MboRemote objectRemote, final String action, final String objectName)\n
    '''
def setExtraAttrValuesForInsert():
    '''returns None\n\n
    setExtraAttrValuesForInsert(final HashMap<String, String> map)\n
    '''
def setExtraAttrValuesForUpdate():
    '''returns None\n\n
    setExtraAttrValuesForUpdate(final HashMap<String, String> map)\n
    '''
def updateInbCommAfterAction():
    '''returns None\n\n
    updateInbCommAfterAction(final InboundCommRemote inboundComm, final MboRemote objectRemote)\n
    '''
def handleException():
    '''returns None\n\n
    handleException(final String objectName, final Exception ee, final MboRemote inboundComm, final String action)\n
    '''
