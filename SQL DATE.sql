-- SISTEMA DE VENDAS DE PRODUTOS

-- CRIAR BANCO DE DADOS
CREATE DATABASE comercial;
-- 
USE comercial;
-- Clientes

create table cliente(
     cliente_id int not null auto_increment,
     cliente_codigo varchar(10),
     cliente_nome varchar(100),
     cliente_razao varchar(100),
     cliente_data date,
     cliente_cnpj varchar(20),
     cliente_contato varchar(20),
     cliente_cidade varchar(50),
     cliente_estado varchar(50),
primary key (cliente_id));

-- Forn
create table fornecedor(
     fornecedor_id int not null auto_increment,
     fornecedor_codigo varchar(10),
     fornecedor_nome varchar(100),
     fornecedor_razao varchar(100),
     fornecedor_contato varchar(20),
primary key(fornecedor_id));


create table vendedor(
     vendedor_id int not null auto_increment,
     vendedor_codigo varchar(10),
     vendedor_nome varchar(100),
     vendedor_razao varchar(100),
     vendedor_contato varchar(20),
     vendedor_comissao float(10,2), 
primary key(vendedor_id));

-- Produto
create table produto(
     produto_id int not null auto_increment,
     produto_codigo varchar(20),
     produto_descricao varchar(100),
     produto_valor float(10,2),
     produto_situacao varchar(1),
     fornecedor_id int,
primary key(produto_id));

create table venda(
     venda_id int not null auto_increment,
     venda_codigo varchar(10),
     cliente_id int not null,
     fornecedor_id int not null,
     vendedor_id int not null,
     venda_valor float(10,2),
     venda_desconto float(10,2),
     venda_total float(10,2),
     venda_data date,
primary key(venda_id));

create table ivenda(
     ivenda_id int not null auto_increment,
     venda_id int not null,
     produto_id int not null,
     ivenda_valor float(10,2),
     ivenda_quantidade int,
     ivenda_desconto float(10,2),
primary key(ivenda_id));

-- # 02. CRIAR CONSTRAINT
alter table venda add constraint  fk_produto_fornecedor 
     foreign key(fornecedor_id) references fornecedor(fornecedor_id) 
          on delete no action 
          on update no action;

alter table venda add constraint  fk_produto_vendedor 
     foreign key(vendedor_id) references vendedor(vendedor_id) 
          on delete no action 
          on update no action;

alter table venda add constraint  fk_venda_cliente
     foreign key(cliente_id) references cliente(cliente_id) 
          on delete no action 
          on update no action;

alter table ivenda add constraint  fk_ivenda_produto 
     foreign key(produto_id) references produto(produto_id) 
          on delete no action 
          on update no action;

alter table ivenda add constraint  fk_ivenda_venda
     foreign key(venda_id) references venda(venda_id) 
          on delete no action 
          on update no action;

-- POPULAR BANCO
-- Cliente
INSERT INTO cliente (
    cliente_id, 
    cliente_codigo, 
    cliente_nome, 
    cliente_razao, 
    cliente_data, 
    cliente_cnpj, 
    cliente_contato, 
    cliente_cidade, 
    cliente_estado
) VALUES
(1, '0001', 'AARONSON FURNITURE', 'AARONSON FURNITURE LTD', '2015-02-17', '17.807.928/0001-85', '(21) 8167-6584', 'QUEIMADOS', 'RJ'),
(2, '0002', 'LITTLER', 'LITTLER LTDA', '2015-02-17', '55.643.605/0001-92', '(27) 7990-9502', 'SERRA', 'ES'),
(3, '0003', 'KELSEY NEIGHBOURHOOD', 'KELSEY NEIGHBOURHOOD', '2015-02-17', '05.202.361/0001-34', '(11) 4206-9703', 'BRAGANÇA PAULISTA', 'SP'),
(4, '0004', 'GREAT AMERICAN MUSIC', 'GREAT AMERICAN MUSIC', '2015-02-17', '11.880.735/0001-73', '(75) 7815-7801', 'SANTO ANTÔNIO DE JESUS', 'BA'),
(5, '0005', 'LIFE PLAN COUNSELLING', 'LIFE PLAN COUNSELLING', '2015-02-17', '75.185.467/0001-52', '(17) 4038-9355', 'BEDOURO', 'SP'),
(6, '0006', 'PRACTI-PLAN', 'PRACTI-PLAN LTDA', '2015-02-17', '32.518.106/0001-78', '(28) 2267-6159', 'CACHOEIRO DE ITAPEMIRI', 'ES'),
(7, '0007', 'SPORTSWEST', 'SPORTSWEST LTDA', '2015-02-17', '83.175.645/0001-92', '(61) 4094-7184', 'TAGUATINGA', 'DF'),
(8, '0008', 'HUGHES MARKETS', 'HUGHES MARKETS', '2015-02-17', '04.728.160/0001-02', '(21) 7984-9809', 'RIO DE JANEIRO', 'RJ'),
(9, '0009', 'AUTO WORKS', 'AUTO WORKS LTDA', '2015-02-17', '08.271.985/0001-00', '(21) 8548-5556', 'RIO DE JANEIRO', 'RJ'),
(10, '0010', 'DAHLKEMPER', 'DAHLKEMPER LTDA', '2015-02-17', '49.815.047/0001-00', '(11) 4519-7670', 'SÃO PAULO', 'SP');
-- Vendedores
INSERT INTO vendedor (vendedor_id, vendedor_codigo, vendedor_nome, vendedor_razao, vendedor_contato, vendedor_comissao) VALUES
(1, '0001', 'CARLOS FERNANDES', 'CARLOS FERNANDES LTDA', '(47) 7535-8144', 12.00),
(2, '0002', 'JÚLIA GOMES', 'JÚLIA GOMES LTDA', '(12) 8037-6661', 25.00);
-- Fornecedores
INSERT INTO fornecedor (fornecedor_id, fornecedor_codigo, fornecedor_nome, fornecedor_razao, fornecedor_contato) VALUES
(1, '0001', 'DUN RITE LAWN MAINTENANCE', 'DUN RITE LAWN MAINTENANCE LTDA', '(85) 7886-8837'),
(2, '0002', 'SEWFRO FABRICS', 'SEWFRO FABRICS LTDA', '(91) 5171-8483');
-- Produtos
INSERT INTO produto (produto_id, produto_codigo, produto_descricao, produto_valor, produto_situacao, fornecedor_id) VALUES
(1, '123131', 'NOTEBOOK', 1251.29, 'A', 1),
(2, '123223', 'SMARTPHONE', 1242.21, 'A', 2),
(3, '1231', 'DESKTOP', 1241.21, 'A', 1),
(4, '142123', 'TELEVISÃO', 2564.92, 'A', 2),
(5, '7684', 'DRONE', 2325.32, 'A', 1),
(6, '159876', 'MONITOR GAMER', 1251.29, 'A', 1);
-- Venda
INSERT INTO venda (
    venda_id, 
    venda_codigo, 
    cliente_id, 
    fornecedor_id, 
    vendedor_id, 
    venda_valor, 
    venda_desconto, 
    venda_total, 
    venda_data
) VALUES
(1, '1', 1, 1, 1, 25141.02, 0, 25141.02, '2015-01-01'),
(2, '2', 2, 2, 2, 12476.58, 0, 12476.58, '2015-01-02'),
(3, '3', 3, 1, 1, 16257.32, 0, 16257.32, '2015-01-03'),
(4, '4', 4, 2, 2, 8704.55, 0, 8704.55, '2015-01-03'),
(5, '5', 5, 1, 1, 13078.81, 0, 13078.81, '2015-01-01'),
(6, '6', 6, 2, 2, 6079.19, 0, 6079.19, '2015-01-02'),
(7, '7', 7, 1, 1, 7451.26, 0, 7451.26, '2015-01-03'),
(8, '8', 8, 2, 2, 15380.47, 0, 15380.47, '2015-01-04'),
(9, '9', 9, 1, 1, 13508.34, 0, 13508.34, '2015-01-01'),
(10, '10', 10, 2, 2, 20315.07, 0, 20315.07, '2015-01-07'),
(11, '11', 1, 1, 1, 8704.55, 0, 8704.55, '2015-01-01'),
(12, '12', 2, 2, 2, 11198.05, 0, 11198.05, '2015-01-02'),
(13, '13', 3, 1, 1, 4967.84, 0, 4967.84, '2015-01-03'),
(14, '14', 3, 2, 2, 7451.26, 0, 7451.26, '2015-01-04'),
(15, '15', 5, 1, 1, 10747.359, 0, 10747.36, '2015-01-01'),
(16, '16', 6, 2, 2, 13502.34, 0, 13502.34, '2015-01-02'),
(17, '17', 7, 1, 1, 22222.99, 0, 22222.99, '2015-01-03'),
(18, '18', 8, 2, 2, 15465.69, 0, 15465.69, '2015-01-04'),
(19, '19', 9, 1, 1, 4650.64, 0, 4650.64, '2015-01-01'),
(20, '20', 9, 2, 2, 6975.96, 0, 6975.96, '2015-01-02');
-- Item Venda
INSERT INTO ivenda (
    ivenda_id, 
    venda_id, 
    produto_id, 
    ivenda_valor, 
    ivenda_quantidade, 
    ivenda_desconto
) VALUES
(1, 1, 1, 1242.21, 2, 0),
(2, 3, 3, 1241.21, 1, 0),
(3, 3, 4, 1513.77, 4, 0),
(4, 4, 2, 2325.32, 5, 0),
(5, 1, 6, 1251.29, 2, 0),
(6, 2, 2, 1241.21, 6, 0),
(7, 3, 3, 1241.21, 7, 0),
(8, 4, 1, 1251.29, 2, 0),
(9, 5, 3, 1241.21, 2, 0),
(10, 6, 1, 1251.29, 3, 0),
(11, 7, 2, 1242.21, 4, 0),
(12, 8, 5, 2325.32, 5, 0),
(13, 9, 2, 1242.21, 6, 0),
(14, 10, 3, 1241.21, 7, 0),
(15, 11, 1, 1251.29, 1, 0),
(16, 12, 1, 1251.29, 2, 0),
(17, 13, 2, 1242.21, 3, 0),
(18, 14, 2, 1242.21, 4, 0),
(19, 15, 3, 1241.21, 5, 0),
(20, 16, 3, 1241.21, 6, 0),
(21, 17, 4, 1513.77, 7, 0),
(22, 18, 4, 1513.77, 1, 0),
(23, 19, 5, 2325.32, 2, 0),
(24, 20, 5, 2325.32, 3, 0),
(25, 2, 2, 1242.21, 4, 0),
(26, 3, 4, 1513.77, 5, 0),
(27, 4, 2, 1242.21, 6, 0),
(28, 5, 4, 1513.77, 7, 0),
(29, 6, 5, 2325.32, 1, 0),
(30, 7, 3, 1241.21, 2, 0),
(31, 8, 1, 1251.29, 3, 0),
(32, 9, 4, 1513.77, 4, 0),
(33, 10, 5, 2325.32, 5, 0),
(34, 11, 2, 1242.21, 6, 0),
(35, 12, 2, 1242.21, 7, 0),
(36, 13, 3, 1241.21, 1, 0),
(37, 14, 3, 1241.21, 2, 0),
(38, 15, 4, 1513.77, 3, 0),
(39, 16, 4, 1513.77, 4, 0),
(40, 17, 5, 2325.32, 5, 0),
(41, 18, 5, 2325.32, 6, 0);

USE comercial;
-- Secionar todos os dados da tabela
SELECT * FROM cliente;

-- Selecionar campos especificos
SELECT cliente_id, cliente_codigo, cliente_razao
FROM cliente;
-- WHERE
SELECT cliente_razao FROM cliente
WHERE cliente_codigo = '0001';
-- WHERE diferente
SELECT cliente_razao FROM cliente
WHERE cliente_codigo <> '0001';
-- Where Maior
SELECT cliente_razao FROM cliente
WHERE cliente_codigo >= 5;
-- DISTINCT
SELECT DISTINCT cliente_id FROM venda;
-- IN
SELECT cliente_id, cliente_razao FROM cliente
WHERE cliente_id IN (1, 2, 3);
-- NOT IN
SELECT cliente_id, cliente_razao FROM cliente
WHERE cliente_id NOT IN (1, 2, 3);
-- SUBCONSULTA: RAZÃO SOCIAL DE QUEM REALIZOU A COMPRA
SELECT cliente_id FROM venda;
SELECT cliente_razao FROM cliente
WHERE cliente_id IN (
	SELECT cliente_id FROM venda);
    
-- AGREGAÇÃO 
-- COUNT : CONTAR
SELECT COUNT(*) total_clientes FROM cliente;
-- MIN
SELECT MAX(venda_total) maior_venda FROM venda;
SELECT MIN(venda_desconto) menor_desconto FROM venda;

-- SOMAR VENDAS
SELECT SUM(venda_total) FROM venda
WHERE venda_data
BETWEEN '2014-01-01' AND '2015-01-01';

-- MEDIA
SELECT AVG(venda_total) FROM venda;