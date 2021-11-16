#pragma once

#include <QtCore/qglobal.h>

#ifndef BUILD_STATIC
# if defined(FPCONVERT_LIB)
#  define FPCONVERT_EXPORT Q_DECL_EXPORT
# else
#  define FPCONVERT_EXPORT Q_DECL_IMPORT
# endif
#else
# define FPCONVERT_EXPORT
#endif
