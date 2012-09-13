#!/usr/bin/env python

'''
file_locking.py - Example usage of POSIX fcntl calls to lock files.

If two processes both rely on a shared file for reading and writing, it is
possible that one may be writing while the other is reading. In this case,
the reading process can reach the end of the (truncated) file before it is
completely written, resulting in incomplete or corrupted data.

On Unix-based systems, file locking is implemented by the filesystem. By acquiring
a lock, a process can restrict what other processes may do with the file. Calls
will block until the lock is released.

There are three sorts of lock available:
    Shared lock      (fcntl.LOCK_SH) - Denies write access, allows read access.
    Exclusive lock   (fcntl.LOCK_EX) - Denies read and write access.
    Nonblocking lock (fcntl.LOCK_NB) - Returns immediately.

    The locks can be bitwise-or'd together if necessary.

In this example, we use exclusive locks.

Author: Eric Saunders
December 2010
'''

import fcntl
import sys
from time import sleep

def write_file(file_to_write):
    '''Write some data to a file, locking it during the write.'''

    # Open a file for writing
    print "Opened file for writing..."
    fh = open(file_to_write, 'w')

    # Acquire an exclusive lock for the duration of the write
    lock = fcntl.LOCK_EX
    fcntl.flock(fh.fileno(), lock)
    print "Acquired exclusive lock for duration of write..."

    # Write the data
    print "Writing data to file..."
    write_file_quite_slowly(fh)

    # Flush the buffer to ensure the whole file is written
    fh.flush()

    # Release the lock
    unlock = fcntl.LOCK_UN
    fcntl.flock(fh.fileno(), unlock)

    # Close the file
    fh.close()

    print "Released lock and closed file..."


def write_file_quite_slowly(fh):
    '''Write some data to a file, taking some time.'''

    n = 20
    for i in range(n):
        sleep(1)
        fh.write(str(i) + "\n")
        print "Wrote %d/%d" % ( i, n)


def read_file(file_to_read):
    '''Read data from a file, locking it during the read.'''

    # Open a file for reading
    fh = open(file_to_read, 'r')
    print "Opened file for reading..."

    # Acquire an exclusive lock for the duration of the read
    lock = fcntl.LOCK_EX
    fcntl.flock(fh.fileno(), lock)
    print "Acquired exclusive lock for duration of read..."

    # Read the data
    print "Reading data from file..."
    data = read_file_quite_slowly(fh)
    print "Got data!", data

    # Release the lock
    unlock = fcntl.LOCK_UN
    fcntl.flock(fh.fileno(), unlock)
    
    # Close the file
    fh.close()

    print "Released lock and closed file..."


def read_file_quite_slowly(fh):
    '''Read some data from a file, taking some time.'''

    data = []
    for val in fh:
        val = int(val.strip())
        data.append(val)
        sleep(1)
        print "Read values:", val

    return data


if __name__ == "__main__":

    usage = "Usage: python %s read|write" % sys.argv[0]
    # Give up unless we got a command line argument
    if len(sys.argv) < 2:
        print usage
        exit()

    shared_file = 'shared_stuff.dat'
    read_or_write = sys.argv[1]

    if read_or_write == 'read':
        read_file(shared_file)

    elif read_or_write == 'write':
        write_file(shared_file)

    else:
        print usage
        exit()
