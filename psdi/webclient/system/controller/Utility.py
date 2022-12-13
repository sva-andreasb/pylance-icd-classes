MSG_BTNOK = "int  2"
MSG_BTNCANCEL = "int  4"
MSG_BTNYES = "int  8"
MSG_BTNNO = "int  16"
def makesafevalue():
'''public static String makesafevalue(final String value)
'''
pass
def isNull():
'''public static boolean isNull(final String val)
'''
pass
def getHost():
'''public static String getHost()
'''
pass
def getHostAddress():
'''public static String getHostAddress()
'''
pass
def isParam():
'''public static boolean isParam(final HttpServletRequest request, final String val)
'''
pass
def escapeForJScript():
'''public static String escapeForJScript(final String str)
'''
pass
def isNumeric():
'''public static boolean isNumeric(final MboValueData mvData)
'''
pass
def replaceParams():
'''public static String replaceParams(final String message, final String[] params)
'''
pass
def formatDataString():
'''public static String formatDataString(final String dataString)
'''
pass
def getPrependValue():
'''public static String getPrependValue(final String prependString)
'''
pass
def formatStringForTags():
'''public static String formatStringForTags(final String str)
'''
pass
def unFormatString():
'''public static String unFormatString(final String str)
'''
pass
def addMXWarnings():
'''public static boolean addMXWarnings(final SessionContext sessionContext, final MXException[] warnings)
'''
pass
def handleMXWarnings():
'''public static boolean handleMXWarnings(final SessionContext sessionContext)
'''
pass
def clearUserInput():
'''public static void clearUserInput(final SessionContext sessionContext)
'''
pass
def getMessage():
'''public static String getMessage(final SessionContext sessionContext, final MXException mxe)
public static String getMessage(final SessionContext sessionContext, final String messageFile, final String key)
public static String getMessage(final SessionContext sessionContext, final String messageFile, final String key, final String[] params)
'''
pass
def getMaxMessage():
'''public static MaxMessage getMaxMessage(final SessionContext sessionContext, final String group, final String key)
'''
pass
def showMessageBox():
'''public static void showMessageBox(final WebClientEvent srcEvent, final String title, final String warnings, final int flags)
public static void showMessageBox(final WebClientEvent srcEvent, final String messageFile, final String key, final String[] params)
public static void showMessageBox(final WebClientEvent srcEvent, final MXException mxe)
public static void showMessageBox(final WebClientEvent srcEvent, final RemoteException re)
'''
pass
def sendEvent():
'''public static int sendEvent(final SessionContext sc, final String targetId, final String event, final Object value)
public static int sendEvent(final WebClientSession sc, final String targetId, final String event, final Object value)
public static int sendEvent(final WebClientEvent event)
'''
pass
def getDataBean():
'''public static DataBean getDataBean(final SessionContext sc, final String beanId)
'''
pass
def getDataSource():
'''public static DataBean getDataSource(final SessionContext sc, final ControlHandler handler)
'''
pass
def getSettingsProperty():
'''public static String getSettingsProperty(final SessionContext sc, final String prop)
public static String getSettingsProperty(final SessionContext sc, final String prop, final String[] params)
'''
pass
def handleDialogOK():
'''public static boolean handleDialogOK(final SessionContext sc)
'''
pass
def replaceString():
'''public static String replaceString(final String str, final String pattern, final String replacement)
'''
pass
def createStatusText():
'''public static String createStatusText(final MXException[] warnings, final SessionContext sc)
'''
pass
