def EmailListnerTask():
    '''    public EmailListnerTask()
    '''
def performTask():
    '''    public void performTask(final String taskName, final String instanceName)
    '''
def getLogger():
    '''    public static MXLogger getLogger()
    '''
def setLogger():
    '''    public void setLogger(final MXLogger logger)
    '''
def getRunAsUserInfo():
    '''    public UserInfo getRunAsUserInfo()
    '''
def setRunAsUserInfo():
    '''    public void setRunAsUserInfo(final UserInfo userInfo)
    '''
def readMessagesFromMailServer():
    '''    public void readMessagesFromMailServer(final InboundCommCfgData cfgData, final MboRemote inboundCommCfgMbo)
    '''
def processNEWStatusFromInboundComm():
    '''    public void processNEWStatusFromInboundComm(final MboRemote inboundCommCfgMbo)
    '''
def processNewStatusMail():
    '''    public MboRemote processNewStatusMail(MboRemote inboundComm)
    '''
def getAppFromInbCommSecurity():
    '''    public String getAppFromInbCommSecurity(final MboRemote inboundComm, final String objectName)
    '''
def appExistForSecurityCheck():
    '''    public void appExistForSecurityCheck(MboRemote inboundComm, final int formatMode)
    '''
def getAppFromMaxApps():
    '''    public String getAppFromMaxApps(final String objectName)
    '''
def parseFormattedMessage():
    '''    public void parseFormattedMessage(final MboRemote inboundComm, final LSNRParser parser, final int mode)
    '''
def processMailForFreeformMode():
    '''    public MboRemote processMailForFreeformMode(final MboRemote inboundComm)
    '''
def getObjectActionForFormattedMode():
    '''    public MboRemote getObjectActionForFormattedMode(MboRemote inboundComm, final LSNRParser parser, final int mode)
    '''
def getMultipartPart():
    '''    public MailData getMultipartPart(final MimeMultipart mp, final MailData md, final Vector<Object> vector)
    '''
def getTextPart():
    '''    public String getTextPart(final MimeBodyPart mbp, String text)
    '''
def writeIntoInboundComm():
    '''    public MboRemote writeIntoInboundComm(final MailData md, final InboundCommCfgData cfgData, final MboRemote inboundCommCfgMbo)
    public MboRemote writeIntoInboundComm(final MailData md, final InboundCommCfgData cfgData, final MboRemote inboundCommCfgMbo, final Message m)
    '''
def writeToDocInfoAndDocLinks():
    '''    public void writeToDocInfoAndDocLinks(final MailData md, final String inbCommUser, final MboRemote inboundComm, final String attFileName, final String doclinkName, final boolean msgFirstLevel, final int msgLevel)
    '''
def getContentTypeFrom():
    '''    public static String getContentTypeFrom(final String fileName)
    '''
def isNewMail():
    '''    public boolean isNewMail(final String mailId, final String emailAddress, final UserInfo ui)
    public boolean isNewMail(final String mailId, final String emailAddress)
    public boolean isNewMail(final String mailId)
    '''
def deleteMailAfterAgeThreshold():
    '''    public void deleteMailAfterAgeThreshold(final Message m, final int age, final String ageUOM, final String emailAddress)
    '''
def getAccessToken():
    '''    public HashMap<String, Integer> getAccessToken(final String tokenUrl, final String clientId, final String clientSecret, final String refreshToken, final String grantType)
    '''
