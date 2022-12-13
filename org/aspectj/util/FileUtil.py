def isZipFile():
    '''public static boolean isZipFile(final File file)
    '''
def zipSuffixLength():
    '''public static int zipSuffixLength(final File file)
    public static int zipSuffixLength(final String path)
    '''
def hasSourceSuffix():
    '''public static boolean hasSourceSuffix(final File file)
    public static boolean hasSourceSuffix(final String path)
    '''
def sourceSuffixLength():
    '''public static int sourceSuffixLength(final File file)
    public static int sourceSuffixLength(final String path)
    '''
def canReadDir():
    '''public static boolean canReadDir(final File dir)
    '''
def canReadFile():
    '''public static boolean canReadFile(final File file)
    '''
def canWriteDir():
    '''public static boolean canWriteDir(final File dir)
    '''
def canWriteFile():
    '''public static boolean canWriteFile(final File file)
    '''
def throwIaxUnlessCanReadDir():
    '''public static void throwIaxUnlessCanReadDir(final File dir, final String label)
    '''
def throwIaxUnlessCanWriteFile():
    '''public static void throwIaxUnlessCanWriteFile(final File file, final String label)
    '''
def throwIaxUnlessCanWriteDir():
    '''public static void throwIaxUnlessCanWriteDir(final File dir, final String label)
    '''
def getPaths():
    '''public static String[] getPaths(final File[] files)
    public static String[] getPaths(final List<File> files)
    '''
def fileToClassName():
    '''public static String fileToClassName(final File basedir, final File classFile)
    '''
def normalizedPath():
    '''public static String normalizedPath(final File file, final File basedir)
    public static String normalizedPath(final File file)
    '''
def flatten():
    '''public static String flatten(final File[] files, final String infix)
    public static String flatten(final String[] paths, String infix)
    '''
def weakNormalize():
    '''public static String weakNormalize(String path)
    '''
def getBestFile():
    '''public static File getBestFile(final String[] paths)
    public static File getBestFile(final File file)
    '''
def getBestPath():
    '''public static String getBestPath(final File file)
    '''
def getAbsolutePaths():
    '''public static String[] getAbsolutePaths(final File[] files)
    '''
def deleteContents():
    '''public static int deleteContents(final File dir)
    public static int deleteContents(final File dir, final FileFilter filter)
    public static int deleteContents(final File dir, final FileFilter filter, final boolean deleteEmptyDirs)
    '''
def copyDir():
    '''public static int copyDir(final File fromDir, final File toDir)
    public static int copyDir(final File fromDir, final File toDir, final String fromSuffix, final String toSuffix)
    public static int copyDir(final File fromDir, final File toDir, final String fromSuffix, final String toSuffix, final FileFilter delegate)
    '''
def accept():
    '''public boolean accept(final File dir, final String name)
    public boolean accept(final File file)
    public boolean accept(final File f)
    public boolean accept(final File file)
    public boolean accept(final File pathname)
    '''
def listFiles():
    '''public static String[] listFiles(final File srcDir)
    public static File[] listFiles(final File srcDir, final FileFilter fileFilter)
    '''
def listClassFiles():
    '''public static List<File> listClassFiles(final File dir)
    '''
def getBaseDirFiles():
    '''public static File[] getBaseDirFiles(final File basedir, final String[] paths)
    public static File[] getBaseDirFiles(final File basedir, final String[] paths, final String[] suffixes)
    '''
def copyFiles():
    '''public static File[] copyFiles(final File srcDir, final String[] relativePaths, final File destDir)
    '''
def copyFile():
    '''public static void copyFile(final File fromFile, final File toFile)
    '''
def ensureParentWritable():
    '''public static File ensureParentWritable(final File path)
    '''
def copyValidFiles():
    '''public static void copyValidFiles(final File fromFile, final File toFile)
    '''
def copyStream():
    '''public static void copyStream(final DataInputStream in, final PrintStream out)
    public static void copyStream(final InputStream in, final OutputStream out)
    public static void copyStream(final Reader in, final Writer out)
    '''
def makeNewChildDir():
    '''public static File makeNewChildDir(final File parent, String child)
    '''
def getTempDir():
    '''public static File getTempDir(String name)
    '''
def getFileURLs():
    '''public static URL[] getFileURLs(final File[] files)
    '''
def getFileURL():
    '''public static URL getFileURL(final File file)
    '''
def writeAsString():
    '''public static String writeAsString(final File file, String contents)
    '''
def readBooleanArray():
    '''public static boolean[] readBooleanArray(final DataInputStream s)
    '''
def writeBooleanArray():
    '''public static void writeBooleanArray(final boolean[] a, final DataOutputStream s)
    '''
def readIntArray():
    '''public static int[] readIntArray(final DataInputStream s)
    '''
def writeIntArray():
    '''public static void writeIntArray(final int[] a, final DataOutputStream s)
    '''
def readStringArray():
    '''public static String[] readStringArray(final DataInputStream s)
    '''
def writeStringArray():
    '''public static void writeStringArray(final String[] a, final DataOutputStream s)
    '''
def readAsString():
    '''public static String readAsString(final File file)
    '''
def readAsByteArray():
    '''public static byte[] readAsByteArray(final File file)
    public static byte[] readAsByteArray(final InputStream inStream)
    '''
def getStreamFromZip():
    '''public static InputStream getStreamFromZip(final String zipFile, final String name)
    '''
def lineSeek():
    '''public static List<String> lineSeek(final String sought, final List<String> sources, final boolean listAll, final PrintStream errorSink)
    public static String lineSeek(final String sought, final String sourcePath, final boolean listAll, final ArrayList<String> sink)
    '''
def makeOutputStream():
    '''public static BufferedOutputStream makeOutputStream(final File file)
    '''
def sleepPastFinalModifiedTime():
    '''public static boolean sleepPastFinalModifiedTime(final File[] files)
    '''
def makeClasspath():
    '''public static List<String> makeClasspath(final URL[] urls)
    '''
def toString():
    '''public String toString()
    '''
def setSnoop():
    '''public void setSnoop(final ByteArrayOutputStream snoop)
    '''
def run():
    '''public void run()
    '''
def halt():
    '''public boolean halt(final boolean wait, final boolean finishStream)
    '''
def totalWritten():
    '''public long totalWritten()
    '''
def getThrown():
    '''public Throwable getThrown()
    '''
