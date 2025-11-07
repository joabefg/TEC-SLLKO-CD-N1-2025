# cadastrar aluno 
POST alunos/_doc/56?pretty
{
  "id": "1",
  "nome": "Joab Martins",
  "matricula": 1234,
  "curso": "ciencia de dados"
}

# obter aluno
GET alunos/_doc/1