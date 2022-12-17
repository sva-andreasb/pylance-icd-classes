def ():
    '''returns MediaNegotiator\n\n
    (final JingleSession session, final JingleMediaManager mediaManager, final List<PayloadType> pts, final ContentNegotiator parentNegotiator)\n
    '''
def getMediaManager():
    '''returns JingleMediaManager\n\n
    getMediaManager()\n
    '''
def dispatchIncomingPacket():
    '''returns List<IQ>\n\n
    dispatchIncomingPacket(final IQ iq, final String id)\n
    '''
def isEstablished():
    '''returns boolean\n\n
    isEstablished()\n
    '''
def isFullyEstablished():
    '''returns boolean\n\n
    isFullyEstablished()\n
    '''
def addRemoteAudioPayloadType():
    '''returns None\n\n
    addRemoteAudioPayloadType(final PayloadType.Audio pt)\n
    '''
def getBestCommonAudioPt():
    '''returns PayloadType\n\n
    getBestCommonAudioPt()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def getJingleDescription():
    '''returns JingleDescription\n\n
    getJingleDescription()\n
    '''
