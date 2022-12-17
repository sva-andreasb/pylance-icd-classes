def ():
    '''returns Lucene60PointsWriter\n\n
    (final SegmentWriteState writeState, final int maxPointsInLeafNode, final double maxMBSortInHeap)\n
    (final SegmentWriteState writeState)\n
    '''
def writeField():
    '''returns None\n\n
    writeField(final FieldInfo fieldInfo, final PointsReader reader)\n
    '''
def visit():
    '''returns None\n\n
    visit(final int docID)\n
    visit(final int docID, final byte[] packedValue)\n
    '''
def merge():
    '''returns None\n\n
    merge(final MergeState mergeState)\n
    '''
def finish():
    '''returns None\n\n
    finish()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
