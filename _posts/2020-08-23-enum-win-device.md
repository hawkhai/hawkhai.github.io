---
layout: post
title: "编程 C++ -- Enumerating windows device"
author:
location: "珠海"
categories: ["编程"]
tags: ["Prog Note", "C++"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
---

Enumerating the device using the SetupDi* API provided with WinXP.

Download <a href="{% include relref.html url="/source/DevMgr-SRC.zip" %}" target="_blank">source</a> files \- 57\.8 Kb<br/>
Download <a href="{% include relref.html url="/source/DevMgr-DEMO.zip" %}" target="_blank">demo</a> project \- 29\.8 Kb


## Sample screenshot

{% include image.html url="/assets/images/200823-enum-win-device/full.jpg" %}


## Introduction

Windows has a rich collection of APIs to get useful information about installed devices. In this article, I will show how you can enumerate devices on a machine using SetupDiXXX API and CM_XXXX API.

The program has a simple GUI: only a a treeview control that shows all of the installed devices. All the information about a device (such as name and its icon) is grabbed from Windows SetupDiXXX API.


## SetupDiXXX API

The Setup application programming interface (API) provides a set of functions that your setup application can call to perform installation operations or get several information about installed devices, their class and also their GUID (a unique identifier for every device).

{% highlight cpp %}
WINSETUPAPI BOOL WINAPI SetupDiGetClassImageList(
    OUT PSP_CLASSIMAGELIST_DATA  ClassImageListData);
{% endhighlight %}

The SetupDiGetClassImageList function builds an image list that contains bitmaps for every installed class and returns the list in a data structure.

{% highlight cpp %}
WINSETUPAPI BOOL WINAPI SetupDiDestroyClassImageList(
    IN PSP_CLASSIMAGELIST_DATA  ClassImageListData);
{% endhighlight %}

The SetupDiDestroyClassImageList function destroys a class image list that was built by a call to SetupDiGetClassImageList.

{% highlight cpp %}
WINSETUPAPI BOOL WINAPI SetupDiGetClassImageIndex(
    IN PSP_CLASSIMAGELIST_DATA  ClassImageListData,
    IN LPGUID  ClassGuid,
    OUT PINT  ImageIndex);
{% endhighlight %}

The SetupDiGetClassImageIndex function retrieves the index within the class image list of a specified class.

Get device info set for device class (SetupDiGetClassDevs function), when first call , the first and second parameters for this function should be set to “0”, the last parameter should be set property DIGCF_ALLCLASSES constant to get all class device.

{% highlight cpp %}
HDEVINFO SetupDiGetClassDevs(
    IN LPGUID  ClassGuid  OPTIONAL,
    IN PCTSTR  Enumerator  OPTIONAL,
    IN HWND  hwndParent  OPTIONAL,
    IN DWORD  Flags);
{% endhighlight %}

{% highlight cpp %}
hDevInfo = SetupDiGetClassDevs(0L,    // Retrieve all classes
                               0L,    // no enumerator
                               _hDlg, // Parent Windows, usually set to “0”
                               // control options used in building the device information set
                               DIGCF_PRESENT |
                               DIGCF_ALLCLASSES |
                               DIGCF_PROFILE);
{% endhighlight %}


## Getting the Info

Using (SetupDiEnumDeviceInfo function) to enumeration all class devices.

{% highlight cpp %}
WINSETUPAPI BOOL WINAPI SetupDiEnumDeviceInfo(
    IN HDEVINFO  DeviceInfoSet,
    IN DWORD  MemberIndex,
    OUT PSP_DEVINFO_DATA  DeviceInfoData);
{% endhighlight %}

The function returns TRUE if it is successful. Otherwise, it returns FALSE and the logged error can be retrieved with a call to GetLastError.

{% highlight cpp %}
wIndex = 0;
spDevInfoData.cbSize = sizeof(SP_DEVINFO_DATA);
while (true)
{
    if (SetupDiEnumDeviceInfo(hDevInfo,
                              wIndex,
                              &spDevInfoData)) {
        .
        .
    }
}
{% endhighlight %}

The second parameter is Supplies the zero-based index of the device information element to retrieve.

The Last parameter is Supplies a pointer to an SP_DEVINFO_DATA structure to receive information about this element. The caller must set cbSize to sizeof(SP_DEVINFO_DATA).

Get device name from Registry via SetupDiGetDeviceRegistryPropertyA function

{% highlight cpp %}
WINSETUPAPI BOOL WINAPI SetupDiGetDeviceRegistryProperty(
    IN HDEVINFO  DeviceInfoSet,
    IN PSP_DEVINFO_DATA  DeviceInfoData,
    IN DWORD  Property,
    OUT PDWORD  PropertyRegDataType  OPTIONAL,
    OUT PBYTE  PropertyBuffer,
    IN DWORD  PropertyBufferSize,
    OUT PDWORD  RequiredSize  OPTIONAL);
{% endhighlight %}

{% highlight cpp %}
if (!SetupDiGetDeviceRegistryProperty(hDevInfo,
                                      &spDevInfoData,
                                      SPDRP_CLASS, // Retrieve property type,
                                      0L,
                                      (PBYTE) szBuf,
                                      2048,
                                      0)) {
    wIndex++;
    continue;
}

// retrieves the index within the class image list of a specified class
if (SetupDiGetClassImageIndex(&_spImageData,
                              &spDevInfoData.ClassGuid,
                              (int*) &wImageIdx)) {
    .
    .

    // retrieves the class description associated with the specified setup class GUID
    if (!SetupDiGetClassDescription(&spDevInfoData.ClassGuid,
                                    szBuf,
                                    MAX_PATH,
                                    &dwRequireSize)) {
        .
        .
    }
}
{% endhighlight %}


## Get Device Resource

All devices in the system join in the device classes. As you can see in the below picture, the class has name and GUID (so it can be found in Registry). The class can also have a description. For example, for class "Ports" the description is "Ports (COM & LPT)". Class also has devices that are present in the configuration.

Get information about current configuration (`CM_Get_First_Log_Conf` function).

{% highlight cpp %}
CMAPI CONFIGRET WINAPI CM_Get_First_Log_Conf(
    OUT PLOG_CONF  plcLogConf  OPTIONAL,
    IN DEVINST  dnDevInst,
    IN ULONG  ulFlags);
{% endhighlight %}

Get resource descriptor from current configuration (`CM_Get_Next_Res_Des` function, do this and follow steps for every resource till they exist)

{% highlight cpp %}
CMAPI CONFIGRET WINAPI CM_Get_Next_Res_Des(
    OUT PRES_DES  prdResDes,
    IN RES_DES  rdResDes,
    IN RESOURCEID  ForResource,
    OUT PRESOURCEID  pResourceID,
    IN ULONG  ulFlags);
{% endhighlight %}

Get information about size of resource data (`CM_Get_Res_Des_Data_Size` function)

{% highlight cpp %}
CMAPI CONFIGRET WINAPI CM_Get_Res_Des_Data_Size(
    OUT PULONG  pulSize,
    IN RES_DES  rdResDes,
    IN ULONG  ulFlags);
{% endhighlight %}

Get resource data (`CM_Get_Res_Des_Data` function)

{% highlight cpp %}
CMAPI CONFIGRET WINAPI CM_Get_Res_Des_Data(
    IN RES_DES  rdResDes,
    OUT PVOID  Buffer,
    IN ULONG  BufferLen,
    IN ULONG  ulFlags);
{% endhighlight %}

{% highlight cpp %}
cmRet = CM_Get_First_Log_Conf(&firstLogConf, DevInst, ALLOC_LOG_CONF);
if (cmRet != CR_SUCCESS) {
    cmRet = CM_Get_First_Log_Conf(&firstLogConf, DevInst, BOOT_LOG_CONF);
    if (cmRet != CR_SUCCESS) return;
}
cmRet = CM_Get_Next_Res_Des(&nextLogConf,
                            firstLogConf,
                            dwResType,
                            0L,
                            0L);
if (cmRet != CR_SUCCESS) {
    CM_Free_Res_Des_Handle(firstLogConf);
    return;
}
while (true) {
    ulSize = 0;
    cmRet = CM_Get_Res_Des_Data_Size(&ulSize, nextLogConf, 0L);
    if (cmRet != CR_SUCCESS) {
        CM_Free_Res_Des_Handle(nextLogConf);
        break;
    }
    pBuf = (char*) LocalAlloc(LPTR, 2048);
    if (!pBuf) {
        ShowErrorMsg(_hDlg, GetLastError(), "LocalAlloc");
        CM_Free_Res_Des_Handle(nextLogConf);
        break;
    }
    cmRet = CM_Get_Res_Des_Data(nextLogConf, pBuf, ulSize, 0L);
    if (cmRet != CR_SUCCESS) {
        .
        .
    }
}
{% endhighlight %}


## Load/Unload Non-PNP Driver

Windows allows loading drivers at runtime using the **Service Control Manager**. Yes, the Service Control Manager in Windows not only can be used to load and manage services. You can use it with device drivers as you use it to load/unload/start/stop windows services.

The OpenSCManager function establishes a connection to the service control manager on the specified computer and opens the specified service control manager database.

{% highlight cpp %}
SC_HANDLE OpenSCManager(
    IN LPCTSTR  lpMachineName,
    IN LPCTSTR  lpDatabaseName,
    IN DWORD  dwDesiredAccess);
{% endhighlight %}

The CreateService function creates a service object and installs it in the service control manager database by creating a key with the same name as the service under the following registry key:

{% highlight plaintext %}
HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services
{% endhighlight %}

{% highlight cpp %}
SC_HANDLE CreateService(
    IN SC_HANDLE  hSCManager,
    IN LPCTSTR  lpServiceName,
    IN LPCTSTR  lpDisplayName,
    IN DWORD  dwDesiredAccess,
    IN DWORD  dwServiceType,
    IN DWORD  dwStartType,
    IN DWORD  dwErrorControl,
    IN LPCTSTR  lpBinaryPathName,
    IN LPCTSTR  lpLoadOrderGroup,
    IN LPDWORD  lpdwTagId,
    IN LPCTSTR  lpDependencies,
    IN LPCTSTR  lpServiceStartName,
    IN LPCTSTR  lpPassword);
{% endhighlight %}

The OpenService function opens an existing service.

{% highlight cpp %}
SC_HANDLE OpenService(
    IN SC_HANDLE  hSCManager,
    IN LPCTSTR  lpServiceName,
    IN DWORD  dwDesiredAccess);
{% endhighlight %}

{% highlight cpp %}
hSCManager = OpenSCManager(0L,
                           0L,
                           SC_MANAGER_ALL_ACCESS);
if (hSCManager) { // Create new device service
    hService = CreateService(hSCManager,
                             lpszServiceName, // DosDeviceName
                             lpszServiceName, // DosDeviceName
                             SERVICE_ALL_ACCESS,
                             SERVICE_KERNEL_DRIVER,
                             wStart,
                             wError,
                             lpszDriverPath, // Image path
                             0L,
                             0L,
                             0L,
                             0L,
                             0L);
    if (!hService) {
        DWORD dwErrorCode = GetLastError();
        if (dwErrorCode == ERROR_SERVICE_EXISTS) {
            // If service already existed? Open it.
            hService = OpenService(hSCManager, lpszServiceName, SERVICE_ALL_ACCESS);
        } else {
            ShowErrorMsg(_hDlg, dwErrorCode, "CreateService");
            return 0;
        }
    }
    if (hService) { // Start new service
        if (!StartService(hService, 0, 0L)) {
            CloseServiceHandle(hService);
            ShowErrorMsg(_hDlg, GetLastError(), "StartService");
            return 0;
        }
    }
    CloseServiceHandle(hSCManager);
}
{% endhighlight %}

If you want to send/receive data to the device driver loaded, to allow this, you have to get a handle to the driver. For this purpose you can use the function CreateFile, and pass the driver name as the file name. You can see Windows is so abstract in this aspect.

{% include image.html url="/assets/images/200823-enum-win-device/addlegacy.jpg" %}


## Load/Unload WDM Driver

Windows also allows loading drivers at runtime using the SetupDiXXX API. The first we need to call SetuiDiGetINFClass to get the class of a specified device INF file.

{% include image.html url="/assets/images/200823-enum-win-device/infinst.jpg" %}

{% highlight cpp %}
WINSETUPAPI BOOL WINAPI SetupDiGetINFClass(
    IN PCTSTR  InfName,
    OUT LPGUID  ClassGuid,
    OUT PTSTR  ClassName,
    IN DWORD  ClassNameSize,
    OUT PDWORD  RequiredSize  OPTIONAL);
{% endhighlight %}

The second parameter, Receives the class GUID for the specified INF file. If the INF file does not specify a class name, this variable is set to GUID_NULL. Call SetupDiClassGuidsFromName to determine if one or more classes with this name are already installed.

When function return TRUE, NOW we need create an empty device information set and optionally associates the set with a device setup class and a top-level window. Use SetupDiCreateDeviceInfo function creates a new device information element and adds it as a new member to the specified device information set.

{% highlight cpp %}
HDEVINFO SetupDiCreateDeviceInfoList(
    IN LPGUID  ClassGuid  OPTIONAL,
    IN HWND  hwndParent  OPTIONAL);
{% endhighlight %}

The caller of this function must delete the returned device information set when it is no longer needed by calling SetupDiDestroyDeviceInfoList.

To create a device information list for a remote machine use SetupDiCreateDeviceInfoListEx.

{% highlight cpp %}
WINSETUPAPI BOOL WINAPI SetupDiCreateDeviceInfo(
    IN HDEVINFO  DeviceInfoSet,
    IN PCTSTR  DeviceName,
    IN LPGUID  ClassGuid,
    IN PCTSTR  DeviceDescription  OPTIONAL,
    IN HWND  hwndParent  OPTIONAL,
    IN DWORD  CreationFlags,
    OUT PSP_DEVINFO_DATA  DeviceInfoData  OPTIONAL);
{% endhighlight %}

The sixth parameter. Controls how the device information element is created. Can be a combination of the following values:

**DICD_GENERATE_ID**

If this flag is specified, DeviceName contains only a Root-enumerated device ID and the system creates a unique device instance key for it. This unique device instance key is generated as:

{% highlight plaintext %}
Enum\Root\DeviceName\InstanceID
{% endhighlight %}

where InstanceID is a four-digit, base-10 number that is unique among all subkeys under `Enum\Root\DeviceName`. Call SetupDiGetDeviceInstanceId to find out what ID was generated for this device information element.

**DICD_INHERIT_CLASSDRVS**

If this flag is specified, the resulting device information element inherits the class driver list, if any, associated with the device information set. In addition, if there is a selected driver for the device information set, that same driver is selected for the new device information element.

{% highlight cpp %}
if (!SetupDiGetINFClass(szINFName, &guid, className, MAX_CLASS_NAME_LEN, 0)) {
    return 0;
}
hDevInfo = SetupDiCreateDeviceInfoList(&guid, 0);
if (hDevInfo == (void*) -1) {
    return 0;
}
spDevData.cbSize = sizeof(SP_DEVINFO_DATA);
if (!SetupDiCreateDeviceInfo(hDevInfo,
                             className,
                             &guid,
                             0L,
                             0L,
                             DICD_GENERATE_ID,
                             &spDevData)) {
    SetupDiDestroyDeviceInfoList(hDevInfo);
    return 0;
}
{% endhighlight %}

If this device instance is being added to a set that has an associated class, the device class must be the same or the call fails. In this case, a call to GetLastError returns `ERROR_CLASS_MISMATCH`.

If the specified device instance is the same as an existing device instance key in the registry, the call fails. In this case, a call to GetLastError returns `ERROR_DEVINST_ALREADY_EXISTS`. This occurs only if the `DICD_GENERATE_ID` flag is not set.

If the new device information element was successfully created but the caller-supplied DeviceInfoData buffer is invalid, the function returns FALSE. In this case, a call to GetLastError returns `ERROR_INVALID_USER_BUFFER`. However, the device information element will have been added as a new member of the set already.

That's it! If you have any suggestions or problems to report, post them here. There are plenty of ways this idea could be extended if you are of an inclination to do so.


## License

This article has no explicit license attached to it but may contain usage terms in the article text or the download files themselves. If in doubt please contact the author via the discussion board below.

A list of licenses authors might use can be found here.

from <https://www.codeproject.com/Articles/14412/Enumerating-windows-device>

-----

<font class='ref_snapshot'>参考资料快照</font>

- [1] [https://www.codeproject.com/Articles/14412/Enumerating-windows-device]({% include relref.html url="/backup/2020-08-23-enum-win-device.md/www.codeproject.com/3f5de73a.html" %})
