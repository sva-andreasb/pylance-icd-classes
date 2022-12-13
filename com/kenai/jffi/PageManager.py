PROT_EXEC = "int  4"
PROT_READ = "int  1"
PROT_WRITE = "int  2"
def PageManager():
'''public PageManager()
'''
pass
def getInstance():
'''public static PageManager getInstance()
'''
pass
def pageSize():
'''public final long pageSize()
'''
pass
def allocatePages():
'''public long allocatePages(final int npages, final int protection)
public long allocatePages(final int pageCount, final int protection)
'''
pass
def freePages():
'''public void freePages(final long address, final int npages)
public void freePages(final long address, final int pageCount)
'''
pass
def protectPages():
'''public void protectPages(final long address, final int npages, final int protection)
public void protectPages(final long address, final int pageCount, final int protection)
'''
pass
def Windows():
'''public Windows()
'''
pass
