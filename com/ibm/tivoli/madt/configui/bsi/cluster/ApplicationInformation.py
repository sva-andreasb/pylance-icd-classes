UI_FUNCTION = "int  1"
CRON_FUNCTION = "int  2"
MIF_FUNCTION = "int  4"
REPORT_FUNCTION = "int  8"
JMS_ENABLED = "int  64"
def ():
    '''returns ApplicationInformation\n\n
    (final String applicationName, final String clusterName, final int functions)\n
    (final String clusterName, final String applicationName, final int functions, final boolean persistJMS, final HashMap<ConfigUIPropertyEnum, String> jmsProps)\n
    '''
def getFunctions():
    '''returns int\n\n
    getFunctions()\n
    '''
def getClusterName():
    '''returns String\n\n
    getClusterName()\n
    '''
def setClusterName():
    '''returns None\n\n
    setClusterName(final String name)\n
    '''
def isUIApplication():
    '''returns boolean\n\n
    isUIApplication()\n
    '''
def setUIApplication():
    '''returns None\n\n
    setUIApplication(final boolean isUI)\n
    '''
def isCronApplication():
    '''returns boolean\n\n
    isCronApplication()\n
    '''
def setCronApplication():
    '''returns None\n\n
    setCronApplication(final boolean isCron)\n
    '''
def isMIFApplication():
    '''returns boolean\n\n
    isMIFApplication()\n
    '''
def setMIFApplication():
    '''returns None\n\n
    setMIFApplication(final boolean isMIF)\n
    '''
def isReportingApplication():
    '''returns boolean\n\n
    isReportingApplication()\n
    '''
def setReportingApplication():
    '''returns None\n\n
    setReportingApplication(final boolean isReporting)\n
    '''
def isMaximoCluster():
    '''returns boolean\n\n
    isMaximoCluster()\n
    '''
def isJMSEnabled():
    '''returns boolean\n\n
    isJMSEnabled()\n
    '''
def setJMSEnabled():
    '''returns None\n\n
    setJMSEnabled(final boolean enableJMS)\n
    '''
def setApplicationName():
    '''returns None\n\n
    setApplicationName(final String applicationName)\n
    '''
def getApplicationName():
    '''returns String\n\n
    getApplicationName()\n
    '''
def setWebServerName():
    '''returns None\n\n
    setWebServerName(final String webServerName)\n
    '''
def getWebServerName():
    '''returns String\n\n
    getWebServerName()\n
    '''
def setPersistJMSInfo():
    '''returns None\n\n
    setPersistJMSInfo(final boolean persistJMSInfo)\n
    '''
def isPersistJMSInfo():
    '''returns boolean\n\n
    isPersistJMSInfo()\n
    '''
def setJMSProperties():
    '''returns None\n\n
    setJMSProperties(final HashMap<ConfigUIPropertyEnum, String> jmsProps)\n
    '''
