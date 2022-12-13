def sendDoc():
    '''public ArrayList sendDoc(final String s)
    '''
def DsmlConnection():
    '''public DsmlConnection()
    public DsmlConnection(final LDAPSocketFactory ldapSocketFactory)
    '''
def connect():
    '''public void connect(final String serverString, final int n)
    '''
def bind():
    '''public void bind(final int n, final String s, final byte[] bytes, final LDAPConstraints ldapConstraints)
    public LDAPResponseQueue bind(final int n, final String s, final byte[] array, final LDAPResponseQueue ldapResponseQueue, final LDAPConstraints ldapConstraints)
    public LDAPResponseQueue bind(final int n, final String s, final byte[] array, final LDAPResponseQueue ldapResponseQueue)
    public void bind(final int n, final String s, final byte[] bytes)
    public void bind(final int n, final String s, final String original, final LDAPConstraints ldapConstraints)
    public void bind(final int n, final String s, final String original)
    public void bind(final String s, final String original, final LDAPConstraints ldapConstraints)
    public void bind(final String s, final String original, final Map map, final Object o, final LDAPConstraints ldapConstraints)
    public void bind(final String s, final String original, final Map map, final Object o)
    public void bind(final String s, final String original, final String[] array, final Map map, final Object o, final LDAPConstraints ldapConstraints)
    public void bind(final String s, final String s2, final String[] array, final Map map, final Object o)
    public void bind(final String s, final String s2)
    '''
def add():
    '''public void add(final LDAPEntry ldapEntry, final LDAPConstraints ldapConstraints)
    public LDAPResponseQueue add(final LDAPEntry ldapEntry, final LDAPResponseQueue ldapResponseQueue, final LDAPConstraints ldapConstraints)
    public LDAPResponseQueue add(final LDAPEntry ldapEntry, final LDAPResponseQueue ldapResponseQueue)
    public void add(final LDAPEntry ldapEntry)
    '''
def modify():
    '''public void modify(final String s, final LDAPModification ldapModification, final LDAPConstraints ldapConstraints)
    public LDAPResponseQueue modify(final String s, final LDAPModification ldapModification, final LDAPResponseQueue ldapResponseQueue, final LDAPConstraints ldapConstraints)
    public LDAPResponseQueue modify(final String s, final LDAPModification ldapModification, final LDAPResponseQueue ldapResponseQueue)
    public void modify(final String s, final LDAPModification ldapModification)
    public void modify(final String s, final LDAPModification[] array, final LDAPConstraints ldapConstraints)
    public LDAPResponseQueue modify(final String s, final LDAPModification[] array, final LDAPResponseQueue ldapResponseQueue, final LDAPConstraints ldapConstraints)
    public LDAPResponseQueue modify(final String s, final LDAPModification[] array, final LDAPResponseQueue ldapResponseQueue)
    public void modify(final String s, final LDAPModification[] array)
    '''
def rename():
    '''public void rename(final String s, final String s2, final boolean b, final LDAPConstraints ldapConstraints)
    public LDAPResponseQueue rename(final String s, final String s2, final boolean b, final LDAPResponseQueue ldapResponseQueue, final LDAPConstraints ldapConstraints)
    public LDAPResponseQueue rename(final String s, final String s2, final boolean b, final LDAPResponseQueue ldapResponseQueue)
    public void rename(final String s, final String s2, final boolean b)
    public void rename(final String s, final String s2, final String s3, final boolean b, final LDAPConstraints ldapConstraints)
    public LDAPResponseQueue rename(final String s, final String s2, final String s3, final boolean b, final LDAPResponseQueue ldapResponseQueue, final LDAPConstraints ldapConstraints)
    public LDAPResponseQueue rename(final String s, final String s2, final String s3, final boolean b, final LDAPResponseQueue ldapResponseQueue)
    public void rename(final String s, final String s2, final String s3, final boolean b)
    '''
def delete():
    '''public void delete(final String s, final LDAPConstraints ldapConstraints)
    public LDAPResponseQueue delete(final String s, final LDAPResponseQueue ldapResponseQueue, final LDAPConstraints ldapConstraints)
    public LDAPResponseQueue delete(final String s, final LDAPResponseQueue ldapResponseQueue)
    public void delete(final String s)
    '''
def search():
    '''public LDAPSearchResults search(final String s, final int n, final String s2, final String[] array, final boolean b, final LDAPSearchConstraints ldapSearchConstraints)
    public LDAPSearchQueue search(final String s, final int n, final String s2, final String[] array, final boolean b, final LDAPSearchQueue ldapSearchQueue, final LDAPSearchConstraints ldapSearchConstraints)
    public LDAPSearchQueue search(final String s, final int n, final String s2, final String[] array, final boolean b, final LDAPSearchQueue ldapSearchQueue)
    public LDAPSearchResults search(final String s, final int n, final String s2, final String[] array, final boolean b)
    '''
def isConnectionAlive():
    '''public boolean isConnectionAlive()
    '''
def isBound():
    '''public boolean isBound()
    '''
def isConnected():
    '''public boolean isConnected()
    '''
def isTLS():
    '''public boolean isTLS()
    '''
def disconnect():
    '''public void disconnect()
    public void disconnect(final LDAPConstraints ldapConstraints)
    '''
def sendRequest():
    '''public LDAPMessageQueue sendRequest(final LDAPMessage ldapMessage, final LDAPMessageQueue ldapMessageQueue)
    '''
def getCallback():
    '''public HttpRequestCallback getCallback()
    '''
def setCallback():
    '''public void setCallback(final HttpRequestCallback callback)
    '''
def getBinddn():
    '''public String getBinddn()
    '''
def getCon():
    '''public HttpClient getCon()
    '''
def getHost():
    '''public String getHost()
    '''
def getPass():
    '''public String getPass()
    '''
def getServerString():
    '''public String getServerString()
    '''
