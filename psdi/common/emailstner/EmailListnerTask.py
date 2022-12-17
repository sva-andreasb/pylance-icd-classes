def ():
    '''returns EmailListnerTask\n\n
    ()\n
    '''
def performTask():
    '''returns None\n\n
    performTask(final String taskName, final String instanceName)\n
    '''
def setLogger():
    '''returns None\n\n
    setLogger(final MXLogger logger)\n
    '''
def getRunAsUserInfo():
    '''returns UserInfo\n\n
    getRunAsUserInfo()\n
    '''
def setRunAsUserInfo():
    '''returns None\n\n
    setRunAsUserInfo(final UserInfo userInfo)\n
    '''
def readMessagesFromMailServer():
    '''returns None\n\n
    readMessagesFromMailServer(final InboundCommCfgData cfgData, final MboRemote inboundCommCfgMbo)\n
    '''
def processNEWStatusFromInboundComm():
    '''returns None\n\n
    processNEWStatusFromInboundComm(final MboRemote inboundCommCfgMbo)\n
    '''
def processNewStatusMail():
    '''returns MboRemote\n\n
    processNewStatusMail(MboRemote inboundComm)\n
    '''
def getAppFromInbCommSecurity():
    '''returns String\n\n
    getAppFromInbCommSecurity(final MboRemote inboundComm, final String objectName)\n
    '''
def appExistForSecurityCheck():
    '''returns None\n\n
    appExistForSecurityCheck(MboRemote inboundComm, final int formatMode)\n
    '''
def getAppFromMaxApps():
    '''returns String\n\n
    getAppFromMaxApps(final String objectName)\n
    '''
def parseFormattedMessage():
    '''returns None\n\n
    parseFormattedMessage(final MboRemote inboundComm, final LSNRParser parser, final int mode)\n
    '''
def processMailForFreeformMode():
    '''returns MboRemote\n\n
    processMailForFreeformMode(final MboRemote inboundComm)\n
    '''
def getObjectActionForFormattedMode():
    '''returns MboRemote\n\n
    getObjectActionForFormattedMode(MboRemote inboundComm, final LSNRParser parser, final int mode)\n
    '''
def getMultipartPart():
    '''returns MailData\n\n
    getMultipartPart(final MimeMultipart mp, final MailData md, final Vector<Object> vector)\n
    '''
def getTextPart():
    '''returns String\n\n
    getTextPart(final MimeBodyPart mbp, String text)\n
    '''
def writeIntoInboundComm():
    '''returns MboRemote\n\n
    writeIntoInboundComm(final MailData md, final InboundCommCfgData cfgData, final MboRemote inboundCommCfgMbo)\n
    writeIntoInboundComm(final MailData md, final InboundCommCfgData cfgData, final MboRemote inboundCommCfgMbo, final Message m)\n
    '''
def writeToDocInfoAndDocLinks():
    '''returns None\n\n
    writeToDocInfoAndDocLinks(final MailData md, final String inbCommUser, final MboRemote inboundComm, final String attFileName, final String doclinkName, final boolean msgFirstLevel, final int msgLevel)\n
    '''
def isNewMail():
    '''returns boolean\n\n
    isNewMail(final String mailId, final String emailAddress, final UserInfo ui)\n
    isNewMail(final String mailId, final String emailAddress)\n
    isNewMail(final String mailId)\n
    '''
def deleteMailAfterAgeThreshold():
    '''returns None\n\n
    deleteMailAfterAgeThreshold(final Message m, final int age, final String ageUOM, final String emailAddress)\n
    '''
