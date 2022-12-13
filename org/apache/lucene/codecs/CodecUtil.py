CODEC_MAGIC = "int  1071082519"
FOOTER_MAGIC = "int  -1071082520"
def writeHeader():
    '''    public static void writeHeader(final DataOutput out, final String codec, final int version)
    '''
def writeIndexHeader():
    '''    public static void writeIndexHeader(final DataOutput out, final String codec, final int version, final byte[] id, final String suffix)
    '''
def headerLength():
    '''    public static int headerLength(final String codec)
    '''
def indexHeaderLength():
    '''    public static int indexHeaderLength(final String codec, final String suffix)
    '''
def checkHeader():
    '''    public static int checkHeader(final DataInput in, final String codec, final int minVersion, final int maxVersion)
    '''
def checkHeaderNoMagic():
    '''    public static int checkHeaderNoMagic(final DataInput in, final String codec, final int minVersion, final int maxVersion)
    '''
def checkIndexHeader():
    '''    public static int checkIndexHeader(final DataInput in, final String codec, final int minVersion, final int maxVersion, final byte[] expectedID, final String expectedSuffix)
    '''
def verifyAndCopyIndexHeader():
    '''    public static void verifyAndCopyIndexHeader(final IndexInput in, final DataOutput out, final byte[] expectedID)
    '''
def readIndexHeader():
    '''    public static byte[] readIndexHeader(final IndexInput in)
    '''
def readFooter():
    '''    public static byte[] readFooter(final IndexInput in)
    '''
def checkIndexHeaderID():
    '''    public static byte[] checkIndexHeaderID(final DataInput in, final byte[] expectedID)
    '''
def checkIndexHeaderSuffix():
    '''    public static String checkIndexHeaderSuffix(final DataInput in, final String expectedSuffix)
    '''
def writeFooter():
    '''    public static void writeFooter(final IndexOutput out)
    '''
def footerLength():
    '''    public static int footerLength()
    '''
def checkFooter():
    '''    public static long checkFooter(final ChecksumIndexInput in)
    public static void checkFooter(final ChecksumIndexInput in, final Throwable priorException)
    '''
def retrieveChecksum():
    '''    public static long retrieveChecksum(final IndexInput in)
    '''
def checksumEntireFile():
    '''    public static long checksumEntireFile(final IndexInput input)
    '''
