def eventReceived():
'''public void eventReceived(final EntityBareJid from, final EventElement event, final Message message)
'''
pass
def run():
'''public void run()
public void run()
'''
pass
def authenticated():
'''public void authenticated(final XMPPConnection connection, final boolean resumed)
'''
pass
def getInstanceFor():
'''public static synchronized OmemoManager getInstanceFor(final XMPPConnection connection, Integer deviceId)
public static synchronized OmemoManager getInstanceFor(final XMPPConnection connection)
'''
pass
def initialize():
'''public void initialize()
'''
pass
def encrypt():
'''public Message encrypt(final BareJid to, final String message)
public Message encrypt(final ArrayList<BareJid> recipients, final String message)
public Message encrypt(final MultiUserChat muc, final String message)
'''
pass
def encryptForExistingSessions():
'''public Message encryptForExistingSessions(final CannotEstablishOmemoSessionException exception, final String message)
'''
pass
def decrypt():
'''public ClearTextMessage decrypt(final BareJid sender, final Message omemoMessage)
'''
pass
def decryptMamQueryResult():
'''public List<ClearTextMessage> decryptMamQueryResult(final MamManager.MamQuery mamQuery)
'''
pass
def trustOmemoIdentity():
'''public void trustOmemoIdentity(final OmemoDevice device, final OmemoFingerprint fingerprint)
'''
pass
def distrustOmemoIdentity():
'''public void distrustOmemoIdentity(final OmemoDevice device, final OmemoFingerprint fingerprint)
'''
pass
def isTrustedOmemoIdentity():
'''public boolean isTrustedOmemoIdentity(final OmemoDevice device, final OmemoFingerprint fingerprint)
'''
pass
def isDecidedOmemoIdentity():
'''public boolean isDecidedOmemoIdentity(final OmemoDevice device, final OmemoFingerprint fingerprint)
'''
pass
def purgeDevices():
'''public void purgeDevices()
'''
pass
def regenerate():
'''public void regenerate()
'''
pass
def sendRatchetUpdateMessage():
'''public void sendRatchetUpdateMessage(final OmemoDevice recipient)
'''
pass
def createKeyTransportElement():
'''public OmemoVAxolotlElement createKeyTransportElement(final byte[] aesKey, final byte[] iv, final OmemoDevice... to)
'''
pass
def contactSupportsOmemo():
'''public boolean contactSupportsOmemo(final BareJid contact)
'''
pass
def multiUserChatSupportsOmemo():
'''public boolean multiUserChatSupportsOmemo(final EntityBareJid multiUserChat)
'''
pass
def serverSupportsOmemo():
'''public static boolean serverSupportsOmemo(final XMPPConnection connection, final DomainBareJid server)
'''
pass
def getOurFingerprint():
'''public OmemoFingerprint getOurFingerprint()
'''
pass
def getFingerprint():
'''public OmemoFingerprint getFingerprint(final OmemoDevice device)
'''
pass
def getActiveFingerprints():
'''public HashMap<OmemoDevice, OmemoFingerprint> getActiveFingerprints(final BareJid contact)
'''
pass
def addOmemoMessageListener():
'''public void addOmemoMessageListener(final OmemoMessageListener listener)
'''
pass
def removeOmemoMessageListener():
'''public void removeOmemoMessageListener(final OmemoMessageListener listener)
'''
pass
def addOmemoMucMessageListener():
'''public void addOmemoMucMessageListener(final OmemoMucMessageListener listener)
'''
pass
def removeOmemoMucMessageListener():
'''public void removeOmemoMucMessageListener(final OmemoMucMessageListener listener)
'''
pass
def buildSessionsWith():
'''public void buildSessionsWith(final BareJid contact)
'''
pass
def requestDeviceListUpdateFor():
'''public void requestDeviceListUpdateFor(final BareJid contact)
'''
pass
def rotateSignedPreKey():
'''public void rotateSignedPreKey()
'''
pass
def stanzaContainsOmemoElement():
'''public static boolean stanzaContainsOmemoElement(final Stanza stanza)
'''
pass
def randomDeviceId():
'''public static int randomDeviceId()
'''
pass
def getOwnJid():
'''public BareJid getOwnJid()
'''
pass
def getDeviceId():
'''public int getDeviceId()
'''
pass
def getOwnDevice():
'''public OmemoDevice getOwnDevice()
'''
pass
def shutdown():
'''public void shutdown()
'''
pass
