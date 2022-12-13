def clone():
    '''    public static <T extends Serializable> T clone(final T object)
    '''
def roundtrip():
    '''    public static <T extends Serializable> T roundtrip(final T msg)
    '''
def serialize():
    '''    public static void serialize(final Serializable obj, final OutputStream outputStream)
    public static byte[] serialize(final Serializable obj)
    '''
def deserialize():
    '''    public static <T> T deserialize(final InputStream inputStream)
    public static <T> T deserialize(final byte[] objectData)
    '''
def ClassLoaderAwareObjectInputStream():
    '''    public ClassLoaderAwareObjectInputStream(final InputStream in, final ClassLoader classLoader)
    '''
