def ():
    '''returns SignalOmemoStoreConnector\n\n
    (final OmemoManager omemoManager, final OmemoStore<IdentityKeyPair, IdentityKey, PreKeyRecord, SignedPreKeyRecord, SessionRecord, SignalProtocolAddress, ECPublicKey, PreKeyBundle, SessionCipher> store)\n
    '''
def getIdentityKeyPair():
    '''returns IdentityKeyPair\n\n
    getIdentityKeyPair()\n
    '''
def getLocalRegistrationId():
    '''returns int\n\n
    getLocalRegistrationId()\n
    '''
def saveIdentity():
    '''returns None\n\n
    saveIdentity(final SignalProtocolAddress signalProtocolAddress, final IdentityKey identityKey)\n
    '''
def isTrustedIdentity():
    '''returns boolean\n\n
    isTrustedIdentity(final SignalProtocolAddress signalProtocolAddress, final IdentityKey identityKey)\n
    '''
def loadPreKey():
    '''returns PreKeyRecord\n\n
    loadPreKey(final int i)\n
    '''
def storePreKey():
    '''returns None\n\n
    storePreKey(final int i, final PreKeyRecord preKeyRecord)\n
    '''
def containsPreKey():
    '''returns boolean\n\n
    containsPreKey(final int i)\n
    '''
def removePreKey():
    '''returns None\n\n
    removePreKey(final int i)\n
    '''
def loadSession():
    '''returns SessionRecord\n\n
    loadSession(final SignalProtocolAddress signalProtocolAddress)\n
    '''
def getSubDeviceSessions():
    '''returns List<Integer>\n\n
    getSubDeviceSessions(final String s)\n
    '''
def storeSession():
    '''returns None\n\n
    storeSession(final SignalProtocolAddress signalProtocolAddress, final SessionRecord sessionRecord)\n
    '''
def containsSession():
    '''returns boolean\n\n
    containsSession(final SignalProtocolAddress signalProtocolAddress)\n
    '''
def deleteSession():
    '''returns None\n\n
    deleteSession(final SignalProtocolAddress signalProtocolAddress)\n
    '''
def deleteAllSessions():
    '''returns None\n\n
    deleteAllSessions(final String s)\n
    '''
def loadSignedPreKey():
    '''returns SignedPreKeyRecord\n\n
    loadSignedPreKey(final int i)\n
    '''
def loadSignedPreKeys():
    '''returns List<SignedPreKeyRecord>\n\n
    loadSignedPreKeys()\n
    '''
def storeSignedPreKey():
    '''returns None\n\n
    storeSignedPreKey(final int i, final SignedPreKeyRecord signedPreKeyRecord)\n
    '''
def containsSignedPreKey():
    '''returns boolean\n\n
    containsSignedPreKey(final int i)\n
    '''
def removeSignedPreKey():
    '''returns None\n\n
    removeSignedPreKey(final int i)\n
    '''
