def isZipFile():
'''public static boolean isZipFile(final File file)
'''
pass
def zipSuffixLength():
'''public static int zipSuffixLength(final File file)
public static int zipSuffixLength(final String path)
'''
pass
def hasSourceSuffix():
'''public static boolean hasSourceSuffix(final File file)
public static boolean hasSourceSuffix(final String path)
'''
pass
def sourceSuffixLength():
'''public static int sourceSuffixLength(final File file)
public static int sourceSuffixLength(final String path)
'''
pass
def canReadDir():
'''public static boolean canReadDir(final File dir)
'''
pass
def canReadFile():
'''public static boolean canReadFile(final File file)
'''
pass
def canWriteDir():
'''public static boolean canWriteDir(final File dir)
'''
pass
def canWriteFile():
'''public static boolean canWriteFile(final File file)
'''
pass
def throwIaxUnlessCanReadDir():
'''public static void throwIaxUnlessCanReadDir(final File dir, final String label)
'''
pass
def throwIaxUnlessCanWriteFile():
'''public static void throwIaxUnlessCanWriteFile(final File file, final String label)
'''
pass
def throwIaxUnlessCanWriteDir():
'''public static void throwIaxUnlessCanWriteDir(final File dir, final String label)
'''
pass
def getPaths():
'''public static String[] getPaths(final File[] files)
public static String[] getPaths(final List<File> files)
'''
pass
def fileToClassName():
'''public static String fileToClassName(final File basedir, final File classFile)
'''
pass
def normalizedPath():
'''public static String normalizedPath(final File file, final File basedir)
public static String normalizedPath(final File file)
'''
pass
def flatten():
'''public static String flatten(final File[] files, final String infix)
public static String flatten(final String[] paths, String infix)
'''
pass
def weakNormalize():
'''public static String weakNormalize(String path)
'''
pass
def getBestFile():
'''public static File getBestFile(final String[] paths)
public static File getBestFile(final File file)
'''
pass
def getBestPath():
'''public static String getBestPath(final File file)
'''
pass
def getAbsolutePaths():
'''public static String[] getAbsolutePaths(final File[] files)
'''
pass
def deleteContents():
'''public static int deleteContents(final File dir)
public static int deleteContents(final File dir, final FileFilter filter)
public static int deleteContents(final File dir, final FileFilter filter, final boolean deleteEmptyDirs)
'''
pass
def copyDir():
'''public static int copyDir(final File fromDir, final File toDir)
public static int copyDir(final File fromDir, final File toDir, final String fromSuffix, final String toSuffix)
public static int copyDir(final File fromDir, final File toDir, final String fromSuffix, final String toSuffix, final FileFilter delegate)
'''
pass
def accept():
'''public boolean accept(final File dir, final String name)
public boolean accept(final File file)
public boolean accept(final File f)
public boolean accept(final File file)
public boolean accept(final File pathname)
'''
pass
def listFiles():
'''public static String[] listFiles(final File srcDir)
public static File[] listFiles(final File srcDir, final FileFilter fileFilter)
'''
pass
def listClassFiles():
'''public static List<File> listClassFiles(final File dir)
'''
pass
def getBaseDirFiles():
'''public static File[] getBaseDirFiles(final File basedir, final String[] paths)
public static File[] getBaseDirFiles(final File basedir, final String[] paths, final String[] suffixes)
'''
pass
def copyFiles():
'''public static File[] copyFiles(final File srcDir, final String[] relativePaths, final File destDir)
'''
pass
def copyFile():
'''public static void copyFile(final File fromFile, final File toFile)
'''
pass
def ensureParentWritable():
'''public static File ensureParentWritable(final File path)
'''
pass
def copyValidFiles():
'''public static void copyValidFiles(final File fromFile, final File toFile)
'''
pass
def copyStream():
'''public static void copyStream(final DataInputStream in, final PrintStream out)
public static void copyStream(final InputStream in, final OutputStream out)
public static void copyStream(final Reader in, final Writer out)
'''
pass
def makeNewChildDir():
'''public static File makeNewChildDir(final File parent, String child)
'''
pass
def getTempDir():
'''public static File getTempDir(String name)
'''
pass
def getFileURLs():
'''public static URL[] getFileURLs(final File[] files)
'''
pass
def getFileURL():
'''public static URL getFileURL(final File file)
'''
pass
def writeAsString():
'''public static String writeAsString(final File file, String contents)
'''
pass
def readBooleanArray():
'''public static boolean[] readBooleanArray(final DataInputStream s)
'''
pass
def writeBooleanArray():
'''public static void writeBooleanArray(final boolean[] a, final DataOutputStream s)
'''
pass
def readIntArray():
'''public static int[] readIntArray(final DataInputStream s)
'''
pass
def writeIntArray():
'''public static void writeIntArray(final int[] a, final DataOutputStream s)
'''
pass
def readStringArray():
'''public static String[] readStringArray(final DataInputStream s)
'''
pass
def writeStringArray():
'''public static void writeStringArray(final String[] a, final DataOutputStream s)
'''
pass
def readAsString():
'''public static String readAsString(final File file)
'''
pass
def readAsByteArray():
'''public static byte[] readAsByteArray(final File file)
public static byte[] readAsByteArray(final InputStream inStream)
'''
pass
def getStreamFromZip():
'''public static InputStream getStreamFromZip(final String zipFile, final String name)
'''
pass
def lineSeek():
'''public static List<String> lineSeek(final String sought, final List<String> sources, final boolean listAll, final PrintStream errorSink)
public static String lineSeek(final String sought, final String sourcePath, final boolean listAll, final ArrayList<String> sink)
'''
pass
def makeOutputStream():
'''public static BufferedOutputStream makeOutputStream(final File file)
'''
pass
def sleepPastFinalModifiedTime():
'''public static boolean sleepPastFinalModifiedTime(final File[] files)
'''
pass
def makeClasspath():
'''public static List<String> makeClasspath(final URL[] urls)
'''
pass
def toString():
'''public String toString()
'''
pass
def setSnoop():
'''public void setSnoop(final ByteArrayOutputStream snoop)
'''
pass
def run():
'''public void run()
'''
pass
def halt():
'''public boolean halt(final boolean wait, final boolean finishStream)
'''
pass
def totalWritten():
'''public long totalWritten()
'''
pass
def getThrown():
'''public Throwable getThrown()
'''
pass
