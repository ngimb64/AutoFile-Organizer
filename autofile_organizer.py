""" Built-in modules """
import os
import shutil
import sys
import time
# External modules #
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


#  Pseudo Constants #
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

# Global variables #
text_ext = ('.txt', '.pdf', '.rtf', '.tif', '.tiff', '.vob')

img_ext = ('.bmp', '.gif', '.jpg', '.jpeg', '.png', '.thm')

vid_ext = ('.acc', '.adt', '.adts', '.avi', '.flv', '.mov', '.mpeg', '.wmv')

music_ext = ('.aif', '.aifc', '.aiff', '.m4a', '.mp3', '.mp4', '.wav', '.wma')

code_ext = ('.bat', '.csv', '.dll', '.htm', '.html', '.xhtml', '.jhtml', '.ini',
            '.jar', '.c', '.cc', '.cpp', '.cxx', '.js', '.jse', '.cs', '.py',
            '.css', '.jsp', '.jspx', '.wss', '.do', '.action', '.pl', '.php',
            '.php3', '.php4', '.phtml', '.rb', '.rhtml', '.xml')

comp_ext = ('.ar', '.bz2', '.gzip', '.rar', '.zip')

data_ext = ('.bin', '.dif', '.dump', '.exe', '.iso', '.mid', '.midi', '.swf', '.tmp')

win_ext = ('.doc', '.docm', '.docx', '.dot', '.dotx', '.eml', '.mdb', '.msi',
           '.pot', '.potm', '.potx', '.ppam', '.pps', '.ppsm', '.ppsx', '.ppt',
           '.pptm', '.pptx', '.pst', '.pub', '.sldm', '.sldx', '.sys', '.wks', '.wmd')


class BackupHandler(FileSystemEventHandler):
    """ Class is trigger when the monitored SRC_DIR detects modification """
    def on_modified(self, event):
        """
        Copies contents of source dir to dest dir on event detection per modification.

        :param event:  On detection of modification of contents of SRC_DIR.
        :return:  Nothing
        """
        # Get the current working directory #
        cwd = os.getcwd()

        # Iterate through available files in source dir #
        for file in os.scandir(SRC_DIR):
            # If the OS is Windows #
            if os.name == 'nt':
                src_file = f'{cwd}\\{SRC_DIR}\\{file.name}'
            # If the OS is Linux #
            else:
                # Set the source and destination files #
                src_file = f'{cwd}/{SRC_DIR}/{file.name}'

            # If the file is a text file #
            if file.name.endswith(text_ext):
                # If the OS is Windows #
                if os.name == 'nt':
                    dst_file = f'{cwd}\\{TEXT_DIR}\\{file.name}'
                # If the OS is Linux #
                else:
                    # Move file to the TextFile dir #
                    dst_file = f'{cwd}/{TEXT_DIR}/{file.name}'

            # If the file is a image #
            elif file.name.endswith(img_ext):
                # If the OS is Windows #
                if os.name == 'nt':
                    dst_file = f'{cwd}\\{IMG_DIR}\\{file.name}'
                # If the Os is Linux #
                else:
                    # Move file to the Images dir #
                    dst_file = f'{cwd}/{IMG_DIR}/{file.name}'

            # If the file is a video #
            elif file.name.endswith(vid_ext):
                # If the OS is Windows #
                if os.name == 'nt':
                    dst_file = f'{cwd}\\{VID_DIR}\\{file.name}'
                # If the OS is Linux #
                else:
                    # Move file to the Videos dir #
                    dst_file = f'{cwd}/{VID_DIR}/{file.name}'

            # If the file is a music track #
            elif file.name.endswith(music_ext):
                # If the OS is Windows #
                if os.name == 'nt':
                    dst_file = f'{cwd}\\{MUSIC_DIR}\\{file.name}'
                # If the OS is Linux #
                else:
                    # Move file to the Music dir #
                    dst_file = f'{cwd}/{MUSIC_DIR}/{file.name}'

            # If the file is source code #
            elif file.name.endswith(code_ext):
                # If the OS is Windows #
                if os.name == 'nt':
                    dst_file = f'{cwd}\\{CODE_DIR}\\{file.name}'
                # If the OS is Linux #
                else:
                    # Move file to the Code dir #
                    dst_file = f'{cwd}/{CODE_DIR}/{file.name}'

            # If the file is a compressed archive #
            elif file.name.endswith(comp_ext):
                # If the OS is Windows #
                if os.name == 'nt':
                    dst_file = f'{cwd}\\{COMP_DIR}\\{file.name}'
                # If the OS is Linux #
                else:
                    # Move file to the CompressedData dir #
                    dst_file = f'{cwd}/{COMP_DIR}/{file.name}'

            # If the file in raw data format #
            elif file.name.endswith(data_ext):
                # If the OS is Windows #
                if os.name == 'nt':
                    dst_file = f'{cwd}\\{DATA_DIR}\\{file.name}'
                else:
                    # Move file to the RawData dir #
                    dst_file = f'{cwd}/{DATA_DIR}/{file.name}'

            # If the file is a Windows based file #
            elif file.name.endswith(win_ext):
                # If the OS is Windows #
                if os.name == 'nt':
                    dst_file = f'{cwd}\\{WIN_DIR}\\{file.name}'
                # If the OS is Linux #
                else:
                    # Move file to the MicrosoftFiles dir #
                    dst_file = f'{cwd}/{WIN_DIR}/{file.name}'

            # If the file is of unknown data type #
            else:
                # If the OS is Windows #
                if os.name == 'nt':
                    dst_file = f'{cwd}\\{OTHER_DIR}\\{file.name}'
                else:
                    # Move file to the OtherData dir #
                    dst_file = f'{cwd}/{OTHER_DIR}/{file.name}'

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
        if not os.path.isdir(dirname):
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