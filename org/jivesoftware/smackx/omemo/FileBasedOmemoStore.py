def ():
    '''returns FileBasedOmemoStore\n\n
    ()\n
    (final File basePath)\n
    '''
def isFreshInstallation():
    '''returns boolean\n\n
    isFreshInstallation(final OmemoManager omemoManager)\n
    '''
def getDefaultDeviceId():
    '''returns int\n\n
    getDefaultDeviceId(final BareJid user)\n
    '''
def setDefaultDeviceId():
    '''returns None\n\n
    setDefaultDeviceId(final BareJid user, final int defaultDeviceId)\n
    '''
def loadLastPreKeyId():
    '''returns int\n\n
    loadLastPreKeyId(final OmemoManager omemoManager)\n
    '''
def storeLastPreKeyId():
    '''returns None\n\n
    storeLastPreKeyId(final OmemoManager omemoManager, final int currentPreKeyId)\n
    '''
def loadOmemoIdentityKeyPair():
    '''returns T_IdKeyPair\n\n
    loadOmemoIdentityKeyPair(final OmemoManager omemoManager)\n
    '''
def storeOmemoIdentityKeyPair():
    '''returns None\n\n
    storeOmemoIdentityKeyPair(final OmemoManager omemoManager, final T_IdKeyPair identityKeyPair)\n
    '''
def loadOmemoIdentityKey():
    '''returns T_IdKey\n\n
    loadOmemoIdentityKey(final OmemoManager omemoManager, final OmemoDevice device)\n
    '''
def storeOmemoIdentityKey():
    '''returns None\n\n
    storeOmemoIdentityKey(final OmemoManager omemoManager, final OmemoDevice device, final T_IdKey t_idKey)\n
    '''
def isTrustedOmemoIdentity():
    '''returns boolean\n\n
    isTrustedOmemoIdentity(final OmemoManager omemoManager, final OmemoDevice device, final OmemoFingerprint fingerprint)\n
    '''
def isDecidedOmemoIdentity():
    '''returns boolean\n\n
    isDecidedOmemoIdentity(final OmemoManager omemoManager, final OmemoDevice device, final OmemoFingerprint fingerprint)\n
    '''
def trustOmemoIdentity():
    '''returns None\n\n
    trustOmemoIdentity(final OmemoManager omemoManager, final OmemoDevice device, final OmemoFingerprint fingerprint)\n
    '''
def distrustOmemoIdentity():
    '''returns None\n\n
    distrustOmemoIdentity(final OmemoManager omemoManager, final OmemoDevice device, final OmemoFingerprint fingerprint)\n
    '''
def setDateOfLastReceivedMessage():
    '''returns None\n\n
    setDateOfLastReceivedMessage(final OmemoManager omemoManager, final OmemoDevice from, final Date date)\n
    '''
def getDateOfLastReceivedMessage():
    '''returns Date\n\n
    getDateOfLastReceivedMessage(final OmemoManager omemoManager, final OmemoDevice from)\n
    '''
def setDateOfLastSignedPreKeyRenewal():
    '''returns None\n\n
    setDateOfLastSignedPreKeyRenewal(final OmemoManager omemoManager, final Date date)\n
    '''
def getDateOfLastSignedPreKeyRenewal():
    '''returns Date\n\n
    getDateOfLastSignedPreKeyRenewal(final OmemoManager omemoManager)\n
    '''
def loadOmemoPreKey():
    '''returns T_PreKey\n\n
    loadOmemoPreKey(final OmemoManager omemoManager, final int preKeyId)\n
    '''
def storeOmemoPreKey():
    '''returns None\n\n
    storeOmemoPreKey(final OmemoManager omemoManager, final int preKeyId, final T_PreKey t_preKey)\n
    '''
def removeOmemoPreKey():
    '''returns None\n\n
    removeOmemoPreKey(final OmemoManager omemoManager, final int preKeyId)\n
    '''
def loadCurrentSignedPreKeyId():
    '''returns int\n\n
    loadCurrentSignedPreKeyId(final OmemoManager omemoManager)\n
    '''
def storeCurrentSignedPreKeyId():
    '''returns None\n\n
    storeCurrentSignedPreKeyId(final OmemoManager omemoManager, final int currentSignedPreKeyId)\n
    '''
def loadOmemoSignedPreKey():
    '''returns T_SigPreKey\n\n
    loadOmemoSignedPreKey(final OmemoManager omemoManager, final int signedPreKeyId)\n
    '''
def storeOmemoSignedPreKey():
    '''returns None\n\n
    storeOmemoSignedPreKey(final OmemoManager omemoManager, final int signedPreKeyId, final T_SigPreKey signedPreKey)\n
    '''
def removeOmemoSignedPreKey():
    '''returns None\n\n
    removeOmemoSignedPreKey(final OmemoManager omemoManager, final int signedPreKeyId)\n
    '''
def loadRawSession():
    '''returns T_Sess\n\n
    loadRawSession(final OmemoManager omemoManager, final OmemoDevice device)\n
    '''
def storeRawSession():
    '''returns None\n\n
    storeRawSession(final OmemoManager omemoManager, final OmemoDevice device, final T_Sess session)\n
    '''
def removeRawSession():
    '''returns None\n\n
    removeRawSession(final OmemoManager omemoManager, final OmemoDevice device)\n
    '''
def removeAllRawSessionsOf():
    '''returns None\n\n
    removeAllRawSessionsOf(final OmemoManager omemoManager, final BareJid contact)\n
    '''
def containsRawSession():
    '''returns boolean\n\n
    containsRawSession(final OmemoManager omemoManager, final OmemoDevice device)\n
    '''
def loadCachedDeviceList():
    '''returns CachedDeviceList\n\n
    loadCachedDeviceList(final OmemoManager omemoManager, final BareJid contact)\n
    '''
def storeCachedDeviceList():
    '''returns None\n\n
    storeCachedDeviceList(final OmemoManager omemoManager, final BareJid contact, final CachedDeviceList deviceList)\n
    '''
def purgeOwnDeviceKeys():
    '''returns None\n\n
    purgeOwnDeviceKeys(final OmemoManager omemoManager)\n
    '''
