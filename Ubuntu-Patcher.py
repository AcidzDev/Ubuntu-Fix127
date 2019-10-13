#!/usr/bin/python

import os
import sys
import time
import wget
import shutil

##Variables
homedir = os.path.expanduser("~")
systemInfo = os.uname()
KernelURL = 'https://cdn.kernel.org/pub/linux/kernel/v5.x/linux-5.3.5.tar.xz'
PatchURL = 'https://clbin.com/VCiYJ'

##Script Start
print ("This script will download and compile the latest linux")
input("Press ENTER to continue...")

print("Changing directory to Downloads")
os.chdir(homedir+"/Downloads")

##Creating compile folder and download kernel
print("Creating folde to compile the kernel")
os.mkdir(homedir+"/Downloads/kernel")
os.chdir(homedir+"/Downloads/kernel")
print("Dowloading Kernel from source")
time.sleep(1)
wget.download(KernelURL, homedir+'/Downloads/kernel')
print()
time.sleep(1)

##Enable scoure
print("Enable build sources")
time.sleep(1)
os.system("sudo sed -i '/deb-src/s/^# //' /etc/apt/sources.list && sudo apt update")
os.system("sudo apt update")
time.sleep(1)

##Required packages
print("Downloading required packages")
os.system("sudo apt install kernel-package libncurses5-dev bzip2 fakeroot libncurses-dev flex bison openssl libssl-dev dkms libelf-dev libudev-dev libpci-dev libiberty-dev autoconf")

##Extracting Kernel
print("Extracting kernel")
os.system("tar -xvf linux-*.tar.xz")
os.system("ln -s linux-5.3.5 linux")
os.chdir(homedir+"/Downloads/kernel/linux")

##Applying Patch
print("Applying kernel patch\n")
time.sleep(1)
wget.download(PatchURL, homedir+'/Downloads/kernel/linux')
currentdir = os.getcwd()
shutil.move('VCiYJ', 'pci.patch')
os.system("patch -p1 < pci.patch")
time.sleep(1)

##Copy current config
os.system("sudo cp /boot/config-$(uname -r) .config")

##Compile kernel
os.system('clear')
time.sleep(1)
print("Are you ready to compile the kernel\n")
input("Press ENTER to continue...")
os.system("fakeroot make-kpkg -j$(nproc) --initrd --append-to-version=pci-patched kernel_image kernel_headers")

##Install compile kernel
os.system('clear')
answer = None
while answer not in ("yes", "no"):
    answer = input("Do you wish to install the kernel now?, Enter yes or no: ")
    if answer == "yes":
         os.chdir(homedir+'/Downloads/kernel/')
         os.system("sudo dpkg -i *.deb")
         os.system("sudo update-grub")
         print("\nPlease reboot to apply changes and load the newly complied kernel")
    elif answer == "no":
         exit()
    else:
    	print("Please enter yes or no.")
