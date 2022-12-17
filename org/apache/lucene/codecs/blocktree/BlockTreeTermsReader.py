FST_MODE_KEY = "String  \"blocktree.terms.fst\""
VERSION_START = "int  2"
VERSION_AUTO_PREFIX_TERMS_REMOVED = "int  3"
VERSION_META_LONGS_REMOVED = "int  4"
VERSION_COMPRESSED_SUFFIXES = "int  5"
VERSION_CURRENT = "int  5"
def ():
    '''returns BlockTreeTermsReader\n\n
    (final PostingsReaderBase postingsReader, final SegmentReadState state, final FSTLoadMode defaultLoadMode)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def iterator():
    '''returns Iterator<String>\n\n
    iterator()\n
    '''
def terms():
    '''returns Terms\n\n
    terms(final String field)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def ramBytesUsed():
    '''returns long\n\n
    ramBytesUsed()\n
    '''
def getChildResources():
    '''returns Collection<Accountable>\n\n
    getChildResources()\n
    '''
def checkIntegrity():
    '''returns None\n\n
    checkIntegrity()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
