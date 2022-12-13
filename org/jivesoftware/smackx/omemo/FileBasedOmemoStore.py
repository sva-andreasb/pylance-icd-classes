def FileBasedOmemoStore():
'''public FileBasedOmemoStore()
public FileBasedOmemoStore(final File basePath)
'''
pass
def isFreshInstallation():
'''public boolean isFreshInstallation(final OmemoManager omemoManager)
'''
pass
def getDefaultDeviceId():
'''public int getDefaultDeviceId(final BareJid user)
'''
pass
def setDefaultDeviceId():
'''public void setDefaultDeviceId(final BareJid user, final int defaultDeviceId)
'''
pass
def loadLastPreKeyId():
'''public int loadLastPreKeyId(final OmemoManager omemoManager)
'''
pass
def storeLastPreKeyId():
'''public void storeLastPreKeyId(final OmemoManager omemoManager, final int currentPreKeyId)
'''
pass
def loadOmemoIdentityKeyPair():
'''public T_IdKeyPair loadOmemoIdentityKeyPair(final OmemoManager omemoManager)
'''
pass
def storeOmemoIdentityKeyPair():
'''public void storeOmemoIdentityKeyPair(final OmemoManager omemoManager, final T_IdKeyPair identityKeyPair)
'''
pass
def loadOmemoIdentityKey():
'''public T_IdKey loadOmemoIdentityKey(final OmemoManager omemoManager, final OmemoDevice device)
'''
pass
def storeOmemoIdentityKey():
'''public void storeOmemoIdentityKey(final OmemoManager omemoManager, final OmemoDevice device, final T_IdKey t_idKey)
'''
pass
def isTrustedOmemoIdentity():
'''public boolean isTrustedOmemoIdentity(final OmemoManager omemoManager, final OmemoDevice device, final OmemoFingerprint fingerprint)
'''
pass
def isDecidedOmemoIdentity():
'''public boolean isDecidedOmemoIdentity(final OmemoManager omemoManager, final OmemoDevice device, final OmemoFingerprint fingerprint)
'''
pass
def trustOmemoIdentity():
'''public void trustOmemoIdentity(final OmemoManager omemoManager, final OmemoDevice device, final OmemoFingerprint fingerprint)
'''
pass
def distrustOmemoIdentity():
'''public void distrustOmemoIdentity(final OmemoManager omemoManager, final OmemoDevice device, final OmemoFingerprint fingerprint)
'''
pass
def setDateOfLastReceivedMessage():
'''public void setDateOfLastReceivedMessage(final OmemoManager omemoManager, final OmemoDevice from, final Date date)
'''
pass
def getDateOfLastReceivedMessage():
'''public Date getDateOfLastReceivedMessage(final OmemoManager omemoManager, final OmemoDevice from)
'''
pass
def setDateOfLastSignedPreKeyRenewal():
'''public void setDateOfLastSignedPreKeyRenewal(final OmemoManager omemoManager, final Date date)
'''
pass
def getDateOfLastSignedPreKeyRenewal():
'''public Date getDateOfLastSignedPreKeyRenewal(final OmemoManager omemoManager)
'''
pass
def loadOmemoPreKey():
'''public T_PreKey loadOmemoPreKey(final OmemoManager omemoManager, final int preKeyId)
'''
pass
def storeOmemoPreKey():
'''public void storeOmemoPreKey(final OmemoManager omemoManager, final int preKeyId, final T_PreKey t_preKey)
'''
pass
def removeOmemoPreKey():
'''public void removeOmemoPreKey(final OmemoManager omemoManager, final int preKeyId)
'''
pass
def loadCurrentSignedPreKeyId():
'''public int loadCurrentSignedPreKeyId(final OmemoManager omemoManager)
'''
pass
def storeCurrentSignedPreKeyId():
'''public void storeCurrentSignedPreKeyId(final OmemoManager omemoManager, final int currentSignedPreKeyId)
'''
pass
def loadOmemoPreKeys():
'''public HashMap<Integer, T_PreKey> loadOmemoPreKeys(final OmemoManager omemoManager)
'''
pass
def loadOmemoSignedPreKey():
'''public T_SigPreKey loadOmemoSignedPreKey(final OmemoManager omemoManager, final int signedPreKeyId)
'''
pass
def loadOmemoSignedPreKeys():
'''public HashMap<Integer, T_SigPreKey> loadOmemoSignedPreKeys(final OmemoManager omemoManager)
'''
pass
def storeOmemoSignedPreKey():
'''public void storeOmemoSignedPreKey(final OmemoManager omemoManager, final int signedPreKeyId, final T_SigPreKey signedPreKey)
'''
pass
def removeOmemoSignedPreKey():
'''public void removeOmemoSignedPreKey(final OmemoManager omemoManager, final int signedPreKeyId)
'''
pass
def loadRawSession():
'''public T_Sess loadRawSession(final OmemoManager omemoManager, final OmemoDevice device)
'''
pass
def loadAllRawSessionsOf():
'''public HashMap<Integer, T_Sess> loadAllRawSessionsOf(final OmemoManager omemoManager, final BareJid contact)
'''
pass
def storeRawSession():
'''public void storeRawSession(final OmemoManager omemoManager, final OmemoDevice device, final T_Sess session)
'''
pass
def removeRawSession():
'''public void removeRawSession(final OmemoManager omemoManager, final OmemoDevice device)
'''
pass
def removeAllRawSessionsOf():
'''public void removeAllRawSessionsOf(final OmemoManager omemoManager, final BareJid contact)
'''
pass
def containsRawSession():
'''public boolean containsRawSession(final OmemoManager omemoManager, final OmemoDevice device)
'''
pass
def loadCachedDeviceList():
'''public CachedDeviceList loadCachedDeviceList(final OmemoManager omemoManager, final BareJid contact)
'''
pass
def storeCachedDeviceList():
'''public void storeCachedDeviceList(final OmemoManager omemoManager, final BareJid contact, final CachedDeviceList deviceList)
'''
pass
def purgeOwnDeviceKeys():
'''public void purgeOwnDeviceKeys(final OmemoManager omemoManager)
'''
pass
def deleteDirectory():
'''public static void deleteDirectory(final File root)
'''
pass