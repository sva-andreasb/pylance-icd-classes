def OmemoStore():
    '''    public OmemoStore()
    '''
def getOmemoSessionOf():
    '''    public OmemoSession<T_IdKeyPair, T_IdKey, T_PreKey, T_SigPreKey, T_Sess, T_Addr, T_ECPub, T_Bundle, T_Ciph> getOmemoSessionOf(final OmemoManager omemoManager, final OmemoDevice device)
    '''
def generateOmemoIdentityKeyPair():
    '''    public T_IdKeyPair generateOmemoIdentityKeyPair()
    '''
def isTrustedOmemoIdentity():
    '''    public boolean isTrustedOmemoIdentity(final OmemoManager omemoManager, final OmemoDevice device, final T_IdKey identityKey)
    '''
def isDecidedOmemoIdentity():
    '''    public boolean isDecidedOmemoIdentity(final OmemoManager omemoManager, final OmemoDevice device, final T_IdKey identityKey)
    '''
def trustOmemoIdentity():
    '''    public void trustOmemoIdentity(final OmemoManager omemoManager, final OmemoDevice device, final T_IdKey identityKey)
    '''
def distrustOmemoIdentity():
    '''    public void distrustOmemoIdentity(final OmemoManager omemoManager, final OmemoDevice device, final T_IdKey identityKey)
    '''
def setDateOfLastReceivedMessage():
    '''    public void setDateOfLastReceivedMessage(final OmemoManager omemoManager, final OmemoDevice from)
    '''
def setDateOfLastSignedPreKeyRenewal():
    '''    public void setDateOfLastSignedPreKeyRenewal(final OmemoManager omemoManager)
    '''
def generateOmemoPreKeys():
    '''    public HashMap<Integer, T_PreKey> generateOmemoPreKeys(final int startId, final int count)
    '''
def storeOmemoPreKeys():
    '''    public void storeOmemoPreKeys(final OmemoManager omemoManager, final HashMap<Integer, T_PreKey> preKeyHashMap)
    '''
def generateOmemoSignedPreKey():
    '''    public T_SigPreKey generateOmemoSignedPreKey(final T_IdKeyPair identityKeyPair, final int signedPreKeyId)
    '''
def getFingerprint():
    '''    public OmemoFingerprint getFingerprint(final OmemoManager omemoManager)
    public OmemoFingerprint getFingerprint(final OmemoManager omemoManager, final OmemoDevice device)
    '''
