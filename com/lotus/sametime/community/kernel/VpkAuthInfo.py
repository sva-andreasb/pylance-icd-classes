ST_AUTH_TYPE_PLAIN_PASSWD = "short  0"
ST_AUTH_TYPE_PLAIN_NOTES_TOKEN = "short  1"
ST_AUTH_TYPE_ENC_PASSWORD = "short  2"
ST_AUTH_TYPE_ANON = "short  3"
ST_AUTH_TYPE_ENC_DH_PASSWORD = "short  4"
ST_AUTH_TYPE_ENC_DH_NOTES_TOKEN = "short  5"
def VpkAuthInfo():
    '''    public VpkAuthInfo(final short type, final byte[] data)
    '''
def getType():
    '''    public synchronized short getType()
    '''
def getData():
    '''    public synchronized byte[] getData()
    '''
def dump():
    '''    public void dump(final NdrOutputStream ndrOutputStream)
    '''
def equals():
    '''    public boolean equals(final Object o)
    '''
