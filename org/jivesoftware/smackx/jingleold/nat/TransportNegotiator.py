CANDIDATES_ACCEPT_PERIOD = "int  4000"
def TransportNegotiator():
    '''    public TransportNegotiator(final JingleSession session, final TransportResolver transResolver, final ContentNegotiator parentNegotiator)
    '''
def getBestLocalCandidate():
    '''    public final TransportCandidate getBestLocalCandidate()
    '''
def getAcceptedLocalCandidate():
    '''    public TransportCandidate getAcceptedLocalCandidate()
    '''
def close():
    '''    public void close()
    '''
def getJingleTransport():
    '''    public JingleTransport getJingleTransport()
    public JingleTransport getJingleTransport(final TransportCandidate bestRemote)
    public JingleTransport getJingleTransport(final TransportCandidate candidate)
    '''
def getOfferedCandidates():
    '''    public List<TransportCandidate> getOfferedCandidates()
    '''
def candidateChecked():
    '''    public void candidateChecked(final TransportCandidate cand, final boolean validCandidate)
    '''
def candidateChecking():
    '''    public void candidateChecking(final TransportCandidate cand)
    '''
def isFullyEstablished():
    '''    public final boolean isFullyEstablished()
    '''
def run():
    '''    public void run()
    '''
def getValidRemoteCandidates():
    '''    public final Iterator<TransportCandidate> getValidRemoteCandidates()
    '''
def candidateAdded():
    '''    public void candidateAdded(final TransportCandidate cand)
    '''
def end():
    '''    public void end()
    '''
def init():
    '''    public void init()
    '''
def dispatchIncomingPacket():
    '''    public final List<IQ> dispatchIncomingPacket(final IQ iq, final String id)
    '''
def RawUdp():
    '''    public RawUdp(final JingleSession js, final TransportResolver res, final ContentNegotiator parentNegotiator)
    '''
def getBestRemoteCandidate():
    '''    public TransportCandidate getBestRemoteCandidate()
    public TransportCandidate getBestRemoteCandidate()
    '''
def acceptableTransportCandidate():
    '''    public boolean acceptableTransportCandidate(final TransportCandidate tc, final List<TransportCandidate> localCandidates)
    public boolean acceptableTransportCandidate(final TransportCandidate tc, final List<TransportCandidate> localCandidates)
    '''
def Ice():
    '''    public Ice(final JingleSession js, final TransportResolver res, final ContentNegotiator parentNegotiator)
    '''
