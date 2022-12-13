def sendSTReplyMailVerySmall():
    '''    public void sendSTReplyMailVerySmall(final MboRemote inboundComm, final MboRemote commTemplate, final MboRemote targetMbo, final MboRemote trackEntry, final UserInfo ui, final String valueList, final int deviceClass)
    '''
def sendWFNotifyMail():
    '''    public void sendWFNotifyMail(final MboRemote track, final MboRemote tempTargetMbo, final MfMailWFCtrlInfo wc)
    '''
def sendErrorMail():
    '''    public void sendErrorMail(final MboRemote inboundComm, final String template)
    '''
def getCommTemplate():
    '''    public static MboRemote getCommTemplate(final String templateId, final UserInfo ui)
    '''
def logMailInfo():
    '''    public void logMailInfo(final MboRemote inboundComm)
    public static void logMailInfo(final MXLogger pLogger, final MboRemote inboundComm)
    '''
def sendErrorMailToAdmin():
    '''    public void sendErrorMailToAdmin(final String errMsg, final String template)
    '''
def createInboundCommLog():
    '''    public void createInboundCommLog(final MboRemote inboundComm, final MboRemote targetMbo, final Date cDate)
    '''
def isKeyAttribute():
    '''    public boolean isKeyAttribute(final String[] keys, final String attribute)
    '''
def getHashSet():
    '''    public HashSet<String> getHashSet(final String commaSeparatedList)
    '''
def getSenderFromTemplate():
    '''    public String getSenderFromTemplate(final MboRemote commTemplate)
    '''
def getLogger():
    '''    public MXLogger getLogger()
    '''
def setLogger():
    '''    public void setLogger(final MXLogger logger)
    '''
def isMailHTML():
    '''    public boolean isMailHTML()
    '''
def checkAppAuth():
    '''    public boolean checkAppAuth(final InboundCommRemote inboundComm, final MboRemote targetMbo)
    '''
def checkStatusAuth():
    '''    public boolean checkStatusAuth(final InboundCommRemote inboundComm, final MboRemote targetMbo, final UserInfo ui)
    '''
