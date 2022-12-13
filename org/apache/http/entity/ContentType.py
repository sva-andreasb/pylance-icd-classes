def getMimeType():
'''public String getMimeType()
'''
pass
def getCharset():
'''public Charset getCharset()
'''
pass
def getParameter():
'''public String getParameter(final String name)
'''
pass
def toString():
'''public String toString()
'''
pass
def create():
'''public static ContentType create(final String mimeType, final Charset charset)
public static ContentType create(final String mimeType)
public static ContentType create(final String mimeType, final String charset)
public static ContentType create(final String mimeType, final NameValuePair... params)
'''
pass
def parse():
'''public static ContentType parse(final String s)
'''
pass
def get():
'''public static ContentType get(final HttpEntity entity)
'''
pass
def getLenient():
'''public static ContentType getLenient(final HttpEntity entity)
'''
pass
def getOrDefault():
'''public static ContentType getOrDefault(final HttpEntity entity)
'''
pass
def getLenientOrDefault():
'''public static ContentType getLenientOrDefault(final HttpEntity entity)
'''
pass
def withCharset():
'''public ContentType withCharset(final Charset charset)
public ContentType withCharset(final String charset)
'''
pass
def withParameters():
'''public ContentType withParameters(final NameValuePair... params)
'''
pass
