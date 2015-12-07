#!/usr/bin/python3.5
import sys
import hashlib
import os


# standard intro header with name and py version
def header():
    print("HashPuppy - Quick Hashing Utility")
    print("Python v{0}\n".format(sys.version[:5]))
    return


# sets source file if module is run standalone
def setup():
    source_file = input("Source file: ")
    return source_file


# strip quotation marks if they exist
def path_normalization(source_file_path):
    if source_file_path.startswith('"'):
        source_file_path = source_file_path[1:-1]
        return source_file_path
    else:
        return source_file_path


# primary functional code to produce hash values for source file
def main(source_file):
    print("Hashing '{0}'...\n".format(source_file))

    if os.path.isfile(source_file) is True:
        md5 = hashlib.md5(source_file.encode('utf-8')).hexdigest()
        sha1 = hashlib.sha1(source_file.encode('utf-8')).hexdigest()
        sha256 = hashlib.sha256(source_file.encode('utf-8')).hexdigest()
        sha512 = hashlib.sha512(source_file.encode('utf-8')).hexdigest()
        print("MD5: {0}\n"
              "SHA-1: {1}\n"
              "SHA-256: {2}\n"
              "SHA-512: {3}".format(md5, sha1, sha256, sha512))
        print("\nHashing complete.")

    elif source_file == "":
        if __name__ == '__main__':
            print("ERROR: No path provided")
            input("Press RETURN key to continue...")
            sys.exit()
        else:
            print("No argument provided. Exiting...")
            sys.exit()

    else:
        if __name__ == '__main__':
            print("ERROR: Error with path provided")
            input("Press RETURN key to continue...")
            sys.exit()
        else:
            print("Unknown argument provided. Exiting...")
            sys.exit()

# detect if script run standalone or by another python module
if __name__ == '__main__':
    os.system('cls')
    header()
    path = setup()
    main(path_normalization(path))
    input("Press RETURN key to continue...")
    sys.exit()

else:
    file = sys.argv[1]
    file = source_file[1:]
    main(file)
    input("Press RETURN key to continue...")
    sys.exit()
