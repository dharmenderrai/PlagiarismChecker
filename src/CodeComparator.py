import sys
from pprint import pprint
from difflib import Differ, SequenceMatcher
from difflib import context_diff


'''
1. Read two files
2. Convert them in code objects

'''

# Global variables to store file name and its data
file1 = ""
file2 = ""
code1 = ""  # code from 1st file
code2 = ""  # code from second file

def byteCodeGenerator(file1, file2):

    codeObj1 = compile(code1, file1, 'exec')
    codeObj2 = compile(code2, file2, 'exec')
    return (codeObj1, codeObj2)


def populate_byte_code_hash():
    # compare the byte code - field by field
    if codeObj1.co_argcount == codeObj2.co_argcount:
        byte_code_compare_hash["arg_count"] = True
    else:
        byte_code_compare_hash["arg_count"] = False
    if codeObj1.co_cellvars == codeObj2.co_cellvars:
        byte_code_compare_hash["co_cellvars"] = True
    else:
        byte_code_compare_hash["co_cellvars"] = False
    if codeObj1.co_consts == codeObj2.co_consts:
        byte_code_compare_hash["co_consts"] = True
    else:
        byte_code_compare_hash["co_consts"] = False
    if codeObj1.co_code == codeObj2.co_code:
        byte_code_compare_hash["co_code"] = True
    else:
        byte_code_compare_hash["co_code"] = False
    if codeObj1.co_filename == codeObj2.co_filename:
        byte_code_compare_hash["co_filename"] = True
    else:
        byte_code_compare_hash["co_filename"] = False
    if codeObj1.co_firstlineno == codeObj2.co_firstlineno:
        byte_code_compare_hash["co_firstlineno"] = True
    else:
        byte_code_compare_hash["co_firstlineno"] = False
    if codeObj1.co_flags == codeObj2.co_flags:
        byte_code_compare_hash["co_flags"] = True
    else:
        byte_code_compare_hash["co_flags"] = False
    if codeObj1.co_freevars == codeObj2.co_freevars:
        byte_code_compare_hash["co_freevars"] = True
    else:
        byte_code_compare_hash["co_freevars"] = False
    if codeObj1.co_kwonlyargcount == codeObj2.co_kwonlyargcount:
        byte_code_compare_hash["co_freevars"] = True
    else:
        byte_code_compare_hash["co_freevars"] = False

    if codeObj1.co_lnotab == codeObj2.co_lnotab:
        byte_code_compare_hash["co_lnotab"] = True
    else:
        byte_code_compare_hash["co_lnotab"] = False
    if codeObj1.co_name == codeObj2.co_name:
        byte_code_compare_hash["co_name"] = True
    else:
        byte_code_compare_hash["co_name"] = False
    if codeObj1.co_names == codeObj2.co_names:
        byte_code_compare_hash["co_names"] = True
    else:
        byte_code_compare_hash["co_names"] = False
    if codeObj1.co_nlocals == codeObj2.co_nlocals:
        byte_code_compare_hash["co_nlocals"] = True
    else:
        byte_code_compare_hash["co_nlocals"] = False
    if codeObj1.co_posonlyargcount == codeObj2.co_stacksize:
        byte_code_compare_hash["co_posonlyargcount"] = True
    else:
        byte_code_compare_hash["co_posonlyargcount"] = False
    if codeObj1.co_varnames == codeObj2.co_varnames:
        byte_code_compare_hash["co_varnames"] = True
    else:
        byte_code_compare_hash["co_varnames"] = False


def read_files():
    global file1, file2, code1, code2
    # read the files
    file1 = "./inputs/" + input().strip()
    file2 = "./inputs/" + input().strip()
    with open(file1) as f:
        code1 = f.read()
    with open(file2) as f:
        code2 = f.read()


if __name__ == "__main__":
    read_files()

    '''
    Plain vanilla diff
    '''
    pprint("<----------------Printing  Differ------------------------->")
    file_diff = Differ()
    result = list(file_diff.compare(code1, code2))
    pprint(result)
    pprint("<----------------Printing Context Diff------------------------->")
    sys.stdout.writelines(context_diff(code1, code2, file1, file2))

    '''
    Sequence matcher showing delta between tokens used in both files
    '''
    s = SequenceMatcher(None, file1, file2)
    for tag, i1, i2, j1, j2 in s.get_opcodes():
        pprint('{:7}   a[{}:{}] --> b[{}:{}] {!r:>8} --> {!r}'.format(
            tag, i1, i2, j1, j2, file1[i1:i2], file2[j1:j2]))
    '''
    Byte code compare
    '''
    byte_code_compare_hash = {}

    (codeObj1, codeObj2) = byteCodeGenerator(file1, file2)
    populate_byte_code_hash()

    pprint("<----------------Printing  Byte Code "
           "Comparision------------------------->")
    pprint(byte_code_compare_hash)




