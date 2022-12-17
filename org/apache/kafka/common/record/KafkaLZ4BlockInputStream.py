PREMATURE_EOS = "String  \"Stream ended prematurely\""
NOT_SUPPORTED = "String  \"Stream unsupported (invalid magic bytes)\""
BLOCK_HASH_MISMATCH = "String  \"Block checksum mismatch\""
DESCRIPTOR_HASH_MISMATCH = "String  \"Stream frame descriptor corrupted\""
def ():
    '''returns KafkaLZ4BlockInputStream\n\n
    (final ByteBuffer in, final BufferSupplier bufferSupplier, final boolean ignoreFlagDescriptorChecksum)\n
    '''
def ignoreFlagDescriptorChecksum():
    '''returns boolean\n\n
    ignoreFlagDescriptorChecksum()\n
    '''
def read():
    '''returns int\n\n
    read()\n
    read(final byte[] b, final int off, int len)\n
    '''
def skip():
    '''returns long\n\n
    skip(final long n)\n
    '''
def available():
    '''returns int\n\n
    available()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def mark():
    '''returns None\n\n
    mark(final int readlimit)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def markSupported():
    '''returns boolean\n\n
    markSupported()\n
    '''
