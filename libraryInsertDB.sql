USE libraryDatabase;

INSERT INTO Admin (adminID, fName, lName, email, password)
VALUES('AD001', 'Kinh', 'Truong', 'truongkinhlong@gmail.com', 'BLrider301!'); 

INSERT INTO Staff (staffID, fName, lName, email, password)
VALUES('ST001', 'Adrian', 'Nguyen', 'ANguyen@gmail.com', 'AdNg001'),
	('ST002', 'Cerian', 'Jaime', 'CJaime@gmail.com', 'CeJa002'),
	('ST003', 'Nathan', 'Nguyen', 'NNguyen@gmail.com', 'NaNg003'),
	('ST004', 'Cooper', 'Tran', 'CTran@gmail.com', 'CoTr004'); 
    
INSERT INTO Member (memberID, fName, lName, email, password)
VALUES
    ('MB001', 'Alice', 'Jones', 'alice.jones@example.com', 'password1'),
    ('MB002', 'Bob', 'Smith', 'bob.smith@example.com', 'password2'),
    ('MB003', 'Charlie', 'Brown', 'charlie.brown@example.com', 'password3'),
    ('MB004', 'David', 'Lee', 'david.lee@example.com', 'password4'),
    ('MB005', 'Emily', 'Wang', 'emily.wang@example.com', 'password5'),
    ('MB006', 'Frank', 'Garcia', 'frank.garcia@example.com', 'password6'),
    ('MB007', 'Grace', 'Nguyen', 'grace.nguyen@example.com', 'password7'),
    ('MB008', 'Henry', 'Kim', 'henry.kim@example.com', 'password8'),
    ('MB009', 'Isabella', 'Chen', 'isabella.chen@example.com', 'password9'),
    ('MB010', 'James', 'Liu', 'james.liu@example.com', 'password10');