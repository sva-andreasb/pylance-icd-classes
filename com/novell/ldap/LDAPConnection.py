SCOPE_BASE = "int  0"
SCOPE_ONE = "int  1"
SCOPE_SUB = "int  2"
NO_ATTRS = "String  \"1.1\""
ALL_USER_ATTRS = "String  \"*\""
LDAP_V3 = "int  3"
DEFAULT_PORT = "int  389"
DEFAULT_SSL_PORT = "int  636"
LDAP_PROPERTY_SDK = "String  \"version.sdk\""
LDAP_PROPERTY_PROTOCOL = "String  \"version.protocol\""
LDAP_PROPERTY_SECURITY = "String  \"version.security\""
SERVER_SHUTDOWN_OID = "String  \"1.3.6.1.4.1.1466.20036\""
def ():
    '''returns LDAPConnection\n\n
    ()\n
    (final LDAPSocketFactory ldapSocketFactory)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def getProtocolVersion():
    '''returns int\n\n
    getProtocolVersion()\n
    '''
def getAuthenticationDN():
    '''returns String\n\n
    getAuthenticationDN()\n
    '''
def getAuthenticationMethod():
    '''returns String\n\n
    getAuthenticationMethod()\n
    '''
def getSaslBindProperties():
    '''returns Map\n\n
    getSaslBindProperties()\n
    '''
def getSaslBindCallbackHandler():
    '''returns Object\n\n
    getSaslBindCallbackHandler()\n
    '''
def getConstraints():
    '''returns LDAPConstraints\n\n
    getConstraints()\n
    '''
def getHost():
    '''returns String\n\n
    getHost()\n
    '''
def getPort():
    '''returns int\n\n
    getPort()\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String s)\n
    '''
def getSearchConstraints():
    '''returns LDAPSearchConstraints\n\n
    getSearchConstraints()\n
    '''
def getSocketFactory():
    '''returns LDAPSocketFactory\n\n
    getSocketFactory()\n
    '''
def isBound():
    '''returns boolean\n\n
    isBound()\n
    '''
def isConnected():
    '''returns boolean\n\n
    isConnected()\n
    '''
def isConnectionAlive():
    '''returns boolean\n\n
    isConnectionAlive()\n
    '''
def isTLS():
    '''returns boolean\n\n
    isTLS()\n
    '''
def setConstraints():
    '''returns None\n\n
    setConstraints(final LDAPConstraints ldapConstraints)\n
    '''
def addUnsolicitedNotificationListener():
    '''returns None\n\n
    addUnsolicitedNotificationListener(final LDAPUnsolicitedNotificationListener ldapUnsolicitedNotificationListener)\n
    '''
def removeUnsolicitedNotificationListener():
    '''returns None\n\n
    removeUnsolicitedNotificationListener(final LDAPUnsolicitedNotificationListener ldapUnsolicitedNotificationListener)\n
    '''
def startTLS():
    '''returns None\n\n
    startTLS()\n
    '''
def stopTLS():
    '''returns None\n\n
    stopTLS()\n
    '''
def abandon():
    '''returns None\n\n
    abandon(final LDAPSearchResults ldapSearchResults)\n
    abandon(final LDAPSearchResults ldapSearchResults, final LDAPConstraints ldapConstraints)\n
    abandon(final int n)\n
    abandon(final int n, final LDAPConstraints ldapConstraints)\n
    abandon(final LDAPMessageQueue ldapMessageQueue)\n
    abandon(final LDAPMessageQueue ldapMessageQueue, final LDAPConstraints ldapConstraints)\n
    '''
def add():
    '''returns LDAPResponseQueue\n\n
    add(final LDAPEntry ldapEntry)\n
    add(final LDAPEntry ldapEntry, final LDAPConstraints ldapConstraints)\n
    add(final LDAPEntry ldapEntry, final LDAPResponseQueue ldapResponseQueue)\n
    add(final LDAPEntry ldapEntry, final LDAPResponseQueue ldapResponseQueue, LDAPConstraints defSearchCons)\n
    '''
def bind():
    '''returns None\n\n
    bind(final String s, final String s2)\n
    bind(final int n, final String s, final String s2)\n
    bind(final String s, final String s2, final LDAPConstraints ldapConstraints)\n
    bind(final int n, final String s, final String s2, final LDAPConstraints ldapConstraints)\n
    bind(final int n, final String s, final byte[] array)\n
    bind(final int n, final String s, final byte[] array, final LDAPConstraints ldapConstraints)\n
    bind(final int n, final String s, final byte[] array, final LDAPResponseQueue ldapResponseQueue)\n
    bind(final int n, String trim, byte[] array, final LDAPResponseQueue ldapResponseQueue, LDAPConstraints defSearchCons)\n
    bind(final String s, final String s2, final Map map, final Object o)\n
    bind(final String s, final String s2, final Map map, final Object o, final LDAPConstraints ldapConstraints)\n
    bind(final String s, final String s2, final String[] array, final Map map, final Object o)\n
    bind(String s, String s2, final String[] array, final Map map, final Object o, final LDAPConstraints ldapConstraints)\n
    '''
def compare():
    '''returns LDAPResponseQueue\n\n
    compare(final String s, final LDAPAttribute ldapAttribute)\n
    compare(final String s, final LDAPAttribute ldapAttribute, final LDAPConstraints ldapConstraints)\n
    compare(final String s, final LDAPAttribute ldapAttribute, final LDAPResponseQueue ldapResponseQueue)\n
    compare(final String s, final LDAPAttribute ldapAttribute, final LDAPResponseQueue ldapResponseQueue, LDAPConstraints defSearchCons)\n
    '''
def connect():
    '''returns None\n\n
    connect(final String str, final int n)\n
    '''
def delete():
    '''returns LDAPResponseQueue\n\n
    delete(final String s)\n
    delete(final String s, final LDAPConstraints ldapConstraints)\n
    delete(final String s, final LDAPResponseQueue ldapResponseQueue)\n
    delete(final String s, final LDAPResponseQueue ldapResponseQueue, LDAPConstraints defSearchCons)\n
    '''
def disconnect():
    '''returns None\n\n
    disconnect()\n
    disconnect(final LDAPConstraints ldapConstraints)\n
    '''
def extendedOperation():
    '''returns LDAPResponseQueue\n\n
    extendedOperation(final LDAPExtendedOperation ldapExtendedOperation)\n
    extendedOperation(final LDAPExtendedOperation ldapExtendedOperation, final LDAPConstraints ldapConstraints)\n
    extendedOperation(final LDAPExtendedOperation ldapExtendedOperation, final LDAPResponseQueue ldapResponseQueue)\n
    extendedOperation(final LDAPExtendedOperation ldapExtendedOperation, LDAPConstraints defSearchCons, final LDAPResponseQueue ldapResponseQueue)\n
    '''
def getResponseControls():
    '''returns LDAPControl[]\n\n
    getResponseControls()\n
    '''
def modify():
    '''returns LDAPResponseQueue\n\n
    modify(final String s, final LDAPModification ldapModification)\n
    modify(final String s, final LDAPModification ldapModification, final LDAPConstraints ldapConstraints)\n
    modify(final String s, final LDAPModification[] array)\n
    modify(final String s, final LDAPModification[] array, final LDAPConstraints ldapConstraints)\n
    modify(final String s, final LDAPModification ldapModification, final LDAPResponseQueue ldapResponseQueue)\n
    modify(final String s, final LDAPModification ldapModification, final LDAPResponseQueue ldapResponseQueue, final LDAPConstraints ldapConstraints)\n
    modify(final String s, final LDAPModification[] array, final LDAPResponseQueue ldapResponseQueue)\n
    modify(final String s, final LDAPModification[] array, final LDAPResponseQueue ldapResponseQueue, LDAPConstraints defSearchCons)\n
    '''
def read():
    '''returns LDAPEntry\n\n
    read(final String s)\n
    read(final String s, final LDAPSearchConstraints ldapSearchConstraints)\n
    read(final String s, final String[] array)\n
    read(final String s, final String[] array, final LDAPSearchConstraints ldapSearchConstraints)\n
    '''
def rename():
    '''returns LDAPResponseQueue\n\n
    rename(final String s, final String s2, final boolean b)\n
    rename(final String s, final String s2, final boolean b, final LDAPConstraints ldapConstraints)\n
    rename(final String s, final String s2, final String s3, final boolean b)\n
    rename(final String s, final String s2, final String s3, final boolean b, final LDAPConstraints ldapConstraints)\n
    rename(final String s, final String s2, final boolean b, final LDAPResponseQueue ldapResponseQueue)\n
    rename(final String s, final String s2, final boolean b, final LDAPResponseQueue ldapResponseQueue, final LDAPConstraints ldapConstraints)\n
    rename(final String s, final String s2, final String s3, final boolean b, final LDAPResponseQueue ldapResponseQueue)\n
    rename(final String s, final String s2, final String s3, final boolean b, final LDAPResponseQueue ldapResponseQueue, LDAPConstraints defSearchCons)\n
    '''
def search():
    '''returns LDAPSearchQueue\n\n
    search(final String s, final int n, final String s2, final String[] array, final boolean b)\n
    search(final String s, final int n, final String s2, final String[] array, final boolean b, LDAPSearchConstraints defSearchCons)\n
    search(final String s, final int n, final String s2, final String[] array, final boolean b, final LDAPSearchQueue ldapSearchQueue)\n
    search(final String s, final int n, String s2, final String[] array, final boolean b, final LDAPSearchQueue ldapSearchQueue, LDAPSearchConstraints defSearchCons)\n
    '''
def sendRequest():
    '''returns LDAPMessageQueue\n\n
    sendRequest(final LDAPMessage ldapMessage, final LDAPMessageQueue ldapMessageQueue)\n
    sendRequest(final LDAPMessage ldapMessage, final LDAPMessageQueue ldapMessageQueue, LDAPConstraints defSearchCons)\n
    '''
def fetchSchema():
    '''returns LDAPSchema\n\n
    fetchSchema(final String s)\n
    '''
def getSchemaDN():
    '''returns String\n\n
    getSchemaDN()\n
    getSchemaDN(final String s)\n
    '''
