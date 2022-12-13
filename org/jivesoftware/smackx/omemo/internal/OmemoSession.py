def OmemoSession():
    '''public OmemoSession(final OmemoManager omemoManager, final OmemoStore<T_IdKeyPair, T_IdKey, T_PreKey, T_SigPreKey, T_Sess, T_Addr, T_ECPub, T_Bundle, T_Ciph> omemoStore, final OmemoDevice remoteDevice, final T_IdKey identityKey)
    public OmemoSession(final OmemoManager omemoManager, final OmemoStore<T_IdKeyPair, T_IdKey, T_PreKey, T_SigPreKey, T_Sess, T_Addr, T_ECPub, T_Bundle, T_Ciph> omemoStore, final OmemoDevice remoteDevice)
    '''
def decryptTransportedKey():
    '''public CipherAndAuthTag decryptTransportedKey(final OmemoElement element, final int keyId)
    '''
def decryptMessageElement():
    '''public static Message decryptMessageElement(final OmemoElement element, final CipherAndAuthTag cipherAndAuthTag)
    public Message decryptMessageElement(final OmemoElement element, final int keyId)
    '''
def getPreKeyId():
    '''public int getPreKeyId()
    '''
def getIdentityKey():
    '''public T_IdKey getIdentityKey()
    '''
def setIdentityKey():
    '''public void setIdentityKey(final T_IdKey identityKey)
    '''
def getFingerprint():
    '''public OmemoFingerprint getFingerprint()
    '''
