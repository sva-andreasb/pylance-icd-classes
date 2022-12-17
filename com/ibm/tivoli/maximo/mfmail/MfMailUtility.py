def sendSTReplyMailVerySmall():
    '''returns None\n\n
    sendSTReplyMailVerySmall(final MboRemote inboundComm, final MboRemote commTemplate, final MboRemote targetMbo, final MboRemote trackEntry, final UserInfo ui, final String valueList, final int deviceClass)\n
    '''
def sendWFNotifyMail():
    '''returns None\n\n
    sendWFNotifyMail(final MboRemote track, final MboRemote tempTargetMbo, final MfMailWFCtrlInfo wc)\n
    '''
def sendErrorMail():
    '''returns None\n\n
    sendErrorMail(final MboRemote inboundComm, final String template)\n
    '''
def logMailInfo():
    '''returns None\n\n
    logMailInfo(final MboRemote inboundComm)\n
    '''
def sendErrorMailToAdmin():
    '''returns None\n\n
    sendErrorMailToAdmin(final String errMsg, final String template)\n
    '''
def createInboundCommLog():
    '''returns None\n\n
    createInboundCommLog(final MboRemote inboundComm, final MboRemote targetMbo, final Date cDate)\n
    '''
def isKeyAttribute():
    '''returns boolean\n\n
    isKeyAttribute(final String[] keys, final String attribute)\n
    '''
def getHashSet():
    '''returns HashSet<String>\n\n
    getHashSet(final String commaSeparatedList)\n
    '''
def getSenderFromTemplate():
    '''returns String\n\n
    getSenderFromTemplate(final MboRemote commTemplate)\n
    '''
def getLogger():
    '''returns MXLogger\n\n
    getLogger()\n
    '''
def setLogger():
    '''returns None\n\n
    setLogger(final MXLogger logger)\n
    '''
def isMailHTML():
    '''returns boolean\n\n
    isMailHTML()\n
    '''
def checkAppAuth():
    '''returns boolean\n\n
    checkAppAuth(final InboundCommRemote inboundComm, final MboRemote targetMbo)\n
    '''
def checkStatusAuth():
    '''returns boolean\n\n
    checkStatusAuth(final InboundCommRemote inboundComm, final MboRemote targetMbo, final UserInfo ui)\n
    '''
