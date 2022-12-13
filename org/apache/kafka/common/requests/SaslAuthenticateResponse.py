def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def SaslAuthenticateResponse():
'''public SaslAuthenticateResponse(final Errors error, final String errorMessage)
public SaslAuthenticateResponse(final Errors error, final String errorMessage, final ByteBuffer saslAuthBytes)
public SaslAuthenticateResponse(final Struct struct)
'''
pass
def error():
'''public Errors error()
'''
pass
def errorMessage():
'''public String errorMessage()
'''
pass
def saslAuthBytes():
'''public ByteBuffer saslAuthBytes()
'''
pass
def errorCounts():
'''public Map<Errors, Integer> errorCounts()
'''
pass
def toStruct():
'''public Struct toStruct(final short version)
'''
pass
def parse():
'''public static SaslAuthenticateResponse parse(final ByteBuffer buffer, final short version)
'''
pass
