USEJMX = "String  \"usejmx\""
HOST = "String  \"host\""
PORT = "String  \"port\""
TYPE = "String  \"conntype\""
HOST_DEFAULT = "String  \"localhost\""
PORT_DEFAULT = "String  \"8880\""
TYPE_DEFAULT = "String  \"SOAP\""
TIMEOUT = "String  \"timeout\""
TIMEOUT_DEFAULT = "int  300"
def ():
    '''returns UninstallApp\n\n
    (final String aName, final Hashtable cmdLine)\n
    '''
def uninstall():
    '''returns None\n\n
    uninstall()\n
    '''
def appEventReceived():
    '''returns None\n\n
    appEventReceived(final AppNotification ev)\n
    '''
def handleNotification():
    '''returns None\n\n
    handleNotification(final Notification notf, final Object handback)\n
    '''
