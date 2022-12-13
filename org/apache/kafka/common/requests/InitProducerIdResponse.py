def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def InitProducerIdResponse():
'''public InitProducerIdResponse(final int throttleTimeMs, final Errors error, final long producerId, final short epoch)
public InitProducerIdResponse(final Struct struct)
public InitProducerIdResponse(final int throttleTimeMs, final Errors errors)
'''
pass
def throttleTimeMs():
'''public int throttleTimeMs()
'''
pass
def producerId():
'''public long producerId()
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
def epoch():
'''public short epoch()
'''
pass
def parse():
'''public static InitProducerIdResponse parse(final ByteBuffer buffer, final short version)
'''
pass
def toString():
'''public String toString()
'''
pass
