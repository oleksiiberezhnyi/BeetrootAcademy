sqlite3 serial_beam.db
CREATE TABLE for65mm(mark TEXT, length REAL, width REAL, height REAL, maximum_loads REAL, minimum_support REAL, volume REAL, weight REAL);
.dbinfo
.schema for65mm
INSERT INTO for65mm VALUES ('1ПБ10-1','1.030','0.120','0.065','0.98','0.1','0.008','0.196');
.header on
INSERT INTO for65mm VALUES ('2ПБ10-1','1.03','0.12','0.14','0.98','0.1','0.017','0.417');
INSERT INTO for65mm VALUES ('1ПБ13-1','1.29','0.12','0.065','1.47','0.1','0.01','0.245');
INSERT INTO for65mm VALUES ('2ПБ13-1','1.29','0.12','0.14','1.47','0.1','0.022','0.539');
INSERT INTO for65mm VALUES ('1ПБ16-1','1.55','0.12','0.065','1.47','0.1','0.012','0.294');
INSERT INTO for65mm VALUES ('2ПБ16-2','1.55','0.12','0.14','2.45','0.1','0.026','0.637');
INSERT INTO for65mm VALUES ('2ПБ17-2','1.68','0.12','0.14','2.45','0.1','0.028','0.686');
INSERT INTO for65mm VALUES ('2ПБ19-3','1.94','0.12','0.14','2.92','0.1','0.033','0.808');
INSERT INTO for65mm VALUES ('2ПБ22-3','2.2','0.12','0.14','3.43','0.1','0.037','0.906');
INSERT INTO for65mm VALUES ('2ПБ25-3','2.46','0.12','0.14','3.43','0.1','0.041','1.004');
INSERT INTO for65mm VALUES ('2ПБ26-4','2.59','0.12','0.14','3.92','0.1','0.044','1.078');
INSERT INTO for65mm VALUES ('2ПБ29-4','2.85','0.12','0.14','3.92','0.1','0.048','1.176');
INSERT INTO for65mm VALUES ('2ПБ30-4','2.98','0.12','0.14','3.92','0.15','0.05','1.225');
INSERT INTO for65mm VALUES ('4ПБ30-4','2.98','0.12','0.29','3.92','0.1','0.104','2.548');
INSERT INTO for65mm VALUES ('3ПБ34-4','3.37','0.12','0.22','3.92','0.1','0.089','2.18');
INSERT INTO for65mm VALUES ('3ПБ36-4','3.63','0.12','0.22','3.92','0.1','0.096','2.352');
INSERT INTO for65mm VALUES ('3ПБ39-8','3.89','0.12','0.22','7.85','0.21','0.103','2.523');
UPDATE for65mm SET length = '4.00', width = '0.15' WHERE mark = '3ПБ39-8';
select * from for65mm;
DELETE FROM for65mm WHERE mark = '3ПБ39-8';
select * from for65mm;
