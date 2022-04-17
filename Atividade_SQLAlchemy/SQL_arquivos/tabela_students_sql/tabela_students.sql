-- Table: public.students

-- DROP TABLE IF EXISTS public.students;

CREATE TABLE IF NOT EXISTS public.students
(
    student_id integer NOT NULL DEFAULT nextval('students_student_id_seq'::regclass),
    name character varying(100) COLLATE pg_catalog."default",
    city character varying(50) COLLATE pg_catalog."default",
    addr character varying(200) COLLATE pg_catalog."default",
    pin character varying(10) COLLATE pg_catalog."default",
    CONSTRAINT students_pkey PRIMARY KEY (student_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.students
    OWNER to postgres;