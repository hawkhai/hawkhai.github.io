#pragma once

#include "fpconvert_global.h"
#include "fpconvertConvert.h"

class fpconvertDLL : public fpconvert::IFPConvertInterface {
public:
    fpconvertDLL();

public:
    virtual int GetFPConvertVersion() override;
    virtual int Release() override;
};
