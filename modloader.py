
import time, os, shutil

def modinstaller(mld, gl): # lazy code here
    while True:
        mdir = input("drop mod folder here. ")
        if (os.path.isdir(mdir + "\\modmeta.json")): print("not a valid folder")
        else: 
            import json
            modmeta = json.load(open(mdir + "\\modmeta.json"))
            modfiles = modmeta['files']
            print("mod name: " + modmeta['name'])
            print("files to patch: ")
            for i in modfiles:
                print(" - " + i)
            time.sleep(0.5);
            os.mkdir(gl + "\\mods\\" + modmeta['name'])
            print("\n")
            for i in modfiles:
                print("patching - " + i);
                shutil.copy(gl + "\\" + i, gl + "\\mods\\" + i + ".rollback") # create a backup 
                if modmeta['patchmode'] == "append": merge(mdir+"\\"+i, gl+"\\"+i)
                elif modmeta['patchmode'] == "replace": shutil.copy(mdir + "\\" + i, gl + "\\" + i)
                else: print("invalid patchmode, skipping.");
            print("\ndone."); input(); exit();

def merge(mod, target):
    with open(target) as f: # load target
        targetdata = f.read()
    with open(mod) as f: # load mod
        moddata = f.read()

    targetdata +="\n" # insert newline 
    targetdata += moddata # megre
    os.remove(target) # remove original file
    with open(target, "w") as f: # write it from memory
        f.write(targetdata) 
        f.close()

def installer():   
    time.sleep(0.2); print("\ninstalling mod loader.")
    time.sleep(0.4); os.chdir(modloaderdir)

    # install files

    print("backing up... 1/2 "); shutil.copy(gamelocation + "\\launcher.py", gamelocation + "\\bak_launcher.py"); time.sleep(0.1)
    print("backing up... 2/2 "); shutil.copy(gamelocation + "\\lib\\randomthings.py", gamelocation + "\\lib\\bak_randomthings.py"); time.sleep(0.1)

    print("patching... "); time.sleep(0.1)
    shutil.copy("mld1", gamelocation + "\\launcher.py")
    shutil.copy("mld2", gamelocation + "\\lib\\randomthings.py")

    print("creating mods folder... "); time.sleep(0.1)
    os.mkdir(gamelocation + "\\mods")
    os.mkdir(gamelocation + "\\mods\\lib\\")
    os.mkdir(gamelocation + "\\mods\\entitylogic\\")
    os.mkdir(gamelocation + "\\mods\\assets\\")
    with open(gamelocation + "\\.warning", "w") as wfile:
        wfile.write("a"); wfile.close()

    time.sleep(0.2)
    print("done."); input()

if ( not os.name == 'nt' ):
    print("only windows is supported!")
    print("to install manually:")
    print(" - replace launcher.py with mld1")
    print(" - replace lib/randomthings.py with mld2")
    input()
print("SimpleRPG, Mod Loader"); time.sleep(1)

modloaderdir = os.getcwd()
gamelocation = input("drop simplerpg folder here. ")

print("validating ..."); time.sleep(0.1); shutil.copy(gamelocation + "\\lib\\randomthings.py", "rt.py")
from rt import *; print("checking " + game.version + " ..", end=""); 

if (game.version.startswith("m")):
    print("game is already modded! skipping to installer...");
    modinstaller(modloaderdir, gamelocation)


if (game.version) != '2.2a':
    print("Update your game to compatible version! Else things will break.")
    input();

time.sleep(0.4); print(" ok"); installer()

