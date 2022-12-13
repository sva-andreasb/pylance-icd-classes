def filter():
    '''    public static File[] filter(final IOFileFilter filter, final File... files)
    public static File[] filter(final IOFileFilter filter, final Iterable<File> files)
    '''
def filterList():
    '''    public static List<File> filterList(final IOFileFilter filter, final Iterable<File> files)
    public static List<File> filterList(final IOFileFilter filter, final File... files)
    '''
def filterSet():
    '''    public static Set<File> filterSet(final IOFileFilter filter, final File... files)
    public static Set<File> filterSet(final IOFileFilter filter, final Iterable<File> files)
    '''
def prefixFileFilter():
    '''    public static IOFileFilter prefixFileFilter(final String prefix)
    public static IOFileFilter prefixFileFilter(final String prefix, final IOCase caseSensitivity)
    '''
def suffixFileFilter():
    '''    public static IOFileFilter suffixFileFilter(final String suffix)
    public static IOFileFilter suffixFileFilter(final String suffix, final IOCase caseSensitivity)
    '''
def nameFileFilter():
    '''    public static IOFileFilter nameFileFilter(final String name)
    public static IOFileFilter nameFileFilter(final String name, final IOCase caseSensitivity)
    '''
def directoryFileFilter():
    '''    public static IOFileFilter directoryFileFilter()
    '''
def fileFileFilter():
    '''    public static IOFileFilter fileFileFilter()
    '''
def andFileFilter():
    '''    public static IOFileFilter andFileFilter(final IOFileFilter filter1, final IOFileFilter filter2)
    '''
def orFileFilter():
    '''    public static IOFileFilter orFileFilter(final IOFileFilter filter1, final IOFileFilter filter2)
    '''
def and():
    '''    public static IOFileFilter and(final IOFileFilter... filters)
    '''
def or():
    '''    public static IOFileFilter or(final IOFileFilter... filters)
    '''
def toList():
    '''    public static List<IOFileFilter> toList(final IOFileFilter... filters)
    '''
def notFileFilter():
    '''    public static IOFileFilter notFileFilter(final IOFileFilter filter)
    '''
def trueFileFilter():
    '''    public static IOFileFilter trueFileFilter()
    '''
def falseFileFilter():
    '''    public static IOFileFilter falseFileFilter()
    '''
def asFileFilter():
    '''    public static IOFileFilter asFileFilter(final FileFilter filter)
    public static IOFileFilter asFileFilter(final FilenameFilter filter)
    '''
def ageFileFilter():
    '''    public static IOFileFilter ageFileFilter(final long cutoff)
    public static IOFileFilter ageFileFilter(final long cutoff, final boolean acceptOlder)
    public static IOFileFilter ageFileFilter(final Date cutoffDate)
    public static IOFileFilter ageFileFilter(final Date cutoffDate, final boolean acceptOlder)
    public static IOFileFilter ageFileFilter(final File cutoffReference)
    public static IOFileFilter ageFileFilter(final File cutoffReference, final boolean acceptOlder)
    '''
def sizeFileFilter():
    '''    public static IOFileFilter sizeFileFilter(final long threshold)
    public static IOFileFilter sizeFileFilter(final long threshold, final boolean acceptLarger)
    '''
def sizeRangeFileFilter():
    '''    public static IOFileFilter sizeRangeFileFilter(final long minSizeInclusive, final long maxSizeInclusive)
    '''
def magicNumberFileFilter():
    '''    public static IOFileFilter magicNumberFileFilter(final String magicNumber)
    public static IOFileFilter magicNumberFileFilter(final String magicNumber, final long offset)
    public static IOFileFilter magicNumberFileFilter(final byte[] magicNumber)
    public static IOFileFilter magicNumberFileFilter(final byte[] magicNumber, final long offset)
    '''
def makeCVSAware():
    '''    public static IOFileFilter makeCVSAware(final IOFileFilter filter)
    '''
def makeSVNAware():
    '''    public static IOFileFilter makeSVNAware(final IOFileFilter filter)
    '''
def makeDirectoryOnly():
    '''    public static IOFileFilter makeDirectoryOnly(final IOFileFilter filter)
    '''
def makeFileOnly():
    '''    public static IOFileFilter makeFileOnly(final IOFileFilter filter)
    '''
