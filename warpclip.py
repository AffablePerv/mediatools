#!/usr/bin/env python
from moviepy.editor import VideoFileClip, concatenate_videoclips
from ClipFactory import ClipFactory
import sys, json, os, fnmatch
import sys
 
def warpAndRepeatClip(refFunscript, videoFile, clipFunscript, outputFile, actionOffset=0, debug=False):
    """  """
    outputClipList = []
    clipFactory = ClipFactory(videoFile, clipFunscript)
    with open(refFunscript) as user_file:
        inputcontent = json.loads(user_file.read())
    if debug: print("successfully read",str(len(inputcontent.get("actions"))),"actions from script",refFunscript)
    actions = inputcontent.get("actions")
    previousAction = 0
    for idx, i in enumerate(actions):
        duration = i['at'] - previousAction
        if debug: print('  idx:',idx,'i:',str(i),'duration:',duration)
        if duration > 0:
            outputClipList.append(clipFactory.warpSubclip(idx + actionOffset, duration))
        previousAction = i['at']
    final_clip = concatenate_videoclips(outputClipList)
    final_clip.write_videofile(outputFile)

def warpAllClipsInDir(refFunscript, directory, outputDir, debug=False):
    funscriptExtension = 'funscript'
    videoExtensions = ['mp4', 'mkv', 'avi', 'webm']

    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in fnmatch.filter(filenames, f"*{funscriptExtension}"):
            i = os.path.join(dirpath, filename)
            if debug: print("i",i)
            for j in videoExtensions:
                if debug: print("j",j)
                parts = i.rsplit(j, 1)
                parts[-1] = parts[-1].replace(funscriptExtension, j, 1)
                potentialVideoFile = funscriptExtension.join(parts)
                if debug: print('potentialVideoFile', potentialVideoFile)
                if os.path.exists(potentialVideoFile):
                    videoFile = potentialVideoFile
                    if debug: print('found file')
                    break
            if videoFile != None:
                warpAndRepeatClip(refFunscript, videoFile, i, outputDir + '/' + videoFile.replace('/', '_'))
                videoFile = None

if len(sys.argv) < 2:
    print('Usage: ./warpclip.py [warpClip|warpAllClips]')
elif sys.argv[1] == 'warpClip':
    if len(sys.argv) != 6:
        print('Usage: ./warpclip.py warpClip /path/to/ref/funscript /path/to/video/clip.mp4 /path/to/clip.funscript /path/to/output/file')
    else:
        warpAndRepeatClip(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
elif sys.argv[1] == 'warpAllClips':
    if len(sys.argv) != 5:
        print('Usage: ./warpclip.py warpAllClips /path/to/ref/funscript /path/to/dir/containing/clips /path/to/output/dir')
    else:
        warpAllClipsInDir(sys.argv[2], sys.argv[3], sys.argv[4])
