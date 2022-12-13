def merge():
'''public void merge(final MergeState mergeState)
'''
pass
def mergeNumericField():
'''public void mergeNumericField(final FieldInfo mergeFieldInfo, final MergeState mergeState)
'''
pass
def getNumeric():
'''public NumericDocValues getNumeric(final FieldInfo fieldInfo)
'''
pass
def docID():
'''public int docID()
public int docID()
public int docID()
public int docID()
public int docID()
'''
pass
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
pass
def advance():
'''public int advance(final int target)
public int advance(final int target)
public int advance(final int target)
public int advance(final int target)
public int advance(final int target)
'''
pass
def advanceExact():
'''public boolean advanceExact(final int target)
public boolean advanceExact(final int target)
public boolean advanceExact(final int target)
public boolean advanceExact(final int target)
public boolean advanceExact(final int target)
'''
pass
def cost():
'''public long cost()
public long cost()
public long cost()
public long cost()
public long cost()
'''
pass
def longValue():
'''public long longValue()
'''
pass
def mergeBinaryField():
'''public void mergeBinaryField(final FieldInfo mergeFieldInfo, final MergeState mergeState)
'''
pass
def getBinary():
'''public BinaryDocValues getBinary(final FieldInfo fieldInfo)
'''
pass
def binaryValue():
'''public BytesRef binaryValue()
'''
pass
def mergeSortedNumericField():
'''public void mergeSortedNumericField(final FieldInfo mergeFieldInfo, final MergeState mergeState)
'''
pass
def getSortedNumeric():
'''public SortedNumericDocValues getSortedNumeric(final FieldInfo fieldInfo)
'''
pass
def docValueCount():
'''public int docValueCount()
'''
pass
def nextValue():
'''public long nextValue()
'''
pass
def mergeSortedField():
'''public void mergeSortedField(final FieldInfo fieldInfo, final MergeState mergeState)
'''
pass
def getSorted():
'''public SortedDocValues getSorted(final FieldInfo fieldInfoIn)
'''
pass
def ordValue():
'''public int ordValue()
'''
pass
def getValueCount():
'''public int getValueCount()
public long getValueCount()
'''
pass
def lookupOrd():
'''public BytesRef lookupOrd(final int ord)
public BytesRef lookupOrd(final long ord)
'''
pass
def termsEnum():
'''public TermsEnum termsEnum()
public TermsEnum termsEnum()
'''
pass
def mergeSortedSetField():
'''public void mergeSortedSetField(final FieldInfo mergeFieldInfo, final MergeState mergeState)
'''
pass
def getSortedSet():
'''public SortedSetDocValues getSortedSet(final FieldInfo fieldInfo)
'''
pass
def nextOrd():
'''public long nextOrd()
'''
pass
def isSingleValued():
'''public static boolean isSingleValued(final Iterable<Number> docToValueCount)
'''
pass
def singletonView():
'''public static Iterable<Number> singletonView(final Iterable<Number> docToValueCount, final Iterable<Number> values, final Number missingValue)
'''
pass
def iterator():
'''public Iterator<Number> iterator()
'''
pass
def hasNext():
'''public boolean hasNext()
'''
pass
def next():
'''public Number next()
public BytesRef next()
'''
pass
def remove():
'''public void remove()
'''
pass
def NumericDocValuesSub():
'''public NumericDocValuesSub(final MergeState.DocMap docMap, final NumericDocValues values)
'''
pass
def BinaryDocValuesSub():
'''public BinaryDocValuesSub(final MergeState.DocMap docMap, final BinaryDocValues values)
'''
pass
def SortedNumericDocValuesSub():
'''public SortedNumericDocValuesSub(final MergeState.DocMap docMap, final SortedNumericDocValues values)
'''
pass
def term():
'''public BytesRef term()
'''
pass
def ord():
'''public long ord()
'''
pass
def attributes():
'''public AttributeSource attributes()
'''
pass
def seekExact():
'''public boolean seekExact(final BytesRef text)
public void seekExact(final long ord)
public void seekExact(final BytesRef term, final TermState state)
'''
pass
def seekCeil():
'''public SeekStatus seekCeil(final BytesRef text)
'''
pass
def docFreq():
'''public int docFreq()
'''
pass
def totalTermFreq():
'''public long totalTermFreq()
'''
pass
def postings():
'''public PostingsEnum postings(final PostingsEnum reuse, final int flags)
'''
pass
def impacts():
'''public ImpactsEnum impacts(final int flags)
'''
pass
def termState():
'''public TermState termState()
'''
pass
def SortedDocValuesSub():
'''public SortedDocValuesSub(final MergeState.DocMap docMap, final SortedDocValues values, final LongValues map)
'''
pass
def SortedSetDocValuesSub():
'''public SortedSetDocValuesSub(final MergeState.DocMap docMap, final SortedSetDocValues values, final LongValues map)
'''
pass
def toString():
'''public String toString()
'''
pass
