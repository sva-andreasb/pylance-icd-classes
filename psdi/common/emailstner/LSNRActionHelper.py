def LSNRActionHelper():
'''public LSNRActionHelper()
'''
pass
def requiredFieldsExist():
'''public boolean requiredFieldsExist(final MboRemote actionObject, final long uniqueId)
'''
pass
def createCommLog():
'''public void createCommLog(final MboRemote inboundComm, final MboRemote actionObject)
'''
pass
def createDocLinkForCommLog():
'''public void createDocLinkForCommLog(final MboRemote inboundComm, final MboRemote commlog)
'''
pass
def updateDoclinkForActionObject():
'''public void updateDoclinkForActionObject(final MboRemote inboundComm, final MboRemote actionObject)
'''
pass
def updateStatusAndSendMail():
'''public void updateStatusAndSendMail(MboRemote inboundComm, final String status, final String msgStr, final String templateName)
'''
pass
def convertToDate():
'''public Date convertToDate(final int type, final String value, final UserInfo u)
'''
pass
def createObject():
'''public MboRemote createObject(InboundCommRemote inboundComm, final MboRemote objectRemote)
'''
pass
def updateObject():
'''public MboRemote updateObject(InboundCommRemote inboundComm, final MboRemote objectRemote)
'''
pass
def performSecuityCheck():
'''public boolean performSecuityCheck(final InboundCommRemote inboundComm, final MboRemote objectMbo)
'''
pass
def authExistForObjectAndAction():
'''public boolean authExistForObjectAndAction(final InboundCommRemote inboundComm, final MboRemote objectRemote, final String action, final String objectName)
'''
pass
def setExtraAttrValuesForInsert():
'''public void setExtraAttrValuesForInsert(final HashMap<String, String> map)
'''
pass
def setExtraAttrValuesForUpdate():
'''public void setExtraAttrValuesForUpdate(final HashMap<String, String> map)
'''
pass
def updateInbCommAfterAction():
'''public void updateInbCommAfterAction(final InboundCommRemote inboundComm, final MboRemote objectRemote)
'''
pass
def handleException():
'''public void handleException(final String objectName, final Exception ee, final MboRemote inboundComm, final String action)
'''
pass
