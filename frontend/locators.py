from selenium.webdriver.common.by import By


class BasePageLocators(object):
    PAGE_TITLE = "Monarch Swarm 2017"
    PAGE_HEADER = (By.CSS_SELECTOR, "div.ng-isolate-scope:nth-child(1)")
    PAGE_ALERT_SECTION = (By.CSS_SELECTOR, "div.ng-isolate-scope:nth-child(2)")
    MAIN_PAGE_FOOTER = (By.CSS_SELECTOR, ".main-layout__footer")  # for Library & User
    PAGE_FOOTER = (By.CSS_SELECTOR, ".main-layout__footer")
    LOGO = (By.CSS_SELECTOR, ".base-header__logo")
    LOGO_EXT = (By.CSS_SELECTOR, ".logo")
    LIBRARY_TAB = (By.CSS_SELECTOR, "li.top-menu__item:nth-child(1)")
    CONNECTIONS_TAB = (By.CSS_SELECTOR, "li.top-menu__item:nth-child(3)")
    JOBS_TAB = (By.CSS_SELECTOR, "li.top-menu__item:nth-child(4)")
    USER_MANAGEMENT_TAB = (By.CSS_SELECTOR, "li.top-menu__item:nth-child(5)")
    LIBRARY_TAB_NAME = "Swarm Library"
    CONNECTIONS_TAB_NAME = "Connections"
    JOBS_TAB_NAME = "Jobs"
    USER_MANAGEMENT_TAB_NAME = "User Management"
    NOTIFICATION_BELL = (By.CSS_SELECTOR, ".top-controls__icon_notifications")
    NOTIFICATION_BELL_ACTIVE = (By.CSS_SELECTOR, "div.top-controls__item:nth-child(1) >div:nth-child(3)")
    NOTIFICATION_BELL_ICON = (By.CSS_SELECTOR, ".top-controls__icon_notifications>use:nth-child(1)")
    NOTIFICATION_BELL_CLOSED = (By.CSS_SELECTOR, ".top-controls__count")
    NOTIFICATION_BELL_OPENED = (By.CSS_SELECTOR, ".top-controls__count_unread-notifications--open")
    NOTIFICATION_POPUP = (By.CSS_SELECTOR, ".notifications")
    NOTIFICATION_POPUP_NOTIFICATIONS_TITLE = (By.CSS_SELECTOR, ".notifications__title")
    NOTIFICATION_POPUP_MARK_ALL_READ_LINK = (By.CSS_SELECTOR, ".notifications__title-container_mark-all-as-read")
    NOTIFICATION_POPUP_CLOSE_SIGN = (By.CSS_SELECTOR, ".icon-ic_close_black")
    HELP_ICON = (By.CSS_SELECTOR, ".top-controls__icon_help > use:nth-child(1)")
    USER_CIRCLE_ICON = (By.CSS_SELECTOR, ".circle")
    USER_AVATAR = (By.CSS_SELECTOR, ".avatar__placeholder")
    USER_AVATAR_MENU_ICON = (By.CSS_SELECTOR, "svg.icon:nth-child(2) > use:nth-child(1)")
    USER_AVATAR_MENU = (By.CSS_SELECTOR, ".select-menu__items")
    USER_AVATAR_MENU_PROFILE = (By.CSS_SELECTOR, "li.select-menu__item:nth-child(1)")
    USER_AVATAR_MENU_LOGOUT = (By.CSS_SELECTOR, "li.select-menu__item:nth-child(2)")
    USER_AVATAR_MENU_PROFILE_TEXT = "Profile"
    USER_AVATAR_MENU_LOGOUT_TEXT = "Logout"


class LoginPageLocators(object):
    LOGIN_PAGE = (By.CSS_SELECTOR, ".login")
    LOGIN = (By.NAME, "login")
    PASSWORD = (By.NAME, "password")
    SIGN_IN = (By.CSS_SELECTOR, ".button")
    ERROR_MESSAGE_LOGIN = (By.CSS_SELECTOR, ".login-form-input_data_sources-box__error")
    ERROR_MESSAGE_PASSWORD = (By.CSS_SELECTOR, "div.login - form - box__field: nth - child(2) > div:nth - child(2)")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".login-form__error")
    LOGIN_LOGO = (By.CSS_SELECTOR, "svg.icon:nth-child(2)")
    LOGIN_PAGE_GREETING = (By.CSS_SELECTOR, ".login-form__title")
    LOGIN_PAGE_GREETING_TEXT = "Hello! Welcome Back"
    BUILD_INFO = (By.CSS_SELECTOR, ".login-side-right__footer")


class LibraryPageLocators(object):
    LIBRARY_TAB_ACTIVE = (By.CSS_SELECTOR, ".top-menu__link--active")
    # active for nesteed tabs: class_name = "data-page-tabs__tab_active"
    ALL_TAB = (By.CSS_SELECTOR, "div.data-page-tabs__tab:nth-child(1)")
    ALL_TABS_FOOTER = (By.CSS_SELECTOR, ".main-layout__footer>div:nth-child(1)")
    ALL_TAB_ACTIVE = (By.CLASS_NAME, "data-page-tabs__tab_active")
    WORKSPACES_TAB = (By.CSS_SELECTOR, "div.data-page-tabs__tab:nth-child(2)")
    WORKSPACES_TAB_ACTIVE = (By.CLASS_NAME, "data-page-tabs__tab_active")
    DATA_SOURCES_TAB = (By.CSS_SELECTOR, "div.data-page-tabs__tab:nth-child(3)")
    DATA_SOURCES_TAB_ACTIVE = (By.CLASS_NAME, "data-page-tabs__tab_active")
    NEW_BUTTON = (By.CSS_SELECTOR, ".dropdown-in-button")
    NEW_BUTTON_UNCLICKABLE = (By.CSS_SELECTOR, "body>div:nth-child(6)>div:nth-child(1)")
    NEW_BUTTON_TEXT = "New"
    NEW_BUTTON_MENU = (By.CSS_SELECTOR, ".dropdown-base__list")
    ADD_WEB_LINK_TEXT = "Add Web Link"
    ADD_WEB_LINK = (By.CSS_SELECTOR, "li.dropdown-base__list-item:nth-child(3)")
    ADD_WEB_LINK_AFTER_CONN = (By.CSS_SELECTOR, "li.dropdown-base__list-item:nth-child(4)")
    NEW_WORKSPACE = (By.CSS_SELECTOR, "li.dropdown-base__list-item:nth-child(1)")
    NEW_WORKSPACE_TEXT = "New Workspace"
    UPLOAD_LOCAL_FILE = (By.CSS_SELECTOR, "li.dropdown-base__list-item:nth-child(2)")
    UPLOAD_LOCAL_FILE_TEXT = "Upload Local File"
    ADD_FROM_CONNECTION = (By.CSS_SELECTOR, "li.dropdown-base__list-item:nth-child(3)")
    ADD_FROM_CONNECTION_TEXT = "Add from Connection"
    NEW_FOLDER = (By.CSS_SELECTOR, ".main-context-menu__item-name")
    MY_LIBRARY = (By.CSS_SELECTOR, ".bread-crumbs-path__label")
    MY_LIBRARY_TEXT = "My Library"
    TABLE_HEADER = (By.XPATH, "/ html / body / main / div / div[3] / div / div / div / div / section / div / div[1]")
    COLUMN_SET = ('Name', 'Type', 'Shared', 'Curated', 'Liked', 'Creator', 'Subscribed', 'Updated')
    MAIN_TABLE_PLACEHOLDER = (By.CSS_SELECTOR, ".main-table__placeholder")
    MAIN_TABLE_PLACEHOLDER_TEXT = "No Data"
    MAIN_TABLE = (By.CSS_SELECTOR, ".table")
    MAIN_TABLE_HEADER = (By.CSS_SELECTOR, ".table__header")
    MAIN_TABLE_BODY = (By.CSS_SELECTOR, ".table__body")
    FIRST_FOLDER = (By.CSS_SELECTOR, ".main-table__cell-name-name")
    SECOND_FOLDER = (By.CSS_SELECTOR, ".main-table__cell-name-name-wrapper")
    THIRD_FOLDER = (By.CSS_SELECTOR, ".main-table__cell-name-inner-wrapper")
    MAIN_TABLE_NAME = (By.CSS_SELECTOR, "div.table__header-cell:nth-child(2)")
    MAIN_TABLE_TYPE = (By.CSS_SELECTOR, "div.table__header-cell:nth-child(3)")
    MAIN_TABLE_SHARED = (By.CSS_SELECTOR, "div.table__header-cell:nth-child(4)")
    MAIN_TABLE_CURATED = (By.CSS_SELECTOR, "div.table__header-cell:nth-child(5)")
    MAIN_TABLE_LIKED = (By.CSS_SELECTOR, "div.table__header-cell:nth-child(6)")
    MAIN_TABLE_CREATOR = (By.CSS_SELECTOR, "div.table__header-cell:nth-child(7)")
    MAIN_TABLE_SUBSCRIBED = (By.CSS_SELECTOR, "div.table__header-cell:nth-child(8)")
    MAIN_TABLE_UPDATED = (By.CSS_SELECTOR, "div.table__header-cell:nth-child(9)")
    LIBRARY_FOOTER = (By.CSS_SELECTOR, ".main-layout__footer")
    LIBRARY_SEARCH = (By.NAME, "searchLibrary")
    LIBRARY_LEFT_SIDE_SECTION = (By.CSS_SELECTOR, ".main-layout__aside")
    LIBRARY_BODY = (By.CSS_SELECTOR, ".main-layout__body-wrapper")
    LIBRARY_BODY_SECTION_HEADER = (By.CSS_SELECTOR, ".main-layout__header")
    LIBRARY_BODY_SECTION = (By.CSS_SELECTOR, ".main-layout__body")
    # TODO: ADD COUNTERS TO TABLE AND MENUS
    MY_LIBRARY_CSV_FOLDER = (By.CSS_SELECTOR,
                             "div.table__row:nth-child(1)>div:nth-child(2)>div:nth-child(1)>div:nth-child(2)>p:nth-child(1)>span:nth-child(1)")
    MY_LIBRARY_CSV_FOLDER_NAME = "CSV"
    MY_LIBRARY_JSON_FOLDER_NAME = "JSON"
    MY_LIBRARY_XML_FOLDER_NAME = "XML"
    MY_LIBRARY_HTML_FOLDER_NAME = "HTML"
    MY_LIBRARY_EXCEL_FOLDER_NAME = "EXCEL"
    MY_LIBRARY_ACCESS_FOLDER_NAME = "ACCESS"
    ACCESS_FOLDER = (
        By.CSS_SELECTOR, "div.table__row:nth-child(1)>div:nth-child(2)>div:nth-child(1)>div:nth-child(2)")
    EXCEL_FOLDER = (
        By.CSS_SELECTOR, "div.table__row:nth-child(2)>div:nth-child(2)>div:nth-child(1)>div:nth-child(2)")
    HTML_FOLDER = (
        By.CSS_SELECTOR, "div.table__row:nth-child(3)>div:nth-child(2)>div:nth-child(1)>div:nth-child(2)")
    JSON_FOLDER = (
        By.CSS_SELECTOR, "div.table__row:nth-child(4)>div:nth-child(2)>div:nth-child(1)>div:nth-child(2)")
    XML_FOLDER = (
        By.CSS_SELECTOR, "div.table__row:nth-child(5)>div:nth-child(2)>div:nth-child(1)>div:nth-child(2)")
    CSV_ADMIN_FOLDER = (
        By.CSS_SELECTOR, "div.table__row:nth-child(2)>div:nth-child(2)>div:nth-child(1)>div:nth-child(2)")
    INPUT_FOLDER = (By.CSS_SELECTOR, ".form__input-input_data_sources")
    INPUT_WORKSPACE_NAME = (By.TAG_NAME, "input_data_sources")
    ADD_DS_SAVE_BUTTON = (By.CSS_SELECTOR, "button.data-sources-form__button:nth-child(1)")
    ADD_DS_CANCEL_BUTTON = (By.CSS_SELECTOR, "button.data-sources-form__button:nth-child(2)")
    ADD_DS_FORMAT_FIELD = (By.CSS_SELECTOR, ".data-item-form__select-caption-title")
    ADD_DS_DELIMITED_FORMAT = (By.CSS_SELECTOR, "li.data-item-form__select-item:nth-child(2) > span:nth-child(1)")

    EDIT_GRID_ITEM = (
        By.CSS_SELECTOR, "li.main-context-menu__group:nth-child(2)>ul:nth-child(1)>li:nth-child(2)>a:nth-child(2)")

    ADD_DS_TO_WRKS_ICON = (By.CSS_SELECTOR, ".data-preparation-footer-controls__icon")
    ADD_1_DS_TO_WRKS = (By.CSS_SELECTOR,
                        ".aside-add-data-sources>div:nth-child(1)>div:nth-child(1)>div:nth-child(1)>div:nth-child(1)>div:nth-child(1)>div:nth-child(1)>label:nth-child(2)")
    ADD_2_DS_TO_WRKS = (By.CSS_SELECTOR,
                        ".aside-add-data-sources>div:nth-child(2)>div:nth-child(1)>div:nth-child(1)>div:nth-child(1)>div:nth-child(1)>div:nth-child(1)>label:nth-child(2)")
    ADD_3_DS_TO_WRKS = (By.CSS_SELECTOR,
                        ".aside-add-data-sources>div:nth-child(3)>div:nth-child(1)>div:nth-child(1)>div:nth-child(1)>div:nth-child(1)>div:nth-child(1)>label:nth-child(2)")
    OPEN_SELECTED_BUTTON = (By.CSS_SELECTOR, "button.button:nth-child(2)")
    DBA_WORKSPACE = "NewWorkspaceForDBA"
    DBA_WORKSPACE_GRID_CHECK_BOX = (
        By.CSS_SELECTOR, "div.table__row:nth-child(7)>div:nth-child(1)>div:nth-child(1)>label:nth-child(2)")
    DBA_WORKSPACE_GRID_NAME = (By.CSS_SELECTOR,
                               "div.table__row:nth-child(7)>div:nth-child(2)>div:nth-child(1)>div:nth-child(2)>p:nth-child(1)>span:nth-child(1)")
    DBA_WORKSPACE_GRID_TYPE = (By.CSS_SELECTOR, "div.table__row:nth-child(7)>div:nth-child(3)>span:nth-child(1)")
    JXML_WORKSPACE = "NewWorkspaceForJXML"
    JXML_WORKSPACE_GRID_CHECK_BOX = (
        By.CSS_SELECTOR, "div.table__row:nth-child(6)>div:nth-child(1)>div:nth-child(1)>label:nth-child(2)")
    JXML_WORKSPACE_GRID_NAME = (By.CSS_SELECTOR,
                                "div.library-list-page__table-column:nth-child(2)>div:nth-child(1)>div:nth-child(2)>p:nth-child(1)>span:nth-child(1)")
    JXML_WORKSPACE_GRID_TYPE = (By.CSS_SELECTOR, "div.table__row:nth-child(6)>div:nth-child(3)>span:nth-child(1)")
    SAVE_WORKSPACE_MENU = (By.CSS_SELECTOR, ".dropdown-in-button__button")
    SAVE_WORKSPACE_MENU_ADD_WRKS = (By.CSS_SELECTOR, ".button--main")
    SAVE_WORKSPACE = (By.CSS_SELECTOR, "li.dropdown-base__list-item:nth-child(1)")
    SAVE_AND_EXIT_WORKSPACE = (By.CSS_SELECTOR, "li.dropdown-base__list-item:nth-child(2)")
    EXIT_WORKSPACE = (By.CSS_SELECTOR, "li.dropdown-base__list-item:nth-child(3)")


class DashboardPageLocators(object):
    LOGO_ACTIVE = (By.CSS_SELECTOR, ".base-header__logo")
    WELCOME = (By.CSS_SELECTOR, ".dashboard__greet")
    DASHBOARD_GREET = (By.CSS_SELECTOR, ".dashboard__welcome-section > p:nth-child(2)")
    DASHBOARD_GREET_TEXT = "We are thrilled to let you start prepping with Swarm, add your first data source!"
    RECENT_UPDATES = (By.CSS_SELECTOR, ".dashboard__widget_updates > header:nth-child(1) > h2:nth-child(2)")
    RECENT_UPDATES_PLACEHOLDER = (
        By.CSS_SELECTOR, ".dashboard__widget_updates > section:nth-child(2) > div:nth-child(1)")
    SHARED_WITH_ME = (By.XPATH, "/html/body/main/div/div[2]/div/div/div[2]/article/header/h2")
    SHARED_WITH_ME_PLACEHOLDER = (By.XPATH, "/html/body/main/div/div[2]/div/div/div[2]/article/section/div")
    ACTIVITIES_FEED = (By.CSS_SELECTOR, ".dashboard__widget_activity > header:nth-child(1) > h2:nth-child(2)")
    ACTIVITIES_FEED_PLACEHOLDER = (By.CSS_SELECTOR, ".notifications__content")
    GET_STARTED_BUTTON = (By.CSS_SELECTOR, ".button")
    WELCOME_ADMIN_TEXT = "Welcome Administrator!"
    RECENT_UPDATES_NAME = "RECENT UPDATES"
    SHARED_WITH_ME_NAME = "SHARED WITH ME"
    ACTIVITIES_FEED_NAME = "ACTIVITIES FEED"
    RECENT_UPDATES_PLACEHOLDER_TEXT = "No data yet :(\nAdd your first data!"
    SHARED_WITH_ME_PLACEHOLDER_TEXT = "No data yet :(\nAsk someone to share data with you!"
    ACTIVITIES_FEED_PLACEHOLDER_TEXT = "Administrator Administrator has just joined Datawatch Swarm!"
    GET_STARTED_BUTTON_TEXT = "Let’s Get Started!"
    DOC_LINK = (By.CSS_SELECTOR, "a.dashboard__widget_updates")
    DOC_LINK_URL = "http://docs.datawatch.com/"
    DOC_LINK_NAME = "Documentation"
    DOC_LINK_NAME_LOC = (By.CSS_SELECTOR, "a.dashboard__widget_updates > span:nth-child(2)")
    DOC_LINK_TEXT = "Help files and tutorials"
    DOC_LINK_TEXT_LOC = (By.CSS_SELECTOR, "a.dashboard__widget_updates > span:nth-child(3)")
    VIDEO_LINK = (By.CSS_SELECTOR, ".dashboard__widget_shares")
    VIDEO_LINK_URL = "https://www.youtube.com/playlist?list=PLzBLrjkJE1LLLDY4uf1QiaQqSs5WVIn35"
    VIDEO_LINK_NAME = "Video Tutorials"
    VIDEO_LINK_NAME_LOC = (By.CSS_SELECTOR, ".dashboard__widget_shares > span:nth-child(2)")
    VIDEO_LINK_TEXT = "How-to videos and more"
    VIDEO_LINK_TEXT_LOC = (By.CSS_SELECTOR, ".dashboard__widget_shares > span:nth-child(3)")
    # TODO: ADD COUNTERS TO ITEMS IN WIDGETS
    RECENT_UPDATES_ITEMS_ROOT = (By.XPATH, "/html/body/main/div/div[2]/div/div/div[1]/article/section/ul")

    RECENT_UPDATES_TABLE = (By.CSS_SELECTOR, "article.dashboard__widget_updates>section:nth-child(2)>ul:nth-child(1)")


class UserManagementPageLocators(object):
    USER_MANAGEMENT_TAB_ACTIVE = (By.CSS_SELECTOR, ".top-menu__link--active")
    # USERS TAB
    USERS_TAB = (By.CSS_SELECTOR, "div.data-page-tabs__tab:nth-child(1)")
    ADD_NEW_USER_BUTTON = (By.CSS_SELECTOR, ".button")
    ADD_NEW_USER_BUTTON_TEXT = "Add New User"
    FIRST_NAME = (By.NAME, "firstName")
    LAST_NAME = (By.NAME, "lastName")
    LOGIN = (By.NAME, "login")
    PASSWORD = (By.NAME, "password")
    EMAIL = (By.NAME, "email")
    ROLE = (By.NAME, "rolesSelector")
    ROLE_SELECTOR = (By.CSS_SELECTOR, ".selector-suggestions__item")
    GROUPS_MEMBER = (By.NAME, "groupsSelector")
    GROUPS_MEMBER_SELECTOR = (By.CSS_SELECTOR, ".selector-suggestions__item")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button.button:nth-child(1)")
    FOOTER = (By.CSS_SELECTOR, ".main-layout__footer > div:nth-child(1)")
    LIST_LOGIN_1 = (By.CSS_SELECTOR,
                    "div.table__row:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > p:nth-child(1) > span:nth-child(1)")
    LIST_FIRST_NAME_1 = (By.CSS_SELECTOR,
                         "div.table__row:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > p:nth-child(1) > span:nth-child(1)")
    LIST_LAST_NAME_1 = (By.CSS_SELECTOR,
                        "div.table__row:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > p:nth-child(1) > span:nth-child(1)")
    LIST_LOGIN_2 = (By.CSS_SELECTOR,
                    "div.table__row:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > p:nth-child(1) > span:nth-child(1)")
    LIST_FIRST_NAME_2 = (By.CSS_SELECTOR,
                         "div.table__row:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > p:nth-child(1) > span:nth-child(1)")
    LIST_LAST_NAME_2 = (By.CSS_SELECTOR,
                        "div.table__row:nth-child(3) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > p:nth-child(1) > span:nth-child(1)")
    LIST_LOGIN_3 = (By.CSS_SELECTOR,
                    "div.table__row:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > p:nth-child(1) > span:nth-child(1)")
    LIST_FIRST_NAME_3 = (By.CSS_SELECTOR,
                         "div.table__row:nth-child(4) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > p:nth-child(1) > span:nth-child(1)")
    LIST_LAST_NAME_3 = (By.CSS_SELECTOR,
                        "div.table__row:nth-child(4) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > p:nth-child(1) > span:nth-child(1)")
    LIST_LOGIN_4 = (By.CSS_SELECTOR,
                    "div.table__row:nth-child(5) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > p:nth-child(1) > span:nth-child(1)")
    LIST_FIRST_NAME_4 = (By.CSS_SELECTOR,
                         "div.table__row:nth-child(5) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > p:nth-child(1) > span:nth-child(1)")
    LIST_LAST_NAME_4 = (By.CSS_SELECTOR,
                        "div.table__row:nth-child(5) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > p:nth-child(1) > span:nth-child(1)")
    LIST_LOGIN_5 = (By.CSS_SELECTOR,
                    "div.table__row:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > p:nth-child(1) > span:nth-child(1)")
    LIST_FIRST_NAME_5 = (By.CSS_SELECTOR,
                         "div.table__row:nth-child(6) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > p:nth-child(1) > span:nth-child(1)")
    LIST_LAST_NAME_5 = (By.CSS_SELECTOR,
                        "div.table__row:nth-child(6) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > p:nth-child(1) > span:nth-child(1)")
    USER1_CHECKBOX = (
        By.CSS_SELECTOR, "div.table__row:nth-child(2) > div:nth-child(1) > div:nth-child(1) > label:nth-child(2)")
    USER2_CHECKBOX = (
        By.CSS_SELECTOR, "div.table__row:nth-child(3) > div:nth-child(1) > div:nth-child(1) > label:nth-child(2)")
    USER3_CHECKBOX = (
        By.CSS_SELECTOR, "div.table__row:nth-child(4) > div:nth-child(1) > div:nth-child(1) > label:nth-child(2)")
    USER4_CHECKBOX = (
        By.CSS_SELECTOR, "div.table__row:nth-child(5) > div:nth-child(1) > div:nth-child(1) > label:nth-child(2)")
    EDIT_LINK = (By.LINK_TEXT, "Edit")  # CSS_SELECTOR: ".main-context-menu > li:nth-child(1) > a:nth-child(2)"
    # GROUPS TAB
    GROUPS_TAB = (By.CSS_SELECTOR, "div.data-page-tabs__tab:nth-child(2)")
    GROUPS_TAB_FOOTER = (By.CSS_SELECTOR, ".main-layout__footer>div:nth-child(1)")
    ADD_NEW_GROUP_BUTTON = (By.CSS_SELECTOR, ".button")
    ADD_NEW_GROUP_BUTTON_TEXT = "Add New Group"
    NEW_GROUP_NAME = (By.NAME, "name")
    NEW_GROUP_DESCRIPTION = (By.NAME, "description")
    SAVE_NEW_GROUP_BUTTON = (By.CSS_SELECTOR, "button.button:nth-child(1)")
    CANCEL_NEW_GROUP_BUTTON = (By.CSS_SELECTOR, "button.button:nth-child(2)")
    # DBA
    DBA_GROUP_NAME_TEXT = "DBA"
    DBA_GROUP_TABLE_NAME = (By.CSS_SELECTOR,
                            "div.table__row:nth-child(1)>div:nth-child(2)>div:nth-child(1)>div:nth-child(1)>p:nth-child(1)>span:nth-child(1)")
    DBA_GROUP_USERS_COUNT = (By.CSS_SELECTOR,
                             "div.table__row:nth-child(1)>div:nth-child(3)>div:nth-child(1)>div:nth-child(1)>p:nth-child(1)>span:nth-child(1)")
    DBA_GROUP_DESCRIPTION_TEXT = "For Data Base Administrators"
    DBA_GROUP_TABLE_DESCRIPTION = (
        By.CSS_SELECTOR,
        "div.table__row:nth-child(1)>div:nth-child(2)>div:nth-child(1)>div:nth-child(1)>p:nth-child(2)")
    # JXML
    JXML_GROUP_NAME_TEXT = "JXML"
    JXML_GROUP_TABLE_NAME = (By.CSS_SELECTOR,
                             "div.table__row:nth-child(2)>div:nth-child(2)>div:nth-child(1)>div:nth-child(1)>p:nth-child(1)>span:nth-child(1)")
    JXML_GROUP_USERS_COUNT = (By.CSS_SELECTOR,
                              "div.table__row:nth-child(2)>div:nth-child(3)>div:nth-child(1)>div:nth-child(1)>p:nth-child(1)>span:nth-child(1)")
    JXML_GROUP_DESCRIPTION_TEXT = "For JSON and XML Users"
    JXML_GROUP_TABLE_DESCRIPTION = (
        By.CSS_SELECTOR,
        "div.table__row:nth-child(2)>div:nth-child(2)>div:nth-child(1)>div:nth-child(1)>p:nth-child(2)")


class ConnectionsPageLocators(object):
    ADD_NEW_CONNECTION_BUTTON = (By.CSS_SELECTOR, ".button")
    ADD_NEW_CONNECTION_BUTTON_NAME = "Add New Connection"
    CONNECTIONS_GRID_HEADER = (By.CSS_SELECTOR, ".flex-table__header")
    IRIS_CONNECTION = (
        By.CSS_SELECTOR, "div.flex-table__row:nth-child(1)>div:nth-child(1)>div:nth-child(1)>span:nth-child(1)")
    IRIS_CONNECTION_SHARE_LINK = (By.CSS_SELECTOR, ".share-items__icon-text")
    IRIS_CONNECTION_NAME = (
        By.CSS_SELECTOR, "div.flex-table__row:nth-child(1)>div:nth-child(1)>div:nth-child(1)>span:nth-child(1)")
    IRIS_CONNECTION_DESCRIPTION = (By.CSS_SELECTOR, ".dsl-table__title-cell-description")
    IRIS_ADD_FROM_LINK = (By.CSS_SELECTOR, ".folder-tree-view__name")
    CONNECTION_NAME_INPUT = (By.NAME, "connectionAdd.name")
    DESCRIPTION_INPUT = (By.NAME, "connectionAdd.description")
    PATH_INPUT = (By.NAME, "connectionAdd.connection.path")
    SAVE_NEW_CONNECTION_BUTTON = (By.CSS_SELECTOR, "button.button:nth-child(1)")
    IRIS_FILE_FROM_CONNECTION = (
        By.CSS_SELECTOR, "tr.keys-grid__table__row:nth-child(4) > td:nth-child(1) > span:nth-child(1)")
    SELECTED = (By.CSS_SELECTOR, ".keys-grid__header__description")
    OPEN_BUTTON = (By.CSS_SELECTOR, "button.button:nth-child(2)")


class StatusPageLocators(object):
    # VERSION = (By.CSS_SELECTOR, "#\/version > td:nth-child(2) > span:nth-child(1) > span:nth-child(1)")
    # BUILDDATE = (By.CSS_SELECTOR, "#\/buildDate > td:nth-child(2) > span:nth-child(1) > span:nth-child(1)")
    # STATE = (By.CSS_SELECTOR, "#\/state > td:nth-child(2) > span:nth-child(1) > span:nth-child(1)")
    # EVENTSTORAGE_TYPE = (
    #     By.CSS_SELECTOR, "#\/eventStorage\.type > td:nth-child(2) > span:nth-child(1) > span:nth-child(1)")
    # EVENTSTORAGE_STATE = (
    #     By.CSS_SELECTOR, '#\/eventStorage\.state > td:nth-child(2) > span:nth-child(1) > span:nth-child(1)')
    ALL_INFO = (By.TAG_NAME, "pre")
