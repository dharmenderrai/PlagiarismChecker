
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
'''
Calculate and  return the hash for a code object
'''
def calcHash(codeObj):
    code_bytes = marshal.dumps(codeObj)
    return hashlib.sha1(code_bytes).hexdigest()

'''
Compare hash results of the two bytecodes 
'''
def compareHashCode(codeHash1, codeHash2):
    print ("Input hash codes are :")
    print (codeHash1)
    print(codeHash2)
    if codeHash1 == codeHash2:
        return True
    return False


if __name__ == "__main__":
    # read the files
    file1 = input()
    file2 = input()
    (codeObj1, codeObj2) = byteCodeGenerator(file1, file2)
    print(compareHashCode(calcHash(codeObj1), calcHash(codeObj2)))


