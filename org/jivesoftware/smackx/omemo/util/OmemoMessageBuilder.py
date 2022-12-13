def OmemoMessageBuilder():
'''public OmemoMessageBuilder(final OmemoManager omemoManager, final OmemoStore<T_IdKeyPair, T_IdKey, T_PreKey, T_SigPreKey, T_Sess, T_Addr, T_ECPub, T_Bundle, T_Ciph> omemoStore, final byte[] aesKey, final byte[] iv)
public OmemoMessageBuilder(final OmemoManager omemoManager, final OmemoStore<T_IdKeyPair, T_IdKey, T_PreKey, T_SigPreKey, T_Sess, T_Addr, T_ECPub, T_Bundle, T_Ciph> omemoStore, final String message)
'''
pass
def setMessage():
'''public void setMessage(final String message)
'''
pass
def addRecipient():
'''public void addRecipient(final OmemoDevice device)
public void addRecipient(final OmemoDevice device, final boolean ignoreTrust)
'''
pass
def finish():
'''public OmemoVAxolotlElement finish()
'''
pass
def generateKey():
'''public static byte[] generateKey()
'''
pass
def generateIv():
'''public static byte[] generateIv()
'''
pass
def getCiphertextMessage():
'''public byte[] getCiphertextMessage()
'''
pass
def getMessageKey():
'''public byte[] getMessageKey()
'''
pass
