def ():
    '''returns RecordBufferPageMgr\n\n
    (final RecordFactory factory, final BlockMgr blockMgr)\n
    '''
def create():
    '''returns RecordBufferPage\n\n
    create(final int x)\n
    '''
def get():
    '''returns RecordBufferPage\n\n
    get(final int id)\n
    '''
def createFromByteBuffer():
    '''returns RecordBufferPage\n\n
    createFromByteBuffer(final ByteBuffer bb, final BlockType blkType)\n
    '''
def fromByteBuffer():
    '''returns RecordBufferPage\n\n
    fromByteBuffer(final ByteBuffer byteBuffer)\n
    '''
def toByteBuffer():
    '''returns ByteBuffer\n\n
    toByteBuffer(final RecordBufferPage rbp)\n
    '''
