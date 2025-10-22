Sistema de Gerenciamento de Tarefas
Python Oracle

Um sistema simples de gerenciamento de tarefas desenvolvido em Python, utilizando Oracle Database para armazenamento de dados. Este projeto foi criado como trabalho de faculdade para demonstrar operações CRUD (Create, Read, Update, Delete), relatórios com sumarização e junção de tabelas, e um menu interativo no terminal.

📋 Descrição
O sistema permite gerenciar usuários e tarefas associadas a eles. Inclui funcionalidades como:

Inserção, remoção e atualização de usuários e tarefas.
Relatórios com sumarização (ex.: total de tarefas por usuário) e junção de tabelas (ex.: lista de tarefas com nome do usuário).
Verificação automática de registros nas tabelas ao iniciar.
Menu interativo constante, conforme requisitos do trabalho.
Grupo: Renan Miguel e João Silva (substitua pelos nomes reais do grupo).
Objetivo Acadêmico: Atender aos requisitos de um trabalho de faculdade, incluindo splash screen, verificação de registros e menus personalizados.

🚀 Funcionalidades
Splash Screen: Exibe o nome da aplicação e do grupo ao iniciar.
Verificação de Registros: Conta registros nas tabelas USUARIOS e TAREFAS usando SELECT COUNT(1).
Relatórios:
Total de tarefas por usuário (sumarização com GROUP BY).
Lista de tarefas com nome do usuário (junção com JOIN).
Inserir Registros: Adiciona usuários ou tarefas, com opção de inserir múltiplos.
Remover Registros: Lista e remove usuários/tarefas, verificando chaves estrangeiras (FK) para evitar inconsistências.
Atualizar Registros: Edita atributos de usuários/tarefas, exibindo o resultado atualizado.
Menu Principal: Navegação constante entre opções, com submenus para cada funcionalidade.
📋 Pré-requisitos
Python 3.8 ou superior instalado.
Oracle Database rodando (ex.: Oracle XE ou Express Edition).
Biblioteca oracledb para conexão com Oracle:
Instale via pip: pip install oracledb
Acesso ao banco com usuário labdatabase e senha labdatabase (DSN: localhost/XEPDB1). Ajuste no código se necessário.
Cliente Oracle como DBeaver para verificação (opcional).
🛠️ Instalação
Clone ou baixe o repositório:
git clone https://github.com/seu-usuario/sistema-gerenciamento-tarefas.git
cd sistema-gerenciamento-tarefas
Instale as dependências:

bash

Run
Copy code
pip install oracledb
Configure o Oracle:

Certifique-se de que o Oracle está rodando e acessível via localhost/XEPDB1.
Crie o usuário labdatabase com senha labdatabase se necessário (ou ajuste as credenciais no conexion.py).
📖 Como Usar
Crie as tabelas e insira dados iniciais:

bash

Run
Copy code
python criar_tabelas_e_dados.py
Isso cria as tabelas USUARIOS e TAREFAS, sequências, triggers e insere dados de exemplo.
Execute o sistema principal:

bash

Run
Copy code
python principal.py
Aparecerá o splash screen, verificação de registros e o menu principal.
Navegue pelas opções (1-5) para relatórios, inserção, remoção, atualização ou sair.
Exemplo de Uso:
Menu Principal:

Run
Copy code
===== MENU PRINCIPAL =====
1 - Relatórios
2 - Inserir registros
3 - Remover registros
4 - Atualizar registros
5 - Sair
Escolha: 1
Relatórios: Escolha entre sumarização ou junção.
Inserir: Selecione entidade (usuário ou tarefa) e insira dados.
Remover/Atualizar: Lista registros, selecione por número e confirme.
📁 Estrutura do Projeto

Run
Copy code
sistema-gerenciamento-tarefas/
├── conexion.py              # Classe OracleConnection para conectar e executar queries
├── criar_tabelas_e_dados.py # Script para criar tabelas, sequências, triggers e inserir dados
├── principal.py             # Menu principal e funções do sistema
└── README.md                # Este arquivo
conexion.py: Gerencia conexão com Oracle, métodos para executar queries e commits.
criar_tabelas_e_dados.py: Script único para setup inicial do banco.
principal.py: Interface do usuário com menus e lógica de negócio.
🐛 Solução de Problemas
Erro de conexão: Verifique se o Oracle está rodando e o DSN está correto. Teste com DBeaver.
Tabelas não encontradas: Execute criar_tabelas_e_dados.py primeiro.
Erro "TypeError: 'NoneType' object is not subscriptable": Certifique-se de que conexion.py está atualizado (método query deve retornar uma lista).
Permissões: Garanta que o usuário Oracle tem privilégios para criar tabelas e executar queries.
Dependências: Se oracledb não instalar, use pip install --upgrade pip e tente novamente.
🤝 Contribuição
Contribuições são bem-vindas! Para contribuir:

Fork o repositório.
Crie uma branch para sua feature (git checkout -b feature/nova-funcionalidade).
Commit suas mudanças (git commit -m 'Adiciona nova funcionalidade').
Push para a branch (git push origin feature/nova-funcionalidade).
Abra um Pull Request.
📄 Licença
Este projeto é para fins educacionais e não possui licença específica. Use por sua conta e risco.
