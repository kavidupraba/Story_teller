#!/usr/bin/python3

from gtts import gTTS
from pydub import AudioSegment
import os
#import time
import sys

def text_to_audio(file_path):
    with open(file_path, 'r',encoding='utf-8') as f:
        text=f.read()

    tts=gTTS(text=text, lang='en')

    #save the audio file
    voice_file="narration.mp3"
    tts.save(voice_file)

    narration = AudioSegment.from_mp3(voice_file)
    background = AudioSegment.from_mp3("background.mp3")

    if len(background)<len(narration):#match the length of the background music if it is shorter
        loops=(len(narration)//len(background)) + 1
        background = background * loops

    background = background[:len(narration)] - 18 #lowering volume
    combined= background.overlay(narration)

    final_file="story_output.mp3"
    combined.export(final_file, format="mp3")#export the final story with music

    os.system(f"start {final_file}" if  os.name=='nt' else f"xdg-open {final_file}")


if __name__=='__main__':
    if len(sys.argv)!=2:
        print(f"please add the file <text.txt>")
        sys.exit(1)
    text_to_audio(sys.argv[1])
