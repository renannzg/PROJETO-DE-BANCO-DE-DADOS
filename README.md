# PROJETO-DE-BANCO-DE-DADOs
# Sistema de Gerenciamento de Tarefas

### Descrição Geral

O **Sistema de Gerenciamento de Tarefas** é uma aplicação desenvolvida em **Python** com base de dados **Oracle**, cujo objetivo é permitir o cadastro, controle e acompanhamento de tarefas atribuídas a diferentes usuários.  
O projeto foi estruturado seguindo o modelo relacional proposto pelo professor, utilizando scripts SQL para criação do banco de dados e scripts Python para manipulação e consulta dos dados.



### Estrutura do Sistema

O sistema é composto por duas entidades principais:

- **USUÁRIOS**: responsáveis por armazenar as informações dos usuários cadastrados no sistema (nome e e-mail).  
- **TAREFAS**: responsável por armazenar as informações das tarefas associadas aos usuários (título, descrição, datas, status e responsável).

Cada tarefa pertence a um usuário, e essa relação é garantida por meio de chave estrangeira.



### 🗂 Organização do Projeto

#### 1. Diretório `diagrams/`
Contém o **diagrama relacional (lógico)** do sistema, representando as entidades, atributos e relacionamentos entre as tabelas `USUARIOS` e `TAREFAS`.

#### 2. Diretório `sql/`
Contém os scripts responsáveis pela criação da estrutura do banco de dados e inserção de registros de exemplo:

- **create_tables_tarefas.sql**: cria as tabelas, relacionamentos, sequences e triggers necessárias para o funcionamento do sistema.  
- **inserting_sample_records.sql**: insere dados fictícios para fins de teste e validação do sistema.

> Antes de executar os scripts, é importante garantir que o usuário do banco possua privilégios suficientes.  
> Caso necessário, o comando `GRANT ALL PRIVILEGES TO LABDATABASE;` pode ser executado por um usuário com permissões administrativas.

#### 3. Diretório `src/`
Contém todo o código-fonte da aplicação Python, organizado de forma modular.

**Subdiretórios principais:**

- **conexion/**  
  Contém o módulo de conexão com o banco de dados Oracle, encapsulando as operações de conexão, execução de consultas e comandos SQL.

- **controller/**  
  Contém as classes responsáveis pelas operações de CRUD (Create, Read, Update, Delete) sobre as tabelas do banco de dados.

- **model/**  
  Contém as classes que representam as entidades do sistema, como `Usuario` e `Tarefa`.

- **reports/**  
  Contém as classes responsáveis pela geração de relatórios, como listagem de tarefas e estatísticas por usuário.

- **utils/**  
  Contém scripts auxiliares, como configurações iniciais e funções de apoio ao sistema.

**Scripts principais:**
- `create_tables_and_records.py`: executa automaticamente a criação das tabelas e a inserção dos dados iniciais.  
- `principal.py`: representa o ponto de entrada do sistema, exibindo o menu principal e interagindo com os módulos de CRUD e relatórios.  
- `test.py`: utilizado para testar a conexão com o banco de dados e validar o módulo de conexão.


### Requisitos e Dependências

O sistema foi desenvolvido em **Python 3.12** e utiliza as seguintes bibliotecas principais:

- **oracledb**: responsável pela comunicação entre o Python e o banco de dados Oracle.  
- **pandas**: utilizada para exibir resultados de consultas em formato de tabelas estruturadas.  
- **tabulate** *(opcional)*: auxilia na formatação dos relatórios em texto.

As dependências podem ser instaladas de acordo com o arquivo `requirements.txt`.



### Banco de Dados Oracle

O banco de dados foi modelado em conformidade com o modelo relacional e implementado em Oracle.  
Para ambientes Linux baseados em Debian, recomenda-se a instalação do **Oracle Instant Client** para permitir a comunicação entre o Python e o Oracle Database.

> Caso ocorra o erro `ORA-28001: the password has expired`, deve-se redefinir a senha e ajustar a política de expiração com os comandos SQL apropriados.



### Relatórios e Funcionalidades

O sistema oferece as seguintes funcionalidades principais:

- **Cadastro de usuários**  
- **Cadastro de tarefas** associadas a usuários  
- **Listagem geral de tarefas com responsável**  
- **Atualização de status das tarefas**  
- **Exclusão de tarefas concluídas ou obsoletas**  
- **Relatórios automáticos**, como:
  - Total de tarefas por usuário  
  - Tarefas pendentes, em andamento e concluídas  

Essas funcionalidades são acessadas por meio do menu interativo da aplicação Python.

es_and_records.py
