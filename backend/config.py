INPUT_DIR = "input"
OUTPUT_DIR = "output"
INIT_FILENAME = "init.cql"

TEMPLATE = {"event": "", "eventTime": "", "userId": "", "targetEntityType": "", "targetEntityId": "", "properties": {}}

UU_EVENTS = ["Like", "Follow", "Unfollow", "Recommend"]  # "Dislike"
UU_EVENTS_WEIGHTS = [10, 6, 0.5, 3]  # 2

UI_EVENTS = ["Share", "Unshare", "Like", "Dislike", "Subscribe", "Unsubscribe", "Recommend", "Duplicate"]
UI_EVENTS_WEIGHTS = [7, 0.1, 10, 0.2, 8, 0.09, 4, 5]

UI_TRG_ENTITY_TYPE = ["Project", "Datasource", "Connection"]
UI_TRG_ENTITY_IDS_WEIGHTS = [10, 15, 1]

CHANGES = [[{"hide": "true", "@type": "HIDE_COLUMN", "version": 1, "columnName": "hire", "previewMode": "false",
             "createNewColumn": "false", "removeOriginalColumn": "false"},
            {"@type": "REMOVE_COLUMN", "version": 1, "columnName": "gender(1)", "previewMode": "false",
             "createNewColumn": "false", "removeOriginalColumn": "false"},
            {"@type": "FROM_LEFT_SEPARATOR_SPLIT", "version": 2, "delimiter": "-", "columnName": "birth_date",
             "previewMode": "false", "extendedMode": "false", "createNewColumn": "false", "newColumnsCount": 3,
             "selectedColumns": [0, 1, 2], "removeOriginalColumn": "true"},
            {"@type": "RENAME_COLUMN", "version": 1, "columnName": "birth_date1", "previewMode": "false",
             "newColumnName": "birth_year", "createNewColumn": "false", "removeOriginalColumn": "false"},
            {"@type": "COLUMN_TYPE_CONVERT", "format": "null", "version": 1, "columnName": "birth_year",
             "columnType": "NUMERIC", "previewMode": "false", "phraseFactors": "null", "createNewColumn": "false",
             "conversionOptions": "null", "removeOriginalColumn": "false"},
            {"@type": "DUPLICATE_COLUMN", "version": 1, "columnName": "gender", "previewMode": "false",
             "createNewColumn": "false", "removeOriginalColumn": "false"}], [
               {"hide": "true", "@type": "HIDE_COLUMN", "version": 1, "columnName": "hire", "previewMode": "false",
                "createNewColumn": "false", "removeOriginalColumn": "false"},
               {"@type": "REMOVE_COLUMN", "version": 1, "columnName": "gender(1)", "previewMode": "false",
                "createNewColumn": "false", "removeOriginalColumn": "false"},
               {"@type": "FROM_LEFT_SEPARATOR_SPLIT", "version": 2, "delimiter": "-", "columnName": "birth_date",
                "previewMode": "false", "extendedMode": "false", "createNewColumn": "false", "newColumnsCount": 3,
                "selectedColumns": [0, 1, 2], "removeOriginalColumn": "true"},
               {"@type": "RENAME_COLUMN", "version": 1, "columnName": "birth_date1", "previewMode": "false",
                "newColumnName": "birth_year", "createNewColumn": "false", "removeOriginalColumn": "false"},
               {"@type": "COLUMN_TYPE_CONVERT", "format": "null", "version": 1, "columnName": "birth_year",
                "columnType": "NUMERIC", "previewMode": "false", "phraseFactors": "null", "createNewColumn": "false",
                "conversionOptions": "null", "removeOriginalColumn": "false"}], [
               {"hide": "true", "@type": "HIDE_COLUMN", "version": 1, "columnName": "hire", "previewMode": "false",
                "createNewColumn": "false", "removeOriginalColumn": "false"},
               {"@type": "REMOVE_COLUMN", "version": 1, "columnName": "gender(1)", "previewMode": "false",
                "createNewColumn": "false", "removeOriginalColumn": "false"},
               {"@type": "FROM_LEFT_SEPARATOR_SPLIT", "version": 2, "delimiter": "-", "columnName": "birth_date",
                "previewMode": "false", "extendedMode": "false", "createNewColumn": "false", "newColumnsCount": 3,
                "selectedColumns": [0, 1, 2], "removeOriginalColumn": "true"},
               {"@type": "RENAME_COLUMN", "version": 1, "columnName": "birth_date1", "previewMode": "false",
                "newColumnName": "birth_year", "createNewColumn": "false", "removeOriginalColumn": "false"}], [
               {"hide": "true", "@type": "HIDE_COLUMN", "version": 1, "columnName": "hire", "previewMode": "false",
                "createNewColumn": "false", "removeOriginalColumn": "false"},
               {"@type": "REMOVE_COLUMN", "version": 1, "columnName": "gender(1)", "previewMode": "false",
                "createNewColumn": "false", "removeOriginalColumn": "false"},
               {"@type": "FROM_LEFT_SEPARATOR_SPLIT", "version": 2, "delimiter": "-", "columnName": "birth_date",
                "previewMode": "false", "extendedMode": "false", "createNewColumn": "false", "newColumnsCount": 3,
                "selectedColumns": [0, 1, 2], "removeOriginalColumn": "true"}], [
               {"hide": "true", "@type": "HIDE_COLUMN", "version": 1, "columnName": "hire", "previewMode": "false",
                "createNewColumn": "false", "removeOriginalColumn": "false"},
               {"@type": "REMOVE_COLUMN", "version": 1, "columnName": "gender(1)", "previewMode": "false",
                "createNewColumn": "false", "removeOriginalColumn": "false"}], [
               {"hide": "true", "@type": "HIDE_COLUMN", "version": 1, "columnName": "hire", "previewMode": "false",
                "createNewColumn": "false", "removeOriginalColumn": "false"}]]

NAMES = ["departments", "employees", "dept_manager", "dept_emp", "titles", "salaries"]

TABLES = ["userprofiles", "mba_recommendations", "events", "als_user_recommendations", "group_user_popularities",
          "projects", "item_ratings", "next_change_recommendations", "cassandra_migration_version",
          "recommendation_history", "cassandra_migration_version_counts"]
VIEWS = ["events_from_user", "events_by_item", "all_events"]

URI = "http://localhost"
PORT = ":9091"
RESOURCES = dict(
    put_event="/event",
    get_als=["/users-als", "user.id"],
    get_gup=["/users-popularity", "groups"],
    get_mba=["/mba-datasource", "datasources"],
    get_ir=["/item-rating", "user.id", "items"],
    get_likes=["/item-likes", "user.id", "items"],
    get_subscr=["/subscriptions", "user.id"],
    get_followers=["/followers", "users"],
    get_shared=["/shared-items", "user.id", "groups", "size"],
    get_updates=["/recent-updates", "user.id", "groups", "size"],
    get_activities=["/afeed", "user.id", "groups", "size"]
)

REQUEST_TYPES = ["COLLABORATIVE FILTERING", "GROUP USER POPULARITY", "MARKET BASKET ANALYSIS", "ITEM RATING",
                 "RETURN TO MAIN MENU", "EXIT"]
SOCIAL_REQUEST_TYPES = ["LIKES", "SUBSCRIPTIONS", "FOLLOWERS", "SHARED ITEMS", "RECENT UPDATES", "NOTIFICATIONS",
                        "RETURN TO MAIN MENU", "EXIT"]
TABLES_OPTIONS = ["USERPROFILES", "MBA_RECOMMENDATIONS", "EVENTS", "events_from_user", "events_by_item",
                  "ALS_USER_RECOMMENDATIONS", "GROUP_USER_POPULARITIES", "PROJECTS", "ITEM_RATINGS",
                  "NEXT_CHANGE_RECOMMENDATIONS", "COUNT ALL", "RETURN TO MAIN MENU", "EXIT"]

GET_STATISTIC = ["RETRIEVE STORED USERS", "RETRIEVE STORED GROUPS", "RETRIEVE STORED USERS IN GROUP",
                 "RETRIEVE PROJECT CREATORS", "RETRIEVE DATA SOURCE CREATORS", "RETRIEVE CONNECTION CREATORS",
                 "RETRIEVE STORED PROJECTS", "RETRIEVE STORED DATA SOURCES", "RETRIEVE STORED CONNECTIONS",
                 "RETRIEVE DATA SOURCES FROM THE PROJECT", "RETRIEVE PROJECTS WHERE DATA SOURCE WAS ADDED",
                 "RETURN TO MAIN MENU", "EXIT"]
DDL_OPTIONS = ["TRUNCATE TABLES", "DROP KEYSPACE", "CREATE KEYSPACE", "CREATE TABLES", "RETURN TO MAIN MENU", "EXIT"]

HEADERS = {
    'content-type': "application/json",
    'cache-control': "no-cache"
}

RUN_OPTIONS = ["FULL FLOW", "USER-USER EVENTS", "USER-ITEMS", "GET RECOMMENDATIONS", "GET SOCIAL COMPONENTS",
               "COUNT TABLES", "GET SOME STATISTIC", "DDL OPERATION", "EXIT"]
UU_RUN_OPTIONS = ["CREATE USER EVENTS", "EDIT USER EVENTS", "POPULARITY USER EVENTS", "RETURN TO MAIN MENU", "EXIT"]
UI_RUN_OPTIONS = ["CREATE ITEM EVENTS", "ADD TO WORKSPACE EVENT", "EDIT ITEM EVENTS", "POPULARITY ITEM EVENTS",
                  "RETURN TO MAIN MENU", "EXIT"]
FF_RUN_OPTIONS = ["CREATE USER EVENTS", "EDIT USER EVENTS", "POPULARITY USER EVENTS", "CREATE ITEM EVENTS",
                  "ADD TO WORKSPACE EVENT", "EDIT ITEM EVENTS", "POPULARITY ITEM EVENTS"]
