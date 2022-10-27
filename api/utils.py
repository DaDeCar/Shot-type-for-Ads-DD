import hashlib
import os


def allowed_file(filename):
    """
    Checks if the format for the file received is acceptable. For this
    particular case, we must accept only image files. This is, files with
    extension ".png", ".jpg", ".jpeg" or ".gif".

    Parameters
    ----------
    filename : str
        Filename from werkzeug.datastructures.FileStorage file.

    Returns
    -------
    bool
        True if the file is an image, False otherwise.
    """
    # Current implementation will allow any kind of file.
    
    # We keep the extension of the image path. We pass all to lowercase
    ext=os.path.splitext(filename)[1].lower() 

    if ext == ".png" or ext == '.jpg' or ext == '.jpeg' or ext == '.gif':
        result = True
    else:
        result = False

    return result


def get_file_hash(file):
    """
    Returns a new filename based on the file content using MD5 hashing.
    It uses hashlib.md5() function from Python standard library to get
    the hash.

    Parameters
    ----------
    file : werkzeug.datastructures.FileStorage
        File sent by user.

    Returns
    -------
    str
        New filename based in md5 file hash.
    """
    # Current implementation will return the original file name.
    # 
    with open(file.filename, "rb") as f:
        contents = f.read()
        filename_content = hashlib.md5(contents)
        file.filename = filename_content.hexdigest() + "." + file.filename.split('.')[1]
   
    return os.path.basename(file.filename)
    
   
 