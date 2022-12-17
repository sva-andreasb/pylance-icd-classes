DEFAULT_MIN_BLOCK_SIZE = "int  25"
DEFAULT_MAX_BLOCK_SIZE = "int  48"
def ():
    '''returns PendingBlock\n\n
    (final SegmentWriteState state, final PostingsWriterBase postingsWriter, final int minItemsInBlock, final int maxItemsInBlock)\n
    (final FieldInfo fieldInfo, final BytesRef rootCode, final long numTerms, final long indexStartFP, final long sumTotalTermFreq, final long sumDocFreq, final int docCount, final BytesRef minTerm, final BytesRef maxTerm)\n
    (final BytesRef term, final BlockTermState state)\n
    (final BytesRef prefix, final long fp, final boolean hasTerms, final boolean isFloor, final int floorLeadByte, final List<FST<BytesRef>> subIndices)\n
    '''
def write():
    '''returns None\n\n
    write(final Fields fields, final NormsProducer norms)\n
    write(final BytesRef text, final TermsEnum termsEnum, final NormsProducer norms)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def compileIndex():
    '''returns None\n\n
    compileIndex(final List<PendingBlock> blocks, final RAMOutputStream scratchBytes, final IntsRefBuilder scratchIntsRef)\n
    '''
def finish():
    '''returns None\n\n
    finish()\n
    '''
