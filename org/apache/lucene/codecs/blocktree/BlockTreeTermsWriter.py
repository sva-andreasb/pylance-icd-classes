DEFAULT_MIN_BLOCK_SIZE = "int  25"
DEFAULT_MAX_BLOCK_SIZE = "int  48"
def BlockTreeTermsWriter():
    '''public BlockTreeTermsWriter(final SegmentWriteState state, final PostingsWriterBase postingsWriter, final int minItemsInBlock, final int maxItemsInBlock)
    '''
def validateSettings():
    '''public static void validateSettings(final int minItemsInBlock, final int maxItemsInBlock)
    '''
def write():
    '''public void write(final Fields fields, final NormsProducer norms)
    public void write(final BytesRef text, final TermsEnum termsEnum, final NormsProducer norms)
    '''
def close():
    '''public void close()
    '''
def FieldMetaData():
    '''public FieldMetaData(final FieldInfo fieldInfo, final BytesRef rootCode, final long numTerms, final long indexStartFP, final long sumTotalTermFreq, final long sumDocFreq, final int docCount, final BytesRef minTerm, final BytesRef maxTerm)
    '''
def PendingTerm():
    '''public PendingTerm(final BytesRef term, final BlockTermState state)
    '''
def toString():
    '''public String toString()
    public String toString()
    '''
def PendingBlock():
    '''public PendingBlock(final BytesRef prefix, final long fp, final boolean hasTerms, final boolean isFloor, final int floorLeadByte, final List<FST<BytesRef>> subIndices)
    '''
def compileIndex():
    '''public void compileIndex(final List<PendingBlock> blocks, final RAMOutputStream scratchBytes, final IntsRefBuilder scratchIntsRef)
    '''
def finish():
    '''public void finish()
    '''
