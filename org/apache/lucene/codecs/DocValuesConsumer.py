def merge():
    '''public void merge(final MergeState mergeState)
    '''
def mergeNumericField():
    '''public void mergeNumericField(final FieldInfo mergeFieldInfo, final MergeState mergeState)
    '''
def getNumeric():
    '''public NumericDocValues getNumeric(final FieldInfo fieldInfo)
    '''
def docID():
    '''public int docID()
    public int docID()
    public int docID()
    public int docID()
    public int docID()
    '''
def nextDoc():
    '''public int nextDoc()
    public int nextDoc()
    public int nextDoc()
    public int nextDoc()
    public int nextDoc()
    public int nextDoc()
    public int nextDoc()
    public int nextDoc()
    public int nextDoc()
    public int nextDoc()
    '''
def advance():
    '''public int advance(final int target)
    public int advance(final int target)
    public int advance(final int target)
    public int advance(final int target)
    public int advance(final int target)
    '''
def advanceExact():
    '''public boolean advanceExact(final int target)
    public boolean advanceExact(final int target)
    public boolean advanceExact(final int target)
    public boolean advanceExact(final int target)
    public boolean advanceExact(final int target)
    '''
def cost():
    '''public long cost()
    public long cost()
    public long cost()
    public long cost()
    public long cost()
    '''
def longValue():
    '''public long longValue()
    '''
def mergeBinaryField():
    '''public void mergeBinaryField(final FieldInfo mergeFieldInfo, final MergeState mergeState)
    '''
def getBinary():
    '''public BinaryDocValues getBinary(final FieldInfo fieldInfo)
    '''
def binaryValue():
    '''public BytesRef binaryValue()
    '''
def mergeSortedNumericField():
    '''public void mergeSortedNumericField(final FieldInfo mergeFieldInfo, final MergeState mergeState)
    '''
def getSortedNumeric():
    '''public SortedNumericDocValues getSortedNumeric(final FieldInfo fieldInfo)
    '''
def docValueCount():
    '''public int docValueCount()
    '''
def nextValue():
    '''public long nextValue()
    '''
def mergeSortedField():
    '''public void mergeSortedField(final FieldInfo fieldInfo, final MergeState mergeState)
    '''
def getSorted():
    '''public SortedDocValues getSorted(final FieldInfo fieldInfoIn)
    '''
def ordValue():
    '''public int ordValue()
    '''
def getValueCount():
    '''public int getValueCount()
    public long getValueCount()
    '''
def lookupOrd():
    '''public BytesRef lookupOrd(final int ord)
    public BytesRef lookupOrd(final long ord)
    '''
def termsEnum():
    '''public TermsEnum termsEnum()
    public TermsEnum termsEnum()
    '''
def mergeSortedSetField():
    '''public void mergeSortedSetField(final FieldInfo mergeFieldInfo, final MergeState mergeState)
    '''
def getSortedSet():
    '''public SortedSetDocValues getSortedSet(final FieldInfo fieldInfo)
    '''
def nextOrd():
    '''public long nextOrd()
    '''
def isSingleValued():
    '''public static boolean isSingleValued(final Iterable<Number> docToValueCount)
    '''
def singletonView():
    '''public static Iterable<Number> singletonView(final Iterable<Number> docToValueCount, final Iterable<Number> values, final Number missingValue)
    '''
def iterator():
    '''public Iterator<Number> iterator()
    '''
def hasNext():
    '''public boolean hasNext()
    '''
def next():
    '''public Number next()
    public BytesRef next()
    '''
def remove():
    '''public void remove()
    '''
def NumericDocValuesSub():
    '''public NumericDocValuesSub(final MergeState.DocMap docMap, final NumericDocValues values)
    '''
def BinaryDocValuesSub():
    '''public BinaryDocValuesSub(final MergeState.DocMap docMap, final BinaryDocValues values)
    '''
def SortedNumericDocValuesSub():
    '''public SortedNumericDocValuesSub(final MergeState.DocMap docMap, final SortedNumericDocValues values)
    '''
def term():
    '''public BytesRef term()
    '''
def ord():
    '''public long ord()
    '''
def attributes():
    '''public AttributeSource attributes()
    '''
def seekExact():
    '''public boolean seekExact(final BytesRef text)
    public void seekExact(final long ord)
    public void seekExact(final BytesRef term, final TermState state)
    '''
def seekCeil():
    '''public SeekStatus seekCeil(final BytesRef text)
    '''
def docFreq():
    '''public int docFreq()
    '''
def totalTermFreq():
    '''public long totalTermFreq()
    '''
def postings():
    '''public PostingsEnum postings(final PostingsEnum reuse, final int flags)
    '''
def impacts():
    '''public ImpactsEnum impacts(final int flags)
    '''
def termState():
    '''public TermState termState()
    '''
def SortedDocValuesSub():
    '''public SortedDocValuesSub(final MergeState.DocMap docMap, final SortedDocValues values, final LongValues map)
    '''
def SortedSetDocValuesSub():
    '''public SortedSetDocValuesSub(final MergeState.DocMap docMap, final SortedSetDocValues values, final LongValues map)
    '''
def toString():
    '''public String toString()
    '''
