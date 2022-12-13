ONE_KB = "long  1024L"
ONE_MB = "long  1048576L"
ONE_GB = "long  1073741824L"
ONE_TB = "long  1099511627776L"
ONE_PB = "long  1125899906842624L"
ONE_EB = "long  1152921504606846976L"
def getFile():
    '''public static File getFile(final File directory, final String... names)
    public static File getFile(final String... names)
    '''
def getTempDirectoryPath():
    '''public static String getTempDirectoryPath()
    '''
def getTempDirectory():
    '''public static File getTempDirectory()
    '''
def getUserDirectoryPath():
    '''public static String getUserDirectoryPath()
    '''
def getUserDirectory():
    '''public static File getUserDirectory()
    '''
def openInputStream():
    '''public static FileInputStream openInputStream(final File file)
    '''
def openOutputStream():
    '''public static FileOutputStream openOutputStream(final File file)
    public static FileOutputStream openOutputStream(final File file, final boolean append)
    '''
def byteCountToDisplaySize():
    '''public static String byteCountToDisplaySize(final BigInteger size)
    public static String byteCountToDisplaySize(final long size)
    '''
def touch():
    '''public static void touch(final File file)
    '''
def convertFileCollectionToFileArray():
    '''public static File[] convertFileCollectionToFileArray(final Collection<File> files)
    '''
def listFiles():
    '''public static Collection<File> listFiles(final File directory, final IOFileFilter fileFilter, final IOFileFilter dirFilter)
    public static Collection<File> listFiles(final File directory, final String[] extensions, final boolean recursive)
    '''
def listFilesAndDirs():
    '''public static Collection<File> listFilesAndDirs(final File directory, final IOFileFilter fileFilter, final IOFileFilter dirFilter)
    '''
def iterateFiles():
    '''public static Iterator<File> iterateFiles(final File directory, final IOFileFilter fileFilter, final IOFileFilter dirFilter)
    public static Iterator<File> iterateFiles(final File directory, final String[] extensions, final boolean recursive)
    '''
def iterateFilesAndDirs():
    '''public static Iterator<File> iterateFilesAndDirs(final File directory, final IOFileFilter fileFilter, final IOFileFilter dirFilter)
    '''
def contentEquals():
    '''public static boolean contentEquals(final File file1, final File file2)
    '''
def contentEqualsIgnoreEOL():
    '''public static boolean contentEqualsIgnoreEOL(final File file1, final File file2, final String charsetName)
    '''
def toFile():
    '''public static File toFile(final URL url)
    '''
def toFiles():
    '''public static File[] toFiles(final URL[] urls)
    '''
def toURLs():
    '''public static URL[] toURLs(final File[] files)
    '''
def copyFileToDirectory():
    '''public static void copyFileToDirectory(final File srcFile, final File destDir)
    public static void copyFileToDirectory(final File srcFile, final File destDir, final boolean preserveFileDate)
    '''
def copyFile():
    '''public static void copyFile(final File srcFile, final File destFile)
    public static void copyFile(final File srcFile, final File destFile, final boolean preserveFileDate)
    public static long copyFile(final File input, final OutputStream output)
    '''
def copyDirectoryToDirectory():
    '''public static void copyDirectoryToDirectory(final File srcDir, final File destDir)
    '''
def copyDirectory():
    '''public static void copyDirectory(final File srcDir, final File destDir)
    public static void copyDirectory(final File srcDir, final File destDir, final boolean preserveFileDate)
    public static void copyDirectory(final File srcDir, final File destDir, final FileFilter filter)
    public static void copyDirectory(final File srcDir, final File destDir, final FileFilter filter, final boolean preserveFileDate)
    '''
def copyURLToFile():
    '''public static void copyURLToFile(final URL source, final File destination)
    public static void copyURLToFile(final URL source, final File destination, final int connectionTimeout, final int readTimeout)
    '''
def copyInputStreamToFile():
    '''public static void copyInputStreamToFile(final InputStream source, final File destination)
    '''
def copyToFile():
    '''public static void copyToFile(final InputStream source, final File destination)
    '''
def deleteDirectory():
    '''public static void deleteDirectory(final File directory)
    '''
def deleteQuietly():
    '''public static boolean deleteQuietly(final File file)
    '''
def directoryContains():
    '''public static boolean directoryContains(final File directory, final File child)
    '''
def cleanDirectory():
    '''public static void cleanDirectory(final File directory)
    '''
def waitFor():
    '''public static boolean waitFor(final File file, final int seconds)
    '''
def readFileToString():
    '''public static String readFileToString(final File file, final Charset encoding)
    public static String readFileToString(final File file, final String encoding)
    public static String readFileToString(final File file)
    '''
def readFileToByteArray():
    '''public static byte[] readFileToByteArray(final File file)
    '''
def readLines():
    '''public static List<String> readLines(final File file, final Charset encoding)
    public static List<String> readLines(final File file, final String encoding)
    public static List<String> readLines(final File file)
    '''
def lineIterator():
    '''public static LineIterator lineIterator(final File file, final String encoding)
    public static LineIterator lineIterator(final File file)
    '''
def writeStringToFile():
    '''public static void writeStringToFile(final File file, final String data, final Charset encoding)
    public static void writeStringToFile(final File file, final String data, final String encoding)
    public static void writeStringToFile(final File file, final String data, final Charset encoding, final boolean append)
    public static void writeStringToFile(final File file, final String data, final String encoding, final boolean append)
    public static void writeStringToFile(final File file, final String data)
    public static void writeStringToFile(final File file, final String data, final boolean append)
    '''
def write():
    '''public static void write(final File file, final CharSequence data)
    public static void write(final File file, final CharSequence data, final boolean append)
    public static void write(final File file, final CharSequence data, final Charset encoding)
    public static void write(final File file, final CharSequence data, final String encoding)
    public static void write(final File file, final CharSequence data, final Charset encoding, final boolean append)
    public static void write(final File file, final CharSequence data, final String encoding, final boolean append)
    '''
def writeByteArrayToFile():
    '''public static void writeByteArrayToFile(final File file, final byte[] data)
    public static void writeByteArrayToFile(final File file, final byte[] data, final boolean append)
    public static void writeByteArrayToFile(final File file, final byte[] data, final int off, final int len)
    public static void writeByteArrayToFile(final File file, final byte[] data, final int off, final int len, final boolean append)
    '''
def writeLines():
    '''public static void writeLines(final File file, final String encoding, final Collection<?> lines)
    public static void writeLines(final File file, final String encoding, final Collection<?> lines, final boolean append)
    public static void writeLines(final File file, final Collection<?> lines)
    public static void writeLines(final File file, final Collection<?> lines, final boolean append)
    public static void writeLines(final File file, final String encoding, final Collection<?> lines, final String lineEnding)
    public static void writeLines(final File file, final String encoding, final Collection<?> lines, final String lineEnding, final boolean append)
    public static void writeLines(final File file, final Collection<?> lines, final String lineEnding)
    public static void writeLines(final File file, final Collection<?> lines, final String lineEnding, final boolean append)
    '''
def forceDelete():
    '''public static void forceDelete(final File file)
    '''
def forceDeleteOnExit():
    '''public static void forceDeleteOnExit(final File file)
    '''
def forceMkdir():
    '''public static void forceMkdir(final File directory)
    '''
def forceMkdirParent():
    '''public static void forceMkdirParent(final File file)
    '''
def sizeOf():
    '''public static long sizeOf(final File file)
    '''
def sizeOfAsBigInteger():
    '''public static BigInteger sizeOfAsBigInteger(final File file)
    '''
def sizeOfDirectory():
    '''public static long sizeOfDirectory(final File directory)
    '''
def sizeOfDirectoryAsBigInteger():
    '''public static BigInteger sizeOfDirectoryAsBigInteger(final File directory)
    '''
def isFileNewer():
    '''public static boolean isFileNewer(final File file, final File reference)
    public static boolean isFileNewer(final File file, final Date date)
    public static boolean isFileNewer(final File file, final long timeMillis)
    '''
def isFileOlder():
    '''public static boolean isFileOlder(final File file, final File reference)
    public static boolean isFileOlder(final File file, final Date date)
    public static boolean isFileOlder(final File file, final long timeMillis)
    '''
def checksumCRC32():
    '''public static long checksumCRC32(final File file)
    '''
def checksum():
    '''public static Checksum checksum(final File file, final Checksum checksum)
    '''
def moveDirectory():
    '''public static void moveDirectory(final File srcDir, final File destDir)
    '''
def moveDirectoryToDirectory():
    '''public static void moveDirectoryToDirectory(final File src, final File destDir, final boolean createDestDir)
    '''
def moveFile():
    '''public static void moveFile(final File srcFile, final File destFile)
    '''
def moveFileToDirectory():
    '''public static void moveFileToDirectory(final File srcFile, final File destDir, final boolean createDestDir)
    '''
def moveToDirectory():
    '''public static void moveToDirectory(final File src, final File destDir, final boolean createDestDir)
    '''
def isSymlink():
    '''public static boolean isSymlink(final File file)
    '''
def accept():
    '''public boolean accept(final File aFile)
    '''
