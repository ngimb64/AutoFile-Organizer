""" Built-in modules """
import os
import shutil
import sys
import time
from pathlib import Path
# External modules #
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Global variables #
SRC_DIR = 'Dock'
TEXT_DIR = 'TextFiles'
IMG_DIR = 'Images'
VID_DIR = 'Videos'
MUSIC_DIR = 'Music'
CODE_DIR = 'Code'
COMP_DIR = 'CompressedData'
DATA_DIR = 'RawData'
WIN_DIR = 'MicrosoftFiles'
OTHER_DIR = 'OtherData'

TEXT_EXT = ('.txt', '.pdf', '.rtf', '.tif', '.tiff', '.vob')
IMG_EXT = ('.bmp', '.gif', '.jpg', '.jpeg', '.png', '.thm')
VID_EXT = ('.acc', '.adt', '.adts', '.avi', '.flv', '.mov', '.mpeg', '.wmv')
MUSIC_EXT = ('.aif', '.aifc', '.aiff', '.m4a', '.mp3', '.mp4', '.wav', '.wma')
CODE_EXT = ('.bat', '.csv', '.dll', '.htm', '.html', '.xhtml', '.jhtml', '.ini', '.jar', '.c',
            '.cc', '.cpp', '.cxx', '.js', '.jse', '.cs', '.py', '.css', '.jsp', '.jspx', '.wss',
            '.do', '.action', '.pl', '.php', '.php3', '.php4', '.phtml', '.rb', '.rhtml', '.xml')
COMP_EXT = ('.ar', '.bz2', '.gzip', '.rar', '.zip')
DATA_EXT = ('.bin', '.dif', '.dump', '.exe', '.iso', '.mid', '.midi', '.swf', '.tmp')
WIN_EXT = ('.doc', '.docm', '.docx', '.dot', '.dotx', '.eml', '.mdb', '.msi', '.pot', '.potm',
           '.potx', '.ppam', '.pps', '.ppsm', '.ppsx', '.ppt', '.pptm', '.pptx', '.pst', '.pub',
           '.sldm', '.sldx', '.sys', '.wks', '.wmd')


class BackupHandler(FileSystemEventHandler):
    """ Class is trigger when the monitored SRC_DIR detects modification """
    def on_modified(self, event):
        """
        Copies contents of source dir to dest dir on event detection per modification.

        :param event:  On detection of modification of contents of SRC_DIR.
        :return:  Nothing
        """
        # Get the current working directory #
        cwd = Path('.')

        # Iterate through available files in source dir #
        for file in os.scandir(SRC_DIR):
            # Set the source file path #
            src_file = cwd / SRC_DIR / file.name

            # If the file is a text file #
            if file.name.endswith(TEXT_EXT):
                # Set the destination file path #
                dst_file = cwd / TEXT_DIR / file.name

            # If the file is a image #
            elif file.name.endswith(IMG_EXT):
                # Set the destination file path #
                dst_file = cwd / IMG_DIR / file.name

            # If the file is a video #
            elif file.name.endswith(VID_EXT):
                # Set the destination file path #
                dst_file = cwd / VID_DIR / file.name

            # If the file is a music track #
            elif file.name.endswith(MUSIC_EXT):
                # Set the destination file path #
                dst_file = cwd / MUSIC_DIR / file.name

            # If the file is source code #
            elif file.name.endswith(CODE_EXT):
                # Set the destination file path #
                dst_file = cwd / CODE_DIR / file.name

            # If the file is a compressed archive #
            elif file.name.endswith(COMP_EXT):
                # Set the destination file path #
                dst_file = cwd / COMP_DIR / file.name

            # If the file in raw data format #
            elif file.name.endswith(DATA_EXT):
                # Set the destination file path #
                dst_file = cwd / DATA_DIR / file.name

            # If the file is a Windows based file #
            elif file.name.endswith(WIN_EXT):
                # Set the destination file path #
                dst_file = cwd / WIN_DIR / file.name

            # If the file is of unknown data type #
            else:
                # Set the destination file path #
                dst_file = cwd / OTHER_DIR / file.name

            try:
                # Copy the source dir file to the destination dir #
                shutil.copy(src_file, dst_file)
                # Delete moved file from source dir #
                os.remove(src_file)

            # Ignore passive OS access errors #
            except OSError:
                pass


def main():
    """
    Facilitates file system handler, copies data to desired folders based on file extension.

    :return:  Nothing
    """
    # Ensure the program directories exist #
    for dirname in (SRC_DIR, TEXT_DIR, IMG_DIR, VID_DIR, MUSIC_DIR,
                    CODE_DIR, COMP_DIR, DATA_DIR, WIN_DIR, OTHER_DIR):
        # If the directory does not exist #
        if not os.path.exists(dirname):
            # Create the directory #
            os.mkdir(dirname)

    print('[!] Running File Backup Automater, hit Ctrl + C to exit')

    # Initialize BackupHandler object #
    file_monitor = BackupHandler()
    # Initialize the observer object #
    observer = Observer()
    # Schedule the file monitoring object to run #
    observer.schedule(file_monitor, SRC_DIR, recursive=True)
    # Start the file monitoring object #
    observer.start()

    # Run file system monitor until Ctrl+C #
    try:
        while True:
            time.sleep(15)

    # If Ctrl+C is detected #
    except KeyboardInterrupt:
        # Stop the file monitoring object #
        observer.stop()

    # Join the file monitoring child process #
    observer.join()

    sys.exit(0)


if __name__ == '__main__':
    main()
