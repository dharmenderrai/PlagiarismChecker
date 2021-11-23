
import hashlib
import marshal

'''
1. Read two files
2. Convert them in code objects

'''

def byteCodeGenerator(file1, file2):
    with open(file1) as f:
        code1 = f.read()
    with open(file2) as f:
        code2 = f.read()
    codeObj1 = compile(code1, file1, 'exec')
    codeObj2 = compile(code2, file2, 'exec')
    return (codeObj1, codeObj2)



if __name__ == "__main__":
    # read the files
    file1 = "./inputs/" + input().strip()
    file2 = "./inputs/" + input().strip()

    (codeObj1, codeObj2) = byteCodeGenerator(file1, file2)

    '''
    'co_argcount',
 'co_cellvars',
 'co_code',
 'co_consts',
 'co_filename',
 'co_firstlineno',
 'co_flags',
 'co_freevars',
 'co_kwonlyargcount',
 'co_lines',
 'co_linetable',
 'co_lnotab',
 'co_name',
 'co_names',
 'co_nlocals',
 'co_posonlyargcount',
 'co_stacksize',
 'co_varnames',

    '''


