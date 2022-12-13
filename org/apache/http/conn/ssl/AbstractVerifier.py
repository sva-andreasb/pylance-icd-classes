def AbstractVerifier():
    '''public AbstractVerifier()
    '''
def verify():
    '''public final void verify(final String host, final SSLSocket ssl)
    public final boolean verify(final String host, final SSLSession session)
    public final void verify(final String host, final X509Certificate cert)
    public final void verify(final String host, final String[] cns, final String[] subjectAlts, final boolean strictWithSubDomains)
    '''
def acceptableCountryWildcard():
    '''public static boolean acceptableCountryWildcard(final String cn)
    '''
def getCNs():
    '''public static String[] getCNs(final X509Certificate cert)
    '''
def getDNSSubjectAlts():
    '''public static String[] getDNSSubjectAlts(final X509Certificate cert)
    '''
def countDots():
    '''public static int countDots(final String s)
    '''
