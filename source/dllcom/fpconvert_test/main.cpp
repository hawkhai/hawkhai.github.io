#include <QtCore/QCoreApplication>
#include "fpconvertConvert.h"

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    FPConvertWrap fpc;
    fpc.GetFPConvertVersion();
    // return a.exec();
    return 0;
}
