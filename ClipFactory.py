#!/usr/bin/env python
from moviepy.editor import VideoFileClip, concatenate_videoclips
import json, copy, math, glob, os, fnmatch
# config.MELT_BINARY = '/usr/bin/melt'

class ClipFactory:

    def __init__(self, videoFilepath, funscriptPath, debug=False):
        self.videoFilepath = videoFilepath
        self.funscriptPath = funscriptPath
        mainClip = VideoFileClip(videoFilepath)
        clips = []
        with open(funscriptPath) as user_file:
            inputcontent = json.loads(user_file.read())
        if debug: print("successfully read",str(len(inputcontent.get("actions"))),"actions from script",funscriptPath)
        actions = inputcontent.get("actions")
        previousPosition = 0
        startClip = None
        endClip = None
        for idx, i in enumerate(actions):
            if debug: print('  idx:',str(idx),'i:',str(i))
            if idx == 0 and i['at'] > 0:
                if debug: print('    read startClip from 0 to',i['at'])
                startClip = mainClip.subclip(0, i['at']/1000)
            if idx != 0:
                if debug: print('    read clip from',str(previousPosition),' to',str(i['at']))
                clips.append(mainClip.subclip(previousPosition/1000, i['at']/1000))
            if idx == len(actions) - 1:
                endClip = mainClip.subclip(i['at']/1000)
                if startClip is not None:
                    if debug: print('  concatenating endClip & startClip')
                    endClip = concatenate_videoclips([endClip, startClip])
                clips.append(endClip)
            if debug: print('    settingPreviousPosition to',str(previousPosition))
            previousPosition = i['at']
        if debug: print(str(len(clips)),'clips read')
        self.clips = clips

    def __str__(self):
        return f"{self.videoFilepath}: {self.funscriptPath} ({len(self.clips)})"

    def warpSubclip(self, counter, desiredDuration, debug=False) -> VideoFileClip:
        index = counter % len(self.clips)
        if debug: print('warping clip #',str(index), 'to ',str(desiredDuration))
        return self.clips[index].copy().speedx(final_duration=desiredDuration/1000)