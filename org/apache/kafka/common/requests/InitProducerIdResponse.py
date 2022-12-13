def schemaVersions():
    '''public static Schema[] schemaVersions()
    '''
def InitProducerIdResponse():
    '''public InitProducerIdResponse(final int throttleTimeMs, final Errors error, final long producerId, final short epoch)
    public InitProducerIdResponse(final Struct struct)
    public InitProducerIdResponse(final int throttleTimeMs, final Errors errors)
    '''
def throttleTimeMs():
    '''public int throttleTimeMs()
    '''
def producerId():
    '''public long producerId()
    '''
def error():
    '''public Errors error()
    '''
def errorCounts():
    '''public Map<Errors, Integer> errorCounts()
    '''
def epoch():
    '''public short epoch()
    '''
def parse():
    '''public static InitProducerIdResponse parse(final ByteBuffer buffer, final short version)
    '''
def toString():
    '''public String toString()
    '''
