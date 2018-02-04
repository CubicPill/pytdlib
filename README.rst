=======
pytdlib
=======

A python wrapper for telegram's tdlib

----------------------
Building the C++ TDLib
----------------------

**NOTE: You may create a new folder in the source directory to build the c++ lib**, like the following::

    mkdir build
    cd build
    cmake ..
    make

---------------------------------
Building the Boost.Python wrapper
---------------------------------
************
Requirements
************
gcc 7.2.0 (don't use it in the ubuntu mirrors, compile the newest version yourself!)


*********
Procedure
*********
Set the environment variables::

    PYTHON_INCLUDE_PATH    // directory of python headers

And run cmake::

    cmake .

Then compile the wrapper::

    make

