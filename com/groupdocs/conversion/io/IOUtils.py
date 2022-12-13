DIR_SEPARATOR_UNIX = "char  '/'"
DIR_SEPARATOR_WINDOWS = "char  '\\'"
LINE_SEPARATOR_UNIX = "String  \"\n\""
LINE_SEPARATOR_WINDOWS = "String  \"\r\n\""
def close():
    '''    public static void close(final URLConnection conn)
    '''
def closeQuietly():
    '''    public static void closeQuietly(final Reader input)
    public static void closeQuietly(final Writer output)
    public static void closeQuietly(final InputStream input)
    public static void closeQuietly(final OutputStream output)
    public static void closeQuietly(final Closeable closeable)
    public static void closeQuietly(final Socket sock)
    public static void closeQuietly(final Selector selector)
    public static void closeQuietly(final ServerSocket sock)
    '''
def toBufferedInputStream():
    '''    public static InputStream toBufferedInputStream(final InputStream input)
    '''
def toBufferedReader():
    '''    public static BufferedReader toBufferedReader(final Reader reader)
    '''
def toByteArray():
    '''    public static byte[] toByteArray(final InputStream input)
    public static byte[] toByteArray(final InputStream input, final long size)
    public static byte[] toByteArray(final InputStream input, final int size)
    public static byte[] toByteArray(final Reader input)
    public static byte[] toByteArray(final Reader input, final Charset encoding)
    public static byte[] toByteArray(final Reader input, final String encoding)
    public static byte[] toByteArray(final String input)
    public static byte[] toByteArray(final URI uri)
    public static byte[] toByteArray(final URL url)
    public static byte[] toByteArray(final URLConnection urlConn)
    '''
def toCharArray():
    '''    public static char[] toCharArray(final InputStream is)
    public static char[] toCharArray(final InputStream is, final Charset encoding)
    public static char[] toCharArray(final InputStream is, final String encoding)
    public static char[] toCharArray(final Reader input)
    '''
def toString():
    '''    public static String toString(final InputStream input)
    public static String toString(final InputStream input, final Charset encoding)
    public static String toString(final InputStream input, final String encoding)
    public static String toString(final Reader input)
    public static String toString(final URI uri)
    public static String toString(final URI uri, final Charset encoding)
    public static String toString(final URI uri, final String encoding)
    public static String toString(final URL url)
    public static String toString(final URL url, final Charset encoding)
    public static String toString(final URL url, final String encoding)
    public static String toString(final byte[] input)
    public static String toString(final byte[] input, final String encoding)
    '''
def readLines():
    '''    public static List<String> readLines(final InputStream input)
    public static List<String> readLines(final InputStream input, final Charset encoding)
    public static List<String> readLines(final InputStream input, final String encoding)
    public static List<String> readLines(final Reader input)
    '''
def lineIterator():
    '''    public static o lineIterator(final Reader reader)
    public static o lineIterator(final InputStream input, final Charset encoding)
    public static o lineIterator(final InputStream input, final String encoding)
    '''
def toInputStream():
    '''    public static InputStream toInputStream(final CharSequence input)
    public static InputStream toInputStream(final CharSequence input, final Charset encoding)
    public static InputStream toInputStream(final CharSequence input, final String encoding)
    public static InputStream toInputStream(final String input)
    public static InputStream toInputStream(final String input, final Charset encoding)
    public static InputStream toInputStream(final String input, final String encoding)
    '''
def write():
    '''    public static void write(final byte[] data, final OutputStream output)
    public static void write(final byte[] data, final Writer output)
    public static void write(final byte[] data, final Writer output, final Charset encoding)
    public static void write(final byte[] data, final Writer output, final String encoding)
    public static void write(final char[] data, final Writer output)
    public static void write(final char[] data, final OutputStream output)
    public static void write(final char[] data, final OutputStream output, final Charset encoding)
    public static void write(final char[] data, final OutputStream output, final String encoding)
    public static void write(final CharSequence data, final Writer output)
    public static void write(final CharSequence data, final OutputStream output)
    public static void write(final CharSequence data, final OutputStream output, final Charset encoding)
    public static void write(final CharSequence data, final OutputStream output, final String encoding)
    public static void write(final String data, final Writer output)
    public static void write(final String data, final OutputStream output)
    public static void write(final String data, final OutputStream output, final Charset encoding)
    public static void write(final String data, final OutputStream output, final String encoding)
    public static void write(final StringBuffer data, final Writer output)
    public static void write(final StringBuffer data, final OutputStream output)
    public static void write(final StringBuffer data, final OutputStream output, final String encoding)
    '''
def writeLines():
    '''    public static void writeLines(final Collection<?> lines, final String lineEnding, final OutputStream output)
    public static void writeLines(final Collection<?> lines, String lineEnding, final OutputStream output, final Charset encoding)
    public static void writeLines(final Collection<?> lines, final String lineEnding, final OutputStream output, final String encoding)
    public static void writeLines(final Collection<?> lines, String lineEnding, final Writer writer)
    '''
def copy():
    '''    public static int copy(final InputStream input, final OutputStream output)
    public static void copy(final InputStream input, final Writer output)
    public static void copy(final InputStream input, final Writer output, final Charset encoding)
    public static void copy(final InputStream input, final Writer output, final String encoding)
    public static int copy(final Reader input, final Writer output)
    public static void copy(final Reader input, final OutputStream output)
    public static void copy(final Reader input, final OutputStream output, final Charset encoding)
    public static void copy(final Reader input, final OutputStream output, final String encoding)
    '''
def copyLarge():
    '''    public static long copyLarge(final InputStream input, final OutputStream output)
    public static long copyLarge(final InputStream input, final OutputStream output, final byte[] buffer)
    public static long copyLarge(final InputStream input, final OutputStream output, final long inputOffset, final long length)
    public static long copyLarge(final InputStream input, final OutputStream output, final long inputOffset, final long length, final byte[] buffer)
    public static long copyLarge(final Reader input, final Writer output)
    public static long copyLarge(final Reader input, final Writer output, final char[] buffer)
    public static long copyLarge(final Reader input, final Writer output, final long inputOffset, final long length)
    public static long copyLarge(final Reader input, final Writer output, final long inputOffset, final long length, final char[] buffer)
    '''
def contentEquals():
    '''    public static boolean contentEquals(InputStream input1, InputStream input2)
    public static boolean contentEquals(Reader input1, Reader input2)
    '''
def contentEqualsIgnoreEOL():
    '''    public static boolean contentEqualsIgnoreEOL(final Reader input1, final Reader input2)
    '''
def skip():
    '''    public static long skip(final InputStream input, final long toSkip)
    public static long skip(final Reader input, final long toSkip)
    '''
def skipFully():
    '''    public static void skipFully(final InputStream input, final long toSkip)
    public static void skipFully(final Reader input, final long toSkip)
    '''
def read():
    '''    public static int read(final Reader input, final char[] buffer, final int offset, final int length)
    public static int read(final Reader input, final char[] buffer)
    public static int read(final InputStream input, final byte[] buffer, final int offset, final int length)
    public static int read(final InputStream input, final byte[] buffer)
    '''
def readFully():
    '''    public static void readFully(final Reader input, final char[] buffer, final int offset, final int length)
    public static void readFully(final Reader input, final char[] buffer)
    public static void readFully(final InputStream input, final byte[] buffer, final int offset, final int length)
    public static void readFully(final InputStream input, final byte[] buffer)
    '''
