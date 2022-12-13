def SignalOmemoStoreConnector():
'''public SignalOmemoStoreConnector(final OmemoManager omemoManager, final OmemoStore<IdentityKeyPair, IdentityKey, PreKeyRecord, SignedPreKeyRecord, SessionRecord, SignalProtocolAddress, ECPublicKey, PreKeyBundle, SessionCipher> store)
'''
pass
def getIdentityKeyPair():
'''public IdentityKeyPair getIdentityKeyPair()
'''
pass
def getLocalRegistrationId():
'''public int getLocalRegistrationId()
'''
pass
def saveIdentity():
'''public void saveIdentity(final SignalProtocolAddress signalProtocolAddress, final IdentityKey identityKey)
'''
pass
def isTrustedIdentity():
'''public boolean isTrustedIdentity(final SignalProtocolAddress signalProtocolAddress, final IdentityKey identityKey)
'''
pass
def loadPreKey():
'''public PreKeyRecord loadPreKey(final int i)
'''
pass
def storePreKey():
'''public void storePreKey(final int i, final PreKeyRecord preKeyRecord)
'''
pass
def containsPreKey():
'''public boolean containsPreKey(final int i)
'''
pass
def removePreKey():
'''public void removePreKey(final int i)
'''
pass
def loadSession():
'''public SessionRecord loadSession(final SignalProtocolAddress signalProtocolAddress)
'''
pass
def getSubDeviceSessions():
'''public List<Integer> getSubDeviceSessions(final String s)
'''
pass
def storeSession():
'''public void storeSession(final SignalProtocolAddress signalProtocolAddress, final SessionRecord sessionRecord)
'''
pass
def containsSession():
'''public boolean containsSession(final SignalProtocolAddress signalProtocolAddress)
'''
pass
def deleteSession():
'''public void deleteSession(final SignalProtocolAddress signalProtocolAddress)
'''
pass
def deleteAllSessions():
'''public void deleteAllSessions(final String s)
'''
pass
def loadSignedPreKey():
'''public SignedPreKeyRecord loadSignedPreKey(final int i)
'''
pass
def loadSignedPreKeys():
'''public List<SignedPreKeyRecord> loadSignedPreKeys()
'''
pass
def storeSignedPreKey():
'''public void storeSignedPreKey(final int i, final SignedPreKeyRecord signedPreKeyRecord)
'''
pass
def containsSignedPreKey():
'''public boolean containsSignedPreKey(final int i)
'''
pass
def removeSignedPreKey():
'''public void removeSignedPreKey(final int i)
'''
pass
