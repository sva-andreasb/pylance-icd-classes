def generateOmemoIdentityKeyPair():
    '''returns IdentityKeyPair\n\n
    generateOmemoIdentityKeyPair()\n
    '''
def generateOmemoSignedPreKey():
    '''returns SignedPreKeyRecord\n\n
    generateOmemoSignedPreKey(final IdentityKeyPair identityKeyPair, final int currentPreKeyId)\n
    '''
def signedPreKeyFromBytes():
    '''returns SignedPreKeyRecord\n\n
    signedPreKeyFromBytes(final byte[] data)\n
    '''
def signedPreKeyToBytes():
    '''returns byte[]\n\n
    signedPreKeyToBytes(final SignedPreKeyRecord signedPreKeyRecord)\n
    '''
def rawSessionFromBytes():
    '''returns SessionRecord\n\n
    rawSessionFromBytes(final byte[] data)\n
    '''
def rawSessionToBytes():
    '''returns byte[]\n\n
    rawSessionToBytes(final SessionRecord session)\n
    '''
def identityKeyPairFromBytes():
    '''returns IdentityKeyPair\n\n
    identityKeyPairFromBytes(final byte[] data)\n
    '''
def identityKeyFromBytes():
    '''returns IdentityKey\n\n
    identityKeyFromBytes(final byte[] data)\n
    '''
def ellipticCurvePublicKeyFromBytes():
    '''returns ECPublicKey\n\n
    ellipticCurvePublicKeyFromBytes(final byte[] data)\n
    '''
def preKeyToBytes():
    '''returns byte[]\n\n
    preKeyToBytes(final PreKeyRecord preKeyRecord)\n
    '''
def preKeyFromBytes():
    '''returns PreKeyRecord\n\n
    preKeyFromBytes(final byte[] bytes)\n
    '''
def bundleFromOmemoBundle():
    '''returns PreKeyBundle\n\n
    bundleFromOmemoBundle(final OmemoBundleVAxolotlElement bundle, final OmemoDevice contact, final int preKeyId)\n
    '''
def signedPreKeySignatureFromKey():
    '''returns byte[]\n\n
    signedPreKeySignatureFromKey(final SignedPreKeyRecord signedPreKey)\n
    '''
def signedPreKeyIdFromKey():
    '''returns int\n\n
    signedPreKeyIdFromKey(final SignedPreKeyRecord signedPreKey)\n
    '''
def identityKeyPairToBytes():
    '''returns byte[]\n\n
    identityKeyPairToBytes(final IdentityKeyPair identityKeyPair)\n
    '''
def identityKeyFromPair():
    '''returns IdentityKey\n\n
    identityKeyFromPair(final IdentityKeyPair identityKeyPair)\n
    '''
def identityKeyForBundle():
    '''returns byte[]\n\n
    identityKeyForBundle(final IdentityKey identityKey)\n
    '''
def identityKeyToBytes():
    '''returns byte[]\n\n
    identityKeyToBytes(final IdentityKey identityKey)\n
    '''
def preKeyPublicKeyForBundle():
    '''returns byte[]\n\n
    preKeyPublicKeyForBundle(final ECPublicKey preKey)\n
    '''
def preKeyForBundle():
    '''returns byte[]\n\n
    preKeyForBundle(final PreKeyRecord preKeyRecord)\n
    '''
def signedPreKeyPublicForBundle():
    '''returns byte[]\n\n
    signedPreKeyPublicForBundle(final SignedPreKeyRecord signedPreKey)\n
    '''
def getFingerprint():
    '''returns OmemoFingerprint\n\n
    getFingerprint(final IdentityKey identityKey)\n
    '''
def omemoDeviceAsAddress():
    '''returns SignalProtocolAddress\n\n
    omemoDeviceAsAddress(final OmemoDevice contact)\n
    '''
def addressAsOmemoDevice():
    '''returns OmemoDevice\n\n
    addressAsOmemoDevice(final SignalProtocolAddress address)\n
    '''
