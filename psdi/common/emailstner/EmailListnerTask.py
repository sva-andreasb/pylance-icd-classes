def EmailListnerTask():
'''public EmailListnerTask()
'''
pass
def performTask():
'''public void performTask(final String taskName, final String instanceName)
'''
pass
def getLogger():
'''public static MXLogger getLogger()
'''
pass
def setLogger():
'''public void setLogger(final MXLogger logger)
'''
pass
def getRunAsUserInfo():
'''public UserInfo getRunAsUserInfo()
'''
pass
def setRunAsUserInfo():
'''public void setRunAsUserInfo(final UserInfo userInfo)
'''
pass
def readMessagesFromMailServer():
'''public void readMessagesFromMailServer(final InboundCommCfgData cfgData, final MboRemote inboundCommCfgMbo)
'''
pass
def processNEWStatusFromInboundComm():
'''public void processNEWStatusFromInboundComm(final MboRemote inboundCommCfgMbo)
'''
pass
def processNewStatusMail():
'''public MboRemote processNewStatusMail(MboRemote inboundComm)
'''
pass
def getAppFromInbCommSecurity():
'''public String getAppFromInbCommSecurity(final MboRemote inboundComm, final String objectName)
'''
pass
def appExistForSecurityCheck():
'''public void appExistForSecurityCheck(MboRemote inboundComm, final int formatMode)
'''
pass
def getAppFromMaxApps():
'''public String getAppFromMaxApps(final String objectName)
'''
pass
def parseFormattedMessage():
'''public void parseFormattedMessage(final MboRemote inboundComm, final LSNRParser parser, final int mode)
'''
pass
def processMailForFreeformMode():
'''public MboRemote processMailForFreeformMode(final MboRemote inboundComm)
'''
pass
def getObjectActionForFormattedMode():
'''public MboRemote getObjectActionForFormattedMode(MboRemote inboundComm, final LSNRParser parser, final int mode)
'''
pass
def getMultipartPart():
'''public MailData getMultipartPart(final MimeMultipart mp, final MailData md, final Vector<Object> vector)
'''
pass
def getTextPart():
'''public String getTextPart(final MimeBodyPart mbp, String text)
'''
pass
def writeIntoInboundComm():
'''public MboRemote writeIntoInboundComm(final MailData md, final InboundCommCfgData cfgData, final MboRemote inboundCommCfgMbo)
public MboRemote writeIntoInboundComm(final MailData md, final InboundCommCfgData cfgData, final MboRemote inboundCommCfgMbo, final Message m)
'''
pass
def writeToDocInfoAndDocLinks():
'''public void writeToDocInfoAndDocLinks(final MailData md, final String inbCommUser, final MboRemote inboundComm, final String attFileName, final String doclinkName, final boolean msgFirstLevel, final int msgLevel)
'''
pass
def getContentTypeFrom():
'''public static String getContentTypeFrom(final String fileName)
'''
pass
def isNewMail():
'''public boolean isNewMail(final String mailId, final String emailAddress, final UserInfo ui)
public boolean isNewMail(final String mailId, final String emailAddress)
public boolean isNewMail(final String mailId)
'''
pass
def deleteMailAfterAgeThreshold():
'''public void deleteMailAfterAgeThreshold(final Message m, final int age, final String ageUOM, final String emailAddress)
'''
pass
def getAccessToken():
'''public HashMap<String, Integer> getAccessToken(final String tokenUrl, final String clientId, final String clientSecret, final String refreshToken, final String grantType)
'''
pass
