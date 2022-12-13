def MemberAuthenticatorImpl():
    '''    public MemberAuthenticatorImpl(final CoreStackInfo csi)
    '''
def setSharedSecret():
    '''    public synchronized void setSharedSecret(final String updatedSecret)
    '''
def getToken():
    '''    public synchronized byte[] getToken(final String coreStackName, final String targetMemberName)
    '''
def authenticateMember():
    '''    public synchronized boolean authenticateMember(final String coreStackName, final String senderName, final byte[] token, final InetAddress senderIp)
    '''
