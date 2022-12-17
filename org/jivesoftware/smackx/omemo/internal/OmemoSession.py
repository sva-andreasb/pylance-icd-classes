def ():
    '''returns OmemoSession\n\n
    (final OmemoManager omemoManager, final OmemoStore<T_IdKeyPair, T_IdKey, T_PreKey, T_SigPreKey, T_Sess, T_Addr, T_ECPub, T_Bundle, T_Ciph> omemoStore, final OmemoDevice remoteDevice, final T_IdKey identityKey)\n
    (final OmemoManager omemoManager, final OmemoStore<T_IdKeyPair, T_IdKey, T_PreKey, T_SigPreKey, T_Sess, T_Addr, T_ECPub, T_Bundle, T_Ciph> omemoStore, final OmemoDevice remoteDevice)\n
    '''
def decryptTransportedKey():
    '''returns CipherAndAuthTag\n\n
    decryptTransportedKey(final OmemoElement element, final int keyId)\n
    '''
def decryptMessageElement():
    '''returns Message\n\n
    decryptMessageElement(final OmemoElement element, final int keyId)\n
    '''
def getPreKeyId():
    '''returns int\n\n
    getPreKeyId()\n
    '''
def getIdentityKey():
    '''returns T_IdKey\n\n
    getIdentityKey()\n
    '''
def setIdentityKey():
    '''returns None\n\n
    setIdentityKey(final T_IdKey identityKey)\n
    '''
def getFingerprint():
    '''returns OmemoFingerprint\n\n
    getFingerprint()\n
    '''
