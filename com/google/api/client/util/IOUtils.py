def copy():
    '''    public static void copy(final InputStream inputStream, final OutputStream outputStream)
    public static void copy(final InputStream inputStream, final OutputStream outputStream, final boolean closeInputStream)
    '''
def computeLength():
    '''    public static long computeLength(final StreamingContent content)
    '''
def serialize():
    '''    public static byte[] serialize(final Object value)
    public static void serialize(final Object value, final OutputStream outputStream)
    '''
def deserialize():
    '''    public static <S extends Serializable> S deserialize(final byte[] bytes)
    public static <S extends Serializable> S deserialize(final InputStream inputStream)
    '''
def isSymbolicLink():
    '''    public static boolean isSymbolicLink(final File file)
    '''
