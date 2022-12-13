PREMATURE_EOS = "String  \"Stream ended prematurely\""
NOT_SUPPORTED = "String  \"Stream unsupported (invalid magic bytes)\""
BLOCK_HASH_MISMATCH = "String  \"Block checksum mismatch\""
DESCRIPTOR_HASH_MISMATCH = "String  \"Stream frame descriptor corrupted\""
def KafkaLZ4BlockInputStream():
    '''    public KafkaLZ4BlockInputStream(final ByteBuffer in, final BufferSupplier bufferSupplier, final boolean ignoreFlagDescriptorChecksum)
    '''
def ignoreFlagDescriptorChecksum():
    '''    public boolean ignoreFlagDescriptorChecksum()
    '''
def read():
    '''    public int read()
    public int read(final byte[] b, final int off, int len)
    '''
def skip():
    '''    public long skip(final long n)
    '''
def available():
    '''    public int available()
    '''
def close():
    '''    public void close()
    '''
def mark():
    '''    public void mark(final int readlimit)
    '''
def reset():
    '''    public void reset()
    '''
def markSupported():
    '''    public boolean markSupported()
    '''
