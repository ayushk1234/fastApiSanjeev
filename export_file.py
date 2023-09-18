import pandas as pd
import mysql.connector
import numpy as np
from datetime import datetime

# datetime_str = '09/19/22 13:55:26'

# datetime_object = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
df = pd.read_excel('/home/ayush/PycharmProjects/my_amala_earth/excel_sample.xlsx',engine='openpyxl')
df =df.fillna("NULL")
connection = mysql.connector.connect(host='localhost',
user='root',
password='Amala@2022',
database='ae_bkp')
cursor = connection.cursor()

# cursor.execute("CREATE TABLE ae_bkp.excel_sample ( id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT, entity_id VARCHAR(100) NOT NULL ,type VARCHAR(100) NOT NULL,debit FLOAT(11) NOT NULL ,credit FLOAT(11) NOT NULL,amount FLOAT(11) NOT NULL,currency VARCHAR(100) NOT NULL,fee FLOAT(11) NOT NULL,tax FLOAT(11)  NOT NULL,on_hold INT(1) NOT NULL,settled INT(1)  NOT NULL,created_at DATETIME NOT NULL ,settled_at DATE NOT NULL,settlement_id VARCHAR(100) NOT NULL,description VARCHAR(100) ,notes TEXT(20000) NOT NULL, payment_id VARCHAR(100) ,arn VARCHAR(100) ,settlement_utr VARCHAR(100) ,order_id VARCHAR(100) NOT NULL,order_receipt VARCHAR(100) NOT NULL,method VARCHAR(100) NOT NULL,upi_flow VARCHAR(100) ,card_network VARCHAR(100) ,card_issuer VARCHAR(100) ,card_type VARCHAR(100) ,dispute_id VARCHAR(100) ,PRIMARY KEY (id) );")
# cursor.execute("CREATE TABLE ae_bkp.excel ( id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT, entity_id VARCHAR(100) NOT NULL ,type VARCHAR(100) NOT NULL,fig VARCHAR(100) ,PRIMARY KEY (id) );")



# shipment_count BIGINT UNSIGNED NOT NULL,
# fulfillment_status VARCHAR(100) NOT NULL,
# gateway VARCHAR(100) NOT NULL,
# created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
# updated DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
# PRIMARY KEY (oid),
# UNIQUE KEY order_id_unique (order_id) );
# '

# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci '

# query = "INSERT INTO ae_bkp.excel(entity_id ,fig) VALUES ('Mac', 'Mohan');"
query = 'INSERT INTO excel_sample (entity_id,type,debit,credit,amount,currency,fee,tax,on_hold,settled,created_at,settled_at,settlement_id,description,notes,payment_id,arn,settlement_utr,order_id,order_receipt,method,upi_flow,card_network,card_issuer,card_type,dispute_id) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s,%s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s)'

for row in df.itertuples():
    if row.description == "NULL" or row.dispute_id =="NULL"  :
        description = None;
        dispute_id = None;
        print("1",description)

    created_at = datetime.strptime(row.created_at, '%d/%m/%Y %H:%M:%S')
    settled_at = datetime.strptime(row.settled_at, '%d-%m-%Y').date()

    # print(type(created_at),type(settled_at))  # printed in default format
    print(row.entity_id,row.type,row.debit,row.credit,row.amount,row.currency,row.fee,row.tax,row.on_hold,row.settled,created_at,settled_at,row.settlement_id,row.description,row.notes,row.payment_id,row.arn,row.settlement_utr,row.order_id,row.order_receipt,row.method,row.upi_flow,row.card_network,row.card_issuer,row.card_type,dispute_id );
    cursor.execute(query, (row.entity_id,row.type,row.debit,row.credit,row.amount,row.currency,row.fee,row.tax,row.on_hold,row.settled,created_at,settled_at,row.settlement_id,row.description,row.notes,row.payment_id,row.arn,row.settlement_utr,row.order_id,row.order_receipt,row.method,row.upi_flow,row.card_network,row.card_issuer,row.card_type,dispute_id ))

# cursor.execute(query)
connection.commit()