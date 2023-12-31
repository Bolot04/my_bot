CREATE_USER_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS telegram_users
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
USERNAME CHAR(50),
FIRST_NAME CHAR(50),
LAST_NAME CHAR(50),
REFERENCE_LINK TEXT,
BALANCE INTEGER,
UNIQUE (TELEGRAM_ID)
)
"""
ALTER_USER_TABLE = """
ALTER TABLE telegram_users ADD COLUMN REFERENCE_LINK TEXT
"""
ALTER_USER_V2_TABLE = """
ALTER TABLE telegram_users ADD COLUMN BALANCE INTEGER
"""

CREATE_BAN_USER_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS ban_user
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
BAN_COUNT INTEGER,
UNIQUE (TELEGRAM_ID)
)
"""
CREATE_LIKE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS like_profile
(
ID INTEGER PRIMARY KEY,
OWNER_TELEGRAM_ID INTEGER,
LIKE_TELEGRAM_ID INTEGER,
UNIQUE (OWNER_TELEGRAM_ID, LIKE_TELEGRAM_ID)
)
"""
CREATE_PROFILE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS profile
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
NICKNAME CHAR(50),
BIOGRAPHY TEXT,
AGE INTEGER,
GENDER CHAR(50),
USER_NUMBER INTEGER,
USER_STREET TEXT,
PHOTO TEXT,
UNIQUE (TELEGRAM_ID)
)
"""
CREATE_REFERRAL_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS referral
(
ID INTEGER PRIMARY KEY,
OWNER_TELEGRAM_ID INTEGER,
REFERRAL_TELEGRAM_ID INTEGER,
REFERRAL_FIRST_NAME CHAR(50),
UNIQUE (OWNER_TELEGRAM_ID, REFERRAL_TELEGRAM_ID)
)
"""

INSERT_USER_QUERY = """
INSERT OR IGNORE INTO telegram_users VALUES (?,?,?,?,?,?,?)
"""

INSERT_PROFILE_QUERY = """
INSERT OR IGNORE INTO profile VALUES (?,?,?,?,?,?,?,?,?)
"""

INSERT_NEW_BAN_USER_QUERY = """
INSERT INTO ban_user VALUES (?,?,?)
"""

SELECT_BAN_USER_QUERY = """
SELECT * FROM ban_user WHERE TELEGRAM_ID = ?
"""

UPDATE_BAN_USER_QUERY = """
UPDATE ban_user SET BAN_COUNT = BAN_COUNT + 1 WHERE TELEGRAM_ID = ?
"""

SELECT_REGISTRATION_USER = """
SELECT * FROM profile WHERE TELEGRAM_ID = ?
"""

SELECT_PROFILE_QUERY = """
SELECT * FROM profile WHERE TELEGRAM_ID = ?
"""

FILTER_LEFT_JOIN_PROFILE_LIKE_QUERY = """
SELECT * FROM profile
LEFT JOIN like_profile ON profile.TELEGRAM_ID = like_profile.OWNER_TELEGRAM_ID
AND like_profile.LIKE_TELEGRAM_ID = ?
WHERE like_profile.ID IS NULL
AND profile.TELEGRAM_ID !=?
"""

INSERT_LIKE_QUERY = """
INSERT INTO like_profile VALUES (?,?,?)
"""

UPDATE_PROFILE_QUERY = """
UPDATE profile SET NICKNAME = ?, BIOGRAPHY = ?, AGE = ?, GENDER = ?, USER_NUMBER = ?, USER_STREET = ?, PHOTO = ? 
WHERE TELEGRAM_ID = ?
"""

DELETE_PROFILE_QUERY = """
DELETE FROM profile WHERE TELEGRAM_ID = ?
"""

UPDATE_LINK_USER_QUERY = """
UPDATE telegram_users SET REFERENCE_LINK = ? WHERE TELEGRAM_ID =?
"""
SELECT_USER_QUERY = """
SELECT * FROM telegram_users WHERE TELEGRAM_ID = ?
"""

DOUBLE_SELECT_REFERRAL_USER_QUERY = """
SELECT 
    COALESCE(telegram_users.BALANCE, 0) as BALANCE ,
    COUNT(referral.ID) as total_referral
FROM
    telegram_users
LEFT JOIN 
    referral ON telegram_users.TELEGRAM_ID = referral.OWNER_TELEGRAM_ID
WHERE 
    telegram_users.TELEGRAM_ID = ?
"""

SELECT_BY_LINK_QUERY = """
SELECT * FROM telegram_users WHERE REFERENCE_LINK = ?
"""

INSERT_REFERRAL_QUERY = """
INSERT OR IGNORE INTO referral VALUES (?,?,?)
"""

UPDATE_USER_BALANCE_QUERY = """
UPDATE telegram_users SET BALANCE = COALESCE(BALANCE, 0) + 100 WHERE TELEGRAM_ID = ?
"""