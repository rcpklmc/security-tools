#!/usr/bin/python
#
# PHP Exploitable Functions/Vars Scanner
# bl4de | bloorq@gmail.com | Twitter: @_bl4de
#
import sys
import os

class _PefOutput:
    Black = '\33[30m'
    Red = '\33[31m'
    Green = '\33[32m'
    Yellow = '\33[33m'
    Blue ='\33[34m'
    Magenta = '\33[35m'
    Cyan = '\33[36m'
    White = '\33[37m'
    _endline = '\33[0m'
    
    efMsgFound = "exploitable function call"
    efMsgGlobalFound = "global variable explicit call"

# exploitable functions
exploitableFunctions = [" system"," exec"," popen", " pcntl_exec",
" eval"," preg_replace"," create_function", " include"," require"," passthru"," shell_exec"," popen"," proc_open",
" pcntl_exec"," asset"," extract"," parse_str"," putenv"," ini_set"," mail"," header"]

# dangerous global(s)
globalVars = ["$_POST", "$_GET", "$_COOKIE", "$_REQUEST", "$_SERVER"];



# prints formated output line
def printSrcCodeLine(_line, i, _fn, _message):
    print "::  line %d :: \33[33;1m%s\33[0m %s found " % (i, _fn, _message)
    print _PefOutput.Blue + _line + _PefOutput._endline
    
    
# performs code analysis, line by line
def main(__fileToAnalise):
    
    
    # open file to analyse
    _file = open(__fileToAnalise, "r")
    i = 0
    total = 0
    fileNameLength = len(__fileToAnalise)
    lineLength = 97
    
    print "-" * 14," FILE: \33[33m%s\33[0m " % (__fileToAnalise), "-" * (lineLength - fileNameLength - 21)  , "\n"

    for _line in _file:
        i = i + 1
        for _fn in exploitableFunctions:
            if _fn + '(' in _line or _fn + ' (' in _line:
                total = total + 1
                printSrcCodeLine(_line, i, _fn + '()', _PefOutput.efMsgFound)
        for _global in globalVars:
            if _global in _line:
                total = total + 1
                printSrcCodeLine(_line, i, _global, _PefOutput.efMsgGlobalFound)
        
    if total < 1:
        print _PefOutput.Green + "No exploitable functions found\n" + _PefOutput._endline
    else:
        print _PefOutput.Red + "Found %d exploitable functions total\n" % (total) + _PefOutput._endline

# main program
if __name__ == "__main__":
    if len(sys.argv) >= 2:
        print _PefOutput.Green + "\n\n", "-" * 100
        print "-" * 6, " PHP Exploitable functions scanner", " " * 41, "-" * 16
        print "-" * 6, " GitHub: bl4de | Twitter: @_bl4de | bloorq@gmail.com ", " " * 22, "-" * 16
        print "-" * 100, "\33[0m\n"
        
        
        # main program loop
        if len(sys.argv) == 3 and sys.argv[1] == "-R":
            file_list = os.listdir(sys.argv[2])
            for __file in file_list:
                if os.path.isfile(__file) and '.php' in __file:
                    main(__file)
        else:
            main(sys.argv[1])
            
            
        print
    else:
        print "Enter PHP or directory name with file(s) to analyse"
        print "single file: pef filename.php"
        print "directory: pef -R dirname"