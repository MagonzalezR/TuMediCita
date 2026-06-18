INSERT INTO especialidad (nombre) VALUES
    ('Medicina General'),
    ('Pediatría'),
    ('Cardiología'),
    ('Dermatología'),
    ('Ortopedia')
ON CONFLICT (nombre) DO NOTHING;

INSERT INTO doctor (nombres, apellidos, documento, telefono, email, especialidad_id) VALUES
    ('Laura', 'Martínez', '1000111222', '3001234567', 'laura.martinez@clinica.com',
        (SELECT id FROM especialidad WHERE nombre = 'Medicina General')),
    ('Carlos', 'Pérez', '1000333444', '3007654321', 'carlos.perez@clinica.com',
        (SELECT id FROM especialidad WHERE nombre = 'Pediatría')),
    ('Ana', 'Gómez', '1000555666', '3009876543', 'ana.gomez@clinica.com',
        (SELECT id FROM especialidad WHERE nombre = 'Cardiología'))
ON CONFLICT (documento) DO NOTHING;

INSERT INTO paciente (nombres, apellidos, documento, fecha_nacimiento, telefono, email, direccion) VALUES
    ('Juan', 'Rodríguez', '2000111222', '1990-05-12', '3101234567', 'juan.rodriguez@correo.com', 'Calle 10 # 5-20'),
    ('María', 'López', '2000333444', '1985-11-03', '3107654321', 'maria.lopez@correo.com', 'Avenida 7 # 12-30'),
    ('Pedro', 'Sánchez', '2000555666', '2001-02-20', '3109876543', 'pedro.sanchez@correo.com', 'Carrera 15 # 8-40')
ON CONFLICT (documento) DO NOTHING;

INSERT INTO cita (paciente_id, doctor_id, fecha, motivo, estado) VALUES
    (
        (SELECT id FROM paciente WHERE documento = '2000111222'),
        (SELECT id FROM doctor WHERE documento = '1000111222'),
        NOW() + INTERVAL '1 day',
        'Consulta de control general',
        'PROGRAMADA'
    ),
    (
        (SELECT id FROM paciente WHERE documento = '2000333444'),
        (SELECT id FROM doctor WHERE documento = '1000555666'),
        NOW() + INTERVAL '2 day',
        'Dolor en el pecho',
        'PROGRAMADA'
    );
