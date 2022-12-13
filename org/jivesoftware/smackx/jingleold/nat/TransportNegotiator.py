CANDIDATES_ACCEPT_PERIOD = "int  4000"
def TransportNegotiator():
'''public TransportNegotiator(final JingleSession session, final TransportResolver transResolver, final ContentNegotiator parentNegotiator)
'''
pass
def getBestLocalCandidate():
'''public final TransportCandidate getBestLocalCandidate()
'''
pass
def getAcceptedLocalCandidate():
'''public TransportCandidate getAcceptedLocalCandidate()
'''
pass
def close():
'''public void close()
'''
pass
def getJingleTransport():
'''public JingleTransport getJingleTransport()
public JingleTransport getJingleTransport(final TransportCandidate bestRemote)
public JingleTransport getJingleTransport(final TransportCandidate candidate)
'''
pass
def getOfferedCandidates():
'''public List<TransportCandidate> getOfferedCandidates()
'''
pass
def candidateChecked():
'''public void candidateChecked(final TransportCandidate cand, final boolean validCandidate)
'''
pass
def candidateChecking():
'''public void candidateChecking(final TransportCandidate cand)
'''
pass
def isFullyEstablished():
'''public final boolean isFullyEstablished()
'''
pass
def run():
'''public void run()
'''
pass
def getValidRemoteCandidates():
'''public final Iterator<TransportCandidate> getValidRemoteCandidates()
'''
pass
def candidateAdded():
'''public void candidateAdded(final TransportCandidate cand)
'''
pass
def end():
'''public void end()
'''
pass
def init():
'''public void init()
'''
pass
def dispatchIncomingPacket():
'''public final List<IQ> dispatchIncomingPacket(final IQ iq, final String id)
'''
pass
def RawUdp():
'''public RawUdp(final JingleSession js, final TransportResolver res, final ContentNegotiator parentNegotiator)
'''
pass
def getBestRemoteCandidate():
'''public TransportCandidate getBestRemoteCandidate()
public TransportCandidate getBestRemoteCandidate()
'''
pass
def acceptableTransportCandidate():
'''public boolean acceptableTransportCandidate(final TransportCandidate tc, final List<TransportCandidate> localCandidates)
public boolean acceptableTransportCandidate(final TransportCandidate tc, final List<TransportCandidate> localCandidates)
'''
pass
def Ice():
'''public Ice(final JingleSession js, final TransportResolver res, final ContentNegotiator parentNegotiator)
'''
pass
