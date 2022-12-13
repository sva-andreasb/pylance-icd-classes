def SignalOmemoStoreConnector():
    '''public SignalOmemoStoreConnector(final OmemoManager omemoManager, final OmemoStore<IdentityKeyPair, IdentityKey, PreKeyRecord, SignedPreKeyRecord, SessionRecord, SignalProtocolAddress, ECPublicKey, PreKeyBundle, SessionCipher> store)
    '''
def getIdentityKeyPair():
    '''public IdentityKeyPair getIdentityKeyPair()
    '''
def getLocalRegistrationId():
    '''public int getLocalRegistrationId()
    '''
def saveIdentity():
    '''public void saveIdentity(final SignalProtocolAddress signalProtocolAddress, final IdentityKey identityKey)
    '''
def isTrustedIdentity():
    '''public boolean isTrustedIdentity(final SignalProtocolAddress signalProtocolAddress, final IdentityKey identityKey)
    '''
def loadPreKey():
    '''public PreKeyRecord loadPreKey(final int i)
    '''
def storePreKey():
    '''public void storePreKey(final int i, final PreKeyRecord preKeyRecord)
    '''
def containsPreKey():
    '''public boolean containsPreKey(final int i)
    '''
def removePreKey():
    '''public void removePreKey(final int i)
    '''
def loadSession():
    '''public SessionRecord loadSession(final SignalProtocolAddress signalProtocolAddress)
    '''
def getSubDeviceSessions():
    '''public List<Integer> getSubDeviceSessions(final String s)
    '''
def storeSession():
    '''public void storeSession(final SignalProtocolAddress signalProtocolAddress, final SessionRecord sessionRecord)
    '''
def containsSession():
    '''public boolean containsSession(final SignalProtocolAddress signalProtocolAddress)
    '''
def deleteSession():
    '''public void deleteSession(final SignalProtocolAddress signalProtocolAddress)
    '''
def deleteAllSessions():
    '''public void deleteAllSessions(final String s)
    '''
def loadSignedPreKey():
    '''public SignedPreKeyRecord loadSignedPreKey(final int i)
    '''
def loadSignedPreKeys():
    '''public List<SignedPreKeyRecord> loadSignedPreKeys()
    '''
def storeSignedPreKey():
    '''public void storeSignedPreKey(final int i, final SignedPreKeyRecord signedPreKeyRecord)
    '''
def containsSignedPreKey():
    '''public boolean containsSignedPreKey(final int i)
    '''
def removeSignedPreKey():
    '''public void removeSignedPreKey(final int i)
    '''
