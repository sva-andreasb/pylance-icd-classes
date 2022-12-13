SCOPE_BASE = "int  0"
SCOPE_ONE = "int  1"
SCOPE_SUB = "int  2"
NO_ATTRS = "String  \"1.1\""
ALL_USER_ATTRS = "String  \"*\""
DEFAULT_PORT = "int  389"
LDAP_PROPERTY_SDK = "String  \"version.sdk\""
LDAP_PROPERTY_PROTOCOL = "String  \"version.protocol\""
LDAP_PROPERTY_SECURITY = "String  \"version.security\""
def LDAPConnection():
    '''    public LDAPConnection()
    public LDAPConnection(final LDAPSocketFactory ldapSocketFactory)
    '''
def clone():
    '''    public Object clone()
    '''
def getProtocolVersion():
    '''    public int getProtocolVersion()
    '''
def getAuthenticationDN():
    '''    public String getAuthenticationDN()
    '''
def getAuthenticationMethod():
    '''    public String getAuthenticationMethod()
    '''
def getSaslBindProperties():
    '''    public Map getSaslBindProperties()
    '''
def getSaslBindCallbackHandler():
    '''    public Object getSaslBindCallbackHandler()
    '''
def getConstraints():
    '''    public LDAPConstraints getConstraints()
    '''
def getHost():
    '''    public String getHost()
    '''
def getPort():
    '''    public int getPort()
    '''
def getProperty():
    '''    public Object getProperty(final String s)
    '''
def getSearchConstraints():
    '''    public LDAPSearchConstraints getSearchConstraints()
    '''
def getSocketFactory():
    '''    public LDAPSocketFactory getSocketFactory()
    '''
def isBound():
    '''    public boolean isBound()
    '''
def isConnected():
    '''    public boolean isConnected()
    '''
def isTLS():
    '''    public boolean isTLS()
    '''
def setConstraints():
    '''    public void setConstraints(final LDAPConstraints ldapConstraints)
    '''
def setSocketFactory():
    '''    public static void setSocketFactory(final LDAPSocketFactory ldapSocketFactory)
    '''
def addUnsolicitedNotificationListener():
    '''    public void addUnsolicitedNotificationListener(final LDAPUnsolicitedNotificationListener ldapUnsolicitedNotificationListener)
    '''
def removeUnsolicitedNotificationListener():
    '''    public void removeUnsolicitedNotificationListener(final LDAPUnsolicitedNotificationListener key)
    '''
def startTLS():
    '''    public void startTLS()
    '''
def stopTLS():
    '''    public void stopTLS()
    '''
def abandon():
    '''    public void abandon(final LDAPSearchResults ldapSearchResults)
    public void abandon(final LDAPSearchResults ldapSearchResults, final LDAPConstraints ldapConstraints)
    public void abandon(final int n)
    public void abandon(final int n, final LDAPConstraints ldapConstraints)
    public void abandon(final LDAPMessageQueue ldapMessageQueue)
    public void abandon(final LDAPMessageQueue ldapMessageQueue, final LDAPConstraints ldapConstraints)
    '''
def add():
    '''    public void add(final LDAPEntry ldapEntry)
    public void add(final LDAPEntry ldapEntry, final LDAPConstraints ldapConstraints)
    public LDAPResponseQueue add(final LDAPEntry ldapEntry, final LDAPResponseQueue ldapResponseQueue)
    public LDAPResponseQueue add(final LDAPEntry ldapEntry, final LDAPResponseQueue ldapResponseQueue, final LDAPConstraints ldapConstraints)
    '''
def bind():
    '''    public void bind(final int n, final String s, final byte[] array)
    public void bind(final int n, final String s, final byte[] array, final LDAPConstraints ldapConstraints)
    public LDAPResponseQueue bind(final int n, final String s, final byte[] array, final LDAPResponseQueue ldapResponseQueue)
    public LDAPResponseQueue bind(final int n, final String s, final byte[] array, final LDAPResponseQueue ldapResponseQueue, final LDAPConstraints ldapConstraints)
    public void bind(final String s, final String s2, final Map map, final Object o)
    public void bind(final String s, final String s2, final Map map, final Object o, final LDAPConstraints ldapConstraints)
    public void bind(final String s, final String s2, final String[] array, final Map map, final Object o)
    public void bind(final String s, final String s2, final String[] array, final Map map, final Object o, final LDAPConstraints ldapConstraints)
    '''
def compare():
    '''    public boolean compare(final String s, final LDAPAttribute ldapAttribute)
    public boolean compare(final String s, final LDAPAttribute ldapAttribute, final LDAPConstraints ldapConstraints)
    public LDAPResponseQueue compare(final String s, final LDAPAttribute ldapAttribute, final LDAPResponseQueue ldapResponseQueue)
    public LDAPResponseQueue compare(final String s, final LDAPAttribute ldapAttribute, final LDAPResponseQueue ldapResponseQueue, final LDAPConstraints ldapConstraints)
    '''
def connect():
    '''    public void connect(final String s, final int n)
    '''
def delete():
    '''    public void delete(final String s)
    public void delete(final String s, final LDAPConstraints ldapConstraints)
    public LDAPResponseQueue delete(final String s, final LDAPResponseQueue ldapResponseQueue)
    public LDAPResponseQueue delete(final String s, final LDAPResponseQueue ldapResponseQueue, final LDAPConstraints ldapConstraints)
    '''
def disconnect():
    '''    public void disconnect()
    public void disconnect(final LDAPConstraints ldapConstraints)
    '''
def extendedOperation():
    '''    public LDAPExtendedResponse extendedOperation(final LDAPExtendedOperation ldapExtendedOperation)
    public LDAPExtendedResponse extendedOperation(final LDAPExtendedOperation ldapExtendedOperation, final LDAPSearchConstraints ldapSearchConstraints)
    public LDAPResponseQueue extendedOperation(final LDAPExtendedOperation ldapExtendedOperation, final LDAPResponseQueue ldapResponseQueue)
    public LDAPResponseQueue extendedOperation(final LDAPExtendedOperation ldapExtendedOperation, final LDAPSearchConstraints ldapSearchConstraints, final LDAPResponseQueue ldapResponseQueue)
    '''
def getResponseControls():
    '''    public LDAPControl[] getResponseControls()
    '''
def modify():
    '''    public void modify(final String s, final LDAPModification ldapModification)
    public void modify(final String s, final LDAPModification ldapModification, final LDAPConstraints ldapConstraints)
    public void modify(final String s, final LDAPModification[] array)
    public void modify(final String s, final LDAPModification[] array, final LDAPConstraints ldapConstraints)
    public LDAPResponseQueue modify(final String s, final LDAPModification ldapModification, final LDAPResponseQueue ldapResponseQueue)
    public LDAPResponseQueue modify(final String s, final LDAPModification ldapModification, final LDAPResponseQueue ldapResponseQueue, final LDAPConstraints ldapConstraints)
    public LDAPResponseQueue modify(final String s, final LDAPModification[] array, final LDAPResponseQueue ldapResponseQueue)
    public LDAPResponseQueue modify(final String s, final LDAPModification[] array, final LDAPResponseQueue ldapResponseQueue, final LDAPConstraints ldapConstraints)
    '''
def read():
    '''    public LDAPEntry read(final String s)
    public LDAPEntry read(final String s, final LDAPSearchConstraints ldapSearchConstraints)
    public LDAPEntry read(final String s, final String[] array)
    public LDAPEntry read(final String s, final String[] array, final LDAPSearchConstraints ldapSearchConstraints)
    public static LDAPEntry read(final LDAPUrl ldapUrl)
    public static LDAPEntry read(final LDAPUrl ldapUrl, final LDAPSearchConstraints ldapSearchConstraints)
    '''
def rename():
    '''    public void rename(final String s, final String s2, final boolean b)
    public void rename(final String s, final String s2, final boolean b, final LDAPConstraints ldapConstraints)
    public void rename(final String s, final String s2, final String s3, final boolean b)
    public void rename(final String s, final String s2, final String s3, final boolean b, final LDAPConstraints ldapConstraints)
    public LDAPResponseQueue rename(final String s, final String s2, final boolean b, final LDAPResponseQueue ldapResponseQueue)
    public LDAPResponseQueue rename(final String s, final String s2, final boolean b, final LDAPResponseQueue ldapResponseQueue, final LDAPConstraints ldapConstraints)
    public LDAPResponseQueue rename(final String s, final String s2, final String s3, final boolean b, final LDAPResponseQueue ldapResponseQueue)
    public LDAPResponseQueue rename(final String s, final String s2, final String s3, final boolean b, final LDAPResponseQueue ldapResponseQueue, final LDAPConstraints ldapConstraints)
    '''
def search():
    '''    public LDAPSearchResults search(final String s, final int n, final String s2, final String[] array, final boolean b)
    public LDAPSearchResults search(final String s, final int n, final String s2, final String[] array, final boolean b, final LDAPSearchConstraints ldapSearchConstraints)
    public LDAPSearchQueue search(final String s, final int n, final String s2, final String[] array, final boolean b, final LDAPSearchQueue ldapSearchQueue)
    public LDAPSearchQueue search(final String s, final int n, final String s2, final String[] array, final boolean b, final LDAPSearchQueue ldapSearchQueue, final LDAPSearchConstraints ldapSearchConstraints)
    public static LDAPSearchResults search(final LDAPUrl ldapUrl)
    public static LDAPSearchResults search(final LDAPUrl ldapUrl, final LDAPSearchConstraints ldapSearchConstraints)
    '''
def fetchSchema():
    '''    public LDAPSchema fetchSchema(final String s)
    '''
def getSchemaDN():
    '''    public String getSchemaDN()
    public String getSchemaDN(final String s)
    '''
def messageReceived():
    '''    public void messageReceived(final com.novell.ldap.LDAPExtendedResponse ldapExtendedResponse)
    '''
def createSocket():
    '''    public Socket createSocket(final String s, final int n)
    '''
