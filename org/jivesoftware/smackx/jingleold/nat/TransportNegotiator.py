CANDIDATES_ACCEPT_PERIOD = "int  4000"
def ():
    '''returns Ice\n\n
    (final JingleSession session, final TransportResolver transResolver, final ContentNegotiator parentNegotiator)\n
    (final JingleSession js, final TransportResolver res, final ContentNegotiator parentNegotiator)\n
    (final JingleSession js, final TransportResolver res, final ContentNegotiator parentNegotiator)\n
    '''
def getAcceptedLocalCandidate():
    '''returns TransportCandidate\n\n
    getAcceptedLocalCandidate()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def getJingleTransport():
    '''returns JingleTransport\n\n
    getJingleTransport()\n
    getJingleTransport(final TransportCandidate bestRemote)\n
    getJingleTransport(final TransportCandidate candidate)\n
    '''
def getOfferedCandidates():
    '''returns List<TransportCandidate>\n\n
    getOfferedCandidates()\n
    '''
def candidateChecked():
    '''returns None\n\n
    candidateChecked(final TransportCandidate cand, final boolean validCandidate)\n
    '''
def candidateChecking():
    '''returns None\n\n
    candidateChecking(final TransportCandidate cand)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
def candidateAdded():
    '''returns None\n\n
    candidateAdded(final TransportCandidate cand)\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def getBestRemoteCandidate():
    '''returns TransportCandidate\n\n
    getBestRemoteCandidate()\n
    getBestRemoteCandidate()\n
    '''
def acceptableTransportCandidate():
    '''returns boolean\n\n
    acceptableTransportCandidate(final TransportCandidate tc, final List<TransportCandidate> localCandidates)\n
    acceptableTransportCandidate(final TransportCandidate tc, final List<TransportCandidate> localCandidates)\n
    '''
