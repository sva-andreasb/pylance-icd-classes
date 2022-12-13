FST_MODE_KEY = "String  \"blocktree.terms.fst\""
VERSION_START = "int  2"
VERSION_AUTO_PREFIX_TERMS_REMOVED = "int  3"
VERSION_META_LONGS_REMOVED = "int  4"
VERSION_COMPRESSED_SUFFIXES = "int  5"
VERSION_CURRENT = "int  5"
def BlockTreeTermsReader():
    '''public BlockTreeTermsReader(final PostingsReaderBase postingsReader, final SegmentReadState state, final FSTLoadMode defaultLoadMode)
    '''
def close():
    '''public void close()
    '''
def iterator():
    '''public Iterator<String> iterator()
    '''
def terms():
    '''public Terms terms(final String field)
    '''
def size():
    '''public int size()
    '''
def ramBytesUsed():
    '''public long ramBytesUsed()
    '''
def getChildResources():
    '''public Collection<Accountable> getChildResources()
    '''
def checkIntegrity():
    '''public void checkIntegrity()
    '''
def toString():
    '''public String toString()
    '''
