def setMinInflateRatio():
    '''public static void setMinInflateRatio(final double ratio)
    '''
def getMinInflateRatio():
    '''public static double getMinInflateRatio()
    '''
def setMaxEntrySize():
    '''public static void setMaxEntrySize(final long maxEntrySize)
    '''
def getMaxEntrySize():
    '''public static long getMaxEntrySize()
    '''
def setMaxTextSize():
    '''public static void setMaxTextSize(final long maxTextSize)
    '''
def getMaxTextSize():
    '''public static long getMaxTextSize()
    '''
def ZipSecureFile():
    '''public ZipSecureFile(final File file, final int mode)
    public ZipSecureFile(final File file)
    public ZipSecureFile(final String name)
    '''
def getInputStream():
    '''public InputStream getInputStream(final ZipEntry entry)
    '''
def addThreshold():
    '''public static ThresholdInputStream addThreshold(final InputStream zipIS)
    '''
def run():
    '''public ThresholdInputStream run()
    '''
def ThresholdInputStream():
    '''public ThresholdInputStream(final InputStream is, final ThresholdInputStream cis)
    '''
def read():
    '''public int read()
    public int read(final byte[] b, final int off, final int len)
    '''
def skip():
    '''public long skip(final long n)
    '''
def reset():
    '''public synchronized void reset()
    '''
def advance():
    '''public void advance(final int advance)
    '''
def getNextEntry():
    '''public ZipEntry getNextEntry()
    '''
def closeEntry():
    '''public void closeEntry()
    '''
def unread():
    '''public void unread(final int b)
    public void unread(final byte[] b, final int off, final int len)
    '''
def available():
    '''public int available()
    '''
def markSupported():
    '''public boolean markSupported()
    '''
def mark():
    '''public synchronized void mark(final int readlimit)
    '''
