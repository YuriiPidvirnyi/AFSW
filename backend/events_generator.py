import random
import uuid
from datetime import datetime

from config import TEMPLATE, UU_EVENTS, UU_EVENTS_WEIGHTS, UI_TRG_ENTITY_TYPE, UI_TRG_ENTITY_IDS_WEIGHTS, NAMES, \
    CHANGES, UI_EVENTS, UI_EVENTS_WEIGHTS
from cassandra_selector import cassandra_connection, cassandra_stored_groups, cassandra_created_objects, \
    cassandra__event_objects


def main():
    session = cassandra_connection()

    # Create User
    # stored_users = cassandra_stored_users(session)
    # created_users, creators = [], []
    # for i in range(100):
    #     print(create_user(stored_users, creators, created_users))
    # print(len(created_users), len(creators))
    # print("created_users", created_users, "\ncreators", creators)

    # Edit User
    # stored_users = cassandra_stored_users(session)
    # edited_users, editors = [], []
    # for i in range(1):
    #     print(edit_users(stored_users, edited_users, editors))
    # print(len(edited_users), len(editors))
    # print(edited_users, editors)

    # Popularity User
    # stored_users = cassandra_stored_users(session)
    # liked_users, likers, dislikers, disliked_users, followed_users, followers, recommended_users, recommenders, \
    # unfollowed_users, unfollowers = [], [], [], [], [], [], [], [], [], []
    # for i in range(5):
    #     print(popularity_users(session, stored_users, liked_users, likers, dislikers, disliked_users, followed_users,
    #                            followers, recommended_users, recommenders, unfollowed_users, unfollowers))
    # print(len(liked_users), len(likers), len(dislikers), len(disliked_users), len(followed_users), len(followers),
    #       len(recommended_users), len(recommenders), len(unfollowed_users), len(unfollowers))
    # print(liked_users, likers, dislikers, disliked_users, followed_users, followers, recommended_users, recommenders,
    #       unfollowed_users, unfollowers)

    # Create Item
    # stored_users = cassandra_stored_users(session)
    # stored_projects = cassandra_stored_projects(session)
    # stored_data_sources = cassandra_stored_data_sources(session)
    # stored_connections = cassandra_stored_connections(session)
    # created_projects, created_connections, created_data_sources = [], [], []
    # for i in range(1):
    #     print(create_items(session, stored_users, stored_projects, stored_data_sources, stored_connections,
    #                        created_connections, created_data_sources, created_projects))
    # print(len(created_projects), len(created_data_sources), len(created_connections))
    # print(created_projects, created_connections, created_data_sources)
    #
    # AddToWkspc DataSource
    # project_creators = cassandra_project_creators(session)
    # datasource_creators = cassandra_datasource_creators(session)
    # added_datasources, add_to_projects, addetors = [], [], []
    # for i in range(500):
    #     print(
    #         add_to_wkspc(stored_objects, added_datasources, add_to_projects, addetors, datasource_creators, project_creators))
    # print(len(added_datasources), len(add_to_projects), len(addetors))
    # print(added_datasources, add_to_projects, addetors)

    # Edit Item
    stored_objects = cassandra_created_objects(session)
    edited_projects, project_editors = [], []
    edited_projects, project_editors = [], []
    edited_datasources, datasource_editors = [], []
    edited_connections, connection_editors = [], []
    print(edit_items(stored_objects, edited_projects, project_editors, edited_datasources,
                     datasource_editors, edited_connections, connection_editors))
    print(edited_projects, project_editors)

    # Popularity Item
    # stored_users = cassandra_stored_users(session)
    # stored_data_sources = cassandra_stored_data_sources(session)
    # stored_projects = cassandra_stored_projects(session)
    # stored_connections = cassandra_stored_connections(session)
    # stored_groups = cassandra_stored_groups(session)
    # project_creators = cassandra_project_creators(session)
    # datasource_creators = cassandra_datasource_creators(session)
    # connection_creators = cassandra_connection_creators(session)
    # shared_data_sources, shareders, liked_data_sources, likers, subscribed_data_sources, subscribers, \
    # recommended_data_sourced, recommenders, duplicated_data_sources, duplicaters, liked_projects, project_likers, \
    # project_shareders, shared_projects, shared_connection, connection_shareders, subscribed_projects, \
    # project_subscribers, unsubscribed_projects, project_unsubscribers, recommnded_projects, project_recommenders, \
    # duplicated_projects, project_duplicators, disliked_projects, project_dislikers, unshared_projects, \
    # project_unshareders, unsubscribed_data_sources, unsubscribers, unshared_data_sources, unshareders, \
    # unshared_connection, disliked_data_sources, dislikers, connection_unshareders = [], [], [], [], [], [], [], [], [], \
    #                                                                                 [], [], [], [], [], [], [], [], [], \
    #                                                                                 [], [], [], [], [], [], [], [], [], \
    #                                                                                 [], [], [], [], [], [], [], [], []
    # for i in range(500):
    #     print(popularity_items(shared_data_sources, shareders, liked_data_sources, likers,
    #                            subscribed_data_sources, subscribers, recommended_data_sourced,
    #                            recommenders, duplicated_data_sources, duplicaters, liked_projects,
    #                            project_likers, project_shareders, shared_projects, shared_connection,
    #                            connection_shareders, subscribed_projects, project_subscribers,
    #                            unsubscribed_projects, project_unsubscribers, recommnded_projects,
    #                            project_recommenders, duplicated_projects, project_duplicators,
    #                            disliked_projects, project_dislikers, unshared_projects,
    #                            project_unshareders, unsubscribed_data_sources, unsubscribers,
    #                            unshared_data_sources, unshareders, unshared_connection,
    #                            disliked_data_sources, dislikers, connection_unshareders, session, stored_users,
    #                            stored_groups, stored_connections, stored_projects, stored_data_sources,
    #                            project_creators, datasource_creators, connection_creators))
    # print(shared_data_sources, shareders, liked_data_sources, likers, subscribed_data_sources, subscribers,
    #       recommended_data_sourced, recommenders, duplicated_data_sources, duplicaters,
    #       liked_projects, project_likers, project_shareders, shared_projects, shared_connection,
    #       connection_shareders, subscribed_projects, project_subscribers, unsubscribed_projects,
    #       project_unsubscribers, recommnded_projects, project_recommenders, duplicated_projects,
    #       project_duplicators, disliked_projects, project_dislikers, unshared_projects, project_unshareders,
    #       unsubscribed_data_sources, unsubscribers, unshared_data_sources, unshareders, unshared_connection,
    #       disliked_data_sources, dislikers, connection_unshareders)


def event_time():
    time_now = str(datetime.utcnow()).split(" ")
    time_now.insert(1, "T")
    time_now.append("Z")
    return "".join(time_now)


# User-User Interaction Events:
def create_user(stored_users, creators, created_users, template=TEMPLATE):
    template["event"] = "Create"
    template["eventTime"] = event_time()
    template["targetEntityType"] = "User"
    if not stored_users or len(stored_users) == 0 or '' in stored_users:
        admin_user = str(random.randint(90000, 90010))
        template["userId"] = admin_user
        target_entity_id = str(random.randint(10000, 11000))
        while target_entity_id in created_users:
            target_entity_id = str(random.randint(10000, 11500))
        template["targetEntityId"] = target_entity_id
        template["properties"] = {"groups": "20000"}
        if random.randint(1, 6) == 5:
            template["properties"] = {"groups": "20000,{}".format(random.randint(20001, 20005))}
        created_users.append(target_entity_id)
        creators.append(admin_user)
        return template
    else:
        template["userId"] = user_id = str(random.choice(stored_users))
        target_entity_id = str(random.randint(10000, 11000))
        while user_id == target_entity_id or target_entity_id in stored_users or target_entity_id in created_users:
            target_entity_id = str(random.randint(10000, 11500))
        template["targetEntityId"] = target_entity_id
        template["properties"] = {"groups": "20000"}
        if random.randint(1, 6) == 5:
            template["properties"] = {"groups": "20000,{}".format(random.randint(20001, 20005))}
        created_users.append(target_entity_id)
        creators.append(user_id)
        return template


def edit_users(stored_objects, edited_users, editors, template=TEMPLATE):
    stored_users = sorted(",".join([v for k, v in stored_objects[0].items()]).split(','))
    user_creators = sorted(",".join([k for k, v in stored_objects[0].items()]).split(','))
    template["event"] = "Edit"
    template["eventTime"] = event_time()
    template["targetEntityType"] = "User"
    user_id = str(random.choice(stored_users))
    if user_id in user_creators:
        template["userId"] = user_id
        users_created_by_user = sorted(
            ",".join([v for k, v in stored_objects[0].items() if k == "{}".format(user_id)]).split(','))
        users_created_by_user.append(user_id)
        template["targetEntityId"] = target_entity_id = str(random.choice(users_created_by_user))
        editors.append(user_id)
        edited_users.append(target_entity_id)
    else:
        template["userId"] = user_id
        template["targetEntityId"] = target_entity_id = user_id
        editors.append(user_id)
        edited_users.append(target_entity_id)
    group = random.randint(20001, 20006)
    i = random.randint(1, 10)
    if i > 5:
        template["properties"] = {"groups": "20000,{}".format(group)}
    elif i < 5:
        group_3 = random.randint(20007, 20010)
        while group == group_3:
            group_3 = random.randint(20007, 20010)
        template["properties"] = {"groups": "20000,{},{}".format(group, group_3)}
    elif i == 5:
        group_3 = random.randint(20007, 20010)
        group_4 = random.randint(20010, 20015)
        while group == group_4 or group == group_3 or group_3 == group_4:
            group_3 = random.randint(20007, 20010)
            group_4 = random.randint(20010, 20015)
        template["properties"] = {"groups": "20000,{},{},{}".format(group, group_3, group_4)}
    return template


def popularity_users(session, stored_users, liked_users, likers, dislikers, disliked_users, followed_users, followers,
                     recommended_users, recommenders, unfollowed_users, unfollowers, template=TEMPLATE):
    template["event"] = event_type = random.choices(UU_EVENTS, UU_EVENTS_WEIGHTS)[0]
    template["eventTime"] = event_time()
    template["targetEntityType"] = "User"
    template["userId"] = user_id = str(random.choice(stored_users))
    stored_users.remove(user_id)
    template["targetEntityId"] = target_entity_id = str(random.choice(stored_users))
    stored_users.append(user_id)
    template["properties"] = {"groups": cassandra_stored_groups(session, user_id)}
    if event_type == "Like":
        liked_users.append(target_entity_id)
        likers.append(user_id)
    elif event_type == "Dislike":
        event_objects = cassandra__event_objects(session, "Like")
        user_like_event_creators = sorted(set(",".join([v for k, v in event_objects[0].items()]).split(',')))
        template["userId"] = user_id = str(random.choice(user_like_event_creators))
        user_events_created_by_user = [k for k, v in event_objects[0].items() if "{}".format(user_id) in v]
        template["targetEntityId"] = target_entity_id = str(random.choice(user_events_created_by_user))
        disliked_users.append(target_entity_id)
        dislikers.append(user_id)
    elif event_type == "Follow":
        followed_users.append(target_entity_id)
        followers.append(user_id)
    elif event_type == "Unfollow":
        event_objects = cassandra__event_objects(session, "Follow")
        user_follow_event_creators = sorted(set(",".join([v for k, v in event_objects[0].items()]).split(',')))
        template["userId"] = user_id = str(random.choice(user_follow_event_creators))
        user_events_created_by_user = [k for k, v in event_objects[0].items() if "{}".format(user_id) in v]
        template["targetEntityId"] = target_entity_id = str(random.choice(user_events_created_by_user))
        unfollowed_users.append(target_entity_id)
        unfollowers.append(user_id)
    elif event_type == "Recommend":
        recommended_users.append(target_entity_id)
        recommenders.append(user_id)
    return template


# User-Item Interaction Events:
def create_items(stored_objects, stored_users, stored_projects, stored_data_sources, stored_connections,
                 created_connections, created_data_sources, created_projects, template=TEMPLATE):
    template["event"] = "Create"
    template["eventTime"] = event_time()
    template["targetEntityType"] = target_entity_type = random.choices(UI_TRG_ENTITY_TYPE, UI_TRG_ENTITY_IDS_WEIGHTS)[0]
    template["userId"] = user_id = str(random.choice(stored_users))
    template["properties"] = {}
    if target_entity_type == "Project":
        target_entity_id = str(random.randint(10000, 13000))
        while target_entity_id in created_projects or target_entity_id in stored_projects:
            target_entity_id = str(random.randint(10000, 14000))
        template["targetEntityId"] = target_entity_id
        created_projects.append(target_entity_id)
        created_data_sources_by_user = sorted(
            ",".join([v for k, v in stored_objects[2].items() if k == "{}".format(user_id)]).split(','))
        if created_data_sources_by_user:
            template["properties"] = {"datasources": "{}".format(created_data_sources_by_user)}
    elif target_entity_type == "Datasource":
        target_entity_id = str(random.randint(14001, 17500))
        while target_entity_id in created_data_sources or target_entity_id in stored_data_sources:
            target_entity_id = str(random.randint(14001, 18000))
        template["targetEntityId"] = target_entity_id
        created_data_sources.append(target_entity_id)
    elif target_entity_type == "Connection":
        target_entity_id = str(random.randint(18001, 18500))
        while target_entity_id in created_connections or target_entity_id in stored_connections:
            target_entity_id = str(random.randint(18001, 19000))
        template["targetEntityId"] = target_entity_id
        created_connections.append(target_entity_id)
    return template


def add_to_wkspc(stored_objects, added_datasources, add_to_projects, addetors, datasource_creators,
                 project_creators, template=TEMPLATE):
    template["event"] = "AddToWkspc"
    template["eventTime"] = event_time()
    template["targetEntityType"] = "Datasource"
    creators = list(set(datasource_creators).intersection(project_creators))
    user_id = str(random.choice(creators))
    created_data_sources_by_user = sorted(
        ",".join([v for k, v in stored_objects[2].items() if k == "{}".format(user_id)]).split(','))
    created_projects_by_user = sorted(
        ",".join([v for k, v in stored_objects[1].items() if k == "{}".format(user_id)]).split(','))
    add_to_project = random.choice(created_projects_by_user)
    added_datasource = str(random.choice(created_data_sources_by_user))
    template["userId"] = user_id
    template["targetEntityId"] = added_datasource
    template["properties"] = {"project": "{}".format(add_to_project)}
    add_to_projects.append(add_to_project)
    added_datasources.append(added_datasource)
    addetors.append(user_id)
    return template


def edit_items(stored_objects, edited_projects, project_editors, edited_datasources, datasource_editors,
               edited_connections, connection_editors, template=TEMPLATE):
    template["event"] = "Edit"
    template["eventTime"] = event_time()
    template["targetEntityType"] = target_entity_type = random.choices(UI_TRG_ENTITY_TYPE, UI_TRG_ENTITY_IDS_WEIGHTS)[0]
    project_creators = sorted(",".join([k for k, v in stored_objects[1].items()]).split(','))
    datasource_creators = sorted(",".join([k for k, v in stored_objects[2].items()]).split(','))
    connection_creators = sorted(",".join([k for k, v in stored_objects[3].items()]).split(','))
    creators = list(set(datasource_creators).intersection(project_creators))
    template["properties"] = properties = {}
    if target_entity_type == "Project":
        template["userId"] = user_id = str(random.choice(creators))
        created_projects_by_user = sorted(
            ",".join([v for k, v in stored_objects[1].items() if k == "{}".format(user_id)]).split(','))
        created_data_sources_by_user = sorted(
            ",".join([v for k, v in stored_objects[2].items() if k == "{}".format(user_id)]).split(','))
        template["targetEntityId"] = target_entity_id = str(random.choice(created_projects_by_user))
        if random.randint(0, 6) == 6:
            datasource = "{}".format(random.choice(created_data_sources_by_user))
            name_1 = random.choice(NAMES)
            name_2 = random.choice(NAMES)
            if name_1 == name_2:
                name_2 = random.choice(NAMES)
            properties["dataNodes"] = [
                {"id": uuid.uuid4().__str__(), "name": name_1, "@type": "SOURCE", "filter": "null",
                 "changes": CHANGES[0],
                 "dataSource": "null", "sourceItemId": datasource, "timeIntervals": "null", "sourceItemName": name_1,
                 "lastModifiedDate": "null"},
                {"id": uuid.uuid4().__str__(), "name": name_2, "@type": "SOURCE", "filter": "null",
                 "changes": CHANGES[0],
                 "dataSource": "null", "sourceItemId": datasource, "timeIntervals": "null", "sourceItemName": name_2,
                 "lastModifiedDate": "null"}
            ]
        elif random.randint(0, 6) == 5:
            datasource = "{}".format(random.choice(created_data_sources_by_user))
            name = random.choice(NAMES)
            properties["dataNodes"] = [
                {"id": uuid.uuid4().__str__(), "name": name, "@type": "SOURCE", "filter": "null", "changes": CHANGES[1],
                 "dataSource": "null", "sourceItemId": datasource, "timeIntervals": "null", "sourceItemName": name,
                 "lastModifiedDate": "null"}
            ]
        elif random.randint(0, 6) == 4:
            datasource = "{}".format(random.choice(created_data_sources_by_user))
            name_1 = random.choice(NAMES)
            name_2 = random.choice(NAMES)
            if name_1 == name_2:
                name_2 = random.choice(NAMES)
            properties["dataNodes"] = [
                {"id": uuid.uuid4().__str__(), "name": name_1, "@type": "SOURCE", "filter": "null",
                 "changes": CHANGES[2],
                 "dataSource": "null", "sourceItemId": datasource, "timeIntervals": "null", "sourceItemName": name_1,
                 "lastModifiedDate": "null"},
                {"id": uuid.uuid4().__str__(), "name": name_2, "@type": "SOURCE", "filter": "null",
                 "changes": CHANGES[2],
                 "dataSource": "null", "sourceItemId": datasource, "timeIntervals": "null", "sourceItemName": name_2,
                 "lastModifiedDate": "null"}
            ]
        elif random.randint(0, 6) == 3:
            datasource = "{}".format(random.choice(created_data_sources_by_user))
            name = random.choice(NAMES)
            properties["dataNodes"] = [
                {"id": uuid.uuid4().__str__(), "name": name, "@type": "SOURCE", "filter": "null", "changes": CHANGES[3],
                 "dataSource": "null", "sourceItemId": datasource, "timeIntervals": "null", "sourceItemName": name,
                 "lastModifiedDate": "null"}
            ]
        elif random.randint(0, 6) == 2:
            datasource = "{}".format(random.choice(created_data_sources_by_user))
            name_1 = random.choice(NAMES)
            name_2 = random.choice(NAMES)
            if name_1 == name_2:
                name_2 = random.choice(NAMES)
            properties["dataNodes"] = [
                {"id": uuid.uuid4().__str__(), "name": name_1, "@type": "SOURCE", "filter": "null",
                 "changes": CHANGES[4],
                 "dataSource": "null", "sourceItemId": datasource, "timeIntervals": "null", "sourceItemName": name_1,
                 "lastModifiedDate": "null"},
                {"id": uuid.uuid4().__str__(), "name": name_2, "@type": "SOURCE", "filter": "null",
                 "changes": CHANGES[4],
                 "dataSource": "null", "sourceItemId": datasource, "timeIntervals": "null", "sourceItemName": name_2,
                 "lastModifiedDate": "null"}
            ]
        elif random.randint(0, 6) == 1:
            datasource = "{}".format(random.choice(created_data_sources_by_user))
            name = random.choice(NAMES)
            properties["dataNodes"] = [
                {"id": uuid.uuid4().__str__(), "name": name, "@type": "SOURCE", "filter": "null", "changes": CHANGES[5],
                 "dataSource": "null", "sourceItemId": datasource, "timeIntervals": "null", "sourceItemName": name,
                 "lastModifiedDate": "null"}
            ]
        elif random.randint(0, 6) == 0:
            datasource = "{}".format(random.choice(created_data_sources_by_user))
            name_1 = random.choice(NAMES)
            name_2 = random.choice(NAMES)
            name_3 = random.choice(NAMES)
            if name_1 == name_2:
                name_2 = random.choice(NAMES)
                if name_1 == name_3 or name_2 == name_3:
                    name_3 = random.choice(NAMES)
            properties["dataNodes"] = [
                {"id": uuid.uuid4().__str__(), "name": name_1, "@type": "SOURCE", "filter": "null",
                 "changes": CHANGES[5],
                 "dataSource": "null", "sourceItemId": datasource, "timeIntervals": "null", "sourceItemName": name_1,
                 "lastModifiedDate": "null"},
                {"id": uuid.uuid4().__str__(), "name": name_2, "@type": "SOURCE", "filter": "null",
                 "changes": CHANGES[4],
                 "dataSource": "null", "sourceItemId": datasource, "timeIntervals": "null", "sourceItemName": name_2,
                 "lastModifiedDate": "null"},
                {"id": uuid.uuid4().__str__(), "name": name_3, "@type": "SOURCE", "filter": "null",
                 "changes": CHANGES[2],
                 "dataSource": "null", "sourceItemId": datasource, "timeIntervals": "null", "sourceItemName": name_3,
                 "lastModifiedDate": "null"}
            ]
        edited_projects.append(target_entity_id)
        project_editors.append(user_id)
        return template
    elif target_entity_type == "Datasource":
        template["userId"] = user_id = str(random.choice(datasource_creators))
        created_data_sources_by_user = sorted(
            ",".join([v for k, v in stored_objects[2].items() if k == "{}".format(user_id)]).split(','))
        template["targetEntityId"] = target_entity_id = str(random.choice(created_data_sources_by_user))
        edited_datasources.append(target_entity_id)
        datasource_editors.append(user_id)
        return template
    elif target_entity_type == "Connection":
        template["userId"] = user_id = str(random.choice(connection_creators))
        created_connections_by_user = sorted(
            ",".join([v for k, v in stored_objects[3].items() if k == "{}".format(user_id)]).split(','))
        template["targetEntityId"] = target_entity_id = str(random.choice(created_connections_by_user))
        edited_connections.append(target_entity_id)
        connection_editors.append(user_id)
        return template


def popularity_items(stored_objects, shared_data_sources, shareders, liked_data_sources, likers,
                     subscribed_data_sources, subscribers,
                     recommended_data_sourced, recommenders, duplicated_data_sources, duplicaters,
                     liked_projects, project_likers, project_shareders, shared_projects, shared_connection,
                     connection_shareders, subscribed_projects, project_subscribers, unsubscribed_projects,
                     project_unsubscribers, recommnded_projects, project_recommenders, duplicated_projects,
                     project_duplicators, disliked_projects, project_dislikers, unshared_projects, project_unshareders,
                     unsubscribed_data_sources, unsubscribers, unshared_data_sources, unshareders, unshared_connection,
                     disliked_data_sources, dislikers, connection_unshareders, session, stored_groups,
                     template=TEMPLATE):
    template["eventTime"] = event_time()
    template["targetEntityType"] = target_entity_type = \
        random.choices(UI_TRG_ENTITY_TYPE, UI_TRG_ENTITY_IDS_WEIGHTS)[0]
    stored_users = sorted(",".join([v for k, v in stored_objects[0].items()]).split(','))
    stored_projects = sorted(",".join([v for k, v in stored_objects[1].items()]).split(','))
    stored_data_sources = sorted(",".join([v for k, v in stored_objects[2].items()]).split(','))
    project_creators = sorted(",".join([k for k, v in stored_objects[1].items()]).split(','))
    datasource_creators = sorted(",".join([k for k, v in stored_objects[2].items()]).split(','))
    connection_creators = sorted(",".join([k for k, v in stored_objects[3].items()]).split(','))
    if target_entity_type == "Project":
        template["event"] = event_type = random.choices(UI_EVENTS, UI_EVENTS_WEIGHTS)[0]
        template["userId"] = user_id = str(random.choice(stored_users))
        template["targetEntityId"] = target_entity_id = str(random.choice(list(set(stored_projects).difference(
            set(sorted(",".join([v for k, v in stored_objects[1].items() if k == "{}".format(user_id)]).split(',')))))))
        template["properties"] = {}
        if event_type == "Subscribe":
            subscribed_projects.append(target_entity_id)
            project_subscribers.append(user_id)
        elif event_type == "Unsubscribe":
            event_objects = cassandra__event_objects(session, "Subscribe")
            project_event_creators = sorted(set(",".join([v for k, v in event_objects[1].items()]).split(',')))
            template["userId"] = user_id = str(random.choice(project_event_creators))
            project_events_created_by_user = sorted(
                set(",".join([k for k, v in event_objects[1].items() if "{}".format(user_id) in v]).split(',')))
            template["targetEntityId"] = target_entity_id = str(random.choice(project_events_created_by_user))
            unsubscribed_projects.append(target_entity_id)
            project_unsubscribers.append(user_id)
        elif event_type == "Recommend":
            recommnded_projects.append(target_entity_id)
            project_recommenders.append(user_id)
        elif event_type == "Duplicate":
            duplicated_projects.append(target_entity_id)
            project_duplicators.append(user_id)
        elif event_type == "Like":
            liked_projects.append(target_entity_id)
            project_likers.append(user_id)
        elif event_type == "Dislike":
            event_objects = cassandra__event_objects(session, "Like")
            project_event_creators = sorted(set(",".join([v for k, v in event_objects[1].items()]).split(',')))
            template["userId"] = user_id = str(random.choice(project_event_creators))
            project_events_created_by_user = sorted(
                set(",".join([k for k, v in event_objects[1].items() if "{}".format(user_id) in v]).split(',')))
            template["targetEntityId"] = target_entity_id = str(random.choice(project_events_created_by_user))
            disliked_projects.append(target_entity_id)
            project_dislikers.append(user_id)
        elif event_type == "Share":
            template["userId"] = user_id = str(random.choice(project_creators))
            template["targetEntityId"] = target_entity_id = str(
                random.choice(sorted(
                    ",".join([v for k, v in stored_objects[1].items() if k == "{}".format(user_id)]).split(','))))
            template["properties"] = properties = {}
            r = random.choice(range(10))
            users = stored_users
            while user_id not in users:
                template["userId"] = user_id = str(random.choice(datasource_creators))
            if r < 5:
                users.remove(user_id)
                user = str(random.choice(users))
                properties["users"] = "{}".format(user)
                users.append(user_id)
            elif r == 5:
                users.remove(user_id)
                user = str(random.choice(users))
                properties["users"] = "{}".format(user)
                groups = (stored_groups[int("{}".format(random.randint(0, 10)))])
                properties["groups"] = "{}".format(groups)
                users.append(user_id)
            elif r == 9:
                users.remove(user_id)
                user_1 = str(random.choice(users))
                users.remove(user_1)
                user_2 = str(random.choice(users))
                users.remove(user_2)
                user_3 = str(random.choice(users))
                properties["users"] = "{},{},{}".format(user_1, user_2, user_3)
                users.append(user_id)
                users.append(user_1)
                users.append(user_2)
                users.append(user_3)
            elif r == 10:
                users.remove(user_id)
                user_1 = str(random.choice(users))
                users.remove(user_1)
                user_2 = str(random.choice(users))
                users.remove(user_2)
                user_3 = str(random.choice(users))
                properties["users"] = "{},{},{}".format(user_1, user_2, user_3)
                groups = (stored_groups[int("{}".format(random.randint(0, 10)))])
                properties["groups"] = "{}".format(groups)
                users.append(user_id)
                users.append(user_1)
                users.append(user_2)
                users.append(user_3)
            if 5 < r < 9:
                groups = (stored_groups[int("{}".format(random.randint(0, 10)))])
                properties["groups"] = "{}".format(groups)
            shared_projects.append(target_entity_id)
            project_shareders.append(user_id)
        elif event_type == "Unshare":
            event_objects = cassandra__event_objects(session, "Share")
            project_event_creators = sorted(set(",".join([v for k, v in event_objects[1].items()]).split(',')))
            template["userId"] = user_id = str(random.choice(project_event_creators))
            project_events_created_by_user = sorted(
                set(",".join([k for k, v in event_objects[1].items() if "{}".format(user_id) in v]).split(',')))
            template["targetEntityId"] = target_entity_id = str(random.choice(project_events_created_by_user))
            template["properties"] = properties = {}
            r = random.choice(range(10))
            users = stored_users
            while user_id not in users:
                template["userId"] = user_id = str(random.choice(project_event_creators))
            if r < 5:
                users.remove(user_id)
                user = str(random.choice(users))
                properties["users"] = "{}".format(user)
                users.append(user_id)
            elif r == 5:
                users.remove(user_id)
                user = str(random.choice(users))
                properties["users"] = "{}".format(user)
                groups = (stored_groups[int("{}".format(random.randint(0, 10)))])
                properties["groups"] = "{}".format(groups)
                users.append(user_id)
            elif r == 9:
                users.remove(user_id)
                user_1 = str(random.choice(users))
                users.remove(user_1)
                user_2 = str(random.choice(users))
                users.remove(user_2)
                user_3 = str(random.choice(users))
                properties["users"] = "{},{},{}".format(user_1, user_2, user_3)
                users.append(user_id)
                users.append(user_1)
                users.append(user_2)
                users.append(user_3)
            elif r == 10:
                users.remove(user_id)
                user_1 = str(random.choice(users))
                users.remove(user_1)
                user_2 = str(random.choice(users))
                users.remove(user_2)
                user_3 = str(random.choice(users))
                properties["users"] = "{},{},{}".format(user_1, user_2, user_3)
                groups = (stored_groups[int("{}".format(random.randint(0, 10)))])
                properties["groups"] = "{}".format(groups)
                users.append(user_id)
                users.append(user_1)
                users.append(user_2)
                users.append(user_3)
            if 5 < r < 9:
                groups = (stored_groups[int("{}".format(random.randint(0, 10)))])
                properties["groups"] = "{}".format(groups)
            unshared_projects.append(target_entity_id)
            project_unshareders.append(user_id)
        return template
    elif target_entity_type == "Connection":
        template["event"] = event_type = random.choices(["Share", "Unshare"], [5, 1])[0]
        if event_type == "Share":
            template["userId"] = user_id = str(random.choice(connection_creators))
            template["targetEntityId"] = target_entity_id = str(random.choice(
                sorted(",".join([v for k, v in stored_objects[3].items() if k == "{}".format(user_id)]).split(','))))
            template["properties"] = properties = {}
            r = random.choice(range(10))
            users = stored_users
            while user_id not in users:
                template["userId"] = user_id = str(random.choice(datasource_creators))
            if r < 5:
                users.remove(user_id)
                user = str(random.choice(users))
                properties["users"] = "{}".format(user)
                users.append(user_id)
            elif r == 5:
                users.remove(user_id)
                user = str(random.choice(users))
                properties["users"] = "{}".format(user)
                groups = (stored_groups[int("{}".format(random.randint(0, 10)))])
                properties["groups"] = "{}".format(groups)
                users.append(user_id)
            elif r == 9:
                users.remove(user_id)
                user_1 = str(random.choice(users))
                users.remove(user_1)
                user_2 = str(random.choice(users))
                users.remove(user_2)
                user_3 = str(random.choice(users))
                properties["users"] = "{},{},{}".format(user_1, user_2, user_3)
                users.append(user_id)
                users.append(user_1)
                users.append(user_2)
                users.append(user_3)
            elif r == 10:
                users.remove(user_id)
                user_1 = str(random.choice(users))
                users.remove(user_1)
                user_2 = str(random.choice(users))
                users.remove(user_2)
                user_3 = str(random.choice(users))
                properties["users"] = "{},{},{}".format(user_1, user_2, user_3)
                groups = (stored_groups[int("{}".format(random.randint(0, 10)))])
                properties["groups"] = "{}".format(groups)
                users.append(user_id)
                users.append(user_1)
                users.append(user_2)
                users.append(user_3)
            if 5 < r < 9:
                groups = (stored_groups[int("{}".format(random.randint(0, 10)))])
                properties["groups"] = "{}".format(groups)
            shared_connection.append(target_entity_id)
            connection_shareders.append(user_id)
        elif event_type == "Unshare":
            event_objects = cassandra__event_objects(session, "Share")
            connection_event_creators = sorted(set(",".join([v for k, v in event_objects[3].items()]).split(',')))
            template["userId"] = user_id = str(random.choice(connection_event_creators))
            connection_events_created_by_user = sorted(
                ",".join([v for k, v in stored_objects[3].items() if k == "{}".format(user_id)]).split(','))
            template["targetEntityId"] = target_entity_id = str(random.choice(connection_events_created_by_user))
            template["properties"] = properties = {}
            r = random.choice(range(10))
            users = stored_users
            while user_id not in users:
                template["userId"] = user_id = str(random.choice(connection_event_creators))
            if r < 5:
                users.remove(user_id)
                user = str(random.choice(users))
                properties["users"] = "{}".format(user)
                users.append(user_id)
            elif r == 5:
                users.remove(user_id)
                user = str(random.choice(users))
                properties["users"] = "{}".format(user)
                groups = (stored_groups[int("{}".format(random.randint(0, 10)))])
                properties["groups"] = "{}".format(groups)
                users.append(user_id)
            elif r == 9:
                users.remove(user_id)
                user_1 = str(random.choice(users))
                users.remove(user_1)
                user_2 = str(random.choice(users))
                users.remove(user_2)
                user_3 = str(random.choice(users))
                properties["users"] = "{},{},{}".format(user_1, user_2, user_3)
                users.append(user_id)
                users.append(user_1)
                users.append(user_2)
                users.append(user_3)
            elif r == 10:
                users.remove(user_id)
                user_1 = str(random.choice(users))
                users.remove(user_1)
                user_2 = str(random.choice(users))
                users.remove(user_2)
                user_3 = str(random.choice(users))
                properties["users"] = "{},{},{}".format(user_1, user_2, user_3)
                groups = (stored_groups[int("{}".format(random.randint(0, 10)))])
                properties["groups"] = "{}".format(groups)
                users.append(user_id)
                users.append(user_1)
                users.append(user_2)
                users.append(user_3)
            if 5 < r < 9:
                groups = (stored_groups[int("{}".format(random.randint(0, 10)))])
                properties["groups"] = "{}".format(groups)
            unshared_connection.append(target_entity_id)
            connection_unshareders.append(user_id)
        return template
    template["event"] = event_type = random.choices(UI_EVENTS, UI_EVENTS_WEIGHTS)[0]
    template["userId"] = user_id = str(random.choice(stored_users))
    template["targetEntityId"] = target_entity_id = str(random.choice(list(set(stored_data_sources).difference(
        set(sorted(",".join([v for k, v in stored_objects[2].items() if k == "{}".format(user_id)]).split(',')))))))
    template["properties"] = {}
    if event_type == "Share":
        template["userId"] = user_id = str(random.choice(datasource_creators))
        template["targetEntityId"] = target_entity_id = str(
            random.choice(
                sorted(",".join([v for k, v in stored_objects[2].items() if k == "{}".format(user_id)]).split(','))))
        template["properties"] = properties = {}
        r = random.choice(range(10))
        users = [k for k in stored_users]
        while user_id not in users:
            template["userId"] = user_id = str(random.choice(datasource_creators))
        if r < 5:
            users.remove(user_id)
            user = str(random.choice(users))
            properties["users"] = "{}".format(user)
            users.append(user_id)
        elif r == 5:
            users.remove(user_id)
            user = str(random.choice(users))
            properties["users"] = "{}".format(user)
            groups = (stored_groups[int("{}".format(random.randint(0, 10)))])
            properties["groups"] = "{}".format(groups)
            users.append(user_id)
        elif r == 9:
            users.remove(user_id)
            user_1 = str(random.choice(users))
            users.remove(user_1)
            user_2 = str(random.choice(users))
            users.remove(user_2)
            user_3 = str(random.choice(users))
            properties["users"] = "{},{},{}".format(user_1, user_2, user_3)
            users.append(user_id)
            users.append(user_1)
            users.append(user_2)
            users.append(user_3)
        elif r == 10:
            users.remove(user_id)
            user_1 = str(random.choice(users))
            users.remove(user_1)
            user_2 = str(random.choice(users))
            users.remove(user_2)
            user_3 = str(random.choice(users))
            properties["users"] = "{},{},{}".format(user_1, user_2, user_3)
            groups = (stored_groups[int("{}".format(random.randint(0, 10)))])
            properties["groups"] = "{}".format(groups)
            users.append(user_id)
            users.append(user_1)
            users.append(user_2)
            users.append(user_3)
        if 5 < r < 9:
            groups = (stored_groups[int("{}".format(random.randint(0, 10)))])
            properties["groups"] = "{}".format(groups)
        shared_data_sources.append(target_entity_id)
        shareders.append(user_id)
    elif event_type == "Unshare":
        event_objects = cassandra__event_objects(session, "Share")
        datasource_event_creators = sorted(set(",".join([v for k, v in event_objects[2].items()]).split(',')))
        template["userId"] = user_id = str(random.choice(datasource_event_creators))
        datasource_events_created_by_user = sorted(
            set(",".join([k for k, v in event_objects[2].items() if "{}".format(user_id) in v]).split(',')))
        template["targetEntityId"] = target_entity_id = str(random.choice(datasource_events_created_by_user))
        template["properties"] = properties = {}
        r = random.choice(range(10))
        users = stored_users
        while user_id not in users:
            template["userId"] = user_id = str(random.choice(datasource_event_creators))
        if r < 5:
            users.remove(user_id)
            user = str(random.choice(users))
            properties["users"] = "{}".format(user)
            users.append(user_id)
        elif r == 5:
            users.remove(user_id)
            user = str(random.choice(users))
            properties["users"] = "{}".format(user)
            groups = (stored_groups[int("{}".format(random.randint(0, 10)))])
            properties["groups"] = "{}".format(groups)
            users.append(user_id)
        elif r == 9:
            users.remove(user_id)
            user_1 = str(random.choice(users))
            users.remove(user_1)
            user_2 = str(random.choice(users))
            users.remove(user_2)
            user_3 = str(random.choice(users))
            properties["users"] = "{},{},{}".format(user_1, user_2, user_3)
            users.append(user_id)
            users.append(user_1)
            users.append(user_2)
            users.append(user_3)
        elif r == 10:
            users.remove(user_id)
            user_1 = str(random.choice(users))
            users.remove(user_1)
            user_2 = str(random.choice(users))
            users.remove(user_2)
            user_3 = str(random.choice(users))
            properties["users"] = "{},{},{}".format(user_1, user_2, user_3)
            groups = (stored_groups[int("{}".format(random.randint(0, 10)))])
            properties["groups"] = "{}".format(groups)
            users.append(user_id)
            users.append(user_1)
            users.append(user_2)
            users.append(user_3)
        if 5 < r < 9:
            groups = (stored_groups[int("{}".format(random.randint(0, 10)))])
            properties["groups"] = "{}".format(groups)
        unshared_data_sources.append(target_entity_id)
        unshareders.append(user_id)
    elif event_type == "Like":
        liked_data_sources.append(target_entity_id)
        likers.append(user_id)
    elif event_type == "Dislike":
        event_objects = cassandra__event_objects(session, "Like")
        data_source_event_creators = sorted(set(",".join([v for k, v in event_objects[2].items()]).split(',')))
        template["userId"] = user_id = str(random.choice(data_source_event_creators))
        data_source_events_created_by_user = sorted(
            set(",".join([k for k, v in event_objects[2].items() if "{}".format(user_id) in v]).split(',')))
        template["targetEntityId"] = target_entity_id = str(random.choice(data_source_events_created_by_user))
        disliked_data_sources.append(target_entity_id)
        dislikers.append(user_id)
    elif event_type == "Subscribe":
        subscribed_data_sources.append(target_entity_id)
        subscribers.append(user_id)
    elif event_type == "Unsubscribe":
        event_objects = cassandra__event_objects(session, "Subscribe")
        data_source_event_creators = sorted(set(",".join([v for k, v in event_objects[2].items()]).split(',')))
        template["userId"] = user_id = str(random.choice(data_source_event_creators))
        data_source_events_created_by_user = sorted(
            set(",".join([k for k, v in event_objects[2].items() if "{}".format(user_id) in v]).split(',')))
        template["targetEntityId"] = target_entity_id = str(random.choice(data_source_events_created_by_user))
        unsubscribed_data_sources.append(target_entity_id)
        unsubscribers.append(user_id)
    elif event_type == "Recommend":
        recommended_data_sourced.append(target_entity_id)
        recommenders.append(user_id)
    elif event_type == "Duplicate":
        duplicated_data_sources.append(target_entity_id)
        duplicaters.append(user_id)
    return template


if __name__ == '__main__':
    main()
