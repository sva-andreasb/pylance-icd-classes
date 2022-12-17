def ():
    '''returns OmemoMessageBuilder\n\n
    (final OmemoManager omemoManager, final OmemoStore<T_IdKeyPair, T_IdKey, T_PreKey, T_SigPreKey, T_Sess, T_Addr, T_ECPub, T_Bundle, T_Ciph> omemoStore, final byte[] aesKey, final byte[] iv)\n
    (final OmemoManager omemoManager, final OmemoStore<T_IdKeyPair, T_IdKey, T_PreKey, T_SigPreKey, T_Sess, T_Addr, T_ECPub, T_Bundle, T_Ciph> omemoStore, final String message)\n
    '''
def setMessage():
    '''returns None\n\n
    setMessage(final String message)\n
    '''
def addRecipient():
    '''returns None\n\n
    addRecipient(final OmemoDevice device)\n
    addRecipient(final OmemoDevice device, final boolean ignoreTrust)\n
    '''
def finish():
    '''returns OmemoVAxolotlElement\n\n
    finish()\n
    '''
def getCiphertextMessage():
    '''returns byte[]\n\n
    getCiphertextMessage()\n
    '''
def getMessageKey():
    '''returns byte[]\n\n
    getMessageKey()\n
    '''
