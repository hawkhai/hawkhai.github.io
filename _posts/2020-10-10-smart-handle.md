---
layout: post
title: "利用 C++ 类生命周期，自动释放 HANDLE 句柄"
location: "珠海"
categories: ["编程"]
tags: [Windows Prog]
toc: true
---

利用 C++ 类生命周期，自动释放 HANDLE 句柄，香。

```cpp
template<typename T = HANDLE, BOOL (__stdcall *Closer)(T) = ::CloseHandle>
class SmartHandleTmpl
{
	SmartHandleTmpl(const SmartHandleTmpl&);
	SmartHandleTmpl& operator=(const SmartHandleTmpl&);

public:
	SmartHandleTmpl(T handle = NULL) : _handle(handle) { }
	virtual ~SmartHandleTmpl() {
		if (_handle && _handle != INVALID_HANDLE_VALUE)
			Closer(_handle);
	}

	operator T() const { return _handle; }
	template<typename F>
	operator F*() const { return (F*) _handle; }
	T* operator&() { return &_handle; }
	T operator=(T handle) {
		if (_handle != handle && _handle && _handle != INVALID_HANDLE_VALUE)
			Closer(_handle);
		return _handle = handle;
	}

private:
	T _handle;
};

typedef SmartHandleTmpl<> SmartHandle;
// SmartHandleTmpl<HANDLE, ::FindClose>
// SmartHandleTmpl<LPCVOID, ::UnmapViewOfFile>
```

另外两个就是：

```cpp
SmartHandleTmpl<HANDLE, ::FindClose>
SmartHandleTmpl<LPCVOID, ::UnmapViewOfFile>
```
