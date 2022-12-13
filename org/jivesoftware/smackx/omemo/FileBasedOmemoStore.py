def FileBasedOmemoStore():
    '''public FileBasedOmemoStore()
    public FileBasedOmemoStore(final File basePath)
    '''
def isFreshInstallation():
    '''public boolean isFreshInstallation(final OmemoManager omemoManager)
    '''
def getDefaultDeviceId():
    '''public int getDefaultDeviceId(final BareJid user)
    '''
def setDefaultDeviceId():
    '''public void setDefaultDeviceId(final BareJid user, final int defaultDeviceId)
    '''
def loadLastPreKeyId():
    '''public int loadLastPreKeyId(final OmemoManager omemoManager)
    '''
def storeLastPreKeyId():
    '''public void storeLastPreKeyId(final OmemoManager omemoManager, final int currentPreKeyId)
    '''
def loadOmemoIdentityKeyPair():
    '''public T_IdKeyPair loadOmemoIdentityKeyPair(final OmemoManager omemoManager)
    '''
def storeOmemoIdentityKeyPair():
    '''public void storeOmemoIdentityKeyPair(final OmemoManager omemoManager, final T_IdKeyPair identityKeyPair)
    '''
def loadOmemoIdentityKey():
    '''public T_IdKey loadOmemoIdentityKey(final OmemoManager omemoManager, final OmemoDevice device)
    '''
def storeOmemoIdentityKey():
    '''public void storeOmemoIdentityKey(final OmemoManager omemoManager, final OmemoDevice device, final T_IdKey t_idKey)
    '''
def isTrustedOmemoIdentity():
    '''public boolean isTrustedOmemoIdentity(final OmemoManager omemoManager, final OmemoDevice device, final OmemoFingerprint fingerprint)
    '''
def isDecidedOmemoIdentity():
    '''public boolean isDecidedOmemoIdentity(final OmemoManager omemoManager, final OmemoDevice device, final OmemoFingerprint fingerprint)
    '''
def trustOmemoIdentity():
    '''public void trustOmemoIdentity(final OmemoManager omemoManager, final OmemoDevice device, final OmemoFingerprint fingerprint)
    '''
def distrustOmemoIdentity():
    '''public void distrustOmemoIdentity(final OmemoManager omemoManager, final OmemoDevice device, final OmemoFingerprint fingerprint)
    '''
def setDateOfLastReceivedMessage():
    '''public void setDateOfLastReceivedMessage(final OmemoManager omemoManager, final OmemoDevice from, final Date date)
    '''
def getDateOfLastReceivedMessage():
    '''public Date getDateOfLastReceivedMessage(final OmemoManager omemoManager, final OmemoDevice from)
    '''
def setDateOfLastSignedPreKeyRenewal():
    '''public void setDateOfLastSignedPreKeyRenewal(final OmemoManager omemoManager, final Date date)
    '''
def getDateOfLastSignedPreKeyRenewal():
    '''public Date getDateOfLastSignedPreKeyRenewal(final OmemoManager omemoManager)
    '''
def loadOmemoPreKey():
    '''public T_PreKey loadOmemoPreKey(final OmemoManager omemoManager, final int preKeyId)
    '''
def storeOmemoPreKey():
    '''public void storeOmemoPreKey(final OmemoManager omemoManager, final int preKeyId, final T_PreKey t_preKey)
    '''
def removeOmemoPreKey():
    '''public void removeOmemoPreKey(final OmemoManager omemoManager, final int preKeyId)
    '''
def loadCurrentSignedPreKeyId():
    '''public int loadCurrentSignedPreKeyId(final OmemoManager omemoManager)
    '''
def storeCurrentSignedPreKeyId():
    '''public void storeCurrentSignedPreKeyId(final OmemoManager omemoManager, final int currentSignedPreKeyId)
    '''
def loadOmemoPreKeys():
    '''public HashMap<Integer, T_PreKey> loadOmemoPreKeys(final OmemoManager omemoManager)
    '''
def loadOmemoSignedPreKey():
    '''public T_SigPreKey loadOmemoSignedPreKey(final OmemoManager omemoManager, final int signedPreKeyId)
    '''
def loadOmemoSignedPreKeys():
    '''public HashMap<Integer, T_SigPreKey> loadOmemoSignedPreKeys(final OmemoManager omemoManager)
    '''
def storeOmemoSignedPreKey():
    '''public void storeOmemoSignedPreKey(final OmemoManager omemoManager, final int signedPreKeyId, final T_SigPreKey signedPreKey)
    '''
def removeOmemoSignedPreKey():
    '''public void removeOmemoSignedPreKey(final OmemoManager omemoManager, final int signedPreKeyId)
    '''
def loadRawSession():
    '''public T_Sess loadRawSession(final OmemoManager omemoManager, final OmemoDevice device)
    '''
def loadAllRawSessionsOf():
    '''public HashMap<Integer, T_Sess> loadAllRawSessionsOf(final OmemoManager omemoManager, final BareJid contact)
    '''
def storeRawSession():
    '''public void storeRawSession(final OmemoManager omemoManager, final OmemoDevice device, final T_Sess session)
    '''
def removeRawSession():
    '''public void removeRawSession(final OmemoManager omemoManager, final OmemoDevice device)
    '''
def removeAllRawSessionsOf():
    '''public void removeAllRawSessionsOf(final OmemoManager omemoManager, final BareJid contact)
    '''
def containsRawSession():
    '''public boolean containsRawSession(final OmemoManager omemoManager, final OmemoDevice device)
    '''
def loadCachedDeviceList():
    '''public CachedDeviceList loadCachedDeviceList(final OmemoManager omemoManager, final BareJid contact)
    '''
def storeCachedDeviceList():
    '''public void storeCachedDeviceList(final OmemoManager omemoManager, final BareJid contact, final CachedDeviceList deviceList)
    '''
def purgeOwnDeviceKeys():
    '''public void purgeOwnDeviceKeys(final OmemoManager omemoManager)
    '''
def deleteDirectory():
    '''public static void deleteDirectory(final File root)
    '''
