#!/usr/bin/python
import os
import sys
import urllib


## If not windows, exit
if ( os.name != "nt" and os.name != "Windows" ):
    print("Not windows, exiting");
    sys.exit(0);

## Enumerated package urls
downloadUrls={}
baseDownloadUrl_1="http://download.windowsupdate.com/d/msdownload/update/software/secu/2019/09/"
baseDownloadUrl_2="http://download.windowsupdate.com/d/msdownload/update/software/secu/2019/10/"
baseDownloadUrl_3="http://download.windowsupdate.com/c/msdownload/update/software/secu/2019/10/"

## Determine x64 or x86

try:
    os.environ["PROGRAMFILES(X86)"]
    arch="x64"
except:
    arch="x86"

## Determine OS version
key = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion"
val = "ReleaseID"
output = os.popen( 'REG QUERY "{0}" /V "{1}"'.format( key , val)  ).read()
releaseId = output.strip().split(' ')[-1]         
print("Release ID" + releaseId)
versionCode = releaseId + "_" + arch
print(versionCode)


if (releaseId == ""):
    print("Checking if server");
    output = os.popen ('wmic os get Caption /value').read().lstrip().rstrip()
    print(output)
    # output = "Caption=Microsoft Windows Server 2012 R2 Standard"
    if ( output.find("2012 R2") != -1 ): 
        versionCode="SERVER_2012R2"
    elif ( output.find("2012") != -1 ): 
        versionCode="SERVER_2012"
    if ( output.find("2008 R2") != -1 ): 
        versionCode="SERVER_2008R2"
    elif ( output.find("2008") != -1 ): 
        versionCode="SERVER_2008"
    if ( output.find("2016") != -1 ): 
        versionCode="SERVER_2016"

    
print (versionCode)

## Apply patch
if ( versionCode == "SERVER_2012R2" ):
    packageName="windows8.1-kb4521864-x64_a08bfe1c54e710e319a1dd6a8115967eecd1fdad.msu"
    downloadUrl="http://download.windowsupdate.com/d/msdownload/update/software/secu/2019/09/"
    
if ( versionCode == "SERVER_2012" ):
    packageName="windows8-rt-kb4521857-x64_50f6015ca96c9d98838ce4ff09fbf41ea280324f.msu"
    downloadUrl="http://download.windowsupdate.com/d/msdownload/update/software/secu/2019/09/"
    
if ( versionCode == "SERVER_2016" ):
    packageName="windows10.0-kb4521858-x64_4660e9135b9de2ec006aee76499588d729fbbc60.msu"
    downloadUrl="http://download.windowsupdate.com/d/msdownload/update/software/secu/2019/09/"
    
if ( versionCode == "SERVER_2008" ):
    packageName="windows6.0-kb4517134-x64_a8d3ee8dcfb54c69549081a3060d4cd487f73c2e.msu"
    downloadUrl="http://download.windowsupdate.com/d/msdownload/update/software/secu/2019/09/"

if ( versionCode == "SERVER_2008R2" ):
    packageName="windows6.1-kb4516655-x64_8acf6b3aeb8ebb79973f034c39a9887c9f7df812.msu"
    downloadUrl="http://download.windowsupdate.com/c/msdownload/update/software/secu/2019/09/"

if ( versionCode == "1607_x86"): 
    packageName="windows10.0-kb4521858-x86_217787ec847049ba1582266e05b27001cd9346c8.msu"
    downloadUrl=baseDownloadUrl_1

if ( versionCode == "1607_x64"): 
    packageName="windows10.0-kb4521858-x64_4660e9135b9de2ec006aee76499588d729fbbc60.msu"
    downloadUrl=baseDownloadUrl_1

if ( versionCode == "1703_x86"): 
    packageName="windows10.0-kb4521859-x86_bcdeb525ecced9a60bf0f679a7c7c049ab3ff53a.msu"
    downloadUrl=baseDownloadUrl_1

if ( versionCode == "1703_x64"): 
    packageName="windows10.0-kb4521859-x64_4b0272df95f1a1167da05fe7640e1620b66ad470.msu"
    downloadUrl=baseDownloadUrl_1

if ( versionCode == "1809_x86"): 
    packageName="windows10.0-kb4521862-x86_4130389632388d35dce31134b12545a861a5b30c.msu"
    downloadUrl=baseDownloadUrl_1

if ( versionCode == "1809_x64"): 
    packageName="windows10.0-kb4521862-x64_bc8ec939f5cc57db5843b689be5ea12954c185cc.msu"
    downloadUrl=baseDownloadUrl_1

if ( versionCode == "1709_x86"): 
    packageName="windows10.0-kb4521860-x86_45a605e5e9c362318899394ea6d675ce0dd9f935.msu"
    downloadUrl=baseDownloadUrl_2

if ( versionCode == "1903_x86"): 
    packageName="windows10.0-kb4521863-x86_9833de6c0b33fae78cf5d91af9a78baf938bc3e1.msu"
    downloadUrl=baseDownloadUrl_2

if ( versionCode == "1903_x64"): 
    packageName="windows10.0-kb4521863-x64_a26672b0d37671b49d9306874bfab9db47007ddb.msu"
    downloadUrl=baseDownloadUrl_2

if ( versionCode == "1709_x64"): 
    packageName="windows10.0-kb4521860-x64_486da3e1878a8b4631765795d1dc50c9524a62c8.msu"
    downloadUrl=baseDownloadUrl_3

if ( versionCode == "1803_x64"): 
    packageName="windows10.0-kb4521861-x64_423fa096aa7181e817ca9eb97b9acefbea5304fc.msu"
    downloadUrl=baseDownloadUrl_3

if ( versionCode == "1803_x86"): 
    packageName="windows10.0-kb4521861-x86_265543ab6ab627141403ace27fa08c73d0007309.msu"
    downloadUrl=baseDownloadUrl_3


print("downloading " + downloadUrl + packageName)
print("OS Arch: " + versionCode)
urllib.urlretrieve(downloadUrl+packageName, 'C:\Windows\Temp\\' + packageName)
print("download complete, install fired")
installCmd="c:\windows\system32\wusa.exe C:\Windows\Temp\\" + packageName + " /quiet /norestart"
print(installCmd)
os.system( installCmd )
sys.exit(0)
