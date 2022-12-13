def createURI():
'''public static URI createURI(final String scheme, final String host, final int port, final String path, final String query, final String fragment)
'''
pass
def rewriteURI():
'''public static URI rewriteURI(final URI uri, final HttpHost target, final boolean dropFragment)
public static URI rewriteURI(final URI uri, final HttpHost target)
public static URI rewriteURI(final URI uri)
'''
pass
def rewriteURIForRoute():
'''public static URI rewriteURIForRoute(final URI uri, final RouteInfo route)
'''
pass
def resolve():
'''public static URI resolve(final URI baseURI, final String reference)
public static URI resolve(final URI baseURI, final URI reference)
public static URI resolve(final URI originalURI, final HttpHost target, final List<URI> redirects)
'''
pass
def extractHost():
'''public static HttpHost extractHost(final URI uri)
'''
pass
