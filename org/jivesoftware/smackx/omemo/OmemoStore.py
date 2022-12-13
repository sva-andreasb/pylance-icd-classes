def OmemoStore():
'''public OmemoStore()
'''
pass
def getOmemoSessionOf():
'''public OmemoSession<T_IdKeyPair, T_IdKey, T_PreKey, T_SigPreKey, T_Sess, T_Addr, T_ECPub, T_Bundle, T_Ciph> getOmemoSessionOf(final OmemoManager omemoManager, final OmemoDevice device)
'''
pass
def generateOmemoIdentityKeyPair():
'''public T_IdKeyPair generateOmemoIdentityKeyPair()
'''
pass
def isTrustedOmemoIdentity():
'''public boolean isTrustedOmemoIdentity(final OmemoManager omemoManager, final OmemoDevice device, final T_IdKey identityKey)
'''
pass
def isDecidedOmemoIdentity():
'''public boolean isDecidedOmemoIdentity(final OmemoManager omemoManager, final OmemoDevice device, final T_IdKey identityKey)
'''
pass
def trustOmemoIdentity():
'''public void trustOmemoIdentity(final OmemoManager omemoManager, final OmemoDevice device, final T_IdKey identityKey)
'''
pass
def distrustOmemoIdentity():
'''public void distrustOmemoIdentity(final OmemoManager omemoManager, final OmemoDevice device, final T_IdKey identityKey)
'''
pass
def setDateOfLastReceivedMessage():
'''public void setDateOfLastReceivedMessage(final OmemoManager omemoManager, final OmemoDevice from)
'''
pass
def setDateOfLastSignedPreKeyRenewal():
'''public void setDateOfLastSignedPreKeyRenewal(final OmemoManager omemoManager)
'''
pass
def generateOmemoPreKeys():
'''public HashMap<Integer, T_PreKey> generateOmemoPreKeys(final int startId, final int count)
'''
pass
def storeOmemoPreKeys():
'''public void storeOmemoPreKeys(final OmemoManager omemoManager, final HashMap<Integer, T_PreKey> preKeyHashMap)
'''
pass
def generateOmemoSignedPreKey():
'''public T_SigPreKey generateOmemoSignedPreKey(final T_IdKeyPair identityKeyPair, final int signedPreKeyId)
'''
pass
def getFingerprint():
'''public OmemoFingerprint getFingerprint(final OmemoManager omemoManager)
public OmemoFingerprint getFingerprint(final OmemoManager omemoManager, final OmemoDevice device)
'''
pass
