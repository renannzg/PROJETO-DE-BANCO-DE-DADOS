```
# 📝 Sistema de Gerenciamento de Tarefas

Um sistema simples de **gerenciamento de tarefas** desenvolvido em **Python**, utilizando **Oracle Database** para armazenamento de dados. Este projeto foi criado como trabalho de faculdade para demonstrar **operações CRUD**, relatórios com **sumarização e junção de tabelas** e um **menu interativo** no terminal.

---

## 📋 Descrição

O sistema permite gerenciar **usuários** e **tarefas** associadas a eles, com funcionalidades como:

- Inserção, remoção e atualização de usuários e tarefas  
- Relatórios com sumarização (ex.: total de tarefas por usuário)  
- Relatórios com junção de tabelas (ex.: lista de tarefas com nome do usuário)  
- Verificação automática de registros nas tabelas ao iniciar  
- Menu interativo constante, conforme requisitos do trabalho  

**Grupo:** Renan Miguel e Matheus Rhamet  
**Objetivo Acadêmico:** Atender aos requisitos do trabalho de faculdade, incluindo splash screen, verificação de registros e menus personalizados

---

## 🚀 Funcionalidades

- **Splash Screen:** Exibe o nome da aplicação e do grupo ao iniciar  
- **Verificação de Registros:** Conta registros nas tabelas `USUARIOS` e `TAREFAS` usando `SELECT COUNT(1)`  
- **Relatórios:**  
  - Total de tarefas por usuário (`GROUP BY`)  
  - Lista de tarefas com nome do usuário (`JOIN`)  
- **Inserir Registros:** Adiciona usuários ou tarefas, com opção de inserir múltiplos  
- **Remover Registros:** Lista e remove usuários/tarefas, verificando **chaves estrangeiras (FK)**  
- **Atualizar Registros:** Edita atributos de usuários/tarefas e exibe o resultado atualizado  
- **Menu Principal:** Navegação constante entre opções, com submenus para cada funcionalidade

---

## 📋 Pré-requisitos

- **Python 3.8+**  
- **Oracle Database** (ex.: Oracle XE ou Express Edition)  
- **Biblioteca `oracledb`** para Python  

```bash
pip install oracledb
```

- Acesso ao banco com:  
  ```
  usuário: labdatabase
  senha: labdatabase
  DSN: localhost/XEPDB1
  ```
- Cliente Oracle como **DBeaver** (opcional)

---

## 🛠️ Instalação

1. Clone o repositório:  
```bash
git clone https://github.com/seu-usuario/sistema-gerenciamento-tarefas.git
cd sistema-gerenciamento-tarefas
```

2. Instale as dependências:  
```bash
pip install oracledb
```

3. Configure o Oracle:  
- Certifique-se que o Oracle está rodando e acessível via `localhost/XEPDB1`  
- Crie o usuário `labdatabase` com senha `labdatabase` ou ajuste as credenciais no `conexion.py`

---

## 📖 Como Usar

1. Crie as tabelas e insira dados iniciais:  
```bash
python criar_tabelas_e_dados.py
```  
Isso cria as tabelas `USUARIOS` e `TAREFAS`, sequências, triggers e insere dados de exemplo

2. Execute o sistema principal:  
```bash
python principal.py
```  
- O **splash screen** será exibido, seguido da **verificação de registros**  
- Navegue pelas opções do **menu principal**:

```
===== MENU PRINCIPAL =====
1 - Relatórios
2 - Inserir registros
3 - Remover registros
4 - Atualizar registros
5 - Sair
```

---

## 📁 Estrutura do Projeto

```
sistema-gerenciamento-tarefas/
├── conexion.py               # Classe OracleConnection para conectar e executar queries
├── criar_tabelas_e_dados.py # Script para criar tabelas, sequências, triggers e inserir dados
├── principal.py             # Menu principal e lógica do sistema
└── README.md                # Este arquivo
```

---

## 🐛 Solução de Problemas

- **Erro de conexão:** Verifique se o Oracle está rodando e o DSN está correto. Teste com DBeaver  
- **Tabelas não encontradas:** Execute `criar_tabelas_e_dados.py` primeiro  
- **Erro TypeError:** Certifique-se que `conexion.py` está atualizado (método `query` deve retornar uma lista)  
- **Permissões:** Garanta que o usuário Oracle tenha privilégios para criar tabelas e executar queries  
- **Dependências:** Se `oracledb` não instalar, atualize o pip:  
```bash
pip install --upgrade pip
```

---

## 🤝 Contribuição

Contribuições são bem-vindas:

1. Fork o repositório  
2. Crie uma branch para sua feature:  
```bash
git checkout -b feature/nova-funcionalidade
```
3. Commit suas mudanças:  
```bash
git commit -m "Adiciona nova funcionalidade"
```
4. Push para a branch:  
```bash
git push origin feature/nova-funcionalidade
```
5. Abra um Pull Request

---

## 📄 Licença

Este projeto é para fins **educacionais** e não possui licença específica. Use por sua conta e risco
```
