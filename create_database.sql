DROP DATABASE ecl_careerpath_tst;
DROP USER 'edu_user'@'localhost';
CREATE USER 'edu_user'@'localhost';
CREATE DATABASE ecl_careerpath_tst;
USE ecl_careerpath_tst;
GRANT ALL PRIVILEGES ON ecl_careerpath_tst TO  'edu_user'@'localhost';