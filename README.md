# Media / Funscript Tools

This repo is a collection of tools for interacting with media (video) and funscripts.

**Disclaimer**: This is a work in progress, you execute these scripts / commands at your own risk.

## Prerequisites

Tested in a linux (ubuntu) environment.

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

```bash
./FunscriptTools.py completeHalfTrack /path/to/input.funscript /path/to/output.funscript
```

Turns

```json
"actions": [
        {
            "at": 3633,
            "pos": 0
        },
        {
            "at": 7203,
            "pos": 0
        },
        {
            "at": 7664,
            "pos": 0
        }
    ]
```

into

```json
    "actions": [
        {
            "at": 3633,
            "pos": 0
        },
        {
            "at": 5418,
            "pos": 100
        },
        {
            "at": 7203,
            "pos": 0
        },
        {
            "at": 7434,
            "pos": 100
        },
        {
            "at": 7664,
            "pos": 0
        }
    ]
```

### Sync video clips to funscript

```bash
./warpclip.py warpClip \
    /path/to/reference.funscript \
    /path/to/video/clip.mp4 \
    /path/to/video/clip.funscript \
    /path/to/output/file.mp4
```

* reference funscript (usually set to music)
* a video clip (ideally a loop) which you want to sync to the reference funscript
* a funscript which marks the actions of the video clip
* file to write the video loop to

#### Recursively find all funscripts in a directory and sync their respective video to a reference funscript

```bash
./warpclip.py warpAllClips /path/to/ref/funscript /path/to/dir/containing/clips /path/to/output/dir
```
