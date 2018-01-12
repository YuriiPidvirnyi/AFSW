import json
import os
import sys

import cassandra
from cassandra.cluster import Cluster, NoHostAvailable
from cassandra.protocol import SyntaxException
from cassandra.query import SimpleStatement

from config import TABLES, INPUT_DIR, VIEWS, INIT_FILENAME
from progress_bar import print_progress


def main():
    session = cassandra_connection()
    # stored_users = cassandra_stored_users(session)
    # print("STORED DISTINCT USERS ({})".format(len(stored_users)), stored_users)
    # for user in stored_users:
    #     print("STORED GROUPS WHERE USER #{} IS A MEMBER>>> ".format(user), cassandra_stored_groups(session, user))
    #     print("CREATED PROJECTS BY USER #{} >>>".format(user), cassandra_stored_projects(session, user))
    #     print("CREATED CONNECTIONS BY USER #{} >>>".format(user), cassandra_stored_connections(session, user))
    #     print("CREATED DATASOURCES BY USER #{} >>>".format(user), cassandra_stored_data_sources(session, user_id=user))
    # print("STORED DISTINCT GROUPS >>> ", cassandra_stored_groups(session))
    # stored_projects = cassandra_stored_projects(session)
    # print("STORED DISTINCT PROJECTS >>> ", stored_projects)
    # for project in stored_projects:
    #     print("STORED DATASOURCES BY PROJECT #{} >>>".format(project),
    #           cassandra_stored_data_sources(session, project_id=project))
    # print("STORED DISTINCT CONNECTIONS >>> ", cassandra_stored_connections(session))
    # print("STORED DISTINCT DATASOURCES >>> ", cassandra_stored_data_sources(session))
    # drop_keyspace(session)
    # create_keyspace(session)
    # create_tables(session)
    # print("STORED PROJECTS DY USER>>> ", cassandra_stored_projects(session, user_id='10910'))
    # print(cassandra_stored_users_in_groups(session, "20000"))
    # print(cassandra_stored_datasources_in_projects(session, project_id="11465", datasource_id=None))
    # print(cassandra_stored_datasources_in_projects(session, project_id=None, datasource_id="15017"))
    # print(cassandra_project_creators(session))
    # print(cassandra_datasource_creators(session))
    # print(cassandra_connection_creators(session))
    # print("CREATED PROJECTS BY USER #{} >>>".format('10012'), cassandra_stored_projects(session, '10012'))
    # print(cassandra_created_objects(session))
    # event_type = "Like"
    # print("cassandra_created_objects", cassandra_created_objects(session))
    stored_objects = cassandra_created_objects(session)
    stored_users = sorted(",".join([v for k, v in stored_objects[0].items()]).split(','))
    stored_projects = sorted(",".join([v for k, v in stored_objects[1].items()]).split(','))
    stored_data_sources = sorted(",".join([v for k, v in stored_objects[2].items()]).split(','))
    stored_connections = sorted(",".join([v for k, v in stored_objects[3].items()]).split(','))
    connection_creators = sorted(",".join([k for k, v in stored_objects[3].items()]).split(','))
    stored_groups = cassandra_stored_groups(session)
    print("{} stored_users: ".format(len(stored_users)), sorted(list(set(stored_users))), "\n")
    print("{} stored_projects: ".format(len(stored_projects)), sorted(list(set(stored_projects))), "\n")
    print("{} stored_data_sources: ".format(len(stored_data_sources)), sorted(list(set(stored_data_sources))), "\n")
    print("{} stored_connections: ".format(len(stored_connections)), sorted(list(set(stored_connections))), "\n")
    print("{} stored_groups: ".format(len(stored_groups)), sorted(list(set(stored_groups))), "\n")
    project_creators = sorted(",".join([k for k, v in stored_objects[1].items()]).split(','))
    datasource_creators = sorted(",".join([k for k, v in stored_objects[2].items()]).split(','))
    connection_creators = sorted(",".join([k for k, v in stored_objects[3].items()]).split(','))
    print("{} project_creators: ".format(len(project_creators)), sorted(list(set(project_creators))), "\n")
    print("{} datasource_creators: ".format(len(datasource_creators)), sorted(list(set(datasource_creators))), "\n")
    print("{} connection_creators: ".format(len(connection_creators)), sorted(list(set(connection_creators))), "\n")
    event_objects = cassandra__event_objects(session, "Unsubscribe")
    created_data_sources_by_user = sorted(
        ",".join([v for k, v in stored_objects[2].items() if k == "{}".format('10009')]).split(','))
    created_projects_by_user = sorted(
        ",".join([v for k, v in stored_objects[1].items() if k == "{}".format('10009')]).split(','))
    print("created_data_sources_by_user", created_data_sources_by_user)
    print("created_projects_by_user", created_projects_by_user)
    project_events_created_by_user = sorted(
        set(",".join([k for k, v in event_objects[1].items() if v == "{}".format('10009')]).split(',')))
    print("project_events_created_by_user", project_events_created_by_user)

    # print(cassandra__event_objects(session, event_type)[0])
    # print(cassandra__event_objects(session, event_type)[2])
    # print(count_tables(session))
    # truncate_tables(session)
    # event_objects = cassandra__event_objects(session, "Like")
    # project_like_event_creators = sorted(set(",".join([v for k, v in event_objects[1].items()]).split(',')))
    # projects_liked = sorted(set([k for k, v in event_objects[1].items()]))
    # data_source_like_event_creators = sorted(set(",".join([v for k, v in event_objects[2].items()]).split(',')))
    # data_sources_liked = sorted(set([k for k, v in event_objects[2].items()]))
    # print("\n", event_objects[1])
    # print("\n", event_objects[0])
    # print("\nproject_like_event_creators", project_like_event_creators)
    # print("\nprojects_liked", projects_liked)
    # print("\n", event_objects[2])
    # print("\ndata_source_like_event_creators", data_source_like_event_creators)
    # print("\ndata_sources_liked", data_sources_liked)
    # projects_liked_by_euser = sorted(
    #     set(",".join([k for k, v in event_objects[1].items() if "{}".format('10006') in v]).split(',')))
    # data_sources_liked_by_euser = sorted(
    #     set(",".join([k for k, v in event_objects[2].items() if "{}".format('10017') in v]).split(',')))
    # print("\nprojects_liked_by_euser", projects_liked_by_euser)
    # print("\ndata_sources_liked_by_euser", data_sources_liked_by_euser)
    # users_liked_project = sorted(
    #     set(",".join([v for k, v in event_objects[1].items() if k == "{}".format('10046')]).split(',')))
    # print("\nusers_liked_project", users_liked_project)


def cassandra_connection(keyspace="datawatch"):
    cluster = Cluster()
    try:
        session = cluster.connect(keyspace)
        return session
    except NoHostAvailable:
        print("Please inspect cassandra keyspace!")
        sys.exit(1)


def cassandra_created_objects(session):
    statement = SimpleStatement(
        "SELECT target_entity_type, target_entity_id, user_id FROM all_events WHERE event_type='Create' ALLOW FILTERING;")
    users, projects, data_sources, connections = dict(), dict(), dict(), dict()
    try:
        session.execute(statement)
    except cassandra.InvalidRequest as e:
        print(e, "Please run \"init.cql\" in 8) DDL OPERATION")
        sys.exit(1)
    else:
        for row in session.execute(statement):
            if row.target_entity_type == "Project":
                if row.user_id in projects:
                    projects[row.user_id] = projects[row.user_id] + ",{}".format(row.target_entity_id)
                elif row.user_id not in projects:
                    projects[row.user_id] = row.target_entity_id
            elif row.target_entity_type == "Datasource":
                if row.user_id in data_sources:
                    data_sources[row.user_id] = data_sources[row.user_id] + ",{}".format(row.target_entity_id)
                elif row.user_id not in data_sources:
                    data_sources[row.user_id] = row.target_entity_id
            elif row.target_entity_type == "Connection":
                if row.user_id in connections:
                    connections[row.user_id] = connections[row.user_id] + ",{}".format(row.target_entity_id)
                elif row.user_id not in connections:
                    connections[row.user_id] = row.target_entity_id
            elif row.target_entity_type == "User":
                if row.user_id in users:
                    users[row.user_id] = users[row.user_id] + ",{}".format(row.target_entity_id)
                elif row.user_id not in users:
                    users[row.user_id] = row.target_entity_id
        return users, projects, data_sources, connections


def cassandra__event_objects(session, event_type):
    statement = SimpleStatement(
        "SELECT target_entity_type, target_entity_id, user_id FROM all_events WHERE event_type='{}' ALLOW FILTERING;".format(
            event_type))
    users, projects, data_sources, connections = dict(), dict(), dict(), dict()
    for row in session.execute(statement):
        if row.target_entity_type == "Project":
            if row.target_entity_id in projects:
                projects[row.target_entity_id] = projects[row.target_entity_id] + ",{}".format(row.user_id)
            elif row.target_entity_id not in projects:
                projects[row.target_entity_id] = row.user_id
        elif row.target_entity_type == "Datasource":
            if row.target_entity_id in data_sources:
                data_sources[row.target_entity_id] = data_sources[row.target_entity_id] + ",{}".format(row.user_id)
            elif row.target_entity_id not in data_sources:
                data_sources[row.target_entity_id] = row.user_id
        elif row.target_entity_type == "Connection":
            if row.target_entity_id in connections:
                connections[row.target_entity_id] = connections[row.target_entity_id] + ",{}".format(row.user_id)
            elif row.target_entity_id not in connections:
                connections[row.target_entity_id] = row.user_id
        elif row.target_entity_type == "User":
            if row.target_entity_id in users:
                users[row.target_entity_id] = users[row.target_entity_id] + ",{}".format(row.user_id)
            elif row.target_entity_id not in users:
                users[row.target_entity_id] = row.user_id
    return users, projects, data_sources, connections


def cassandra_stored_groups(session, user_id=None):
    if user_id:
        statement = SimpleStatement(
            "SELECT groups FROM userprofiles WHERE user_id='{}' ALLOW FILTERING;".format(user_id))
        for user_row in session.execute(statement):
            stored_groups = user_row.groups
            stored_groups_by_user = ",".join(stored_groups)
            return stored_groups_by_user
    else:
        statement = SimpleStatement("SELECT groups FROM userprofiles;")
        groups = []
        for group_by_user in session.execute(statement):
            stored_groups_by_user = group_by_user.groups
            for group in stored_groups_by_user:
                groups.append(group)
        stored_groups = sorted(list(set(groups)))
        return stored_groups


def cassandra_stored_users_in_groups(session, group_id):
    statement = SimpleStatement(
        "SELECT JSON user_id, groups FROM userprofiles;".format(group_id))
    users_in_group = []
    for row in session.execute(statement):
        row_dict = json.loads(row.json)
        if group_id in row_dict["groups"]:
            users_in_group.append(row_dict["user_id"])
    users_in_group = sorted(list(set(users_in_group)))
    return users_in_group


def cassandra_stored_datasources_in_projects(session, project_id=None, datasource_id=None):
    if project_id:
        statement = SimpleStatement(
            "SELECT datasources FROM projects WHERE project_id='{}';".format(project_id))
        for row in session.execute(statement):
            try:
                datasources_in_project = list(row.datasources)
            except TypeError:
                datasources_in_project = []
            return datasources_in_project
        else:
            return ''
    elif datasource_id:
        statement = SimpleStatement(
            "SELECT JSON project_id, datasources FROM projects;")
        datasource_in_projects = []
        for row in session.execute(statement):
            row_dict = json.loads(row.json)
            if row_dict["datasources"] and datasource_id in row_dict["datasources"]:
                datasource_in_projects.append(row_dict["project_id"])
        datasource_in_projects = sorted(list(set(datasource_in_projects)))
        return datasource_in_projects


def cassandra_project_creators(session):
    statement = SimpleStatement(
        "SELECT user_id FROM all_events WHERE event_type='Create' AND target_entity_type='Project' ALLOW FILTERING;")
    p_creators = []
    for row in session.execute(statement):
        p_creators.append(row.user_id)
    p_creators = sorted(list(set(p_creators)))
    return p_creators


def cassandra_datasource_creators(session):
    statement = SimpleStatement(
        "SELECT user_id FROM all_events WHERE event_type='Create' AND target_entity_type='Datasource' ALLOW FILTERING;")
    d_creators = []
    for row in session.execute(statement):
        d_creators.append(row.user_id)
    d_creators = sorted(list(set(d_creators)))
    return d_creators


def cassandra_connection_creators(session):
    statement = SimpleStatement(
        "SELECT user_id FROM all_events WHERE event_type='Create' AND target_entity_type='Connection' ALLOW FILTERING;")
    c_creators = []
    for row in session.execute(statement):
        c_creators.append(row.user_id)
    c_creators = sorted(list(set(c_creators)))
    return c_creators


def cassandra_stored_projects(session, user_id=None):
    statement = SimpleStatement("SELECT target_entity_id FROM all_events WHERE event_type='Create' AND\
     target_entity_type='Project' AND user_id='{}' ALLOW FILTERING;".format(user_id))
    if user_id:
        stored_projects = []
        for user_row in session.execute(statement):
            stored_projects.append(user_row.target_entity_id)
        stored_projects_by_user = sorted(list(set(stored_projects)))
        if len(stored_projects_by_user) > 1:
            return ",".join(stored_projects_by_user)
        elif len(stored_projects_by_user) == 1:
            return stored_projects_by_user[0]
        else:
            return ""
    else:
        statement = SimpleStatement(
            "SELECT target_entity_id FROM all_events WHERE event_type='Create' AND target_entity_type='Project'\
             ALLOW FILTERING;")
        projects = []
        for user_row in session.execute(statement):
            projects.append(user_row.target_entity_id)
        stored_projects = sorted(list(set(projects)))
        return stored_projects


def cassandra_stored_data_sources(session, project_id=None, user_id=None):
    if project_id:
        statement = SimpleStatement(
            "SELECT datasources FROM projects WHERE project_id='{}' ALLOW FILTERING;".format(project_id))
        for project_row in session.execute(statement):
            stored_datasources = project_row.datasources
            if stored_datasources is not None:
                stored_datasources_by_project = ",".join(stored_datasources)
                return stored_datasources_by_project
            else:
                return ""
    if user_id:
        statement = SimpleStatement(
            "SELECT target_entity_id FROM all_events WHERE event_type='Create' AND target_entity_type='Datasource' AND user_id='{}' ALLOW FILTERING;".format(
                user_id))
        stored_datasources = []
        for user_row in session.execute(statement):
            stored_datasources.append(user_row.target_entity_id)
        stored_datasources_by_user = sorted(list(set(stored_datasources)))
        if len(stored_datasources_by_user) > 1:
            return ",".join(stored_datasources_by_user)
        elif len(stored_datasources_by_user) == 1:
            return stored_datasources_by_user[0]
        else:
            return ""
    elif not project_id and not user_id:
        statement = SimpleStatement(
            "SELECT target_entity_id FROM all_events WHERE event_type='Create' AND target_entity_type='Datasource'\
             ALLOW FILTERING;")
        datasources = []
        for user_row in session.execute(statement):
            datasource = user_row.target_entity_id
            datasources.append(datasource)
        stored_datasources = sorted(list(set(datasources)))
        return stored_datasources


def cassandra_stored_connections(session, user_id=None):
    statement = SimpleStatement("SELECT target_entity_id FROM all_events WHERE event_type='Create' AND\
     target_entity_type='Connection' AND user_id='{}' ALLOW FILTERING;".format(user_id))
    if user_id:
        stored_connections = []
        for user_row in session.execute(statement):
            stored_connections.append(user_row.target_entity_id)
        stored_connections_by_user = sorted(list(set(stored_connections)))
        if len(stored_connections_by_user) > 1:
            return ",".join(stored_connections_by_user)
        elif len(stored_connections_by_user) == 1:
            return stored_connections_by_user[0]
        else:
            return ""
    else:
        statement = SimpleStatement(
            "SELECT target_entity_id FROM all_events WHERE event_type='Create' AND target_entity_type='Project'\
             ALLOW FILTERING;")
        connections = []
        for user_row in session.execute(statement):
            connections.append(user_row.target_entity_id)
        stored_connections = sorted(list(set(connections)))
        return stored_connections


def truncate_tables(session, tables=TABLES):
    print_progress(0, 1)
    i = 0
    for table in tables:
        try:
            statement = SimpleStatement("TRUNCATE {};".format(table))
            session.execute(statement)
            print_progress(i + 1, len(tables), prefix="Truncating: {}".format(table),
                           suffix="Truncated")
            i += 1
        except:
            pass


def truncate_table(session, table):
    statement = SimpleStatement("TRUNCATE {};".format(table))
    session.execute(statement)


def count_tables(session, tables=TABLES, views=VIEWS, table_name=None):
    if table_name:
        statement = SimpleStatement("SELECT COUNT(*) FROM {};".format(table_name))
        count = session.execute(statement).was_applied
        return count
    else:
        t_results = []
        for table in tables:
            statement = SimpleStatement("SELECT COUNT(*) FROM {};".format(table))
            count = session.execute(statement)
            t_results.append(count.was_applied)
        t_counts = dict(zip(tables, t_results))
        v_results = []
        for view in views:
            statement = SimpleStatement("SELECT COUNT(*) FROM {};".format(view))
            count = session.execute(statement)
            v_results.append(count.was_applied)
        v_counts = dict(zip(views, v_results))
        return t_counts, v_counts


def drop_keyspace(session, keyspace="datawatch"):
    statement = SimpleStatement("DROP KEYSPACE {};".format(keyspace))
    result = session.execute(statement)
    return result


def create_keyspace(keyspace=None):
    session = Cluster().connect()
    if not keyspace:
        try:
            statement = SimpleStatement(
                "CREATE KEYSPACE datawatch WITH REPLICATION = { 'class' : 'NetworkTopologyStrategy', 'datacenter1' : 1 };")
            result = session.execute(statement)
            # print("Creating \"datawatch\" keyspace...")
            return result
        except cassandra.AlreadyExists as e:
            print("\n>>> ", e)
            return None
    else:
        try:
            statement = SimpleStatement(
                "CREATE KEYSPACE {}".format(
                    keyspace) + " WITH REPLICATION = { 'class' : 'NetworkTopologyStrategy', 'datacenter1' : 1 };")
            result = session.execute(statement)
            # print("Creating \"{}\" keyspace...".format(keyspace))
            return result
        except cassandra.AlreadyExists as e:
            print("\n>>> ", e)
            return None


def create_tables(session, init_filename=INIT_FILENAME):
    base_dir = "\\".join(os.path.abspath(INPUT_DIR).split("\\")[:-1])
    _input = os.path.join(base_dir, INPUT_DIR)
    if not os.path.exists(_input):
        input_dir = "backend\input"
        _input = os.path.join(base_dir, input_dir)
        if not os.path.exists(_input):
            os.mkdir(_input)
    init = open(os.path.join(_input, init_filename), "r")
    init_file = init.read()
    init.close()
    init_commands = init_file.split(";")
    try:
        i = 0
        for command in init_commands[2:]:
            statement = SimpleStatement(command.strip())
            try:
                result = session.execute(statement)
                print_progress(i + 1, len(init_commands[3:]), prefix="Creating: ", suffix="Created")
                i += 1
            except cassandra.AlreadyExists as e:
                print("\n>>> ", e)
    except SyntaxException as e:
        # print("\n>>> ", e)
        pass


if __name__ == '__main__':
    main()
    # pass
