-- Criar Banco de dados
CREATE DATABASE School;
-- Usar Banco de dados
--  Obs: Deve ser executado sempre que acessar o workbench antes de executar qualquer query
USE School;
-- Criar Tabela
CREATE TABLE Student (
	StudentID INT PRIMARY KEY NOT NULL,
    StudentName VARCHAR(100),
    DateOfBirth DATE,
    Major VARCHAR(100),
    Contactnumber VARCHAR(15)
);
CREATE TABLE Course (
	CourseID VARCHAR(10) PRIMARY KEY NOT NULL,
    CourseName VARCHAR(100)
);
-- Criar tabela relacionamento com contraint e foreign key
CREATE TABLE StudentCourse (
	EnrollmentID BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    StudentID INT,
    CourseID VARCHAR(10),
    Grade CHAR(2),
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
);
-- Inserir Dados
INSERT INTO Student VALUES 
(1, 'John Doe', '2000-05-15', 'Computer Science', '61123456'),
(2, 'Jane Smith', '2001-03-12', 'Physics', '6132165487'),
(3, 'Jim Bean', '1999-07-25', 'Mathematics', '621234565'); 
-- Buscar todos os estudantes
SELECT * FROM Student;
-- Inserir cursos
INSERT INTO Course VALUES 
('CSC101', 'Introduction to Computer Science'),
('DSC102', 'Introduction to Design an Modeling Databases'),
('DSC101', 'Introduction to Data Science');
-- Atribuir alunos a cursos
INSERT INTO StudentCourse (StudentID, CourseID, Grade) VALUES 
(1, 'CSC101', 'A'),
(2, 'CSC101', 'A'),
(3, 'DSC101', 'B'),
(1, 'DSC101', 'A');
-- Adicionar estudante a um curso
INSERT INTO StudentCourse (StudentID, CourseID, Grade) VALUES 
(4, 'CSC101', 'A');
-- Adicionar estudante
INSERT INTO Student VALUES 
(4, 'Phillip', '2000-05-15', 'Computer Science', '61123456');
-- Remover estudante
DELETE FROM Student WHERE StudentID = 4;
-- Remover coluna
ALTER TABLE Student DROP COLUMN  StudentName;
-- Adicionar coluna
ALTER TABLE Student ADD COLUMN  StudentName VARCHAR(100);

