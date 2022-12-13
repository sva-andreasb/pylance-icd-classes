def AbstractVerifier():
'''public AbstractVerifier()
'''
pass
def verify():
'''public final void verify(final String host, final SSLSocket ssl)
public final boolean verify(final String host, final SSLSession session)
public final void verify(final String host, final X509Certificate cert)
public final void verify(final String host, final String[] cns, final String[] subjectAlts, final boolean strictWithSubDomains)
'''
pass
def acceptableCountryWildcard():
'''public static boolean acceptableCountryWildcard(final String cn)
'''
pass
def getCNs():
'''public static String[] getCNs(final X509Certificate cert)
'''
pass
def getDNSSubjectAlts():
'''public static String[] getDNSSubjectAlts(final X509Certificate cert)
'''
pass
def countDots():
'''public static int countDots(final String s)
'''
pass
