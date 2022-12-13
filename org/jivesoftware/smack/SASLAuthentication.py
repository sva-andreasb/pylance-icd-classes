def registerSASLMechanism():
'''public static void registerSASLMechanism(final String name, final Class mClass)
'''
pass
def unregisterSASLMechanism():
'''public static void unregisterSASLMechanism(final String name)
'''
pass
def supportSASLMechanism():
'''public static void supportSASLMechanism(final String name)
public static void supportSASLMechanism(final String name, final int index)
'''
pass
def unsupportSASLMechanism():
'''public static void unsupportSASLMechanism(final String name)
'''
pass
def getRegisterSASLMechanisms():
'''public static List<Class> getRegisterSASLMechanisms()
'''
pass
def hasAnonymousAuthentication():
'''public boolean hasAnonymousAuthentication()
'''
pass
def hasNonAnonymousAuthentication():
'''public boolean hasNonAnonymousAuthentication()
'''
pass
def authenticate():
'''public String authenticate(final String username, final String resource, final CallbackHandler cbh)
public String authenticate(final String username, final String password, final String resource)
'''
pass
def authenticateAnonymously():
'''public String authenticateAnonymously()
'''
pass
def isAuthenticated():
'''public boolean isAuthenticated()
'''
pass
def send():
'''public void send(final Packet stanza)
'''
pass
