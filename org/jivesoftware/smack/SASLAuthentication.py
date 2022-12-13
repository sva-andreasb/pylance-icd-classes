def registerSASLMechanism():
    '''public static void registerSASLMechanism(final String name, final Class mClass)
    '''
def unregisterSASLMechanism():
    '''public static void unregisterSASLMechanism(final String name)
    '''
def supportSASLMechanism():
    '''public static void supportSASLMechanism(final String name)
    public static void supportSASLMechanism(final String name, final int index)
    '''
def unsupportSASLMechanism():
    '''public static void unsupportSASLMechanism(final String name)
    '''
def getRegisterSASLMechanisms():
    '''public static List<Class> getRegisterSASLMechanisms()
    '''
def hasAnonymousAuthentication():
    '''public boolean hasAnonymousAuthentication()
    '''
def hasNonAnonymousAuthentication():
    '''public boolean hasNonAnonymousAuthentication()
    '''
def authenticate():
    '''public String authenticate(final String username, final String resource, final CallbackHandler cbh)
    public String authenticate(final String username, final String password, final String resource)
    '''
def authenticateAnonymously():
    '''public String authenticateAnonymously()
    '''
def isAuthenticated():
    '''public boolean isAuthenticated()
    '''
def send():
    '''public void send(final Packet stanza)
    '''
