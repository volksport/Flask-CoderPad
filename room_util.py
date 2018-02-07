import json
import os
from threading import Lock

from models import Room

file_lock = Lock()
def get_room_meta_path(room_name):
    return os.path.join(os.path.dirname(__file__), 'metadata', '%s.json' % room_name)
def get_program_path(room_name):
    return os.path.join(os.path.dirname(__file__),'sessions','%s.program'%room_name)
def get_latest_prog(room_name):
    cache_file = get_program_path(room_name)
    if not os.path.exists(cache_file):
        open(cache_file,'wb').close()
    return open(cache_file,"rb").read()
def update_latest_prog(room,prog_text):
    file_lock.acquire()
    cache_file = get_program_path(room)
    with open(cache_file,"wb") as f:
        f.write(prog_text)
    file_lock.release()

def get_room_data(room_name):
    try:
        return json.load(open(get_room_meta_path(room_name),"rb"))
    except:
        return {}
def room_active(room_name):
    return get_room_data(room_name).get('active',False)

    # with open(get_room_meta_path(payload['room_name']),"wb") as f:
    #     json.dump(payload,f)