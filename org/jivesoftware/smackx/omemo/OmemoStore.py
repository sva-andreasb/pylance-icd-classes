def ():
    '''returns OmemoStore\n\n
    ()\n
    '''
def generateOmemoIdentityKeyPair():
    '''returns T_IdKeyPair\n\n
    generateOmemoIdentityKeyPair()\n
    '''
def isTrustedOmemoIdentity():
    '''returns boolean\n\n
    isTrustedOmemoIdentity(final OmemoManager omemoManager, final OmemoDevice device, final T_IdKey identityKey)\n
    '''
def isDecidedOmemoIdentity():
    '''returns boolean\n\n
    isDecidedOmemoIdentity(final OmemoManager omemoManager, final OmemoDevice device, final T_IdKey identityKey)\n
    '''
def trustOmemoIdentity():
    '''returns None\n\n
    trustOmemoIdentity(final OmemoManager omemoManager, final OmemoDevice device, final T_IdKey identityKey)\n
    '''
def distrustOmemoIdentity():
    '''returns None\n\n
    distrustOmemoIdentity(final OmemoManager omemoManager, final OmemoDevice device, final T_IdKey identityKey)\n
    '''
def setDateOfLastReceivedMessage():
    '''returns None\n\n
    setDateOfLastReceivedMessage(final OmemoManager omemoManager, final OmemoDevice from)\n
    '''
def setDateOfLastSignedPreKeyRenewal():
    '''returns None\n\n
    setDateOfLastSignedPreKeyRenewal(final OmemoManager omemoManager)\n
    '''
def storeOmemoPreKeys():
    '''returns None\n\n
    storeOmemoPreKeys(final OmemoManager omemoManager, final HashMap<Integer, T_PreKey> preKeyHashMap)\n
    '''
def generateOmemoSignedPreKey():
    '''returns T_SigPreKey\n\n
    generateOmemoSignedPreKey(final T_IdKeyPair identityKeyPair, final int signedPreKeyId)\n
    '''
def getFingerprint():
    '''returns OmemoFingerprint\n\n
    getFingerprint(final OmemoManager omemoManager)\n
    getFingerprint(final OmemoManager omemoManager, final OmemoDevice device)\n
    '''
