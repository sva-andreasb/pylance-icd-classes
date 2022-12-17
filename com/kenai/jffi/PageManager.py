PROT_EXEC = "int  4"
PROT_READ = "int  1"
PROT_WRITE = "int  2"
def ():
    '''returns Windows\n\n
    ()\n
    ()\n
    '''
def allocatePages():
    '''returns long\n\n
    allocatePages(final int npages, final int protection)\n
    allocatePages(final int pageCount, final int protection)\n
    '''
def freePages():
    '''returns None\n\n
    freePages(final long address, final int npages)\n
    freePages(final long address, final int pageCount)\n
    '''
def protectPages():
    '''returns None\n\n
    protectPages(final long address, final int npages, final int protection)\n
    protectPages(final long address, final int pageCount, final int protection)\n
    '''
