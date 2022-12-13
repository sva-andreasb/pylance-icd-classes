def clone():
'''public static <T extends Serializable> T clone(final T object)
'''
pass
def roundtrip():
'''public static <T extends Serializable> T roundtrip(final T msg)
'''
pass
def serialize():
'''public static void serialize(final Serializable obj, final OutputStream outputStream)
public static byte[] serialize(final Serializable obj)
'''
pass
def deserialize():
'''public static <T> T deserialize(final InputStream inputStream)
public static <T> T deserialize(final byte[] objectData)
'''
pass
def ClassLoaderAwareObjectInputStream():
'''public ClassLoaderAwareObjectInputStream(final InputStream in, final ClassLoader classLoader)
'''
pass
