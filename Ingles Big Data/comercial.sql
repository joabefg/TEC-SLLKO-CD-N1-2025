-- sistema para vendas de produtos --
-- create database comercial;


-- # 01. CRIAR TABELAS
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

-- lista as colunas de uma tabela
-- desc cliente

-- alterar tabela
--   adicionar auto increment inicial
--   ALTER TABLE cliente AUTO_INCREMENT=100;

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
     vendedor_comissao float(10,2), -- era porc, mas preferi comissão para saber de que é a porcentagem
primary key(vendedor_id));

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

-- não existe
create table vendas(
     venda_id int not null auto_increment,
     venda_codigo varchar(10),
     cliente_id int not null,
     fornecedor_id int not null,
     vendedor_id int not null,
     venda_valor float(10,2),
     venda_descricao float(10,2),
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

-- alterar tabela
alter table ivenda DROP COLUMN ivenda_descricao;
alter table ivenda add COLUMN ivenda_desconto float(10,2);

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

-- deletar constraint
-- ALTER TABLE ivenda DROP FOREIGN KEY fk_ivenda_produto;

-- # 03. POPULAR BANCO
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

INSERT INTO vendedor (vendedor_id, vendedor_codigo, vendedor_nome, vendedor_razao, vendedor_contato, vendedor_comissao) VALUES
(1, '0001', 'CARLOS FERNANDES', 'CARLOS FERNANDES LTDA', '(47) 7535-8144', 12.00),
(2, '0002', 'JÚLIA GOMES', 'JÚLIA GOMES LTDA', '(12) 8037-6661', 25.00);

INSERT INTO fornecedor (fornecedor_id, fornecedor_codigo, fornecedor_nome, fornecedor_razao, fornecedor_contato) VALUES
(1, '0001', 'DUN RITE LAWN MAINTENANCE', 'DUN RITE LAWN MAINTENANCE LTDA', '(85) 7886-8837'),
(2, '0002', 'SEWFRO FABRICS', 'SEWFRO FABRICS LTDA', '(91) 5171-8483');

INSERT INTO produto (produto_id, produto_codigo, produto_descricao, produto_valor, produto_situacao, fornecedor_id) VALUES
(1, '123131', 'NOTEBOOK', 1251.29, 'A', 1),
(2, '123223', 'SMARTPHONE', 1242.21, 'A', 2),
(3, '1231', 'DESKTOP', 1241.21, 'A', 1),
(4, '142123', 'TELEVISÃO', 2564.92, 'A', 2),
(5, '7684', 'DRONE', 2325.32, 'A', 1),
(6, '159876', 'MONITOR GAMER', 1251.29, 'A', 1);

-- alterado a tabela produto
INSERT INTO produto (produto_id, produto_codigo, produto_descricao, produto_valor, produto_situacao, fornecedor_id) VALUES
(6, '159876', 'MONITOR GAMER', 1251.29, 'A', 1);

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
(15, '15', 5, 1, 1, 10747.359, 0, 10747.36, '2015-01-01'), -- Arredondado para 2 casas
(16, '16', 6, 2, 2, 13502.34, 0, 13502.34, '2015-01-02'),
(17, '17', 7, 1, 1, 22222.99, 0, 22222.99, '2015-01-03'),
(18, '18', 8, 2, 2, 15465.69, 0, 15465.69, '2015-01-04'),
(19, '19', 9, 1, 1, 4650.64, 0, 4650.64, '2015-01-01'),
(20, '20', 9, 2, 2, 6975.96, 0, 6975.96, '2015-01-02');

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

-- alterar um registro
update comclien set c_nomeclien = 'AARONSON FURNITURE'
     , c_cidaclien = 'LONDRINA'
     , c_estaclien = 'PR'
     where n_numeclien = 1;
commit;
rollback;

-- remover um registro
delete from comclien where n_numeclien = 1;
commit;

-- # 03. SELECT

-- Selecionar todos os itens de uma tabela.
select * from cliente;
-- Selecionar campos específicos de uma tabela.
select cliente_id, cliente_codigo, cliente_razao
from cliente;
-- WHERE: Usado para utilizar condições na hora de buscar registros
select cliente_id, cliente_codigo, cliente_razao
from cliente
where cliente_codigo = '0001';
-- DIFERENTE
select n_numeclien, c_codiclien, c_razaclien
from comclien
where c_codiclien <> '0001';
-- MAIOR QUE
select cliente_id, cliente_codigo, cliente_razao
from cliente
where cliente_id > 5;
-- DISTINCT: Buscar itens não repetidos
-- Buscar somente os clientes que tiveram vendas
SELECT cliente_id from venda; -- sem DISTINCT trás tudo
SELECT DISTINCT cliente_id from venda; -- com DISTINCT trás somente um registro por pessoa
-- IN: Usado para buscar comparando com mais de um valor
-- Buscar somente clientes com id 1 e 2
SELECT cliente_id, cliente_razao FROM cliente WHERE cliente_id = 1; -- igual só funciona com um registro
SELECT cliente_id, cliente_razao FROM cliente WHERE cliente_id IN (1,2); -- in faz o mesmo, mas com vários registros
-- NOT IN: Faz o opostro, busca trazendo todos os registros, exceto os especificados
-- Buscar todos os clientes EXCETO os com id 1 e 2
SELECT cliente_id, cliente_razao FROM cliente WHERE cliente_id NOT IN (1,2);
-- SUBQUERY/SUBCONSULTA: Permite fazer um select dentro de outro select
-- Trazer a razão social (que só existe na tabela cliente) dos clientes que efetuaram compras (só existe na tabela venda)
SELECT cliente_id FROM venda WHERE cliente_id; -- retorna só os ids
SELECT cliente_razao FROM cliente WHERE cliente_id IN (
    SELECT cliente_id FROM venda WHERE cliente_id -- não tem vírgula
);
-- Trazer o mesmo do anterior, desta vez dos clientes que não efetuaram compras
SELECT cliente_razao FROM cliente WHERE cliente_id NOT IN (
    SELECT cliente_id FROM venda WHERE cliente_id -- não tem vírgula
);
-- Trazer o código da venda e a razão do cliente de todas as vendas
SELECT venda_id, (
    SELECT cliente_razao FROM cliente WHERE cliente_id = venda.venda_id) Nome_Cliente
FROM venda;
-- Alias: dá um nome para a coluna, independente se ela já tem um nome, só vale na query executada, fora não muda.
-- usado em nomes grandes, iguais ou funç~eos
SELECT cliente_id CODIGO, cliente_nome cliente 
FROM cliente WHERE cliente_id NOT IN (1,2,3,4)

-- JOIN SIMPLES
-- Buscas utilizando mais de uma tabela
SELECT cliente_nome, cliente_razao, venda_id 
FROM venda, cliente 
WHERE venda.cliente_id = cliente.cliente_id 
ORDER BY razão

-- FUNÇÕES 
--   AGREGAÇÃO
--   Agrupam vários dados mas só retorna uma informação. (ex. count, max, media)

-- 1. FUNÇÕES DE CÁLCULOS
-- a. round(): Arredonda valores, mas pode passar a qtd de casas decimais para limitar (arredondando)
SELECT round(venda_total, 1) -- 1 casa decimal
FROM venda;
-- b. format(): Formata valores, mas pode passar a qtd de casas decimais para limitar (corta)
SELECT format(venda_total, 1) -- 1 casa decimal
FROM venda;
-- c. truncate(): Omite casas decimais (corta)
SELECT truncate(venda_total, 1) -- 1 casa decimal
FROM venda;
-- d. funções de cálculo E funções de agregação
SELECT avg(venda_total)
FROM venda; -- sem truncate: 12213.964453
SELECT truncate(avg(venda_total), 2)
FROM venda;

-- 2. FUNÇÕES DE DATA
-- Servem principalmente para buscar registros em um determinado período. Vendas de hoje, antes de hoje.
-- a. curdate(): retorna apenas a data atual.
SELECT curdate();
-- b. curtime(): retorna apenas a hora atual.
SELECT curtime();
-- c. now(): retorna a datz e hora atual.
SELECT now(); -- UTC-0
-- d. datediff(): retorna o intervalo entre duas datas. OBS: COMO USAR COM VARIÁVEIS VINDO DO BANCO?
SELECT datediff('2025-02-01', '2025-01-01');
SELECT datediff('2025-02-01', '2025-01-01') 'PERÍODO DE INSCRIÇÃO';
-- e. date_add(): adiciona um período a uma data. de x até 30 dias depois.
SELECT date_add('2023-02-01', interval 31 day);
-- f. dayname(): retorna o dia da semana, ideal para não precisar ficar salvando dia da semana no banco.
SELECT dayname('2025-01-01');
-- g. extract(): retorna parte da data
SELECT EXTRACT(YEAR FROM '2019-07-02');
SELECT EXTRACT(MONTH FROM '2019-07-02 01:02:03');
SELECT EXTRACT(DAY_MINUTE FROM '2019-07-02 01:02:03');
-- h. get_format(): retorna um padrão dia.mês.ano (o formato brasileiro não é legal por causa da barra)
SELECT date_format('2025-01-10',get_format(date,'EUR'));

-- 3. FUNÇÕES DE AGREGAÇÃO
-- a. count(): conta o número total de itens de venda registrados.
SELECT COUNT(ivenda_id) FROM ivenda;
-- b. distinct(): conta quantos itens diferentes foram vendidos.
SELECT COUNT(DISTINCT produto_id) FROM comercial.ivenda;
-- c. avg: mostra a média de vários valores passados.
SELECT AVG(ivenda_valor) FROM comercial.ivenda;
-- d. Soma (SUM) - Total Bruto : Calcula o valor total bruto de todas as vendas (antes dos descontos).
SELECT SUM(venda_valor) FROM comercial.venda;	
-- e. Soma (SUM) - Quantidade: Calcula a quantidade total de produtos vendidos.
SELECT SUM(ivenda_quantidade) FROM comercial.ivenda;	
-- f. Máximo (MAX) - Valor: Encontra a venda de maior valor (o total final da venda).
SELECT MAX(venda_total) FROM comercial.venda;
-- g. Mínimo (MIN) - Valor: Encontra a venda de menor valor (o total final da venda).
SELECT MIN(venda_total) FROM comercial.venda;	
-- h. Máximo (MAX) - Desconto	: Encontra o maior desconto individual aplicado em um item.
SELECT MAX(ivenda_desconto) FROM comercial.ivenda;	
-- i. Soma (SUM) - Desconto Total: Calcula o valor total de todos os descontos concedidos.
SELECT SUM(ivenda_desconto * ivenda_quantidade) FROM comercial.ivenda;	
-- j. Média (AVG) - Total Final: Calcula o valor total final médio de todas as transações de venda.
SELECT AVG(venda_total) FROM comercial.venda;

-- 4. AGREGAÇÃO COM GROUP BY
-- O GROUP BY agrupa as linhas que têm os mesmos valores nas colunas especificadas, e então as funções de agregação calculam um valor para cada grupo.
-- a. Vendas por Cliente: Conta o número de vendas realizadas por cada cliente.
SELECT cliente_id, COUNT(venda_id) AS total_vendas FROM comercial.venda GROUP BY cliente_id;	
-- b. Total Vendido por Vendedor: Calcula o valor total de vendas que cada vendedor realizou.
SELECT vendedor_id, SUM(venda_total) AS valor_total FROM comercial.venda GROUP BY vendedor_id;	
-- c. Quantidade Vendida por Produto: Soma a quantidade total de cada produto individual vendido.
SELECT produto_id, SUM(ivenda_quantidade) AS total_unidades FROM comercial.ivenda GROUP BY produto_id;	
-- d. Máximo Desconto por Venda: Encontra o maior desconto aplicado dentro de cada venda específica.
SELECT venda_id, MAX(ivenda_desconto) AS maior_desconto FROM comercial.ivenda GROUP BY venda_id;	
-- e. Média de Vendas por Data: Calcula a média de valor das vendas por dia.
SELECT DATE(venda_data) AS data_venda, AVG(venda_total) AS media_diaria FROM comercial.venda GROUP BY data_venda;	

-- 5. JOIN
-- Os JOINs combinam linhas de duas ou mais tabelas com base em uma coluna relacionada, como chaves primárias e estrangeiras.
-- a. INNER JOIN
--   Venda + Cliente: Lista o ID da Venda e o Nome do Cliente que a realizou. Só lista vendas que têm clientes e clientes que fizeram vendas.
SELECT v.venda_id, c.cliente_nome FROM comercial.venda v INNER JOIN comercial.cliente c ON v.cliente_id = c.cliente_id;
--   Item + Produto: Exibe o ID do item da venda e a descrição do produto vendido.
SELECT iv.ivenda_id, p.produto_descricao FROM comercial.ivenda iv INNER JOIN comercial.produto p ON iv.produto_id = p.produto_id;	
--   Venda + Vendedor: Exibe o ID da Venda e o Nome do Vendedor responsável.
SELECT v.venda_id, vd.vendedor_nome FROM comercial.venda v INNER JOIN comercial.vendedor vd ON v.vendedor_id = vd.vendedor_id;
--   Vendas Detalhadas (3 Tabelas): Combina Venda, Cliente e Vendedor para mostrar uma visão completa da transação.
SELECT v.venda_id, c.cliente_nome, vd.vendedor_nome FROM comercial.venda v INNER JOIN comercial.cliente c ON v.cliente_id = c.cliente_id INNER JOIN comercial.vendedor vd ON v.vendedor_id = vd.vendedor_id;	
-- b. LEFT JOIN
-- Todos os Produtos e suas Vendas: Lista todos os produtos (tabela da esquerda), e a quantidade se foi vendido. Se o produto nunca foi vendido, a quantidade será NULL.
SELECT p.produto_descricao, iv.ivenda_quantidade FROM comercial.produto p LEFT JOIN comercial.ivenda iv ON p.produto_id = iv.produto_id;	
-- Todos os Clientes e suas Vendas: Lista todos os clientes, mesmo aqueles que nunca fizeram uma venda (venda_id será NULL).
SELECT c.cliente_nome, v.venda_id FROM comercial.cliente c LEFT JOIN comercial.venda v ON c.cliente_id = v.cliente_id;
-- c. RIGHT JOIN
--   Todos os Vendedores e suas Vendas: Lista todos os vendedores (tabela da direita), mesmo que não tenham feito nenhuma venda (venda_total será NULL).
SELECT vd.vendedor_nome, v.venda_total FROM comercial.venda v RIGHT JOIN comercial.vendedor vd ON v.vendedor_id = vd.vendedor_id;	
-- d. FULL OUTER JOIN (TODOS AMBOS LADOS)
--   Fornecedores e Produtos (Conceitual): Lista todos os fornecedores (mesmo os que não fornecem produto) e todos os produtos (mesmo os que não têm fornecedor registrado).
SELECT f.fornecedor_nome, p.produto_descricao FROM comercial.fornecedor f FULL OUTER JOIN comercial.produto p ON f.fornecedor_id = p.fornecedor_id;	
-- e. SELF JOIN
--   Produtos do Mesmo Fornecedor: Lista pares de produtos que são fornecidos pelo mesmo fornecedor. O p1.produto_id < p2.produto_id é para evitar duplicatas e o par consigo mesmo.
SELECT p1.produto_descricao AS produto_a, p2.produto_descricao AS produto_b, p1.fornecedor_id FROM comercial.produto p1 INNER JOIN comercial.produto p2 ON p1.fornecedor_id = p2.fornecedor_id AND p1.produto_id < p2.produto_id;	
-- f. CROSS JOIN
-- Todos com Todos: Combina cada vendedor com cada fornecedor, gerando uma lista de todas as combinações possíveis. Use com cautela, pois pode gerar muitos resultados.
SELECT vd.vendedor_nome, f.fornecedor_nome FROM comercial.vendedor vd CROSS JOIN comercial.fornecedor f;	


 Entendendo a Cláusula JOIN no SQLA 
 cláusula JOIN é um dos conceitos mais fundamentais e poderosos em SQL. 
 Ela permite combinar colunas e linhas de duas ou mais tabelas em um banco de dados relacional, com base em um relacionamento (geralmente uma chave estrangeira) entre elas.
 Em essência, um JOIN está dizendo: "Mostre-me os dados da Tabela A e os dados da Tabela B onde o valor na coluna de ligação da Tabela A é igual ao valor na coluna de ligação da Tabela B."
 🔑 O Ponto de Ligação: Chaves Estrangeiras
     O JOIN é quase sempre realizado usando as chaves:
     Chave Primária (Primary Key - PK): Um identificador único em uma tabela (ex: cliente_id na tabela cliente).
     Chave Estrangeira (Foreign Key - FK): Uma coluna em uma tabela que referencia a chave primária de outra tabela (ex: cliente_id na tabela venda).
     A sintaxe básica para ligar as tabelas A e B é: 
          SELECT colunas FROM Tabela_A [TIPO DE JOIN] Tabela_B ON Tabela_A.chave_estrangeira = Tabela_B.chave_primaria;
4️⃣ Tipos Principais de JOIN
     Existem quatro tipos principais de JOINs, que se diferenciam pela forma como lidam com as linhas que não possuem correspondência na outra tabela.

     1. INNER JOIN (Interseção)
     O INNER JOIN retorna apenas as linhas que têm correspondência em ambas as tabelas. É o tipo de JOIN mais comum e mais restritivo.O que retorna: Apenas a interseção dos dados. Se um registro existe na Tabela A, mas não tem correspondência na Tabela B, ele é excluído do resultado. 
     -- Retorna apenas as vendas que têm um cliente registrado E clientes que fizeram pelo menos uma venda.
     SELECT v.venda_id, c.cliente_nome FROM comercial.venda v INNER JOIN comercial.cliente c ON v.cliente_id = c.cliente_id;

     2. LEFT JOIN ou LEFT OUTER JOIN (Todos da Esquerda)
     O LEFT JOIN retorna todas as linhas da tabela da esquerda (a primeira tabela listada no FROM) e as linhas correspondentes da tabela da direita.O que retorna: Se não houver correspondência na tabela da direita, as colunas da tabela da direita terão o valor NULL.
     Quando usar: Para listar TUDO da Tabela A e, se houver, os detalhes correspondentes da Tabela B.
     -- Retorna TODOS os produtos. Se um produto não foi vendido, ivenda_id será NULL.
     SELECT p.produto_descricao, iv.ivenda_id FROM comercial.produto p LEFT JOIN comercial.ivenda iv ON p.produto_id = iv.produto_id;

     3. RIGHT JOIN ou RIGHT OUTER JOIN (Todos da Direita)
     O RIGHT JOIN é o oposto do LEFT JOIN. Ele retorna todas as linhas da tabela da direita e as linhas correspondentes da tabela da esquerda.
     O que retorna: Se não houver correspondência na tabela da esquerda, as colunas da tabela da esquerda terão o valor NULL.
     Quando usar: Para listar TUDO da Tabela B e, se houver, os detalhes correspondentes da Tabela A.
     -- Retorna TODOS os vendedores. Se um vendedor não fez nenhuma venda, venda_id será NULL.
     SQLSELECT v.venda_id, vd.vendedor_nome FROM comercial.venda v RIGHT JOIN comercial.vendedor vd ON v.vendedor_id = vd.vendedor_id;

     4. FULL JOIN ou FULL OUTER JOIN (Todos de Ambas)
     O FULL JOIN retorna todas as linhas quando há uma correspondência em uma das tabelas. É a união completa das duas tabelas.
     O que retorna: Linhas correspondentes são unidas; linhas que não correspondem são preenchidas com NULL na tabela onde o registro está ausente.Quando usar: Para ver todos os registros, independentemente de haver correspondência.
     -- Retorna todos os clientes (mesmo sem venda) e todas as vendas (mesmo se o cliente fosse desconhecido).
     SELECT c.cliente_nome, v.venda_id FROM comercial.cliente c FULL JOIN comercial.venda v ON c.cliente_id = v.cliente_id;

     5. SELF JOIN (Junção Própria)
     O SELF JOIN é simplesmente um JOIN normal (geralmente um INNER JOIN) onde uma tabela é ligada a si mesma.
     Uso: É essencial quando uma tabela contém uma relação hierárquica ou quando você precisa comparar registros dentro da mesma tabela.
     Requisito: É obrigatório usar aliases diferentes (apelidos como t1 e t2) para a mesma tabela, para que o SQL possa diferenciá-las.
     -- Comparar produtos que têm o mesmo fornecedor.
     SELECT p1.produto_descricao, p2.produto_descricao
     FROM comercial.produto p1
     INNER JOIN comercial.produto p2
     ON p1.fornecedor_id = p2.fornecedor_id
     AND p1.produto_id < p2.produto_id; -- Garante que não haja duplicatas (A, B) e (B, A)

     6. CROSS JOIN (Produto Cartesiano)
     O CROSS JOIN combina cada linha da primeira tabela com cada linha da segunda tabela.
     O que retorna: Um conjunto de resultados que é o produto cartesiano do número de linhas. Se A tem $N$ linhas e B tem $M$ linhas, o resultado terá $N \times M$ linhas.
     Uso: Raramente usado em consultas de dados, mas útil para gerar todas as combinações possíveis entre conjuntos de dados.
     SELECT vd.vendedor_nome, f.fornecedor_nome
     FROM comercial.vendedor vd
     CROSS JOIN comercial.fornecedor f;
     -- Cada vendedor é listado com CADA fornecedor.