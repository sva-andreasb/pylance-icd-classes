def ():
    '''returns HashBucketMgr\n\n
    (final RecordFactory factory, final BlockMgr blockMgr)\n
    '''
def create():
    '''returns HashBucket\n\n
    create(final int id, final int hash, final int hashBitLen)\n
    '''
def get():
    '''returns HashBucket\n\n
    get(final int id)\n
    '''
def createFromByteBuffer():
    '''returns HashBucket\n\n
    createFromByteBuffer(final ByteBuffer bb, final BlockType blkType)\n
    '''
def fromByteBuffer():
    '''returns HashBucket\n\n
    fromByteBuffer(final ByteBuffer byteBuffer)\n
    '''
def toByteBuffer():
    '''returns ByteBuffer\n\n
    toByteBuffer(final HashBucket bucket)\n
    '''
