def ():
    '''returns ParallelLeafReader\n\n
    (final LeafReader... readers)\n
    (final boolean closeSubReaders, final LeafReader... readers)\n
    (final boolean closeSubReaders, final LeafReader[] readers, final LeafReader[] storedFieldsReaders)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getFieldInfos():
    '''returns FieldInfos\n\n
    getFieldInfos()\n
    '''
def getLiveDocs():
    '''returns Bits\n\n
    getLiveDocs()\n
    '''
def terms():
    '''returns Terms\n\n
    terms(final String field)\n
    terms(final String field)\n
    '''
def numDocs():
    '''returns int\n\n
    numDocs()\n
    '''
def maxDoc():
    '''returns int\n\n
    maxDoc()\n
    '''
def document():
    '''returns None\n\n
    document(final int docID, final StoredFieldVisitor visitor)\n
    '''
def getCoreCacheHelper():
    '''returns CacheHelper\n\n
    getCoreCacheHelper()\n
    '''
def getReaderCacheHelper():
    '''returns CacheHelper\n\n
    getReaderCacheHelper()\n
    '''
def getTermVectors():
    '''returns Fields\n\n
    getTermVectors(final int docID)\n
    '''
def getNumericDocValues():
    '''returns NumericDocValues\n\n
    getNumericDocValues(final String field)\n
    '''
def getBinaryDocValues():
    '''returns BinaryDocValues\n\n
    getBinaryDocValues(final String field)\n
    '''
def getSortedDocValues():
    '''returns SortedDocValues\n\n
    getSortedDocValues(final String field)\n
    '''
def getSortedNumericDocValues():
    '''returns SortedNumericDocValues\n\n
    getSortedNumericDocValues(final String field)\n
    '''
def getSortedSetDocValues():
    '''returns SortedSetDocValues\n\n
    getSortedSetDocValues(final String field)\n
    '''
def getNormValues():
    '''returns NumericDocValues\n\n
    getNormValues(final String field)\n
    '''
def getPointValues():
    '''returns PointValues\n\n
    getPointValues(final String fieldName)\n
    '''
def checkIntegrity():
    '''returns None\n\n
    checkIntegrity()\n
    '''
def getParallelReaders():
    '''returns LeafReader[]\n\n
    getParallelReaders()\n
    '''
def getMetaData():
    '''returns LeafMetaData\n\n
    getMetaData()\n
    '''
def iterator():
    '''returns Iterator<String>\n\n
    iterator()\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
