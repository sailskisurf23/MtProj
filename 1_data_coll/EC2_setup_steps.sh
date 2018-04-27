#instance names
#1
ec2-user@ec2-13-59-88-140.us-east-2.compute.amazonaws.com
#2
ec2-user@ec2-18-188-204-117.us-east-2.compute.amazonaws.com
#3
ec2-user@ec2-18-188-235-107.us-east-2.compute.amazonaws.com
#4
ec2-user@ec2-18-218-9-15.us-east-2.compute.amazonaws.com
#5
ec2-user@ec2-18-219-67-74.us-east-2.compute.amazonaws.com
# Badass
ec2-user@ec2-18-191-25-129.us-east-2.compute.amazonaws.com
# webapp
xxxx


#tunnel through
ssh -i /Users/colinbrochard/.aws/colinbrochard.pem ec2-user@ec2-13-59-88-140.us-east-2.compute.amazonaws.com
ssh -i /Users/colinbrochard/.aws/colinbrochard.pem ec2-user@ec2-18-188-204-117.us-east-2.compute.amazonaws.com
ssh -i /Users/colinbrochard/.aws/colinbrochard.pem ec2-user@ec2-18-188-235-107.us-east-2.compute.amazonaws.com
ssh -i /Users/colinbrochard/.aws/colinbrochard.pem ec2-user@ec2-18-218-9-15.us-east-2.compute.amazonaws.com
ssh -i /Users/colinbrochard/.aws/colinbrochard.pem ec2-user@ec2-18-219-67-74.us-east-2.compute.amazonaws.com
#Badass
ssh -i /Users/colinbrochard/.aws/colinbrochard.pem ec2-user@ec2-18-191-25-129.us-east-2.compute.amazonaws.com
#webapp
xxxxx


#install anaconda
https://medium.com/@josemarcialportilla/getting-spark-python-and-jupyter-notebook-running-on-amazon-ec2-dec599e1c297
export PATH=/home/ec2-user/anaconda3/bin:$PATH

#install mongo
https://docs.mongodb.com/ecosystem/platforms/amazon-ec2/
pip install pymongo

# #split routes.csv files & zip
# split -l 20000 routes88k.csv
# zip -r r88k.zip r88k/

#move script over
# scp -i /Users/colinbrochard/.aws/colinbrochard.pem /Users/colinbrochard/DSI_Capstone_local/MtProjRec/1_data_coll/route_to_db.py ec2-user@ec2-13-59-88-140.us-east-2.compute.amazonaws.com:~/
scp -i /Users/colinbrochard/.aws/colinbrochard.pem /Users/colinbrochard/DSI_Capstone_local/MtProjRec/1_data_coll/routeAPI_to_db.py ec2-user@ec2-13-59-88-140.us-east-2.compute.amazonaws.com:~/



# #transfer routes zip
# scp -i /Users/colinbrochard/.aws/colinbrochard.pem /Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/1_routeIDs/r88k.zip ec2-user@ec2-13-59-88-140.us-east-2.compute.amazonaws.com:~/

#transfer test rts
#scp -i /Users/colinbrochard/.aws/colinbrochard.pem /Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/routes_sample1000.csv ec2-user@ec2-13-59-88-140.us-east-2.compute.amazonaws.com:~/

# run script on EC2
nano route_to_db.py
#insert
/home/ec2-user/r88k/routes88k_5.csv

$ screen
$ python routes_to_db.py

#check on it
ps -ax
cat r2_db_log.txt

# create DB dump on EC2, rename, zip & transfer
mongodump -d routes_db #-o <directory_backup>
mv dump/ dump_5/
zip -r dump_5.zip dump_5/
scp -i /Users/colinbrochard/.aws/colinbrochard.pem ec2-user@ec2-13-59-88-140.us-east-2.compute.amazonaws.com:/home/ec2-user/dump_1.zip .
scp -i /Users/colinbrochard/.aws/colinbrochard.pem ec2-user@ec2-18-188-204-117.us-east-2.compute.amazonaws.com:/home/ec2-user/dump_2.zip .
scp -i /Users/colinbrochard/.aws/colinbrochard.pem ec2-user@ec2-18-188-235-107.us-east-2.compute.amazonaws.com:/home/ec2-user/dump_3.zip .
scp -i /Users/colinbrochard/.aws/colinbrochard.pem ec2-user@ec2-18-218-9-15.us-east-2.compute.amazonaws.com:/home/ec2-user/dump_4.zip .

#split big files into chunks
split -b 1000m /home/ec2-user/alldumps/4_dumps/dump_1/routes_db/routes_db.bson /home/ec2-user/alldumps/4_dumps/dump_1/routes_db/
split -b 1000m /home/ec2-user/alldumps/4_dumps/dump_2/routes_db/routes_db.bson /home/ec2-user/alldumps/4_dumps/dump_2/routes_db/
split -b 1000m /home/ec2-user/alldumps/4_dumps/dump_3/routes_db/routes_db.bson /home/ec2-user/alldumps/4_dumps/dump_3/routes_db/
split -b 1000m /home/ec2-user/alldumps/4_dumps/dump_4/routes_db/routes_db.bson /home/ec2-user/alldumps/4_dumps/dump_4/routes_db/
split -b 1000m /home/ec2-user/alldumps/4_dumps/dump_5/routes_db/routes_db.bson /home/ec2-user/alldumps/4_dumps/dump_5/routes_db/

split -b 1000m /Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/4_dumps/dump_1/routes_db/routes_db.bson /Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/4_dumps/dump_1/routes_db/
split -b 1000m /Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/4_dumps/dump_2/routes_db/routes_db.bson /Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/4_dumps/dump_2/routes_db/
split -b 1000m /Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/4_dumps/dump_3/routes_db/routes_db.bson /Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/4_dumps/dump_3/routes_db/
split -b 1000m /Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/4_dumps/dump_4/routes_db/routes_db.bson /Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/4_dumps/dump_4/routes_db/
split -b 1000m /Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/4_dumps/dump_5/routes_db/routes_db.bson /Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/4_dumps/dump_5/routes_db/


#move read_dump_to_rus
scp -i /Users/colinbrochard/.aws/colinbrochard.pem /Users/colinbrochard/DSI_Capstone_local/MtProjRec/5_analysis/read_dump_to_rus.py ec2-user@ec2-18-191-25-129.us-east-2.compute.amazonaws.com:~/


mongorestore -d routes_db -c dump1 /Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/4_dumps/dump_1/routes_db/routes_db.bson
mongorestore -d routes_db -c dump2 /Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/4_dumps/dump_2/routes_db/routes_db.bson
mongorestore -d routes_db -c dump3 /Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/4_dumps/dump_3/routes_db/routes_db.bson
mongorestore -d routes_db -c dump4 /Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/4_dumps/dump_4/routes_db/routes_db.bson
mongorestore -d routes_db -c dump5 /Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/4_dumps/dump_5/routes_db/routes_db.bson
