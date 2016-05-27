#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2016 Yannick Loiseau <me@yloiseau.net>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See http://www.wtfpl.net/ for more details.
"""
on-modify hook for taskwarrior.

This hook connect taskwarrior and watson. 

When starting a task in taskwarrior, the hook starts a corresponding project in
watson. The project and keywords of the taskwarrior task are used in watson.
When stopping a task in taskwarrior, the hook stops the watson project.

To install, copy in ~/.task/hooks/on-modify-tw-watson.py and make executable.

https://taskwarrior.org/
https://github.com/TailorDev/Watson
"""
# {
#     "description":"Dossiers campus france",
#     "entry":"20160407T131359Z",
#     "modified":"20160408T151257Z",
#     "priority":"H",
#     "project":"Work.GestionL3",
#     "status":"pending",
#     "tags":["dossiers"],
#     "uuid":"ca1d938f-f3bc-4c9c-a808-aeca9cc3c842",
#     "annotations":[
#         {"entry":"20160408T142713Z","description":"Started task"},
#         {"entry":"20160408T151257Z","description":"Stopped task"}]}
#
# {
#     "description":"Dossiers campus france",
#     "entry":"20160407T131359Z",
#     "modified":"20160408T151257Z",
#     "priority":"H",
#     "project":"Work.GestionL3",
#     "start":"20160408T154412Z",
#     "status":"pending",
#     "tags":["dossiers"],
#     "uuid":"ca1d938f-f3bc-4c9c-a808-aeca9cc3c842",
#     "annotations":[
#         {"entry":"20160408T142713Z","description":"Started task"},
#         {"entry":"20160408T151257Z","description":"Stopped task"},
#         {"entry":"20160408T154412Z","description":"Started task"}]}


import sys
import json
from watson import Watson

def load_json():
    return (json.loads(sys.stdin.readline()), json.loads(sys.stdin.readline()))

def is_starting(old, new):
    return "start" in new and "start" not in old

def is_stopping(old, new):
    return "start" in old and "start" not in new

def stop_watson():
    watson = Watson()
    if watson.is_started:
        watson.stop()
        watson.save()

def start_watson(task):
    watson = Watson()
    if watson.is_started and watson.config.getboolean('options', 'stop_on_start'):
        watson.stop()
    watson.start(task.get("project"), task.get("tags"))
    watson.save()


def main(args):
    try:
        old, new = load_json()
        print(json.dumps(new))
        if is_stopping(old, new):
            stop_watson()
            print("Watson project {} {} stoped".format(
                new.get("project"), new.get("tags")))
        elif is_starting(old, new):
            start_watson(new)
            print("Watson project {} {} started".format(
                new.get("project"), new.get("tags")))
        return 0
    except Exception as e:
        print(str(e))
        return 1

if __name__ == "__main__":
    sys.exit(main(sys.argv))