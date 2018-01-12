from _datetime import datetime

import os

from config import OUTPUT_DIR


def main():
    # flow_id, request_type, event_name, user_input, payload = "FullFlow", "get_als", "CreateUser", "100", "payload"
    # out_dir_name = create_out_dir(flow_id, request_type)
    # create_get_file(payload,user_input,out_dir_name,request_type)
    # flow_id, request_type, event_name, user_input, payload = "FullFlow", "put_events", "CreateUser", "100", "payload"
    # out_dir_name = create_out_dir(flow_id, request_type)
    # create_put_file(event_name, user_input, payload, out_dir_name)
    pass


def create_out_dir(flow_id=None, request_type=None):
    base_dir = os.path.join("\\".join(os.path.abspath(OUTPUT_DIR).split("\\")[:-1]) + "\\backend", OUTPUT_DIR)
    if flow_id and request_type:
        out_dir_name = os.path.join(base_dir,
                                    "{}-{}_".format(flow_id,
                                                    request_type.split("_")[0].upper()) + datetime.now().strftime(
                                        '%Y-%m-%d_%H_%M'))
        if not os.path.exists(base_dir):
            os.mkdir(base_dir)
        if not os.path.exists(out_dir_name):
            os.mkdir(out_dir_name)
        return out_dir_name
    else:
        pass


def create_put_file(event_name=None, user_input=None, payload=None, out_dir_name=None):
    if event_name and user_input and payload:
        events_filename = "{}-{}".format(event_name, user_input)
        with open(os.path.join(out_dir_name, events_filename), 'a') as out_events_file:
            out_events_file.write(payload)
    else:
        print("File cannot be created!")


def create_get_file(response_json=None, user_input=None, out_dir_name=None, request_type=None):
    events_filename = "{}-{}".format(request_type.split("_")[1].upper(), user_input)
    try:
        with open(os.path.join(out_dir_name, events_filename), 'a') as out_events_file:
            out_events_file.write(response_json)
    except IOError:
        print("Cannot create or open or write to: '{}' out file".format(os.path.join(out_dir_name, events_filename)))


if __name__ == '__main__':
    main()
