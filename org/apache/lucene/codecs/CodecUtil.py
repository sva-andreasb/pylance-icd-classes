CODEC_MAGIC = "int  1071082519"
FOOTER_MAGIC = "int  -1071082520"
def writeHeader():
'''public static void writeHeader(final DataOutput out, final String codec, final int version)
'''
pass
def writeIndexHeader():
'''public static void writeIndexHeader(final DataOutput out, final String codec, final int version, final byte[] id, final String suffix)
'''
pass
def headerLength():
'''public static int headerLength(final String codec)
'''
pass
def indexHeaderLength():
'''public static int indexHeaderLength(final String codec, final String suffix)
'''
pass
def checkHeader():
'''public static int checkHeader(final DataInput in, final String codec, final int minVersion, final int maxVersion)
'''
pass
def checkHeaderNoMagic():
'''public static int checkHeaderNoMagic(final DataInput in, final String codec, final int minVersion, final int maxVersion)
'''
pass
def checkIndexHeader():
'''public static int checkIndexHeader(final DataInput in, final String codec, final int minVersion, final int maxVersion, final byte[] expectedID, final String expectedSuffix)
'''
pass
def verifyAndCopyIndexHeader():
'''public static void verifyAndCopyIndexHeader(final IndexInput in, final DataOutput out, final byte[] expectedID)
'''
pass
def readIndexHeader():
'''public static byte[] readIndexHeader(final IndexInput in)
'''
pass
def readFooter():
'''public static byte[] readFooter(final IndexInput in)
'''
pass
def checkIndexHeaderID():
'''public static byte[] checkIndexHeaderID(final DataInput in, final byte[] expectedID)
'''
pass
def checkIndexHeaderSuffix():
'''public static String checkIndexHeaderSuffix(final DataInput in, final String expectedSuffix)
'''
pass
def writeFooter():
'''public static void writeFooter(final IndexOutput out)
'''
pass
def footerLength():
'''public static int footerLength()
'''
pass
def checkFooter():
'''public static long checkFooter(final ChecksumIndexInput in)
public static void checkFooter(final ChecksumIndexInput in, final Throwable priorException)
'''
pass
def retrieveChecksum():
'''public static long retrieveChecksum(final IndexInput in)
'''
pass
def checksumEntireFile():
'''public static long checksumEntireFile(final IndexInput input)
'''
pass
