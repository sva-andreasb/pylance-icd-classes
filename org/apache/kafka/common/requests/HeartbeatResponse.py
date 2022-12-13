def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def HeartbeatResponse():
'''public HeartbeatResponse(final Errors error)
public HeartbeatResponse(final int throttleTimeMs, final Errors error)
public HeartbeatResponse(final Struct struct)
'''
pass
def throttleTimeMs():
'''public int throttleTimeMs()
'''
pass
def error():
'''public Errors error()
'''
pass
def errorCounts():
'''public Map<Errors, Integer> errorCounts()
'''
pass
def parse():
'''public static HeartbeatResponse parse(final ByteBuffer buffer, final short version)
'''
pass
