from enum import Enum


class Routes(str, Enum):
    ANCHOR = "-*-*-*-*"
    LOGIN_PREPROD = "-*-*-*-*"
    LOGIN_PROD_NO_PATH = "-*-*-*-*"
    LOGIN_PROD = "-*-*-*-*"
    REDIRECT_VK = "-*-*-*-*"
    YOUTUBE = "-*-*-*-*"
