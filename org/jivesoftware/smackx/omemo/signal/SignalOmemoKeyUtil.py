def generateOmemoIdentityKeyPair():
'''public IdentityKeyPair generateOmemoIdentityKeyPair()
'''
pass
def generateOmemoPreKeys():
'''public HashMap<Integer, PreKeyRecord> generateOmemoPreKeys(final int currentPreKeyId, final int count)
'''
pass
def generateOmemoSignedPreKey():
'''public SignedPreKeyRecord generateOmemoSignedPreKey(final IdentityKeyPair identityKeyPair, final int currentPreKeyId)
'''
pass
def signedPreKeyFromBytes():
'''public SignedPreKeyRecord signedPreKeyFromBytes(final byte[] data)
'''
pass
def signedPreKeyToBytes():
'''public byte[] signedPreKeyToBytes(final SignedPreKeyRecord signedPreKeyRecord)
'''
pass
def createOmemoSession():
'''public OmemoSession<IdentityKeyPair, IdentityKey, PreKeyRecord, SignedPreKeyRecord, SessionRecord, SignalProtocolAddress, ECPublicKey, PreKeyBundle, SessionCipher> createOmemoSession(final OmemoManager omemoManager, final OmemoStore<IdentityKeyPair, IdentityKey, PreKeyRecord, SignedPreKeyRecord, SessionRecord, SignalProtocolAddress, ECPublicKey, PreKeyBundle, SessionCipher> omemoStore, final OmemoDevice contact, final IdentityKey identityKey)
public OmemoSession<IdentityKeyPair, IdentityKey, PreKeyRecord, SignedPreKeyRecord, SessionRecord, SignalProtocolAddress, ECPublicKey, PreKeyBundle, SessionCipher> createOmemoSession(final OmemoManager omemoManager, final OmemoStore<IdentityKeyPair, IdentityKey, PreKeyRecord, SignedPreKeyRecord, SessionRecord, SignalProtocolAddress, ECPublicKey, PreKeyBundle, SessionCipher> omemoStore, final OmemoDevice from)
'''
pass
def rawSessionFromBytes():
'''public SessionRecord rawSessionFromBytes(final byte[] data)
'''
pass
def rawSessionToBytes():
'''public byte[] rawSessionToBytes(final SessionRecord session)
'''
pass
def identityKeyPairFromBytes():
'''public IdentityKeyPair identityKeyPairFromBytes(final byte[] data)
'''
pass
def identityKeyFromBytes():
'''public IdentityKey identityKeyFromBytes(final byte[] data)
'''
pass
def ellipticCurvePublicKeyFromBytes():
'''public ECPublicKey ellipticCurvePublicKeyFromBytes(final byte[] data)
'''
pass
def preKeyToBytes():
'''public byte[] preKeyToBytes(final PreKeyRecord preKeyRecord)
'''
pass
def preKeyFromBytes():
'''public PreKeyRecord preKeyFromBytes(final byte[] bytes)
'''
pass
def bundleFromOmemoBundle():
'''public PreKeyBundle bundleFromOmemoBundle(final OmemoBundleVAxolotlElement bundle, final OmemoDevice contact, final int preKeyId)
'''
pass
def signedPreKeySignatureFromKey():
'''public byte[] signedPreKeySignatureFromKey(final SignedPreKeyRecord signedPreKey)
'''
pass
def signedPreKeyIdFromKey():
'''public int signedPreKeyIdFromKey(final SignedPreKeyRecord signedPreKey)
'''
pass
def identityKeyPairToBytes():
'''public byte[] identityKeyPairToBytes(final IdentityKeyPair identityKeyPair)
'''
pass
def identityKeyFromPair():
'''public IdentityKey identityKeyFromPair(final IdentityKeyPair identityKeyPair)
'''
pass
def identityKeyForBundle():
'''public byte[] identityKeyForBundle(final IdentityKey identityKey)
'''
pass
def identityKeyToBytes():
'''public byte[] identityKeyToBytes(final IdentityKey identityKey)
'''
pass
def preKeyPublicKeyForBundle():
'''public byte[] preKeyPublicKeyForBundle(final ECPublicKey preKey)
'''
pass
def preKeyForBundle():
'''public byte[] preKeyForBundle(final PreKeyRecord preKeyRecord)
'''
pass
def signedPreKeyPublicForBundle():
'''public byte[] signedPreKeyPublicForBundle(final SignedPreKeyRecord signedPreKey)
'''
pass
def getFingerprint():
'''public OmemoFingerprint getFingerprint(final IdentityKey identityKey)
'''
pass
def omemoDeviceAsAddress():
'''public SignalProtocolAddress omemoDeviceAsAddress(final OmemoDevice contact)
'''
pass
def addressAsOmemoDevice():
'''public OmemoDevice addressAsOmemoDevice(final SignalProtocolAddress address)
'''
pass
