def getTermVectorsReader():
    '''returns TermVectorsReader\n\n
    getTermVectorsReader()\n
    '''
def getFieldsReader():
    '''returns StoredFieldsReader\n\n
    getFieldsReader()\n
    '''
def getNormsReader():
    '''returns NormsProducer\n\n
    getNormsReader()\n
    '''
def getDocValuesReader():
    '''returns DocValuesProducer\n\n
    getDocValuesReader()\n
    '''
def getPostingsReader():
    '''returns FieldsProducer\n\n
    getPostingsReader()\n
    '''
def getFieldInfos():
    '''returns FieldInfos\n\n
    getFieldInfos()\n
    '''
def getPointsReader():
    '''returns PointsReader\n\n
    getPointsReader()\n
    '''
def getLiveDocs():
    '''returns Bits\n\n
    getLiveDocs()\n
    '''
def numDocs():
    '''returns int\n\n
    numDocs()\n
    '''
def maxDoc():
    '''returns int\n\n
    maxDoc()\n
    '''
def getCoreCacheHelper():
    '''returns CacheHelper\n\n
    getCoreCacheHelper()\n
    '''
def getReaderCacheHelper():
    '''returns CacheHelper\n\n
    getReaderCacheHelper()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getMetaData():
    '''returns LeafMetaData\n\n
    getMetaData()\n
    '''
def getValues():
    '''returns PointValues\n\n
    getValues(final String field)\n
    '''
def checkIntegrity():
    '''returns None\n\n
    checkIntegrity()\n
    checkIntegrity()\n
    checkIntegrity()\n
    checkIntegrity()\n
    checkIntegrity()\n
    checkIntegrity()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    close()\n
    close()\n
    close()\n
    close()\n
    close()\n
    '''
def ramBytesUsed():
    '''returns long\n\n
    ramBytesUsed()\n
    ramBytesUsed()\n
    ramBytesUsed()\n
    ramBytesUsed()\n
    ramBytesUsed()\n
    ramBytesUsed()\n
    '''
def getNorms():
    '''returns NumericDocValues\n\n
    getNorms(final FieldInfo field)\n
    '''
def getNumeric():
    '''returns NumericDocValues\n\n
    getNumeric(final FieldInfo field)\n
    '''
def getBinary():
    '''returns BinaryDocValues\n\n
    getBinary(final FieldInfo field)\n
    '''
def getSorted():
    '''returns SortedDocValues\n\n
    getSorted(final FieldInfo field)\n
    '''
def getSortedNumeric():
    '''returns SortedNumericDocValues\n\n
    getSortedNumeric(final FieldInfo field)\n
    '''
def getSortedSet():
    '''returns SortedSetDocValues\n\n
    getSortedSet(final FieldInfo field)\n
    '''
def visitDocument():
    '''returns None\n\n
    visitDocument(final int docID, final StoredFieldVisitor visitor)\n
    '''
def clone():
    '''returns TermVectorsReader\n\n
    clone()\n
    clone()\n
    '''
def get():
    '''returns Fields\n\n
    get(final int docID)\n
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
