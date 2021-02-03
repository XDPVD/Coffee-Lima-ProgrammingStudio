INSERT IGNORE INTO distrito
(nombre_distrito)
VALUES
("Lima"),
("Ancón"),
("Ate Vitarte"),
("Barranco"),
("Breña"),
("Carabayllo"),
("Chaclacayo"),
("Chorrillos"),
("Cieneguilla"),
("Comas"),
("El Agustino"),
("Independencia"),
("Jesús María"),
("La Molina"),
("La Victoria"),
("Lince"),
("Los Olivos"),
("Lurigancho"),
("Lurín"),
("Magdalena del Mar"),
("Miraflores"),
("Pachacamac"),
("Pucusana"),
("Pueblo Libre"),
("Puente Piedra"),
("Punta Hermosa"),
("Punta Negra"),
("Rímac"),
("San Bartolo"),
("San Borja"),
("San Isidro"),
("San Juan de Lurigancho"),
("San Juan de Miraflores"),
("San Luis"),
("San Martín de Porres"),
("San Miguel"),
("Santa Anita"),
("Santa María del Mar"),
("Santa Rosa"),
("Santiago de Surco"),
("Surquillo"),
("Villa El Salvador"),
("Villa María del Triunfo");

INSERT IGNORE INTO oficio
(nombre)
VALUES
('Carpintería'),
('Albañilería'),
('Herrería'),
('Cristalería'),
('Servicio técnico'),
('Diseño gráfico'),
('Gasfitería'),
('Plomería');

ALTER TABLE especialista ADD UNIQUE (e_mail);
ALTER TABLE especialista ADD UNIQUE (nro_tlf);
ALTER TABLE especialista ADD UNIQUE (dni);
ALTER TABLE especialista ADD UNIQUE (ruc);

INSERT INTO especialista
(nombre, apellido, e_mail, nro_tlf, contrasena, dni, ruc)
VALUES
('Xocrona', 'Sandoval', 'xocrona.sandoval@gmail.com', 111111111, '123', 11111111, 11111111),
('Erick', 'Palomino', 'erick.palomino@gmail.com', 222222222, '123', 22222222, 22222222),
('Diego', 'Vilca', 'diego.vilca@gmail.com', 333333333, '123', 33333333, 33333333),
('Kenny', 'Suarez', 'kenny.suarez@gmail.com', 444444444, '123', 44444444, 44444444);

ALTER TABLE cliente ADD UNIQUE (e_mail);
ALTER TABLE cliente ADD UNIQUE (nro_tlf);

INSERT INTO cliente
(nombre, apellido, e_mail, nro_tlf, contrasena, id_distrito)
VALUES
('Kori', 'Antunez', 'kori.antunez@gmail.com', 555555555, '123', 5),
('Mishell', 'Gomez', 'mishell.gomez@gmail.com', 666666666, '123', 26);

INSERT IGNORE INTO `area de trabajo`
(id_distrito, id_especialista)
VALUES
(1,1),
(20,1),
(25,1),
(16,1),
(31,2),
(32,2),
(14,2),
(1,3),
(16,3),
(32,3),
(37,4),
(23,4),
(11,4);

INSERT IGNORE INTO `repertorio de oficios`
(id_especialista, id_oficio)
VALUES
(1,4),
(1,3),
(2,5),
(2,6),
(3,1),
(4,7);

INSERT IGNORE INTO post 
(id_especialista, titulo, descripcion, id_oficio)
VALUES
(1, 'Servicios de cristalería', 'Los mejores cristales de la ciudad', 4),
(1, 'Servicios de herrerpia', 'Marcos y estructuras de hierro para tu hogar', 3),
(2, 'Servicio técnico de PC, Laptop y Celulares', 'Regreso tus equipos a la vida', 5),
(2, 'Logos para tu marca', 'Dale un rostro a tu marca con los mejores logos', 6),
(3, 'Acabados de madera', 'Adorna tu hogar con los mejores adornos de madera', 1),
(4, 'Instalación de gas', 'Conexión de tuberías de gas para cocinar', 7);

INSERT IGNORE INTO solicitud
(id_cliente, id_especialista, fecha, rating_trabajo, id_oficio, estado)
VALUES
(1, 2, NOW(), NULL, 6, 1),
(2, 2, NOW(), 4, 6, 5),
(1, 3, NOW(), NULL, 1, 1);