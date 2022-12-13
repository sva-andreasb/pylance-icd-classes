def setLogger():
'''public static void setLogger(final MXLogger log)
'''
pass
def getLogger():
'''public static MXLogger getLogger()
'''
pass
def processMessage():
'''public static void processMessage(MboRemote inboundComm)
public static void processMessage(final ObjectMessage objm)
'''
pass
def handleErrorException():
'''public static void handleErrorException(final Exception e, final String emailAddress, MboRemote inboundComm)
'''
pass
def updateInboundComm():
'''public static MboRemote updateInboundComm(final String[] attributeName, final String[] value, final MboRemote oldInbComm)
'''
pass
def getInboundCommRecord():
'''public static MboRemote getInboundCommRecord(final MboRemote oldInbComm)
'''
pass
def processWorkFlow():
'''public static void processWorkFlow(MboRemote inboundComm, final String processName)
'''
pass
def getCommTemplate():
'''public static MboRemote getCommTemplate(final String templateId, final UserInfo ui)
'''
pass
def sendEmail():
'''public static void sendEmail(final String messageStr, final MboRemote ownMbo, String sendTo, final String templateName)
public static void sendEmail(final MboRemote ownMbo, final String sendTo, final String templateName, final Throwable t)
public static void sendEmail(final MboRemote ownMbo, final String sendTo, final String templateName, final String senderFrom, final String subject, final Date receivedDate, final Throwable t)
'''
pass
def getMboSet():
'''public static MboSetRemote getMboSet(final String name, final UserInfo ui)
'''
pass
