PROT_EXEC = "int  4"
PROT_READ = "int  1"
PROT_WRITE = "int  2"
def PageManager():
    '''    public PageManager()
    '''
def getInstance():
    '''    public static PageManager getInstance()
    '''
def pageSize():
    '''    public final long pageSize()
    '''
def allocatePages():
    '''    public long allocatePages(final int npages, final int protection)
    public long allocatePages(final int pageCount, final int protection)
    '''
def freePages():
    '''    public void freePages(final long address, final int npages)
    public void freePages(final long address, final int pageCount)
    '''
def protectPages():
    '''    public void protectPages(final long address, final int npages, final int protection)
    public void protectPages(final long address, final int pageCount, final int protection)
    '''
def Windows():
    '''    public Windows()
    '''
