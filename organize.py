import os, shutil, sys

EXT_FOLDERS = {
    'images': ['.jpg', '.jpeg', '.png', '.gif'],
    'docs': ['.pdf', '.docx', '.txt', '.xlsx'],
    'archives': ['.zip', '.tar', '.gz'],
    'videos': ['.mp4', '.mkv', '.mov'],
    'audio': ['.mp3', '.wav']
}

def organize(path):
    if not os.path.isdir(path):
        print("Not a directory:", path)
        return
    
    for fname in os.listdir(path):
        fpath = os.path.join(path, fname)
        if os.path.isdir(fpath): continue
        
        ext = os.path.splitext(fname)[1].lower()
        placed = False
        
        for folder, exts in EXT_FOLDERS.items():
            if ext in exts:
                dest = os.path.join(path, folder)
                os.makedirs(dest, exist_ok=True)
                shutil.move(fpath, os.path.join(dest, fname))
                placed = True
                break
        
        if not placed:
            dest = os.path.join(path, 'others')
            os.makedirs(dest, exist_ok=True)
            shutil.move(fpath, os.path.join(dest, fname))
    
    print("Done")

if __name__=='__main__':
    target = sys.argv[1] if len(sys.argv)>1 else '.'
    organize(target)
