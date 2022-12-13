def generateOmemoIdentityKeyPair():
    '''public IdentityKeyPair generateOmemoIdentityKeyPair()
    '''
def generateOmemoPreKeys():
    '''public HashMap<Integer, PreKeyRecord> generateOmemoPreKeys(final int currentPreKeyId, final int count)
    '''
def generateOmemoSignedPreKey():
    '''public SignedPreKeyRecord generateOmemoSignedPreKey(final IdentityKeyPair identityKeyPair, final int currentPreKeyId)
    '''
def signedPreKeyFromBytes():
    '''public SignedPreKeyRecord signedPreKeyFromBytes(final byte[] data)
    '''
def signedPreKeyToBytes():
    '''public byte[] signedPreKeyToBytes(final SignedPreKeyRecord signedPreKeyRecord)
    '''
def createOmemoSession():
    '''public OmemoSession<IdentityKeyPair, IdentityKey, PreKeyRecord, SignedPreKeyRecord, SessionRecord, SignalProtocolAddress, ECPublicKey, PreKeyBundle, SessionCipher> createOmemoSession(final OmemoManager omemoManager, final OmemoStore<IdentityKeyPair, IdentityKey, PreKeyRecord, SignedPreKeyRecord, SessionRecord, SignalProtocolAddress, ECPublicKey, PreKeyBundle, SessionCipher> omemoStore, final OmemoDevice contact, final IdentityKey identityKey)
    public OmemoSession<IdentityKeyPair, IdentityKey, PreKeyRecord, SignedPreKeyRecord, SessionRecord, SignalProtocolAddress, ECPublicKey, PreKeyBundle, SessionCipher> createOmemoSession(final OmemoManager omemoManager, final OmemoStore<IdentityKeyPair, IdentityKey, PreKeyRecord, SignedPreKeyRecord, SessionRecord, SignalProtocolAddress, ECPublicKey, PreKeyBundle, SessionCipher> omemoStore, final OmemoDevice from)
    '''
def rawSessionFromBytes():
    '''public SessionRecord rawSessionFromBytes(final byte[] data)
    '''
def rawSessionToBytes():
    '''public byte[] rawSessionToBytes(final SessionRecord session)
    '''
def identityKeyPairFromBytes():
    '''public IdentityKeyPair identityKeyPairFromBytes(final byte[] data)
    '''
def identityKeyFromBytes():
    '''public IdentityKey identityKeyFromBytes(final byte[] data)
    '''
def ellipticCurvePublicKeyFromBytes():
    '''public ECPublicKey ellipticCurvePublicKeyFromBytes(final byte[] data)
    '''
def preKeyToBytes():
    '''public byte[] preKeyToBytes(final PreKeyRecord preKeyRecord)
    '''
def preKeyFromBytes():
    '''public PreKeyRecord preKeyFromBytes(final byte[] bytes)
    '''
def bundleFromOmemoBundle():
    '''public PreKeyBundle bundleFromOmemoBundle(final OmemoBundleVAxolotlElement bundle, final OmemoDevice contact, final int preKeyId)
    '''
def signedPreKeySignatureFromKey():
    '''public byte[] signedPreKeySignatureFromKey(final SignedPreKeyRecord signedPreKey)
    '''
def signedPreKeyIdFromKey():
    '''public int signedPreKeyIdFromKey(final SignedPreKeyRecord signedPreKey)
    '''
def identityKeyPairToBytes():
    '''public byte[] identityKeyPairToBytes(final IdentityKeyPair identityKeyPair)
    '''
def identityKeyFromPair():
    '''public IdentityKey identityKeyFromPair(final IdentityKeyPair identityKeyPair)
    '''
def identityKeyForBundle():
    '''public byte[] identityKeyForBundle(final IdentityKey identityKey)
    '''
def identityKeyToBytes():
    '''public byte[] identityKeyToBytes(final IdentityKey identityKey)
    '''
def preKeyPublicKeyForBundle():
    '''public byte[] preKeyPublicKeyForBundle(final ECPublicKey preKey)
    '''
def preKeyForBundle():
    '''public byte[] preKeyForBundle(final PreKeyRecord preKeyRecord)
    '''
def signedPreKeyPublicForBundle():
    '''public byte[] signedPreKeyPublicForBundle(final SignedPreKeyRecord signedPreKey)
    '''
def getFingerprint():
    '''public OmemoFingerprint getFingerprint(final IdentityKey identityKey)
    '''
def omemoDeviceAsAddress():
    '''public SignalProtocolAddress omemoDeviceAsAddress(final OmemoDevice contact)
    '''
def addressAsOmemoDevice():
    '''public OmemoDevice addressAsOmemoDevice(final SignalProtocolAddress address)
    '''
