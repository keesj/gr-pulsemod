INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_PULSEMOD pulsemod)

FIND_PATH(
    PULSEMOD_INCLUDE_DIRS
    NAMES pulsemod/api.h
    HINTS $ENV{PULSEMOD_DIR}/include
        ${PC_PULSEMOD_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    PULSEMOD_LIBRARIES
    NAMES gnuradio-pulsemod
    HINTS $ENV{PULSEMOD_DIR}/lib
        ${PC_PULSEMOD_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(PULSEMOD DEFAULT_MSG PULSEMOD_LIBRARIES PULSEMOD_INCLUDE_DIRS)
MARK_AS_ADVANCED(PULSEMOD_LIBRARIES PULSEMOD_INCLUDE_DIRS)

