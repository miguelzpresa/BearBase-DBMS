select * from dataset_1;
LOAD DATA INFILE '/home/sistemas/mtics/distri db/CPdescarga.xls'
INTO TABLE your_table_name
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;