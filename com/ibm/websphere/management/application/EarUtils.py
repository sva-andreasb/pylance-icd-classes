def getEarFile():
'''public static EARFile getEarFile(final String filePath, final boolean useReflection)
public static EARFile getEarFile(final String filePath, final boolean useReflection, final boolean isReadOnly)
'''
pass
def getArchive():
'''public static Archive getArchive(final String filePath, final boolean useReflection, final boolean isReadOnly)
'''
pass
def extractEar():
'''public static void extractEar(final EARFile earFile, final String dirName, final boolean bCleanup)
public static void extractEar(final EARFile earFile, final String dirName, final boolean bCleanup, final int options)
'''
pass
def extractArchive():
'''public static void extractArchive(final Archive arc, final String dirName, final boolean bCleanup, final int options)
'''
pass
def deleteDirTree():
'''public static synchronized void deleteDirTree(final String dir)
public static synchronized void deleteDirTree(final File dir)
'''
pass
def getAppVersionForDeployment():
'''public static int getAppVersionForDeployment(final EARFile ear)
'''
pass
def getLowestNodeVersionForModule():
'''public static int getLowestNodeVersionForModule(final Module module)
'''
pass
