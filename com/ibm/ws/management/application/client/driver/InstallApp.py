INTERACTIVE = "String  \"interactive\""
API = "String  \"api\""
PREPAREONLY = "String  \"prepareonly\""
USEJMX = "String  \"usejmx\""
HOST = "String  \"host\""
PORT = "String  \"port\""
TYPE = "String  \"conntype\""
HOST_DEFAULT = "String  \"localhost\""
PORT_DEFAULT = "String  \"8880\""
TYPE_DEFAULT = "String  \"SOAP\""
MODULESERVER = "String  \"moduleserverfile\""
TIMEOUT = "String  \"timeout\""
TIMEOUT_DEFAULT = "int  300"
def ():
    '''returns InstallApp\n\n
    (final String aName, final Hashtable cmdLine)\n
    '''
def prepareApp():
    '''returns None\n\n
    prepareApp()\n
    '''
def appEventReceived():
    '''returns None\n\n
    appEventReceived(final AppNotification ev)\n
    '''
def handleNotification():
    '''returns None\n\n
    handleNotification(final Notification notf, final Object handback)\n
    '''
