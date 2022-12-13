def OmemoMessageBuilder():
    '''    public OmemoMessageBuilder(final OmemoManager omemoManager, final OmemoStore<T_IdKeyPair, T_IdKey, T_PreKey, T_SigPreKey, T_Sess, T_Addr, T_ECPub, T_Bundle, T_Ciph> omemoStore, final byte[] aesKey, final byte[] iv)
    public OmemoMessageBuilder(final OmemoManager omemoManager, final OmemoStore<T_IdKeyPair, T_IdKey, T_PreKey, T_SigPreKey, T_Sess, T_Addr, T_ECPub, T_Bundle, T_Ciph> omemoStore, final String message)
    '''
def setMessage():
    '''    public void setMessage(final String message)
    '''
def addRecipient():
    '''    public void addRecipient(final OmemoDevice device)
    public void addRecipient(final OmemoDevice device, final boolean ignoreTrust)
    '''
def finish():
    '''    public OmemoVAxolotlElement finish()
    '''
def generateKey():
    '''    public static byte[] generateKey()
    '''
def generateIv():
    '''    public static byte[] generateIv()
    '''
def getCiphertextMessage():
    '''    public byte[] getCiphertextMessage()
    '''
def getMessageKey():
    '''    public byte[] getMessageKey()
    '''
