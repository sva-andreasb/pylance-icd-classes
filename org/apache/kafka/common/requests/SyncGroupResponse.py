def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def SyncGroupResponse():
'''public SyncGroupResponse(final Errors error, final ByteBuffer memberState)
public SyncGroupResponse(final int throttleTimeMs, final Errors error, final ByteBuffer memberState)
public SyncGroupResponse(final Struct struct)
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
def memberAssignment():
'''public ByteBuffer memberAssignment()
'''
pass
def parse():
'''public static SyncGroupResponse parse(final ByteBuffer buffer, final short version)
'''
pass
