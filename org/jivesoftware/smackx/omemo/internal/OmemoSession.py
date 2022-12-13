def OmemoSession():
'''public OmemoSession(final OmemoManager omemoManager, final OmemoStore<T_IdKeyPair, T_IdKey, T_PreKey, T_SigPreKey, T_Sess, T_Addr, T_ECPub, T_Bundle, T_Ciph> omemoStore, final OmemoDevice remoteDevice, final T_IdKey identityKey)
public OmemoSession(final OmemoManager omemoManager, final OmemoStore<T_IdKeyPair, T_IdKey, T_PreKey, T_SigPreKey, T_Sess, T_Addr, T_ECPub, T_Bundle, T_Ciph> omemoStore, final OmemoDevice remoteDevice)
'''
pass
def decryptTransportedKey():
'''public CipherAndAuthTag decryptTransportedKey(final OmemoElement element, final int keyId)
'''
pass
def decryptMessageElement():
'''public static Message decryptMessageElement(final OmemoElement element, final CipherAndAuthTag cipherAndAuthTag)
public Message decryptMessageElement(final OmemoElement element, final int keyId)
'''
pass
def getPreKeyId():
'''public int getPreKeyId()
'''
pass
def getIdentityKey():
'''public T_IdKey getIdentityKey()
'''
pass
def setIdentityKey():
'''public void setIdentityKey(final T_IdKey identityKey)
'''
pass
def getFingerprint():
'''public OmemoFingerprint getFingerprint()
'''
pass
