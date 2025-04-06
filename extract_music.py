import moviepy.editor as mp
import time
import os


def extract_music(path):
    try:
        my_clip = mp.VideoFileClip(path)
        my_clip.audio.write_audiofile('{0}.mp3'.format(path))
        os.system("cls")
        print("-Completed-")
        print("-You Can Change The File Name By Yourself")
        print("-We Will Further Develop This Function-")
    except OSError:
        time.sleep(1)
        os.system("cls")
        print("-There's Something Wrong-")
        print("-Please Check Your Path And Try Again-")


def course():
    os.system('cls')
    path = input("-Please Give Me The Path Which The Movie Is In-\nEnter Here:")
    print("-It May Take For Some Minutes-")
    print("-When The System is Extracting-")
    print("-Let's Have A Break-")
    extract_music(path)
