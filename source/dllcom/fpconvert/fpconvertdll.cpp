#include "fpconvertdll.h"

fpconvert::IFPConvertInterface* fpconvert::CreateFPConverter() {
    return new fpconvertDLL();
}

fpconvertDLL::fpconvertDLL()
{
}

int fpconvertDLL::GetFPConvertVersion() {
    return FPCONVERT_VERSION;
}

int fpconvertDLL::Release() {
    delete this;
    return 0;
}

