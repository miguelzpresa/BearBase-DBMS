SHOW databases;
USE cp_mex;
CREATE TABLE dataset_1 (
    d_codigo INT(20),
    d_asenta VARCHAR(50),
    d_tipo_asenta VARCHAR(50),
    D_mnpio VARCHAR(50),
    d_estado VARCHAR(50),
    d_ciudad VARCHAR(50),
    d_CP INT(20),
    c_estado int(5),
    c_oficina INT(10),
    c_CP INT(1),
    c_tipo_asenta INT(15),
    c_mnpio INT(15),
    id_asenta_cpcons INT(15),
    d_zona VARCHAR(30),
    c_cve_ciudad INT(5)
);
SELECT *FROM  dataset_1;
