#!/bin/sh
git pull
wait
cp -rf /home/ubuntu/eclweb/settings.py /home/ubuntu/eclweb/demo/demo/
wait
mysql ecl_careerpath_tst  -u'edu_user' -p'test_environment_user' < create_database.sql
wait
python manage.py syncdb
wait
mysql ecl_careerpath_tst  -u'edu_user' -p'test_environment_user' < demo_data.sql
sudo service apache2 stop
wait
sudo service apache2 start
