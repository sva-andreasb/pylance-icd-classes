PER_FIELD_NAME = "String  \"PerFieldDV40\""
def PerFieldDocValuesFormat():
    '''public PerFieldDocValuesFormat()
    '''
def fieldsConsumer():
    '''public final DocValuesConsumer fieldsConsumer(final SegmentWriteState state)
    '''
def fieldsProducer():
    '''public final DocValuesProducer fieldsProducer(final SegmentReadState state)
    '''
def close():
    '''public void close()
    public void close()
    public void close()
    '''
def FieldsWriter():
    '''public FieldsWriter(final SegmentWriteState state)
    '''
def addNumericField():
    '''public void addNumericField(final FieldInfo field, final DocValuesProducer valuesProducer)
    '''
def addBinaryField():
    '''public void addBinaryField(final FieldInfo field, final DocValuesProducer valuesProducer)
    '''
def addSortedField():
    '''public void addSortedField(final FieldInfo field, final DocValuesProducer valuesProducer)
    '''
def addSortedNumericField():
    '''public void addSortedNumericField(final FieldInfo field, final DocValuesProducer valuesProducer)
    '''
def addSortedSetField():
    '''public void addSortedSetField(final FieldInfo field, final DocValuesProducer valuesProducer)
    '''
def merge():
    '''public void merge(final MergeState mergeState)
    '''
def FieldsReader():
    '''public FieldsReader(final SegmentReadState readState)
    '''
def getNumeric():
    '''public NumericDocValues getNumeric(final FieldInfo field)
    '''
def getBinary():
    '''public BinaryDocValues getBinary(final FieldInfo field)
    '''
def getSorted():
    '''public SortedDocValues getSorted(final FieldInfo field)
    '''
def getSortedNumeric():
    '''public SortedNumericDocValues getSortedNumeric(final FieldInfo field)
    '''
def getSortedSet():
    '''public SortedSetDocValues getSortedSet(final FieldInfo field)
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
def getMergeInstance():
    '''public DocValuesProducer getMergeInstance()
    '''
def toString():
    '''public String toString()
    '''
