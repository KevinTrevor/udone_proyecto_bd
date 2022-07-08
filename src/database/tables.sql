CREATE TABLE cliente(
    cedula VARCHAR(10) PRIMARY KEY NOT NULL,
    nombre VARCHAR(100),
    whatsapp VARCHAR(12) UNIQUE,
    email VARCHAR(100) UNIQUE
);

CREATE TABLE pedidos(
    id SERIAL PRIMARY KEY,
    cantidad INTEGER NOT NULL,
    monto_delivery MONEY NOT NULL,
    total MONEY NOT NULL,
    screenshot BYTEA,
    estado VARCHAR(20) NOT NULL,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    direccion VARCHAR(100) NOT NULL,
    ciudad VARCHAR(50) NOT NULL,
    municipio VARCHAR(50) NOT NULL,
    observaciones VARCHAR(500) NOT NULL
);