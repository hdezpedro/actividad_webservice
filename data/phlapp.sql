
USE kuora3245678789;

CREATE TABLE users(
    username varchar(20) NOT NULL PRIMARY KEY,
    password varchar(32) NOT NULL,
    privilege integer NOT NULL DEFAULT -1,
    status integer NOT NULL DEFAULT 1,
    name varchar(150) NOT NULL,
    email varchar(100) NOT NULL,
    other_data varchar(50) NOT NULL,
    user_hash varchar(32) NOT NULL,
    change_pwd integer NOT NULL DEFAULT 1,
    created timestamp NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE sessions(
    session_id char(128) UNIQUE NOT NULL,
    atime timestamp NOT NULL default current_timestamp,
    data text
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE logs( 
    id_log integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username varchar(20) NOT NULL,
    ip varchar(16) NOT NULL,
    access timestamp NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE clientes (
    id_cliente int not null primary key AUTO_INCREMENT,
    nombre varchar(30) not null,
    apellido_paterno varchar(30) not null,
    apellido_materno varchar(30) not null,
    telefono varchar(10) not null,
    email varchar(50) not null
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO users (username, password, privilege, status, name, email, other_data, user_hash, change_pwd)
VALUES ('admin',MD5(concat('admin', 'kuorra_key')), 0, 1, 'Admin', 'admin@gmail.com','TIC:SI', MD5(concat('admin', 'kuorra_key', '2016/06/04')), 0),
('guess',MD5(concat('guess', 'kuorra_key')), 1, 1, 'Guess', 'guess@gmail.com','TIC:SI', MD5(concat('guess', 'kuorra_key','2016/06/04')), 0);


INSERT INTO clientes (nombre, apellido_paterno, apellido_materno, telefono, email) VALUES 
    ('Pedro', 'lopez', 'Muños', '775145632', 'okd23@gmail.com'),
    ('Jose', 'Hernandez', 'Merida', '775756342', 'jose@gmail.com'),
    ('Juan ', 'Hernandez', 'Luqueño', '772839189', 'hleo21@gmail.com');


SELECT * FROM users;
SELECT * FROM sessions;
SELECT * FROM clientes;

CREATE USER 'phl'@'localhost' IDENTIFIED BY 'phl.2019';
GRANT ALL PRIVILEGES ON act11_webservice_aahr.* TO 'phl'@'localhost';
FLUSH PRIVILEGES;
