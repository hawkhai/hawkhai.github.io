mkdir test
cd test
copy ..\imgserv.bat imgserv.bat
copy ..\imgserv.exe imgserv.exe
mkdir ksample
cd ksample
mkdir testimg
mkdir 8DetectBorder
cd ..
start imgserv.exe 10.12.168.199
