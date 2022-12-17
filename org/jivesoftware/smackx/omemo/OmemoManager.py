def eventReceived():
    '''returns None\n\n
    eventReceived(final EntityBareJid from, final EventElement event, final Message message)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    '''
def authenticated():
    '''returns None\n\n
    authenticated(final XMPPConnection connection, final boolean resumed)\n
    '''
def initialize():
    '''returns None\n\n
    initialize()\n
    '''
def encrypt():
    '''returns Message\n\n
    encrypt(final BareJid to, final String message)\n
    encrypt(final ArrayList<BareJid> recipients, final String message)\n
    encrypt(final MultiUserChat muc, final String message)\n
    '''
def encryptForExistingSessions():
    '''returns Message\n\n
    encryptForExistingSessions(final CannotEstablishOmemoSessionException exception, final String message)\n
    '''
def decrypt():
    '''returns ClearTextMessage\n\n
    decrypt(final BareJid sender, final Message omemoMessage)\n
    '''
def decryptMamQueryResult():
    '''returns List<ClearTextMessage>\n\n
    decryptMamQueryResult(final MamManager.MamQuery mamQuery)\n
    '''
def trustOmemoIdentity():
    '''returns None\n\n
    trustOmemoIdentity(final OmemoDevice device, final OmemoFingerprint fingerprint)\n
    '''
def distrustOmemoIdentity():
    '''returns None\n\n
    distrustOmemoIdentity(final OmemoDevice device, final OmemoFingerprint fingerprint)\n
    '''
def isTrustedOmemoIdentity():
    '''returns boolean\n\n
    isTrustedOmemoIdentity(final OmemoDevice device, final OmemoFingerprint fingerprint)\n
    '''
def isDecidedOmemoIdentity():
    '''returns boolean\n\n
    isDecidedOmemoIdentity(final OmemoDevice device, final OmemoFingerprint fingerprint)\n
    '''
def purgeDevices():
    '''returns None\n\n
    purgeDevices()\n
    '''
def regenerate():
    '''returns None\n\n
    regenerate()\n
    '''
def sendRatchetUpdateMessage():
    '''returns None\n\n
    sendRatchetUpdateMessage(final OmemoDevice recipient)\n
    '''
def createKeyTransportElement():
    '''returns OmemoVAxolotlElement\n\n
    createKeyTransportElement(final byte[] aesKey, final byte[] iv, final OmemoDevice... to)\n
    '''
def contactSupportsOmemo():
    '''returns boolean\n\n
    contactSupportsOmemo(final BareJid contact)\n
    '''
def multiUserChatSupportsOmemo():
    '''returns boolean\n\n
    multiUserChatSupportsOmemo(final EntityBareJid multiUserChat)\n
    '''
def getOurFingerprint():
    '''returns OmemoFingerprint\n\n
    getOurFingerprint()\n
    '''
def getFingerprint():
    '''returns OmemoFingerprint\n\n
    getFingerprint(final OmemoDevice device)\n
    '''
def addOmemoMessageListener():
    '''returns None\n\n
    addOmemoMessageListener(final OmemoMessageListener listener)\n
    '''
def removeOmemoMessageListener():
    '''returns None\n\n
    removeOmemoMessageListener(final OmemoMessageListener listener)\n
    '''
def addOmemoMucMessageListener():
    '''returns None\n\n
    addOmemoMucMessageListener(final OmemoMucMessageListener listener)\n
    '''
def removeOmemoMucMessageListener():
    '''returns None\n\n
    removeOmemoMucMessageListener(final OmemoMucMessageListener listener)\n
    '''
def buildSessionsWith():
    '''returns None\n\n
    buildSessionsWith(final BareJid contact)\n
    '''
def requestDeviceListUpdateFor():
    '''returns None\n\n
    requestDeviceListUpdateFor(final BareJid contact)\n
    '''
def rotateSignedPreKey():
    '''returns None\n\n
    rotateSignedPreKey()\n
    '''
def getOwnJid():
    '''returns BareJid\n\n
    getOwnJid()\n
    '''
def getDeviceId():
    '''returns int\n\n
    getDeviceId()\n
    '''
def getOwnDevice():
    '''returns OmemoDevice\n\n
    getOwnDevice()\n
    '''
def shutdown():
    '''returns None\n\n
    shutdown()\n
    '''
