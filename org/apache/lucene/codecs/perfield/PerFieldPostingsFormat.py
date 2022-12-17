PER_FIELD_NAME = "String  \"PerField40\""
def ():
    '''returns FieldsReader\n\n
    ()\n
    (final SegmentWriteState writeState)\n
    (final SegmentReadState readState)\n
    '''
def write():
    '''returns None\n\n
    write(final Fields fields, final NormsProducer norms)\n
    '''
def iterator():
    '''returns Iterator<String>\n\n
    iterator()\n
    iterator()\n
    '''
def merge():
    '''returns None\n\n
    merge(final MergeState mergeState, final NormsProducer norms)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    close()\n
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
def getMergeInstance():
    '''returns FieldsProducer\n\n
    getMergeInstance()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
