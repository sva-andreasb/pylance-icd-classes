DEFAULT_MIN_BLOCK_SIZE = "int  25"
DEFAULT_MAX_BLOCK_SIZE = "int  48"
def BlockTreeTermsWriter():
'''public BlockTreeTermsWriter(final SegmentWriteState state, final PostingsWriterBase postingsWriter, final int minItemsInBlock, final int maxItemsInBlock)
'''
pass
def validateSettings():
'''public static void validateSettings(final int minItemsInBlock, final int maxItemsInBlock)
'''
pass
def write():
'''public void write(final Fields fields, final NormsProducer norms)
public void write(final BytesRef text, final TermsEnum termsEnum, final NormsProducer norms)
'''
pass
def close():
'''public void close()
'''
pass
def FieldMetaData():
'''public FieldMetaData(final FieldInfo fieldInfo, final BytesRef rootCode, final long numTerms, final long indexStartFP, final long sumTotalTermFreq, final long sumDocFreq, final int docCount, final BytesRef minTerm, final BytesRef maxTerm)
'''
pass
def PendingTerm():
'''public PendingTerm(final BytesRef term, final BlockTermState state)
'''
pass
def toString():
'''public String toString()
public String toString()
'''
pass
def PendingBlock():
'''public PendingBlock(final BytesRef prefix, final long fp, final boolean hasTerms, final boolean isFloor, final int floorLeadByte, final List<FST<BytesRef>> subIndices)
'''
pass
def compileIndex():
'''public void compileIndex(final List<PendingBlock> blocks, final RAMOutputStream scratchBytes, final IntsRefBuilder scratchIntsRef)
'''
pass
def finish():
'''public void finish()
'''
pass