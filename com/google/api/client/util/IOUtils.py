def copy():
'''public static void copy(final InputStream inputStream, final OutputStream outputStream)
public static void copy(final InputStream inputStream, final OutputStream outputStream, final boolean closeInputStream)
'''
pass
def computeLength():
'''public static long computeLength(final StreamingContent content)
'''
pass
def serialize():
'''public static byte[] serialize(final Object value)
public static void serialize(final Object value, final OutputStream outputStream)
'''
pass
def deserialize():
'''public static <S extends Serializable> S deserialize(final byte[] bytes)
public static <S extends Serializable> S deserialize(final InputStream inputStream)
'''
pass
def isSymbolicLink():
'''public static boolean isSymbolicLink(final File file)
'''
pass
