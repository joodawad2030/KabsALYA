

CREATE TABLE users (
id INT AUTO_INCREMENT PRIMARY KEY ,
username VARCHAR(50) NOT NULL UNIQUE,
email VARCHAR(100) NOT NULL UNIQUE,
password VARCHAR(255) NOT NULL,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (username, email, password) VALUES
('ahmed123', 'ahmed.alshehri@gmail.com', 'pass123'),
('sara99', 'sara.almutairi@yahoo.com', '1111'),
('mohammed_dev', 'mohammed.dev@hotmail.com', '2222'),
('nouraX', 'noura.fahad@gmail.com', '3333'),
('fahad_1', 'fahad.alharbi@outlook.com', '4444');