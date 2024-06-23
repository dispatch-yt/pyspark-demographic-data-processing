docker exec -it 6691bc085033 spark-submit /opt/bitnami/spark/jobs/process.py

The original csv file is split into two, because github doesn't allow file > 100Mb. 

Make sure to merge both csv file into one before processing. 

Original file size referred in code is: demographic_divident.csv

Try merging these files using below command.

cat first-half.csv second-half.csv > demographic_divident.csv
