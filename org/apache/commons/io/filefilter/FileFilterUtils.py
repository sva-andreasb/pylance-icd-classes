def filter():
'''public static File[] filter(final IOFileFilter filter, final File... files)
public static File[] filter(final IOFileFilter filter, final Iterable<File> files)
'''
pass
def filterList():
'''public static List<File> filterList(final IOFileFilter filter, final Iterable<File> files)
public static List<File> filterList(final IOFileFilter filter, final File... files)
'''
pass
def filterSet():
'''public static Set<File> filterSet(final IOFileFilter filter, final File... files)
public static Set<File> filterSet(final IOFileFilter filter, final Iterable<File> files)
'''
pass
def prefixFileFilter():
'''public static IOFileFilter prefixFileFilter(final String prefix)
public static IOFileFilter prefixFileFilter(final String prefix, final IOCase caseSensitivity)
'''
pass
def suffixFileFilter():
'''public static IOFileFilter suffixFileFilter(final String suffix)
public static IOFileFilter suffixFileFilter(final String suffix, final IOCase caseSensitivity)
'''
pass
def nameFileFilter():
'''public static IOFileFilter nameFileFilter(final String name)
public static IOFileFilter nameFileFilter(final String name, final IOCase caseSensitivity)
'''
pass
def directoryFileFilter():
'''public static IOFileFilter directoryFileFilter()
'''
pass
def fileFileFilter():
'''public static IOFileFilter fileFileFilter()
'''
pass
def andFileFilter():
'''public static IOFileFilter andFileFilter(final IOFileFilter filter1, final IOFileFilter filter2)
'''
pass
def orFileFilter():
'''public static IOFileFilter orFileFilter(final IOFileFilter filter1, final IOFileFilter filter2)
'''
pass
def and():
'''public static IOFileFilter and(final IOFileFilter... filters)
'''
pass
def or():
'''public static IOFileFilter or(final IOFileFilter... filters)
'''
pass
def toList():
'''public static List<IOFileFilter> toList(final IOFileFilter... filters)
'''
pass
def notFileFilter():
'''public static IOFileFilter notFileFilter(final IOFileFilter filter)
'''
pass
def trueFileFilter():
'''public static IOFileFilter trueFileFilter()
'''
pass
def falseFileFilter():
'''public static IOFileFilter falseFileFilter()
'''
pass
def asFileFilter():
'''public static IOFileFilter asFileFilter(final FileFilter filter)
public static IOFileFilter asFileFilter(final FilenameFilter filter)
'''
pass
def ageFileFilter():
'''public static IOFileFilter ageFileFilter(final long cutoff)
public static IOFileFilter ageFileFilter(final long cutoff, final boolean acceptOlder)
public static IOFileFilter ageFileFilter(final Date cutoffDate)
public static IOFileFilter ageFileFilter(final Date cutoffDate, final boolean acceptOlder)
public static IOFileFilter ageFileFilter(final File cutoffReference)
public static IOFileFilter ageFileFilter(final File cutoffReference, final boolean acceptOlder)
'''
pass
def sizeFileFilter():
'''public static IOFileFilter sizeFileFilter(final long threshold)
public static IOFileFilter sizeFileFilter(final long threshold, final boolean acceptLarger)
'''
pass
def sizeRangeFileFilter():
'''public static IOFileFilter sizeRangeFileFilter(final long minSizeInclusive, final long maxSizeInclusive)
'''
pass
def magicNumberFileFilter():
'''public static IOFileFilter magicNumberFileFilter(final String magicNumber)
public static IOFileFilter magicNumberFileFilter(final String magicNumber, final long offset)
public static IOFileFilter magicNumberFileFilter(final byte[] magicNumber)
public static IOFileFilter magicNumberFileFilter(final byte[] magicNumber, final long offset)
'''
pass
def makeCVSAware():
'''public static IOFileFilter makeCVSAware(final IOFileFilter filter)
'''
pass
def makeSVNAware():
'''public static IOFileFilter makeSVNAware(final IOFileFilter filter)
'''
pass
def makeDirectoryOnly():
'''public static IOFileFilter makeDirectoryOnly(final IOFileFilter filter)
'''
pass
def makeFileOnly():
'''public static IOFileFilter makeFileOnly(final IOFileFilter filter)
'''
pass
