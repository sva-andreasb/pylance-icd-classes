def eventReceived():
    '''public void eventReceived(final EntityBareJid from, final EventElement event, final Message message)
    '''
def run():
    '''public void run()
    public void run()
    '''
def authenticated():
    '''public void authenticated(final XMPPConnection connection, final boolean resumed)
    '''
def getInstanceFor():
    '''public static synchronized OmemoManager getInstanceFor(final XMPPConnection connection, Integer deviceId)
    public static synchronized OmemoManager getInstanceFor(final XMPPConnection connection)
    '''
def initialize():
    '''public void initialize()
    '''
def encrypt():
    '''public Message encrypt(final BareJid to, final String message)
    public Message encrypt(final ArrayList<BareJid> recipients, final String message)
    public Message encrypt(final MultiUserChat muc, final String message)
    '''
def encryptForExistingSessions():
    '''public Message encryptForExistingSessions(final CannotEstablishOmemoSessionException exception, final String message)
    '''
def decrypt():
    '''public ClearTextMessage decrypt(final BareJid sender, final Message omemoMessage)
    '''
def decryptMamQueryResult():
    '''public List<ClearTextMessage> decryptMamQueryResult(final MamManager.MamQuery mamQuery)
    '''
def trustOmemoIdentity():
    '''public void trustOmemoIdentity(final OmemoDevice device, final OmemoFingerprint fingerprint)
    '''
def distrustOmemoIdentity():
    '''public void distrustOmemoIdentity(final OmemoDevice device, final OmemoFingerprint fingerprint)
    '''
def isTrustedOmemoIdentity():
    '''public boolean isTrustedOmemoIdentity(final OmemoDevice device, final OmemoFingerprint fingerprint)
    '''
def isDecidedOmemoIdentity():
    '''public boolean isDecidedOmemoIdentity(final OmemoDevice device, final OmemoFingerprint fingerprint)
    '''
def purgeDevices():
    '''public void purgeDevices()
    '''
def regenerate():
    '''public void regenerate()
    '''
def sendRatchetUpdateMessage():
    '''public void sendRatchetUpdateMessage(final OmemoDevice recipient)
    '''
def createKeyTransportElement():
    '''public OmemoVAxolotlElement createKeyTransportElement(final byte[] aesKey, final byte[] iv, final OmemoDevice... to)
    '''
def contactSupportsOmemo():
    '''public boolean contactSupportsOmemo(final BareJid contact)
    '''
def multiUserChatSupportsOmemo():
    '''public boolean multiUserChatSupportsOmemo(final EntityBareJid multiUserChat)
    '''
def serverSupportsOmemo():
    '''public static boolean serverSupportsOmemo(final XMPPConnection connection, final DomainBareJid server)
    '''
def getOurFingerprint():
    '''public OmemoFingerprint getOurFingerprint()
    '''
def getFingerprint():
    '''public OmemoFingerprint getFingerprint(final OmemoDevice device)
    '''
def getActiveFingerprints():
    '''public HashMap<OmemoDevice, OmemoFingerprint> getActiveFingerprints(final BareJid contact)
    '''
def addOmemoMessageListener():
    '''public void addOmemoMessageListener(final OmemoMessageListener listener)
    '''
def removeOmemoMessageListener():
    '''public void removeOmemoMessageListener(final OmemoMessageListener listener)
    '''
def addOmemoMucMessageListener():
    '''public void addOmemoMucMessageListener(final OmemoMucMessageListener listener)
    '''
def removeOmemoMucMessageListener():
    '''public void removeOmemoMucMessageListener(final OmemoMucMessageListener listener)
    '''
def buildSessionsWith():
    '''public void buildSessionsWith(final BareJid contact)
    '''
def requestDeviceListUpdateFor():
    '''public void requestDeviceListUpdateFor(final BareJid contact)
    '''
def rotateSignedPreKey():
    '''public void rotateSignedPreKey()
    '''
def stanzaContainsOmemoElement():
    '''public static boolean stanzaContainsOmemoElement(final Stanza stanza)
    '''
def randomDeviceId():
    '''public static int randomDeviceId()
    '''
def getOwnJid():
    '''public BareJid getOwnJid()
    '''
def getDeviceId():
    '''public int getDeviceId()
    '''
def getOwnDevice():
    '''public OmemoDevice getOwnDevice()
    '''
def shutdown():
    '''public void shutdown()
    '''
