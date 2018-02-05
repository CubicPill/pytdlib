=======
pytdlib
=======

A python wrapper for telegram's tdlib

----------------------
Building the C++ TDLib
----------------------
************
Requirements
************
Please see the required libraries listed on the tdlib repo

*********
Procedure
*********

**NOTE: You may create a new folder in the source directory to build the c++ lib**, like the following::

    mkdir build
    cd build
    cmake ..
    make

Then you will get libtdjson.so (or tdjson.dll if you are on Windows), this is the library required in ``TDJSONClient``
---------------------------------
Building the Boost.Python wrapper
---------------------------------
************
Requirements
************
gcc 4+
cmake 3.1+

*********
Procedure
*********
Set the environment variables::

    PYTHON_INCLUDE_PATH    // directory of python headers

And run cmake::

    cmake .

Then compile the wrapper::

    make

