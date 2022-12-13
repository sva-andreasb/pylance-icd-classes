SCOPE_BASE = "int  0"
SCOPE_ONE = "int  1"
SCOPE_SUB = "int  2"
NO_ATTRS = "String  1.1""
ALL_USER_ATTRS = "String  *""
LDAP_V3 = "int  3"
DEFAULT_PORT = "int  389"
DEFAULT_SSL_PORT = "int  636"
LDAP_PROPERTY_SDK = "String  version.sdk""
LDAP_PROPERTY_PROTOCOL = "String  version.protocol""
LDAP_PROPERTY_SECURITY = "String  version.security""
SERVER_SHUTDOWN_OID = "String  1.3.6.1.4.1.1466.20036""
def LDAPConnection():
'''public LDAPConnection()
public LDAPConnection(final LDAPSocketFactory ldapSocketFactory)
'''
pass
def clone():
'''public Object clone()
'''
pass
def getProtocolVersion():
'''public int getProtocolVersion()
'''
pass
def getAuthenticationDN():
'''public String getAuthenticationDN()
'''
pass
def getAuthenticationMethod():
'''public String getAuthenticationMethod()
'''
pass
def getSaslBindProperties():
'''public Map getSaslBindProperties()
'''
pass
def getSaslBindCallbackHandler():
'''public Object getSaslBindCallbackHandler()
'''
pass
def getConstraints():
'''public LDAPConstraints getConstraints()
'''
pass
def getHost():
'''public String getHost()
'''
pass
def getPort():
'''public int getPort()
'''
pass
def getProperty():
'''public Object getProperty(final String s)
'''
pass
def getSearchConstraints():
'''public LDAPSearchConstraints getSearchConstraints()
'''
pass
def getSocketFactory():
'''public LDAPSocketFactory getSocketFactory()
'''
pass
def isBound():
'''public boolean isBound()
'''
pass
def isConnected():
'''public boolean isConnected()
'''
pass
def isConnectionAlive():
'''public boolean isConnectionAlive()
'''
pass
def isTLS():
'''public boolean isTLS()
'''
pass
def setConstraints():
'''public void setConstraints(final LDAPConstraints ldapConstraints)
'''
pass
def setSocketFactory():
'''public static void setSocketFactory(final LDAPSocketFactory socketFactory)
'''
pass
def addUnsolicitedNotificationListener():
'''public void addUnsolicitedNotificationListener(final LDAPUnsolicitedNotificationListener ldapUnsolicitedNotificationListener)
'''
pass
def removeUnsolicitedNotificationListener():
'''public void removeUnsolicitedNotificationListener(final LDAPUnsolicitedNotificationListener ldapUnsolicitedNotificationListener)
'''
pass
def startTLS():
'''public void startTLS()
'''
pass
def stopTLS():
'''public void stopTLS()
'''
pass
def abandon():
'''public void abandon(final LDAPSearchResults ldapSearchResults)
public void abandon(final LDAPSearchResults ldapSearchResults, final LDAPConstraints ldapConstraints)
public void abandon(final int n)
public void abandon(final int n, final LDAPConstraints ldapConstraints)
public void abandon(final LDAPMessageQueue ldapMessageQueue)
public void abandon(final LDAPMessageQueue ldapMessageQueue, final LDAPConstraints ldapConstraints)
'''
pass
def add():
'''public void add(final LDAPEntry ldapEntry)
public void add(final LDAPEntry ldapEntry, final LDAPConstraints ldapConstraints)
public LDAPResponseQueue add(final LDAPEntry ldapEntry, final LDAPResponseQueue ldapResponseQueue)
public LDAPResponseQueue add(final LDAPEntry ldapEntry, final LDAPResponseQueue ldapResponseQueue, LDAPConstraints defSearchCons)
'''
pass
def bind():
'''public void bind(final String s, final String s2)
public void bind(final int n, final String s, final String s2)
public void bind(final String s, final String s2, final LDAPConstraints ldapConstraints)
public void bind(final int n, final String s, final String s2, final LDAPConstraints ldapConstraints)
public void bind(final int n, final String s, final byte[] array)
public void bind(final int n, final String s, final byte[] array, final LDAPConstraints ldapConstraints)
public LDAPResponseQueue bind(final int n, final String s, final byte[] array, final LDAPResponseQueue ldapResponseQueue)
public LDAPResponseQueue bind(final int n, String trim, byte[] array, final LDAPResponseQueue ldapResponseQueue, LDAPConstraints defSearchCons)
public void bind(final String s, final String s2, final Map map, final Object o)
public void bind(final String s, final String s2, final Map map, final Object o, final LDAPConstraints ldapConstraints)
public void bind(final String s, final String s2, final String[] array, final Map map, final Object o)
public void bind(String s, String s2, final String[] array, final Map map, final Object o, final LDAPConstraints ldapConstraints)
'''
pass
def compare():
'''public boolean compare(final String s, final LDAPAttribute ldapAttribute)
public boolean compare(final String s, final LDAPAttribute ldapAttribute, final LDAPConstraints ldapConstraints)
public LDAPResponseQueue compare(final String s, final LDAPAttribute ldapAttribute, final LDAPResponseQueue ldapResponseQueue)
public LDAPResponseQueue compare(final String s, final LDAPAttribute ldapAttribute, final LDAPResponseQueue ldapResponseQueue, LDAPConstraints defSearchCons)
'''
pass
def connect():
'''public void connect(final String str, final int n)
'''
pass
def delete():
'''public void delete(final String s)
public void delete(final String s, final LDAPConstraints ldapConstraints)
public LDAPResponseQueue delete(final String s, final LDAPResponseQueue ldapResponseQueue)
public LDAPResponseQueue delete(final String s, final LDAPResponseQueue ldapResponseQueue, LDAPConstraints defSearchCons)
'''
pass
def disconnect():
'''public void disconnect()
public void disconnect(final LDAPConstraints ldapConstraints)
'''
pass
def extendedOperation():
'''public LDAPExtendedResponse extendedOperation(final LDAPExtendedOperation ldapExtendedOperation)
public LDAPExtendedResponse extendedOperation(final LDAPExtendedOperation ldapExtendedOperation, final LDAPConstraints ldapConstraints)
public LDAPResponseQueue extendedOperation(final LDAPExtendedOperation ldapExtendedOperation, final LDAPResponseQueue ldapResponseQueue)
public LDAPResponseQueue extendedOperation(final LDAPExtendedOperation ldapExtendedOperation, LDAPConstraints defSearchCons, final LDAPResponseQueue ldapResponseQueue)
'''
pass
def getResponseControls():
'''public LDAPControl[] getResponseControls()
'''
pass
def modify():
'''public void modify(final String s, final LDAPModification ldapModification)
public void modify(final String s, final LDAPModification ldapModification, final LDAPConstraints ldapConstraints)
public void modify(final String s, final LDAPModification[] array)
public void modify(final String s, final LDAPModification[] array, final LDAPConstraints ldapConstraints)
public LDAPResponseQueue modify(final String s, final LDAPModification ldapModification, final LDAPResponseQueue ldapResponseQueue)
public LDAPResponseQueue modify(final String s, final LDAPModification ldapModification, final LDAPResponseQueue ldapResponseQueue, final LDAPConstraints ldapConstraints)
public LDAPResponseQueue modify(final String s, final LDAPModification[] array, final LDAPResponseQueue ldapResponseQueue)
public LDAPResponseQueue modify(final String s, final LDAPModification[] array, final LDAPResponseQueue ldapResponseQueue, LDAPConstraints defSearchCons)
'''
pass
def read():
'''public LDAPEntry read(final String s)
public LDAPEntry read(final String s, final LDAPSearchConstraints ldapSearchConstraints)
public LDAPEntry read(final String s, final String[] array)
public LDAPEntry read(final String s, final String[] array, final LDAPSearchConstraints ldapSearchConstraints)
public static LDAPEntry read(final LDAPUrl ldapUrl)
public static LDAPEntry read(final LDAPUrl ldapUrl, final LDAPSearchConstraints ldapSearchConstraints)
'''
pass
def rename():
'''public void rename(final String s, final String s2, final boolean b)
public void rename(final String s, final String s2, final boolean b, final LDAPConstraints ldapConstraints)
public void rename(final String s, final String s2, final String s3, final boolean b)
public void rename(final String s, final String s2, final String s3, final boolean b, final LDAPConstraints ldapConstraints)
public LDAPResponseQueue rename(final String s, final String s2, final boolean b, final LDAPResponseQueue ldapResponseQueue)
public LDAPResponseQueue rename(final String s, final String s2, final boolean b, final LDAPResponseQueue ldapResponseQueue, final LDAPConstraints ldapConstraints)
public LDAPResponseQueue rename(final String s, final String s2, final String s3, final boolean b, final LDAPResponseQueue ldapResponseQueue)
public LDAPResponseQueue rename(final String s, final String s2, final String s3, final boolean b, final LDAPResponseQueue ldapResponseQueue, LDAPConstraints defSearchCons)
'''
pass
def search():
'''public LDAPSearchResults search(final String s, final int n, final String s2, final String[] array, final boolean b)
public LDAPSearchResults search(final String s, final int n, final String s2, final String[] array, final boolean b, LDAPSearchConstraints defSearchCons)
public LDAPSearchQueue search(final String s, final int n, final String s2, final String[] array, final boolean b, final LDAPSearchQueue ldapSearchQueue)
public LDAPSearchQueue search(final String s, final int n, String s2, final String[] array, final boolean b, final LDAPSearchQueue ldapSearchQueue, LDAPSearchConstraints defSearchCons)
public static LDAPSearchResults search(final LDAPUrl ldapUrl)
public static LDAPSearchResults search(final LDAPUrl ldapUrl, LDAPSearchConstraints searchConstraints)
'''
pass
def sendRequest():
'''public LDAPMessageQueue sendRequest(final LDAPMessage ldapMessage, final LDAPMessageQueue ldapMessageQueue)
public LDAPMessageQueue sendRequest(final LDAPMessage ldapMessage, final LDAPMessageQueue ldapMessageQueue, LDAPConstraints defSearchCons)
'''
pass
def fetchSchema():
'''public LDAPSchema fetchSchema(final String s)
'''
pass
def getSchemaDN():
'''public String getSchemaDN()
public String getSchemaDN(final String s)
'''
pass
