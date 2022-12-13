PREMATURE_EOS = "String  Stream ended prematurely""
NOT_SUPPORTED = "String  Stream unsupported (invalid magic bytes)""
BLOCK_HASH_MISMATCH = "String  Block checksum mismatch""
DESCRIPTOR_HASH_MISMATCH = "String  Stream frame descriptor corrupted""
def KafkaLZ4BlockInputStream():
'''public KafkaLZ4BlockInputStream(final ByteBuffer in, final BufferSupplier bufferSupplier, final boolean ignoreFlagDescriptorChecksum)
'''
pass
def ignoreFlagDescriptorChecksum():
'''public boolean ignoreFlagDescriptorChecksum()
'''
pass
def read():
'''public int read()
public int read(final byte[] b, final int off, int len)
'''
pass
def skip():
'''public long skip(final long n)
'''
pass
def available():
'''public int available()
'''
pass
def close():
'''public void close()
'''
pass
def mark():
'''public void mark(final int readlimit)
'''
pass
def reset():
'''public void reset()
'''
pass
def markSupported():
'''public boolean markSupported()
'''
pass
