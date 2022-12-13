def CreateDelegationTokenResponse():
'''public CreateDelegationTokenResponse(final int throttleTimeMs, final Errors error, final KafkaPrincipal owner, final long issueTimestamp, final long expiryTimestamp, final long maxTimestamp, final String tokenId, final ByteBuffer hmac)
public CreateDelegationTokenResponse(final int throttleTimeMs, final Errors error, final KafkaPrincipal owner)
public CreateDelegationTokenResponse(final Struct struct)
'''
pass
def parse():
'''public static CreateDelegationTokenResponse parse(final ByteBuffer buffer, final short version)
'''
pass
def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def errorCounts():
'''public Map<Errors, Integer> errorCounts()
'''
pass
def error():
'''public Errors error()
'''
pass
def owner():
'''public KafkaPrincipal owner()
'''
pass
def issueTimestamp():
'''public long issueTimestamp()
'''
pass
def expiryTimestamp():
'''public long expiryTimestamp()
'''
pass
def maxTimestamp():
'''public long maxTimestamp()
'''
pass
def tokenId():
'''public String tokenId()
'''
pass
def hmacBytes():
'''public byte[] hmacBytes()
'''
pass
def throttleTimeMs():
'''public int throttleTimeMs()
'''
pass
def hasError():
'''public boolean hasError()
'''
pass
