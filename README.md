# Media / Funscript Tools

This repo is a collection of tools for interacting with media (video) and funscripts.

**Disclaimer**: This is a work in progress, you execute these scripts / commands at your own risk.

## Prerequisites

These scripts have been tested in a linux (ubuntu) environment. I do not know if they work on windows.
* [Python](https://www.python.org/)
* [FFMpeg](https://ffmpeg.org/)
* [OpenFunscripter](https://github.com/OpenFunscripter/OFS) is useful for creating funscripts

## Installation

```bash
git clone https://github.com/AffablePerv/mediatools.git
cd mediatools
deactivate
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
source venv/bin/activate
```

## Use cases

### Complete a funscript

Assume you are creating a funscript based on music. You may create a funscript following the basic beat using only the 0 position. You can fill in the gaps like this:

```bash
./FunscriptTools.py completeHalfTrack /path/to/input.funscript /path/to/output.funscript
```

### Sync video clips to funscript

Given the following:

* a "reference" funscript (this is rhythm which the clip should be synched to) 
* a video clip you want to sync (ideally a loop)
* a funscript which marks the rhythm of the video clip

```bash
./warpclip.py warpClip /path/to/reference/funscript /path/to/video/clip.mp4 /path/to/video/clip.funscript /path/to/output/file.mp4
```

The output will be a video file which syncs & repeats the clip for the duration of the reference funscript.

It is also possible to recursively find all funscripts in a directory and sync their respective video to a reference funscript:

```bash
./warpclip.py warpAllClips /path/to/ref/funscript /path/to/dir/containing/clips /path/to/output/dir
```
