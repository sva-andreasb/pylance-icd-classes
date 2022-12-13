def OmemoKeyUtil():
    '''public OmemoKeyUtil()
    '''
def preKeyPublicFromBytes():
    '''public T_ECPub preKeyPublicFromBytes(final byte[] data)
    '''
def signedPreKeyPublicFromBytes():
    '''public T_ECPub signedPreKeyPublicFromBytes(final byte[] data)
    '''
def preKeyPublisKeysForBundle():
    '''public HashMap<Integer, byte[]> preKeyPublisKeysForBundle(final HashMap<Integer, T_PreKey> preKeyHashMap)
    '''
def prettyFingerprint():
    '''public static String prettyFingerprint(final OmemoFingerprint fingerprint)
    public static String prettyFingerprint(final String ugly)
    '''
def addInBounds():
    '''public static int addInBounds(final int value, final int added)
    '''
def identityKey():
    '''public T_IdKey identityKey(final OmemoBundleVAxolotlElement bundle)
    '''
def signedPreKeyPublic():
    '''public T_ECPub signedPreKeyPublic(final OmemoBundleVAxolotlElement bundle)
    '''
def signedPreKeyId():
    '''public int signedPreKeyId(final OmemoBundleVAxolotlElement bundle)
    '''
def signedPreKeySignature():
    '''public byte[] signedPreKeySignature(final OmemoBundleVAxolotlElement bundle)
    '''
def preKeyPublic():
    '''public T_ECPub preKeyPublic(final OmemoBundleVAxolotlElement bundle, final int keyId)
    '''
def bundles():
    '''public HashMap<Integer, T_Bundle> bundles(final OmemoBundleVAxolotlElement bundle, final OmemoDevice contact)
    '''
