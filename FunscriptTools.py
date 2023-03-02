#!/usr/bin/env python
import json, sys

def completeHalfTrack(actions, minimum_distance=30):
    """ take list of actions (e.g. [{"pos": 0, "at": 0},{"pos": 0, "at": 1000}]) and add midpoints (e.g. [{"pos": 0, "at": 0},{"pos": 100, "at": 500},{"pos": 0, "at": 1000}])"""
    allActions = []
    for idx, i in enumerate(actions):
        if idx != 0 and i['pos'] == 0:
            posA = actions[idx-1]['at']
            valueA = actions[idx-1]['pos']
            posB = i['at']
            valueB = i['pos']
            midPos = int(round(posA + ((posB - posA) / 2), 0))
            distance = posB - posA
            if (distance / 2) >= minimum_distance:
                allActions.append({
                    "at": midPos,
                    "pos": (100 - valueA)
                })
        allActions.append(i)
    return allActions

def make_funscript(actions, duration=0, title='', inverted=False, range=90, version='1.0'):
    data = {}
    data['inverted'] = inverted
    data['metadata'] = {
        'creator': '',
        'description': '',
        'duration': duration,
        'license': '',
        'notes': '',
        'performers': [],
        'script_url': '',
        'tags': [],
        'title': title,
        'type': 'basic',
        'video_url': ''
    }
    data['range'] = range
    data['version'] = version
    data['actions'] = actions
    return data

def completeFunscript(input_file, output_file):
    with open(input_file) as user_file:
        inputcontent = json.loads(user_file.read())
    actions = inputcontent.get("actions")
    completedActions = completeHalfTrack(actions)
    funscript = make_funscript(completedActions)
    with open(output_file, 'w') as outfile:
        json.dump(funscript, outfile, sort_keys=False, indent=4)

if len(sys.argv) < 2:
    print('Usage: ./FunscriptTools.py [completeHalfTrack]')
elif sys.argv[1] == 'completeHalfTrack':
    if len(sys.argv) != 4:
        print('Usage: ./FunscriptTools.py completeHalfTrack /path/to/input.funscript /path/to/output.funscript')
    else:
        completeFunscript(sys.argv[2], sys.argv[3])
