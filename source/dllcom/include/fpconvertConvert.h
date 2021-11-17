#include <assert.h>
#include <Windows.h>
#include <string>

#ifndef __FPCONVERT_CONVERT_DLL__
#define __FPCONVERT_CONVERT_DLL__

#include "fpconvert_global.h"

#ifdef __cplusplus
extern "C" {
#endif

namespace fpconvert {

#define FPCONVERT_VERSION 1

__interface IFPConvertInterface {
    virtual int GetFPConvertVersion() = 0;
    virtual int Release() = 0;
};

FPCONVERT_EXPORT IFPConvertInterface* CreateFPConverter();

} // namespace fpconvert

class FPConvertWrap : public fpconvert::IFPConvertInterface {
    static std::wstring getCurrentPath() {
        TCHAR tPath[MAX_PATH];
        DWORD dwRet = GetModuleFileName(NULL, tPath, MAX_PATH);
        std::wstring strexe = tPath;
        int index = strexe.rfind('\\');
        return strexe.substr(0, index + 1);
    }

    static HINSTANCE getLibrary(const TCHAR* libPath) {
        std::wstring curdir = getCurrentPath();
        std::wstring current = curdir;
        current.append(libPath);

        WCHAR lpBuffer[MAX_PATH];
        GetCurrentDirectory(MAX_PATH, lpBuffer);
        SetCurrentDirectory(curdir.c_str());
        HINSTANCE hDLL = LoadLibrary(current.c_str());
        SetCurrentDirectory(lpBuffer);

        if (hDLL == nullptr) {
            int err = GetLastError();
            return nullptr;
        }
        return hDLL;
    }

  public:
    virtual int GetFPConvertVersion() override {
        if (!m_interface) {
            return -1;
        }
        return m_interface->GetFPConvertVersion();
    }

    virtual int Release() override {
        if (!m_interface) {
            return -1;
        }
        int retv = m_interface->Release();
        m_interface = nullptr;
        return retv;
    }

    FPConvertWrap() {
        const TCHAR* libPath = L"fpconvert.dll";
        m_hDLL = getLibrary(libPath);
        if (m_hDLL == nullptr) {
            int err = GetLastError();
            return;
        }

        typedef IFPConvertInterface* (*CreateFPConverterFunc)();
        CreateFPConverterFunc fptr =
            (CreateFPConverterFunc) GetProcAddress(m_hDLL, "CreateFPConverter");
        if (fptr == nullptr) {
            int err = GetLastError();
            return;
        }
        m_interface = fptr();
        if (m_interface->GetFPConvertVersion() < FPCONVERT_VERSION) {
            m_interface->Release();
            m_interface = nullptr;
        }
    }
    virtual ~FPConvertWrap() {
        if (!m_interface) {
            return;
        }
        m_interface->Release();
        m_interface = nullptr;
        // m_hDLL ≤ª Õ∑≈¡À°£
    }

  private:
    fpconvert::IFPConvertInterface* m_interface = nullptr;
    HINSTANCE m_hDLL = nullptr;
};

#ifdef __cplusplus
}
#endif
#endif
