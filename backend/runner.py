import sys

import os

from cassandra.protocol import SyntaxException

from config import RUN_OPTIONS, FF_RUN_OPTIONS, UU_RUN_OPTIONS, UI_RUN_OPTIONS, REQUEST_TYPES, SOCIAL_REQUEST_TYPES, \
    TABLES, TABLES_OPTIONS, GET_STATISTIC, DDL_OPTIONS
from cassandra_selector import cassandra_connection, truncate_tables, cassandra_stored_projects, \
    cassandra_stored_data_sources, cassandra_stored_connections, cassandra_stored_groups, cassandra_project_creators, \
    cassandra_datasource_creators, cassandra_connection_creators, count_tables, cassandra_stored_users_in_groups, \
    cassandra_stored_datasources_in_projects, truncate_table, drop_keyspace, create_keyspace, create_tables, \
    cassandra_created_objects, cassandra__event_objects
from events_generator import create_user, edit_users, popularity_users, create_items, add_to_wkspc, edit_items, \
    popularity_items
from file_writer import create_out_dir, create_put_file, create_get_file
from logger import start, stop
from progress_bar import print_progress
from request_sender import send_put_request, send_get_request


def main():
    user_input = ''
    while user_input not in [1, 2, 3, 4, 5, 6, 7, 8] or user_input == 'p':
        line_separator()
        user_input = let_user_pick_run_options()
        line_separator("=")
        if user_input == 1:
            session = cassandra_connection()
            flow_id, request_type = "FF", "put_event"
            out_dir_name = create_out_dir(flow_id, request_type)
            summary = os.path.join(out_dir_name, out_dir_name.split('\\')[-1])
            user_input = input("Truncate all tables before start? ")
            if user_input == '':
                truncate_tables(session)
            line_separator("=")
            user_input = let_user_pick_run_options(prnt="Full Flow Stages: ",
                                                   prmt="Press Enter to START (with default params)!\n",
                                                   options=FF_RUN_OPTIONS)
            if user_input == '':

                # Create User
                event_name, user_input = "CreateUser", "100"
                stored_objects = cassandra_created_objects(session)
                stored_users = sorted(",".join([v for k, v in stored_objects[0].items()]).split(','))

                created_users, creators = [], []
                print_progress(0, 1)
                for i in range(100):
                    send_request = send_put_request(create_user(stored_users, creators, created_users), request_type)
                    payload = send_request[1]
                    create_put_file(event_name, user_input, payload, out_dir_name)
                    print_progress(i + 1, int(100), prefix="Sending CREATE USER event", suffix="Events have been sent")
                start(summary)
                print("{} USERS created: ".format(len(sorted(list(set(created_users))))),
                      sorted(list(set(created_users))))
                creators = sorted(list(set(creators)))
                print("Created by {} distinct users: ".format(len(creators)), creators)
                stored_objects = cassandra_created_objects(session)
                users = sorted(",".join([v for k, v in stored_objects[0].items()]).split(','))
                print("{} users stored: ".format(len(users)), sorted(list(set(users))), "\n")
                stop()

                # Edit User
                event_name, user_input = "EditUser", "50"
                edited_users, editors = [], []
                stored_objects = cassandra_created_objects(session)
                stored_users = sorted(",".join([v for k, v in stored_objects[0].items()]).split(','))
                print_progress(0, 1)
                for i in range(50):
                    send_request = send_put_request(edit_users(stored_objects, edited_users, editors), request_type)
                    payload = send_request[1]
                    create_put_file(event_name, user_input, payload, out_dir_name)
                    print_progress(i + 1, int(50), prefix="Sending EDIT USER event", suffix="Events have been sent")
                start(summary)
                print("{} USERS have been edited: ".format(len(edited_users)), edited_users)
                editors = sorted(list(set(editors)))
                print("Edited by {} distinct users: ".format(len(editors)), editors, "\n")
                stop()

                # Popularity User
                event_name, user_input = "PopularityUser", "300"
                liked_users, likers, dislikers, disliked_users, followed_users, followers, recommended_users, recommenders, \
                unfollowed_users, unfollowers = [], [], [], [], [], [], [], [], [], []
                stored_objects = cassandra_created_objects(session)
                stored_users = sorted(",".join([v for k, v in stored_objects[0].items()]).split(','))
                print_progress(0, 1)
                for i in range(300):
                    send_request = send_put_request(
                        popularity_users(session, stored_users, liked_users, likers, dislikers, disliked_users,
                                         followed_users, followers, recommended_users, recommenders, unfollowed_users,
                                         unfollowers),
                        request_type)
                    payload = send_request[1]
                    create_put_file(event_name, user_input, payload, out_dir_name)
                    print_progress(i + 1, int(300), prefix="Sending POPULARITY USER event",
                                   suffix="Events have been sent")
                start(summary)
                print("{} USERS have been Liked: ".format(len(liked_users)), liked_users)
                likers = sorted(list(set(likers)))
                print("Liked by {} distinct users: ".format(len(likers)), likers)
                # print("{} USERS have been Disliked: ".format(len(disliked_users)), disliked_users)
                # dislikers = sorted(list(set(dislikers)))
                # print("Disliked by {} distinct users: ".format(len(dislikers)), dislikers)
                print("{} USERS have been Followed: ".format(len(followed_users)), followed_users)
                followers = sorted(list(set(followers)))
                print("Followed by {} distinct users: ".format(len(followers)), followers)
                print("{} USERS have been Unfollowed: ".format(len(unfollowed_users)), unfollowed_users)
                unfollowers = sorted(list(set(unfollowers)))
                print("Unfollowed by {} distinct users: ".format(len(unfollowers)), unfollowers)
                print("{} USERS have been Recommended: ".format(len(recommended_users)), recommended_users)
                recommenders = sorted(list(set(recommenders)))
                print("Recommended by {} distinct users: ".format(len(recommenders)), recommenders, "\n")
                stop()

                # Create Item
                event_name, user_input = "CreateItem", "1000"
                created_projects, created_connections, created_data_sources = [], [], []
                stored_objects = cassandra_created_objects(session)
                stored_projects = sorted(",".join([v for k, v in stored_objects[1].items()]).split(','))
                stored_data_sources = sorted(",".join([v for k, v in stored_objects[2].items()]).split(','))
                stored_connections = sorted(",".join([v for k, v in stored_objects[3].items()]).split(','))
                print_progress(0, 1)
                for i in range(1000):
                    send_request = send_put_request(
                        create_items(stored_objects, stored_users, stored_projects, stored_data_sources,
                                     stored_connections, created_connections, created_data_sources, created_projects),
                        request_type)
                    payload = send_request[1]
                    create_put_file(event_name, user_input, payload, out_dir_name)
                    print_progress(i + 1, int(1000), prefix="Sending CREATE IETM event", suffix="Events have been sent")
                start(summary)
                stored_objects = cassandra_created_objects(session)
                print("{} PROJECTS created: {}".format(len(created_projects), created_projects))
                projects = sorted(",".join([v for k, v in stored_objects[1].items()]).split(','))
                print("{} PROJECTS have been already stored in Cassandra: {}".format(len(projects), projects))
                print("{} DATA SOURCES created: {}".format(len(created_data_sources), created_data_sources))
                data_sources = sorted(",".join([v for k, v in stored_objects[2].items()]).split(','))
                print(
                    "{} DATA SOURCES have been already stored in Cassandra: {}".format(len(data_sources), data_sources))
                print("{} CONNECTIONS created: {}".format(len(created_connections), created_connections))
                connections = sorted(",".join([v for k, v in stored_objects[3].items()]).split(','))
                print("{} CONNECTIONS have been already stored in Cassandra: {}".format(len(connections), connections),
                      "\n")
                stop()

                # AddToWkspc DataSource
                event_name, user_input = "AddToWkspc", "500"
                stored_objects = cassandra_created_objects(session)
                project_creators = sorted(",".join([k for k, v in stored_objects[1].items()]).split(','))
                datasource_creators = sorted(",".join([k for k, v in stored_objects[2].items()]).split(','))
                connection_creators = sorted(",".join([k for k, v in stored_objects[3].items()]).split(','))
                stored_users = sorted(",".join([v for k, v in stored_objects[0].items()]).split(','))
                added_datasources, add_to_projects, addetors = [], [], []
                print_progress(0, 1)
                for i in range(500):
                    send_request = send_put_request(
                        add_to_wkspc(stored_objects, added_datasources, add_to_projects, addetors, datasource_creators,
                                     project_creators), request_type)
                    payload = send_request[1]
                    create_put_file(event_name, user_input, payload, out_dir_name)
                    print_progress(i + 1, int(500), prefix="Sending AddToWkspc ITEM event",
                                   suffix="Events have been sent")
                start(summary)
                print("{} DATA SOURCES have been added: ".format(len(added_datasources)), added_datasources)
                print("To {} Projects: ".format(len(add_to_projects)), add_to_projects)
                addetors = sorted(list(set(addetors)))
                print("Added by {} distinct users: ".format(len(addetors)), addetors, "\n")
                stop()

                # Edit Project
                event_name, user_input = "EditItem", "300"
                stored_objects = cassandra_created_objects(session)
                edited_projects, project_editors = [], []
                edited_datasources, datasource_editors = [], []
                edited_connections, connection_editors = [], []
                print_progress(0, 1)
                for i in range(300):
                    send_request = send_put_request(
                        edit_items(stored_objects, edited_projects, project_editors, edited_datasources,
                                   datasource_editors, edited_connections, connection_editors), request_type)
                    payload = send_request[1]
                    create_put_file(event_name, user_input, payload, out_dir_name)
                    print_progress(i + 1, int(300), prefix="Sending EDIT ITEM event", suffix="Events have been sent")
                start(summary)
                print("{} PROJECTS have been successfully edited: ".format(len(edited_projects)), edited_projects)
                project_editors = sorted(list(set(project_editors)))
                print("Edited by {} distinct users: ".format(len(project_editors)), project_editors)
                print("{} DATASOURCES have been successfully edited: ".format(len(edited_datasources)),
                      edited_datasources)
                datasource_editors = sorted(list(set(datasource_editors)))
                print("Edited by {} distinct users: ".format(len(datasource_editors)), datasource_editors)
                print("{} CONNECTIONS have been successfully edited: ".format(len(edited_connections)),
                      edited_connections)
                connection_editors = sorted(list(set(connection_editors)))
                print("Edited by {} distinct users: ".format(len(connection_editors)), connection_editors, "\n")
                stop()

                # Popularity Item
                event_name, user_input = "PopularityItem", "5000"
                stored_objects = cassandra_created_objects(session)
                stored_groups = cassandra_stored_groups(session)
                shared_data_sources, shareders, liked_data_sources, likers, subscribed_data_sources, subscribers, \
                recommended_data_sourced, recommenders, duplicated_data_sources, duplicaters, liked_projects, project_likers, \
                project_shareders, shared_projects, shared_connection, connection_shareders, subscribed_projects, \
                project_subscribers, unsubscribed_projects, project_unsubscribers, recommnded_projects, project_recommenders, \
                duplicated_projects, project_duplicators, disliked_projects, project_dislikers, unshared_projects, \
                project_unshareders, unsubscribed_data_sources, unsubscribers, unshared_data_sources, unshareders, \
                unshared_connection, disliked_data_sources, dislikers, connection_unshareders = [], [], [], [], [], [], [], [], [], \
                                                                                                [], [], [], [], [], [], [], [], [], \
                                                                                                [], [], [], [], [], [], [], [], [], \
                                                                                                [], [], [], [], [], [], [], [], []
                print_progress(0, 1)
                for i in range(5000):
                    send_request = send_put_request(
                        popularity_items(stored_objects, shared_data_sources, shareders, liked_data_sources, likers,
                                         subscribed_data_sources, subscribers, recommended_data_sourced, recommenders,
                                         duplicated_data_sources, duplicaters, liked_projects, project_likers,
                                         project_shareders, shared_projects, shared_connection, connection_shareders,
                                         subscribed_projects, project_subscribers, unsubscribed_projects,
                                         project_unsubscribers, recommnded_projects, project_recommenders,
                                         duplicated_projects, project_duplicators, disliked_projects, project_dislikers,
                                         unshared_projects, project_unshareders, unsubscribed_data_sources,
                                         unsubscribers, unshared_data_sources, unshareders, unshared_connection,
                                         disliked_data_sources, dislikers, connection_unshareders, session,
                                         stored_groups),
                        request_type)
                    payload = send_request[1]
                    create_put_file(event_name, user_input, payload, out_dir_name)
                    print_progress(i + 1, int(5000), prefix="Sending POPULARITY ITEM event",
                                   suffix="Events have been sent")
                start(summary)
                line_separator("*")
                print("{} PROJECTS have been Subscribed: ".format(len(subscribed_projects)), subscribed_projects)
                project_subscribers = sorted(list(set(project_subscribers)))
                print("Subscribed by {} distinct users: ".format(len(project_subscribers)), project_subscribers)
                print("{} PROJECTS have been Unsubscribed: ".format(len(unsubscribed_projects)), unsubscribed_projects)
                project_unsubscribers = sorted(list(set(project_unsubscribers)))
                print("Unubscribed by {} distinct users: ".format(len(project_unsubscribers)), project_unsubscribers)
                print("{} PROJECTS have been Recommended: ".format(len(recommnded_projects)), recommnded_projects)
                project_recommenders = sorted(list(set(project_recommenders)))
                print("Recommended by {} distinct users: ".format(len(project_recommenders)), project_recommenders)
                print("{} PROJECTS have been Duplicated: ".format(len(duplicated_projects)), duplicated_projects)
                project_duplicators = sorted(list(set(project_duplicators)))
                print("Duplicated by {} distinct users: ".format(len(project_duplicators)), project_duplicators)
                print("{} PROJECTS have been Liked: ".format(len(liked_projects)), sorted(liked_projects))
                project_likers = sorted(list(set(project_likers)))
                print("Liked by {} distinct users: ".format(len(project_likers)), project_likers)
                print("{} PROJECTS have been Disliked: ".format(len(disliked_projects)), disliked_projects)
                project_dislikers = sorted(list(set(project_dislikers)))
                print("Disliked by {} distinct users: ".format(len(project_dislikers)), project_dislikers)
                print("{} PROJECTS have been Shared: ".format(len(shared_projects)), shared_projects)
                project_shareders = sorted(list(set(project_shareders)))
                print("Shared by {} distinct users: ".format(len(project_shareders)), project_shareders)
                print("{} PROJECTS have been Unshared: ".format(len(unshared_projects)), unshared_projects)
                project_unshareders = sorted(list(set(project_unshareders)))
                print("Unshared by {} distinct users: ".format(len(project_unshareders)), project_unshareders)
                line_separator("*")
                print("{} DATA SOURCES have been Subscribed: ".format(len(subscribed_data_sources)),
                      subscribed_data_sources)
                subscribers = sorted(list(set(subscribers)))
                print("Subscribed by {} distinct users: ".format(len(subscribers)), subscribers)
                print("{} DATA SOURCES have been Unsubscribed: ".format(len(unsubscribed_data_sources)),
                      unsubscribed_data_sources)
                unsubscribers = sorted(list(set(unsubscribers)))
                print("Unsubscribed by {} distinct users: ".format(len(unsubscribers)), unsubscribers)
                print("{} DATA SOURCES have been Recommended: ".format(len(recommended_data_sourced)),
                      recommended_data_sourced)
                recommenders = sorted(list(set(recommenders)))
                print("Recommended by {} distinct users: ".format(len(recommenders)), recommenders)
                print("{} DATA SOURCES have been Duplicated: ".format(len(duplicated_data_sources)),
                      duplicated_data_sources)
                duplicaters = sorted(list(set(duplicaters)))
                print("Duplicated by {} distinct users: ".format(len(duplicaters)), duplicaters)
                print("{} DATA SOURCES have been Shared: ".format(len(shared_data_sources)), shared_data_sources)
                shareders = sorted(list(set(shareders)))
                print("Shared by {} distinct users: ".format(len(shareders)), shareders)
                print("{} DATA SOURCES have been Unshared: ".format(len(unshared_data_sources)),
                      unshared_data_sources)
                unshareders = sorted(list(set(unshareders)))
                print("Unshared by {} distinct users: ".format(len(unshareders)), unshareders)
                print("{} DATA SOURCES have been Liked: ".format(len(liked_data_sources)), sorted(liked_data_sources))
                likers = sorted(list(set(likers)))
                print("Liked by {} distinct users: ".format(len(likers)), likers)
                print("{} DATA SOURCES have been Disliked: ".format(len(disliked_data_sources)),
                      disliked_data_sources)
                dislikers = sorted(list(set(dislikers)))
                print("Disliked by {} distinct users: ".format(len(dislikers)), dislikers)
                line_separator("*")
                print("{} CONNECTIONS have been Shared: ".format(len(shared_connection)), shared_connection)
                connection_shareders = sorted(list(set(connection_shareders)))
                print("Shared by {} distinct users: ".format(len(connection_shareders)), connection_shareders)
                print("{} CONNECTIONS have been Unshared: ".format(len(unshared_connection)), unshared_connection)
                connection_unshareders = sorted(list(set(connection_unshareders)))
                print("Unshared by {} distinct users: ".format(len(connection_unshareders)), connection_unshareders)
                stop()
                continue
            else:
                user_input = "p"
        elif user_input == 2:
            session = cassandra_connection()
            flow_id, request_type = "UUF", "put_event"
            out_dir_name = create_out_dir(flow_id, request_type)
            summary = os.path.join(out_dir_name, out_dir_name.split('\\')[-1])
            user_input = input("Truncate all tables before start? ")
            if user_input == '':
                truncate_tables(session)
            line_separator("=")
            while user_input not in [1, 2, 3, "p", 5]:
                line_separator()
                user_input = let_user_pick_run_options(prnt="User-User Interaction Flow Stages: ",
                                                       options=UU_RUN_OPTIONS)
                if user_input == 1:
                    usrinpt = input("How many events should be send: ")
                    line_separator("=")

                    # Create User
                    event_name = "CreateUser"
                    user_input = "{}".format(usrinpt)
                    stored_objects = cassandra_created_objects(session)
                    stored_users = sorted(",".join([v for k, v in stored_objects[0].items()]).split(','))

                    created_users, creators = [], []
                    print_progress(0, 1)
                    for i in range(int(usrinpt)):
                        send_request = send_put_request(create_user(stored_users, creators, created_users),
                                                        request_type)
                        payload = send_request[1]
                        create_put_file(event_name, user_input, payload, out_dir_name)
                        print_progress(i + 1, int(usrinpt), prefix="Sending CREATE USER event",
                                       suffix="Events have been sent")
                    start(summary)
                    print("{} USERS created: ".format(len(sorted(list(set(created_users))))),
                          sorted(list(set(created_users))))
                    creators = sorted(list(set(creators)))
                    print("Created by {} distinct users: ".format(len(creators)), creators)
                    stored_objects = cassandra_created_objects(session)
                    users = sorted(",".join([v for k, v in stored_objects[0].items()]).split(','))
                    print("{} users stored: ".format(len(users)), sorted(list(set(users))), "\n")
                    stop()
                    continue
                elif user_input == 2:
                    usrinpt = input("How many events should be send: ")
                    line_separator("=")

                    # Edit User
                    event_name = "EditUser"
                    user_input = "{}".format(usrinpt)
                    edited_users, editors = [], []
                    stored_objects = cassandra_created_objects(session)
                    stored_users = sorted(",".join([v for k, v in stored_objects[0].items()]).split(','))
                    print_progress(0, 1)
                    for i in range(int(usrinpt)):
                        send_request = send_put_request(edit_users(stored_objects, edited_users, editors), request_type)
                        payload = send_request[1]
                        create_put_file(event_name, user_input, payload, out_dir_name)
                        print_progress(i + 1, int(usrinpt), prefix="Sending EDIT USER event",
                                       suffix="Events have been sent")
                    start(summary)
                    print("{} USERS have been edited: ".format(len(edited_users)), edited_users)
                    editors = sorted(list(set(editors)))
                    print("Edited by {} distinct users: ".format(len(editors)), editors, "\n")
                    stop()
                    continue
                elif user_input == 3:
                    usrinpt = input("How many events should be send: ")
                    line_separator("=")

                    # Popularity User
                    event_name = "PopularityUser"
                    user_input = "{}".format(usrinpt)
                    liked_users, likers, dislikers, disliked_users, followed_users, followers, recommended_users, recommenders, \
                    unfollowed_users, unfollowers = [], [], [], [], [], [], [], [], [], []
                    stored_objects = cassandra_created_objects(session)
                    stored_users = sorted(",".join([v for k, v in stored_objects[0].items()]).split(','))
                    print_progress(0, 1)
                    for i in range(int(usrinpt)):
                        send_request = send_put_request(
                            popularity_users(session, stored_users, liked_users, likers, dislikers, disliked_users,
                                             followed_users, followers, recommended_users, recommenders,
                                             unfollowed_users,
                                             unfollowers),
                            request_type)
                        payload = send_request[1]
                        create_put_file(event_name, user_input, payload, out_dir_name)
                        print_progress(i + 1, int(usrinpt), prefix="Sending POPULARITY USER event",
                                       suffix="Events have been sent")
                    start(summary)
                    print("{} USERS have been Liked: ".format(len(liked_users)), liked_users)
                    likers = sorted(list(set(likers)))
                    print("Liked by {} distinct users: ".format(len(likers)), likers)
                    # print("{} USERS have been Disliked: ".format(len(disliked_users)), disliked_users)
                    # dislikers = sorted(list(set(dislikers)))
                    # print("Disliked by {} distinct users: ".format(len(dislikers)), dislikers)
                    print("{} USERS have been Followed: ".format(len(followed_users)), followed_users)
                    followers = sorted(list(set(followers)))
                    print("Followed by {} distinct users: ".format(len(followers)), followers)
                    print("{} USERS have been Unfollowed: ".format(len(unfollowed_users)), unfollowed_users)
                    unfollowers = sorted(list(set(unfollowers)))
                    print("Unfollowed by {} distinct users: ".format(len(unfollowers)), unfollowers)
                    print("{} USERS have been Recommended: ".format(len(recommended_users)), recommended_users)
                    recommenders = sorted(list(set(recommenders)))
                    print("Recommended by {} distinct users: ".format(len(recommenders)), recommenders, "\n")
                    stop()
                    continue
                elif user_input == 4:
                    user_input = 'p'
                elif user_input == 5:
                    break
            continue
        elif user_input == 3:
            session = cassandra_connection()
            flow_id, request_type = "UIF", "put_event"
            out_dir_name = create_out_dir(flow_id, request_type)
            summary = os.path.join(out_dir_name, out_dir_name.split('\\')[-1])
            user_input = ''
            while user_input not in [1, 2, 3, 4, "p", 6]:
                try:
                    stored_objects = cassandra_created_objects(session)
                    stored_users = sorted(",".join([v for k, v in stored_objects[0].items()]).split(','))
                except:
                    start(summary)
                    print("\n\t\t\t\t\t\t\t>>>At least 10 users should be created before run!<<<")
                    stop()
                    break
                line_separator()
                user_input = let_user_pick_run_options(prnt="User-Item Interaction Flow Stages: ",
                                                       options=UI_RUN_OPTIONS)
                if user_input == 1:
                    usrinpt = input("How many events should be send: ")
                    line_separator("=")

                    # Create Item
                    event_name = "CreateItem"
                    user_input = usrinpt
                    created_projects, created_connections, created_data_sources = [], [], []
                    stored_objects = cassandra_created_objects(session)
                    stored_projects = sorted(",".join([v for k, v in stored_objects[1].items()]).split(','))
                    stored_data_sources = sorted(",".join([v for k, v in stored_objects[2].items()]).split(','))
                    stored_connections = sorted(",".join([v for k, v in stored_objects[3].items()]).split(','))
                    print_progress(0, 1)
                    for i in range(int(usrinpt)):
                        try:
                            send_request = send_put_request(
                                create_items(stored_objects, stored_users, stored_projects, stored_data_sources,
                                             stored_connections, created_connections, created_data_sources,
                                             created_projects),
                                request_type)
                        except IndexError as e:
                            print("\n\n\t\t\t\t\t\t\t>>>At least 10 users should be created before run!<<<")
                            print("\t\t\t\t\t\t\t\tERROR: {}\n".format(e))
                            break
                        payload = send_request[1]
                        create_put_file(event_name, user_input, payload, out_dir_name)
                        print_progress(i + 1, int(usrinpt), prefix="Sending CREATE IETM event",
                                       suffix="Events have been sent")
                    start(summary)
                    stored_objects = cassandra_created_objects(session)
                    print("{} PROJECTS created: {}".format(len(created_projects), created_projects))
                    projects = sorted(",".join([v for k, v in stored_objects[1].items()]).split(','))
                    print("{} PROJECTS have been already stored in Cassandra: {}".format(len(projects), projects))
                    print("{} DATA SOURCES created: {}".format(len(created_data_sources), created_data_sources))
                    data_sources = sorted(",".join([v for k, v in stored_objects[2].items()]).split(','))
                    print("{} DATA SOURCES have been already stored in Cassandra: {}".format(len(data_sources),
                                                                                             data_sources))
                    print("{} CONNECTIONS created: {}".format(len(created_connections), created_connections))
                    connections = sorted(",".join([v for k, v in stored_objects[3].items()]).split(','))
                    print("{} CONNECTIONS have been already stored in Cassandra: {}".format(len(connections),
                                                                                            connections), "\n")
                    stop()
                    continue
                elif user_input == 2:
                    usrinpt = input("How many events should be send: ")
                    line_separator("=")

                    # AddToWkspc DataSource
                    event_name = "AddToWkspc"
                    user_input = usrinpt
                    stored_objects = cassandra_created_objects(session)
                    project_creators = sorted(",".join([k for k, v in stored_objects[1].items()]).split(','))
                    datasource_creators = sorted(",".join([k for k, v in stored_objects[2].items()]).split(','))
                    connection_creators = sorted(",".join([k for k, v in stored_objects[3].items()]).split(','))
                    stored_users = sorted(",".join([v for k, v in stored_objects[0].items()]).split(','))
                    added_datasources, add_to_projects, addetors = [], [], []
                    print_progress(0, 1)
                    for i in range(int(usrinpt)):
                        try:
                            send_request = send_put_request(
                                add_to_wkspc(stored_objects, added_datasources, add_to_projects, addetors,
                                             datasource_creators,
                                             project_creators), request_type)
                        except IndexError as e:
                            print("\n\n\t\t\t\t\t\t\t>>>At least 10 users should be created before run!<<<")
                            print("\t\t\t\t\t\t\t\tERROR: {}\n".format(e))
                            break
                        payload = send_request[1]
                        create_put_file(event_name, user_input, payload, out_dir_name)
                        print_progress(i + 1, int(usrinpt), prefix="Sending AddToWkspc ITEM event",
                                       suffix="Events have been sent")
                    start(summary)
                    print("{} DATA SOURCES have been added: ".format(len(added_datasources)), added_datasources)
                    print("To {} Projects: ".format(len(add_to_projects)), add_to_projects)
                    addetors = sorted(list(set(addetors)))
                    print("Added by {} distinct users: ".format(len(addetors)), addetors, "\n")
                    stop()
                    continue
                elif user_input == 3:
                    usrinpt = input("How many events should be send: ")
                    line_separator("=")

                    # Edit Project
                    event_name = "EditItem"
                    user_input = usrinpt
                    stored_objects = cassandra_created_objects(session)
                    edited_projects, project_editors = [], []
                    edited_datasources, datasource_editors = [], []
                    edited_connections, connection_editors = [], []
                    print_progress(0, 1)
                    for i in range(int(usrinpt)):
                        try:
                            send_request = send_put_request(
                                edit_items(stored_objects, edited_projects, project_editors, edited_datasources,
                                           datasource_editors, edited_connections, connection_editors), request_type)
                        except IndexError as e:
                            print("\n\n\t\t\t\t\t\t\t>>>At least 10 users should be created before run!<<<")
                            print("\t\t\t\t\t\t\t\tERROR: {}\n".format(e))
                            break
                        payload = send_request[1]
                        create_put_file(event_name, user_input, payload, out_dir_name)
                        print_progress(i + 1, int(usrinpt), prefix="Sending EDIT ITEM event",
                                       suffix="Events have been sent")
                    start(summary)
                    print("{} PROJECTS have been successfully edited: ".format(len(edited_projects)), edited_projects)
                    project_editors = sorted(list(set(project_editors)))
                    print("Edited by {} distinct users: ".format(len(project_editors)), project_editors)
                    print("{} DATASOURCES have been successfully edited: ".format(len(edited_datasources)),
                          edited_datasources)
                    datasource_editors = sorted(list(set(datasource_editors)))
                    print("Edited by {} distinct users: ".format(len(datasource_editors)), datasource_editors)
                    print("{} CONNECTIONS have been successfully edited: ".format(len(edited_connections)),
                          edited_connections)
                    connection_editors = sorted(list(set(connection_editors)))
                    print("Edited by {} distinct users: ".format(len(connection_editors)), connection_editors, "\n")
                    stop()
                    continue
                elif user_input == 4:
                    usrinpt = input("How many events should be send: ")
                    line_separator("=")

                    # Popularity Item
                    event_name = "PopularityItem"
                    user_input = usrinpt
                    stored_objects = cassandra_created_objects(session)
                    stored_groups = cassandra_stored_groups(session)
                    shared_data_sources, shareders, liked_data_sources, likers, subscribed_data_sources, subscribers, \
                    recommended_data_sourced, recommenders, duplicated_data_sources, duplicaters, liked_projects, project_likers, \
                    project_shareders, shared_projects, shared_connection, connection_shareders, subscribed_projects, \
                    project_subscribers, unsubscribed_projects, project_unsubscribers, recommnded_projects, project_recommenders, \
                    duplicated_projects, project_duplicators, disliked_projects, project_dislikers, unshared_projects, \
                    project_unshareders, unsubscribed_data_sources, unsubscribers, unshared_data_sources, unshareders, \
                    unshared_connection, disliked_data_sources, dislikers, connection_unshareders = [], [], [], [], [], [], [], [], [], \
                                                                                                    [], [], [], [], [], [], [], [], [], \
                                                                                                    [], [], [], [], [], [], [], [], [], \
                                                                                                    [], [], [], [], [], [], [], [], []
                    print_progress(0, 1)
                    for i in range(int(usrinpt)):
                        try:
                            send_request = send_put_request(
                                popularity_items(stored_objects, shared_data_sources, shareders, liked_data_sources,
                                                 likers, subscribed_data_sources, subscribers, recommended_data_sourced,
                                                 recommenders, duplicated_data_sources, duplicaters, liked_projects,
                                                 project_likers, project_shareders, shared_projects, shared_connection,
                                                 connection_shareders, subscribed_projects, project_subscribers,
                                                 unsubscribed_projects, project_unsubscribers, recommnded_projects,
                                                 project_recommenders, duplicated_projects, project_duplicators,
                                                 disliked_projects, project_dislikers, unshared_projects,
                                                 project_unshareders, unsubscribed_data_sources, unsubscribers,
                                                 unshared_data_sources, unshareders, unshared_connection,
                                                 disliked_data_sources, dislikers, connection_unshareders, session,
                                                 stored_groups),
                                request_type)
                        except IndexError as e:
                            print(
                                "\n\n\t\t\t\t\t\t\t>>>At least 10 users and some items should be created before run!<<<")
                            print("\t\t\t\t\t\t\t\tERROR: {}\n".format(e))
                            break
                        payload = send_request[1]
                        create_put_file(event_name, user_input, payload, out_dir_name)
                        print_progress(i + 1, int(usrinpt), prefix="Sending POPULARITY ITEM event",
                                       suffix="Events have been sent")
                    start(summary)
                    line_separator("*")
                    print("{} PROJECTS have been Subscribed: ".format(len(subscribed_projects)), subscribed_projects)
                    project_subscribers = sorted(list(set(project_subscribers)))
                    print("Subscribed by {} distinct users: ".format(len(project_subscribers)), project_subscribers)
                    print("{} PROJECTS have been Unsubscribed: ".format(len(unsubscribed_projects)),
                          unsubscribed_projects)
                    project_unsubscribers = sorted(list(set(project_unsubscribers)))
                    print("Unubscribed by {} distinct users: ".format(len(project_unsubscribers)),
                          project_unsubscribers)
                    print("{} PROJECTS have been Recommended: ".format(len(recommnded_projects)), recommnded_projects)
                    project_recommenders = sorted(list(set(project_recommenders)))
                    print("Recommended by {} distinct users: ".format(len(project_recommenders)), project_recommenders)
                    print("{} PROJECTS have been Duplicated: ".format(len(duplicated_projects)), duplicated_projects)
                    project_duplicators = sorted(list(set(project_duplicators)))
                    print("Duplicated by {} distinct users: ".format(len(project_duplicators)), project_duplicators)
                    print("{} PROJECTS have been Liked: ".format(len(liked_projects)), sorted(liked_projects))
                    project_likers = sorted(list(set(project_likers)))
                    print("Liked by {} distinct users: ".format(len(project_likers)), project_likers)
                    print("{} PROJECTS have been Disliked: ".format(len(disliked_projects)), disliked_projects)
                    project_dislikers = sorted(list(set(project_dislikers)))
                    print("Disliked by {} distinct users: ".format(len(project_dislikers)), project_dislikers)
                    print("{} PROJECTS have been Shared: ".format(len(shared_projects)), shared_projects)
                    project_shareders = sorted(list(set(project_shareders)))
                    print("Shared by {} distinct users: ".format(len(project_shareders)), project_shareders)
                    print("{} PROJECTS have been Unshared: ".format(len(unshared_projects)), unshared_projects)
                    project_unshareders = sorted(list(set(project_unshareders)))
                    print("Unshared by {} distinct users: ".format(len(project_unshareders)), project_unshareders)
                    line_separator("*")
                    print("{} DATA SOURCES have been Subscribed: ".format(len(subscribed_data_sources)),
                          subscribed_data_sources)
                    subscribers = sorted(list(set(subscribers)))
                    print("Subscribed by {} distinct users: ".format(len(subscribers)), subscribers)
                    print("{} DATA SOURCES have been Unsubscribed: ".format(len(unsubscribed_data_sources)),
                          unsubscribed_data_sources)
                    unsubscribers = sorted(list(set(unsubscribers)))
                    print("Unsubscribed by {} distinct users: ".format(len(unsubscribers)), unsubscribers)
                    print("{} DATA SOURCES have been Recommended: ".format(len(recommended_data_sourced)),
                          recommended_data_sourced)
                    recommenders = sorted(list(set(recommenders)))
                    print("Recommended by {} distinct users: ".format(len(recommenders)), recommenders)
                    print("{} DATA SOURCES have been Duplicated: ".format(len(duplicated_data_sources)),
                          duplicated_data_sources)
                    duplicaters = sorted(list(set(duplicaters)))
                    print("Duplicated by {} distinct users: ".format(len(duplicaters)), duplicaters)
                    print("{} DATA SOURCES have been Shared: ".format(len(shared_data_sources)), shared_data_sources)
                    shareders = sorted(list(set(shareders)))
                    print("Shared by {} distinct users: ".format(len(shareders)), shareders)
                    print("{} DATA SOURCES have been Unshared: ".format(len(unshared_data_sources)),
                          unshared_data_sources)
                    unshareders = sorted(list(set(unshareders)))
                    print("Unshared by {} distinct users: ".format(len(unshareders)), unshareders)
                    print("{} DATA SOURCES have been Liked: ".format(len(liked_data_sources)),
                          sorted(liked_data_sources))
                    likers = sorted(list(set(likers)))
                    print("Liked by {} distinct users: ".format(len(likers)), likers)
                    print("{} DATA SOURCES have been Disliked: ".format(len(disliked_data_sources)),
                          disliked_data_sources)
                    dislikers = sorted(list(set(dislikers)))
                    print("Disliked by {} distinct users: ".format(len(dislikers)), dislikers)
                    line_separator("*")
                    print("{} CONNECTIONS have been Shared: ".format(len(shared_connection)), shared_connection)
                    connection_shareders = sorted(list(set(connection_shareders)))
                    print("Shared by {} distinct users: ".format(len(connection_shareders)), connection_shareders)
                    print("{} CONNECTIONS have been Unshared: ".format(len(unshared_connection)), unshared_connection)
                    connection_unshareders = sorted(list(set(connection_unshareders)))
                    print("Unshared by {} distinct users: ".format(len(connection_unshareders)), connection_unshareders)
                    stop()
                    user_input = ''
                    continue
                elif user_input == 5:
                    user_input = 'p'
                elif user_input == 6:
                    break
            continue
        elif user_input == 4:
            flow_id, request_type = "REC", "get_event"
            out_dir_name = create_out_dir(flow_id, request_type)
            user_input = ''
            while user_input not in [1, 2, 3, 4, "p", 6]:
                line_separator()
                user_input = let_user_pick_run_options(prnt="RECOMMENDATION LIST: ",
                                                       options=REQUEST_TYPES)
                line_separator("=")
                if user_input == 1:
                    request_type = "get_als"
                    user_input = input(
                        ">>> Please put user ID(s) for providing recommendations based on users similarity: ")
                    send_request = send_get_request(request_type, user_input)
                    print_progress(0, 1)
                    create_get_file(send_request, user_input, out_dir_name, request_type)
                    print_progress(1, int(1), prefix="Sending GET ALS request",
                                   suffix="Request has been sent")
                    print(send_request)
                    continue
                elif user_input == 2:
                    request_type = "get_gup"
                    user_input = input(
                        ">>> Please put group ID(s) for providing users rating within the specific group: ")
                    send_request = send_get_request(request_type, user_input)
                    print_progress(0, 1)
                    create_get_file(send_request, user_input, out_dir_name, request_type)
                    print_progress(1, int(1), prefix="Sending GET GUP request",
                                   suffix="Request has been sent")
                    print(send_request)
                    continue
                elif user_input == 3:
                    request_type = "get_mba"
                    user_input = input(
                        ">>> Please put data source ID(s) for providing recommended items that are often used together: ")
                    send_request = send_get_request(request_type, user_input)
                    print_progress(0, 1)
                    create_get_file(send_request, user_input, out_dir_name, request_type)
                    print_progress(1, int(1), prefix="Sending GET MBA request",
                                   suffix="Request has been sent")
                    print(send_request)
                    continue
                elif user_input == 4:
                    request_type = "get_ir"
                    user_input = input(
                        ">>> Please put user ID and item ID(optional) for providing recommendations based on implicit metrics: ").split(
                        ",")
                    send_request = send_get_request(request_type, user_input)
                    print_progress(0, 1)
                    create_get_file(send_request, user_input, out_dir_name, request_type)
                    print_progress(1, int(1), prefix="Sending GET IR request",
                                   suffix="Request has been sent")
                    print(send_request)
                    continue
                elif user_input == 5:
                    user_input = 'p'
                elif user_input == 6:
                    continue
            continue
        elif user_input == 5:
            flow_id, request_type = "SOC", "get_event"
            out_dir_name = create_out_dir(flow_id, request_type)
            user_input = ''
            session = cassandra_connection()
            while user_input not in [1, 2, 3, 4, 5, 6, "p", 8]:
                line_separator()
                user_input = let_user_pick_run_options(prnt="SOCIAL COMPONENTS: ",
                                                       options=SOCIAL_REQUEST_TYPES)
                line_separator("=")
                if user_input == 1:
                    event_objects = cassandra__event_objects(session, "Like")
                    project_like_event_creators = sorted(
                        set(",".join([v for k, v in event_objects[1].items()]).split(',')))
                    projects_liked = sorted(set([k for k, v in event_objects[1].items()]))
                    data_source_like_event_creators = sorted(
                        set(",".join([v for k, v in event_objects[2].items()]).split(',')))
                    data_sources_liked = sorted(set([k for k, v in event_objects[2].items()]))
                    print("Project \"Like\" events senders list: \n", project_like_event_creators)
                    print("Liked project list: \n", projects_liked)
                    line_separator("-")
                    print("Datasource \"Like\" events senders list: \n", data_source_like_event_creators)
                    print("Liked datasource list: \n", data_sources_liked)
                    line_separator("-")
                    request_type = "get_likes"
                    user_input = input(
                        "\n>>> Please put user ID and item ID(s) for providing \"like\" statistics: ").split(',')
                    send_request = send_get_request(request_type, user_input)
                    print_progress(0, 1)
                    create_get_file(send_request, user_input, out_dir_name, request_type)
                    print_progress(1, int(1), prefix="Sending GET LIKES request",
                                   suffix="Request has been sent")
                    print(send_request)
                    euser = user_input[0]
                    if len(euser) != 5:
                        print("Please check user_id")
                        continue
                    projects_liked_by_euser = sorted(
                        set(",".join([k for k, v in event_objects[1].items() if "{}".format(euser) in v]).split(',')))
                    data_sources_liked_by_euser = sorted(
                        set(",".join([k for k, v in event_objects[2].items() if "{}".format(euser) in v]).split(',')))
                    line_separator("~")
                    print(
                        "Take a look this \"{}\" user liked next objects: \n\tprojects >>> {}; \n\tdatasources >>> {}".format(
                            euser, projects_liked_by_euser, data_sources_liked_by_euser))
                    line_separator("-")
                    for p in projects_liked_by_euser:
                        users_liked_project = sorted(
                            set(",".join([v for k, v in event_objects[1].items() if k == "{}".format(p)]).split(',')))
                        try:
                            users_liked_project.remove(euser)
                            if len(users_liked_project) >= 1:
                                print("Another users also liked \"{}\" project: {}".format(p, users_liked_project))
                            else:
                                print("Nobody else liked this project \"{}\"".format(p))
                        except ValueError:
                            print("Please check user_id")
                    line_separator("-")
                    for d in data_sources_liked_by_euser:
                        users_liked_data_source = sorted(
                            set(",".join([v for k, v in event_objects[2].items() if k == "{}".format(d)]).split(
                                ',')))
                        try:
                            users_liked_data_source.remove(euser)
                            if len(users_liked_data_source) >= 1:
                                print(
                                    "Another users also liked \"{}\" datasource: {}".format(d, users_liked_data_source))
                            else:
                                print("Nobody else liked this datasource \"{}\"".format(d))
                        except ValueError:
                            print("Please check user_id")
                    line_separator("-")
                    ui = input(
                        "You can also specify users by typing item type and item id (e.g. 'datasource,10001'): ").split(
                        ',')
                    if ui[0] == "project":
                        print("Users liked \"{}\" project: {}".format(ui[1], sorted(set(
                            ",".join([v for k, v in event_objects[1].items() if k == "{}".format(ui[1])]).split(',')))))
                    elif ui[0] == "datasource":
                        print(
                            "Users liked \"{}\" datasource: {}".format(ui[1], sorted(set(
                                ",".join([v for k, v in event_objects[2].items() if k == "{}".format(ui[1])]).split(
                                    ',')))))
                    elif ui[0] == "":
                        pass
                    continue
                elif user_input == 2:
                    request_type = "get_subscr"
                    user_input = input(
                        ">>> Please put user ID for providing subscription information: ")
                    send_request = send_get_request(request_type, user_input)
                    print_progress(0, 1)
                    create_get_file(send_request, user_input, out_dir_name, request_type)
                    print_progress(1, int(1), prefix="Sending GET SUBSCRIPTIONS request",
                                   suffix="Request has been sent")
                    print(send_request)
                    continue
                elif user_input == 3:
                    request_type = "get_followers"
                    user_input = input(
                        ">>> Please put user ID for providing followers list: ")
                    send_request = send_get_request(request_type, user_input)
                    print_progress(0, 1)
                    create_get_file(send_request, user_input, out_dir_name, request_type)
                    print_progress(1, int(1), prefix="Sending GET FOLLOWERS request",
                                   suffix="Request has been sent")
                    print(send_request)
                    continue
                elif user_input == 4:
                    request_type = "get_shared"
                    user_input = input(
                        ">>> Please put user ID, group ID(s) and size for getting a list of items shared with specified user: ").split(
                        ",")
                    send_request = send_get_request(request_type, user_input)
                    print_progress(0, 1)
                    create_get_file(send_request, user_input, out_dir_name, request_type)
                    print_progress(1, int(1), prefix="Sending GET SHARED ITEMS request",
                                   suffix="Request has been sent")
                    print(send_request)
                    continue
                elif user_input == 5:
                    request_type = "get_updates"
                    user_input = input(
                        ">>> Please put user ID, group ID(s) and size for getting a list of last updated items: ").split(
                        ",")
                    send_request = send_get_request(request_type, user_input)
                    print_progress(0, 1)
                    create_get_file(send_request, user_input, out_dir_name, request_type)
                    print_progress(1, int(1), prefix="Sending GET RECENT UPDATES request",
                                   suffix="Request has been sent")
                    print(send_request)
                    continue
                elif user_input == 6:
                    request_type = "get_activities"
                    user_input = input(
                        ">>> Please put user ID, group ID(s) and size for getting a activity feed list: ").split(
                        ",")
                    send_request = send_get_request(request_type, user_input)
                    print_progress(0, 1)
                    create_get_file(send_request, user_input, out_dir_name, request_type)
                    print_progress(1, int(1), prefix="Sending GET ACTIVITY FEED request",
                                   suffix="Request has been sent")
                    print(send_request)
                    continue
                elif user_input == 7:
                    user_input = "p"
                elif user_input == 8:
                    sys.exit(0)
            continue
        elif user_input == 6:
            user_input = ''
            while user_input not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, "p", 13]:
                session = cassandra_connection()
                line_separator()
                user_input = let_user_pick_run_options(prnt="TABLES LIST: ",
                                                       options=TABLES_OPTIONS)
                line_separator("=")
                if user_input == 1:
                    user_input = ''
                    table_name = TABLES_OPTIONS[0]
                    print_progress(0, 1)
                    count = count_tables(session, table_name=table_name)
                    print_progress(1, int(1), prefix="Counting {} table".format(table_name),
                                   suffix="Completed")
                    print("\tTable: {} contains {} rows".format(table_name, count))
                    continue
                elif user_input == 2:
                    user_input = ''
                    table_name = TABLES_OPTIONS[1]
                    print_progress(0, 1)
                    count = count_tables(session, table_name=table_name)
                    print_progress(1, int(1), prefix="Counting {} table".format(table_name),
                                   suffix="Completed")
                    print("\tTable: {} contains {} rows".format(table_name, count))
                    continue
                elif user_input == 3:
                    user_input = ''
                    table_name = TABLES_OPTIONS[2]
                    print_progress(0, 1)
                    count = count_tables(session, table_name=table_name)
                    print_progress(1, int(1), prefix="Counting {} table".format(table_name),
                                   suffix="Completed")
                    print("\tTable: {} contains {} rows".format(table_name, count))
                    continue
                elif user_input == 4:
                    user_input = ''
                    table_name = TABLES_OPTIONS[3]
                    print_progress(0, 1)
                    count = count_tables(session, table_name=table_name)
                    print_progress(1, int(1), prefix="Counting {} table".format(table_name),
                                   suffix="Completed")
                    print("\tView: {} contains {} rows".format(table_name, count))
                    continue
                elif user_input == 5:
                    user_input = ''
                    table_name = TABLES_OPTIONS[4]
                    print_progress(0, 1)
                    count = count_tables(session, table_name=table_name)
                    print_progress(1, int(1), prefix="Counting {} table".format(table_name),
                                   suffix="Completed")
                    print("\tView: {} contains {} rows".format(table_name, count))
                    continue
                elif user_input == 6:
                    user_input = ''
                    table_name = TABLES_OPTIONS[5]
                    print_progress(0, 1)
                    count = count_tables(session, table_name=table_name)
                    print_progress(1, int(1), prefix="Counting {} table".format(table_name),
                                   suffix="Completed")
                    print("\tTable: {} contains {} rows".format(table_name, count))
                    continue
                elif user_input == 7:
                    user_input = ''
                    table_name = TABLES_OPTIONS[6]
                    print_progress(0, 1)
                    count = count_tables(session, table_name=table_name)
                    print_progress(1, int(1), prefix="Counting {} table".format(table_name),
                                   suffix="Completed")
                    print("\tTable: {} contains {} rows".format(table_name, count))
                    continue
                elif user_input == 8:
                    user_input = ''
                    table_name = TABLES_OPTIONS[7]
                    print_progress(0, 1)
                    count = count_tables(session, table_name=table_name)
                    print_progress(1, int(1), prefix="Counting {} table".format(table_name),
                                   suffix="Completed")
                    print("\tTable: {} contains {} rows".format(table_name, count))
                    continue
                elif user_input == 9:
                    user_input = ''
                    table_name = TABLES_OPTIONS[8]
                    print_progress(0, 1)
                    count = count_tables(session, table_name=table_name)
                    print_progress(1, int(1), prefix="Counting {} table".format(table_name),
                                   suffix="Completed")
                    print("\tTable: {} contains {} rows".format(table_name, count))
                    continue
                elif user_input == 10:
                    user_input = ''
                    table_name = TABLES_OPTIONS[9]
                    print_progress(0, 1)
                    count = count_tables(session, table_name=table_name)
                    print_progress(1, int(1), prefix="Counting {} table".format(table_name),
                                   suffix="Completed")
                    print("\tTable: {} contains {} rows".format(table_name, count))
                    continue
                elif user_input == 11:
                    user_input = ''
                    counts = count_tables(session)
                    for k, v in counts[0].items():
                        print("\tTable: {} contains {} rows".format(k, v))
                        if k == "events":
                            for k, v in count_tables(session)[1].items():
                                print("\t\tView: {} contains {} rows".format(k, v))
                    continue
                elif user_input == 12:
                    user_input = 'p'
                elif user_input == 13:
                    sys.exit(0)
            continue
        elif user_input == 7:
            user_input = ''
            while user_input not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, "p", 13]:
                session = cassandra_connection()
                line_separator()
                user_input = let_user_pick_run_options(prnt="OPERATION LIST: ",
                                                       options=GET_STATISTIC)
                line_separator("=")
                if user_input == 1:
                    user_input = ''
                    print_progress(0, 1)
                    # operation = cassandra_stored_users(session)
                    stored_objects = cassandra_created_objects(session)
                    stored_users = sorted(",".join([v for k, v in stored_objects[0].items()]).split(','))
                    operation = stored_users
                    print_progress(1, int(1), prefix="Retrieving stored users", suffix="Completed")
                    print("\tStored users: {}".format(operation))
                    continue
                elif user_input == 2:
                    user_input = ''
                    user_input = input(
                        ">>> You can specify retrieving by putting user ID to provide groups where user is a member: ")
                    print_progress(0, 1)
                    operation = cassandra_stored_groups(session, user_input)
                    print_progress(1, int(1), prefix="Retrieving stored groups", suffix="Completed")
                    print("\tUser is a member of next groups: {}".format(operation))
                    continue
                elif user_input == 3:
                    user_input = ''
                    user_input = input(
                        ">>> Please specify retrieving by putting group ID to provide members of the group: ")
                    print_progress(0, 1)
                    operation = cassandra_stored_users_in_groups(session, user_input)
                    print_progress(1, int(1), prefix="Retrieving stored users in groups", suffix="Completed")
                    print("\tUsers in the {} group: {}".format(user_input, operation))
                    continue
                elif user_input == 4:
                    user_input = ''
                    print_progress(0, 1)
                    operation = cassandra_project_creators(session)
                    print_progress(1, int(1), prefix="Retrieving project creators", suffix="Completed")
                    print("\tProject creators: {}".format(operation))
                    continue
                elif user_input == 5:
                    user_input = ''
                    print_progress(0, 1)
                    operation = cassandra_datasource_creators(session)
                    print_progress(1, int(1), prefix="Retrieving data source creators", suffix="Completed")
                    print("\tData source creators: {}".format(operation))
                    continue
                elif user_input == 6:
                    user_input = ''
                    print_progress(0, 1)
                    operation = cassandra_connection_creators(session)
                    print_progress(1, int(1), prefix="Retrieving connection creators", suffix="Completed")
                    print("\tConnection creators: {}".format(operation))
                    continue
                elif user_input == 7:
                    user_input = ''
                    user_input = input(
                        ">>> Please specify retrieving by putting user ID to provide projects created by the user: ")
                    print_progress(0, 1)
                    operation = cassandra_stored_projects(session, user_input)
                    print_progress(1, int(1), prefix="Retrieving created projects", suffix="Completed")
                    print("\tStored projects: {}".format(operation))
                    continue
                elif user_input == 8:
                    user_input = ''
                    user_input = input(
                        ">>> Please specify retrieving by putting user ID to provide data sources created by the user: ")
                    print_progress(0, 1)
                    operation = cassandra_stored_data_sources(session, user_input)
                    print_progress(1, int(1), prefix="Retrieving created data sources", suffix="Completed")
                    print("\tStored data sources: {}".format(operation))
                    continue
                elif user_input == 9:
                    user_input = ''
                    user_input = input(
                        ">>> Please specify retrieving by putting user ID to provide connections created by the user: ")
                    print_progress(0, 1)
                    operation = cassandra_stored_connections(session, user_input)
                    print_progress(1, int(1), prefix="Retrieving created connections", suffix="Completed")
                    print("\tStored connections: {}".format(operation))
                    continue
                elif user_input == 10:
                    user_input = ''
                    user_input = input(
                        ">>> Please put project ID to provide data sources added to the project: ")
                    print_progress(0, 1)
                    operation = cassandra_stored_datasources_in_projects(session, project_id=user_input)
                    print_progress(1, int(1), prefix="Retrieving stored groups", suffix="Completed")
                    print("\tData sources in the {} project: {}".format(user_input, operation))
                    continue
                elif user_input == 11:
                    user_input = ''
                    user_input = input(
                        ">>> Please specify retrieving by putting data source ID to provide projects where data source was added: ")
                    print_progress(0, 1)
                    operation = cassandra_stored_datasources_in_projects(session, datasource_id=user_input)
                    print_progress(1, int(1), prefix="Retrieving stored groups", suffix="Completed")
                    print("\tData sources in the {} project: {}".format(user_input, operation))
                    continue
                elif user_input == 12:
                    user_input = 'p'
                elif user_input == 13:
                    sys.exit(0)
            continue
        elif user_input == 8:
            user_input = ''
            while user_input not in [1, 2, 3, 4, "p", 6]:
                try:
                    session = cassandra_connection()
                except:
                    pass
                line_separator()
                user_input = let_user_pick_run_options(prnt="DDL OPERATION LIST: ",
                                                       options=DDL_OPTIONS)
                line_separator("=")
                if user_input == 1:
                    user_input = ''
                    user_input = input(
                        ">>> You can specify table for truncating: ")
                    if user_input == '':
                        print_progress(0, 1)
                        i = 0
                        for table in TABLES:
                            truncate_table(session, table)
                            print_progress(i + 1, len(TABLES), prefix="Truncating: {}".format(table),
                                           suffix="Truncated")
                            i += 1
                    else:
                        print_progress(0, 1)
                        i = 0
                        truncate_table(session, table)
                        print_progress(1, int(1), prefix="Truncating: {}".format(table), suffix="Truncated")
                    continue
                elif user_input == 2:
                    user_input = ''
                    user_input = input(
                        ">>> You can specify keyspace for deleting: ")
                    print_progress(0, 1)
                    if user_input != '':
                        try:
                            operation = drop_keyspace(session, user_input)
                            print_progress(1, int(1), prefix="Deleting keyspace", suffix="Deleted")
                        except SyntaxException:
                            print("\n>>> Keyaspace is already deleted!")
                    else:
                        try:
                            operation = drop_keyspace(session)
                            print_progress(1, int(1), prefix="Deleting keyspace", suffix="Deleted")
                        except SyntaxException:
                            print("\n>>> Keyaspace is already deleted!")
                    continue
                elif user_input == 3:
                    user_input = ''
                    user_input = input(
                        ">>> You can specify keyspace for creating: ")
                    print_progress(0, 1)
                    if not create_keyspace(user_input):
                        print_progress(1, int(1), prefix="Creating keyspace", suffix="Created")
                    continue
                elif user_input == 4:
                    user_input = ''
                    user_input = input(
                        ">>> You can specify init file: ")
                    if user_input == '':
                        create_tables(session)
                    else:
                        create_tables(session, user_input)
                    continue
                elif user_input == 5:
                    user_input = 'p'
                elif user_input == 5:
                    sys.exit(0)
        elif user_input == 9:
            sys.exit(0)
        continue


def let_user_pick_run_options(options=RUN_OPTIONS, prnt="Please choose:", prmt="Enter number: "):
    print("{}".format(prnt))
    for idx, element in enumerate(options):
        print("\t{}) {}".format(idx + 1, element))
    line_separator("=")
    i = input("{}".format(prmt))
    try:
        if 0 < int(i) <= len(options):
            return int(i)
    except:
        return ''
    return None


def line_separator(separator="#"):
    for i in range(0, 120):
        print("{}".format(separator), sep="", end="", flush=True)
    print()
    # def runner(event_group=None, event_type=None):
    #     user_input = input(
    #         "\t\t\t\t\tPlease press 'Enter' button for running Full Flow or")
    # iteration = 0
    # user_input = ''
    # while user_input not in ['UU', 'uu', 'UI', 'ui']:


if __name__ == '__main__':
    main()
