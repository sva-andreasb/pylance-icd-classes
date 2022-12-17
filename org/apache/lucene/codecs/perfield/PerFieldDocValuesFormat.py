PER_FIELD_NAME = "String  \"PerFieldDV40\""
def ():
    '''returns FieldsReader\n\n
    ()\n
    (final SegmentWriteState state)\n
    (final SegmentReadState readState)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    close()\n
    close()\n
    '''
def addNumericField():
    '''returns None\n\n
    addNumericField(final FieldInfo field, final DocValuesProducer valuesProducer)\n
    '''
def addBinaryField():
    '''returns None\n\n
    addBinaryField(final FieldInfo field, final DocValuesProducer valuesProducer)\n
    '''
def addSortedField():
    '''returns None\n\n
    addSortedField(final FieldInfo field, final DocValuesProducer valuesProducer)\n
    '''
def addSortedNumericField():
    '''returns None\n\n
    addSortedNumericField(final FieldInfo field, final DocValuesProducer valuesProducer)\n
    '''
def addSortedSetField():
    '''returns None\n\n
    addSortedSetField(final FieldInfo field, final DocValuesProducer valuesProducer)\n
    '''
def merge():
    '''returns None\n\n
    merge(final MergeState mergeState)\n
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
    '''returns DocValuesProducer\n\n
    getMergeInstance()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
