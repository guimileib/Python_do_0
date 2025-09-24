# 🐍 Python do Zero

Um projeto completo de estudos em Python, estruturado em 30 dias de aprendizado progressivo (futuramente pode ter mais rs), cobrindo desde os conceitos básicos até tópicos avançados como orientação a objetos, APIs e manipulação de arquivos.

## 📚 Sobre o Projeto

Este repositório contém exercícios práticos organizados por dias, onde cada pasta representa um dia de estudos com conceitos específicos e exercícios aplicados. O objetivo é proporcionar uma jornada completa de aprendizado em Python, ideal para iniciantes que querem dominar a linguagem de forma estruturada.

## 🗂️ Estrutura do Projeto

```
python_zero/
├── 01/ - Introdução ao Python
├── 02/ - Variáveis e Tipos de Dados
├── 03/ - Operadores Matemáticos
├── 04/ - Entrada de Dados (Input)
├── 05/ - Estruturas Condicionais
├── 06/ - Laços de Repetição (While)
├── 07/ - Listas e Laços (For)
├── 08/ - Dicionários
├── 09/ - Funções
├── 10/ - Tratamento de Exceções
├── 11/ - Manipulação de Arquivos
├── 12/ - Módulos e Números Aleatórios
├── 13/ - Bibliotecas Externas (ASCII Art)
├── 14/ - Requisições HTTP e APIs
├── 15/ - Projeto: Consultor de Clima
├── 16/ - Introdução à Programação Orientada a Objetos
├── 17/ - Herança
├── 18/ - Polimorfismo
└── 19/ - [Em Desenvolvimento]
```

## 📖 Detalhamento dos Dias

### Dia 01 - Introdução ao Python
**Arquivo:** `01/print.py`

**Conceitos:**
- Função `print()`
- Função `input()`
- Formatação com f-strings

**Exercícios:**
- Hello World
- Captura e exibição de nome e idade do usuário

---

### Dia 02 - Variáveis e Tipos de Dados
**Arquivo:** `02/var.py`

**Conceitos:**
- Tipos de dados: `str`, `int`, `float`, `bool`
- Conversão de tipos
- Entrada de dados com validação

**Exercícios:**
- Criação de variáveis para nome, idade, altura e status de estudante
- Conversão e exibição de diferentes tipos de dados

---

### Dia 03 - Operadores Matemáticos
**Arquivo:** `03/calculadora.py`

**Conceitos:**
- Operadores aritméticos: `+`, `-`, `*`, `/`, `**`, `%`
- Operador módulo para verificar paridade

**Exercícios:**
- Calculadora básica com duas variáveis
- Verificador de números pares/ímpares usando módulo

---

### Dia 04 - Entrada de Dados (Input)
**Arquivo:** `04/input.py`

**Conceitos:**
- Função `input()` avançada
- Formatação com f-strings
- Conversão de tipos em entrada de dados

**Exercícios:**
- Programa de boas-vindas personalizado
- Calculadora de dobro com conversão de tipos

---

### Dia 05 - Estruturas Condicionais
**Arquivo:** `05/conditionals.py`

**Conceitos:**
- Estruturas `if`, `elif`, `else`
- Operadores de comparação
- Lógica condicional

**Exercícios:**
- Verificador de maioridade
- Sistema de notas com aprovação/recuperação/reprovação

---

### Dia 06 - Laços de Repetição (While)
**Arquivo:** `06/while.py`

**Conceitos:**
- Laço `while`
- Controle de fluxo
- Validação com repetição

**Exercícios:**
- Contagem regressiva de 10 a 1
- Sistema de senha com validação contínua

---

### Dia 07 - Listas e Laços (For)
**Arquivo:** `07/list.py`

**Conceitos:**
- Listas em Python
- Laço `for`
- Função `range()`

**Exercícios:**
- Exibição de números de 1 a 10
- Lista de tarefas com iteração

---

### Dia 08 - Dicionários
**Arquivo:** `08/dict.py`

**Conceitos:**
- Estrutura de dicionários
- Chaves e valores
- Método `.get()` para busca segura

**Exercícios:**
- Perfil de contato com informações pessoais
- Tradutor inglês-português com busca segura

---

### Dia 09 - Funções
**Arquivo:** `09/function.py`

**Conceitos:**
- Definição de funções com `def`
- Parâmetros e argumentos
- Retorno de valores com `return`

**Exercícios:**
- Função de saudação simples
- Calculadora de área de retângulo com parâmetros

---

### Dia 10 - Tratamento de Exceções
**Arquivo:** `10/exception.py`

**Conceitos:**
- Blocos `try` e `except`
- Tipos específicos de exceções (`ValueError`, `ZeroDivisionError`)
- Tratamento de erros múltiplos

**Exercícios:**
- Calculadora de dobro com tratamento de entrada inválida
- Divisão com tratamento de erro de divisão por zero

---

### Dia 11 - Manipulação de Arquivos
**Arquivos:** `11/arquivos.py`, `11/lista_compras.txt`

**Conceitos:**
- Abertura e fechamento de arquivos
- Modos de abertura: `'a'` (append), `'r'` (read)
- Context manager com `with`

**Exercícios:**
- Sistema de lista de compras com persistência
- Leitura e exibição de arquivo com numeração

---

### Dia 12 - Módulos e Números Aleatórios
**Arquivos:** `12/aleatorio.py`, `12/lista.py`

**Conceitos:**
- Importação de módulos (`import random`)
- Geração de números aleatórios
- Escolha aleatória de elementos

**Exercícios:**
- Jogo de adivinhação com números aleatórios
- Sugestão aleatória de restaurantes

---

### Dia 13 - Bibliotecas Externas (ASCII Art)
**Arquivo:** `13/ascii.py`

**Conceitos:**
- Instalação de pacotes com `pip`
- Biblioteca `pyfiglet`
- Diferentes fontes de texto ASCII

**Exercícios:**
- Conversão de nome para ASCII art
- Gerador de texto ASCII com fontes personalizadas (slant, starwars)

---

### Dia 14 - Requisições HTTP e APIs
**Arquivos:** `14/api.py`, `14/api2.py`

**Conceitos:**
- Biblioteca `requests`
- Consumo de APIs REST
- Tratamento de respostas JSON
- Códigos de status HTTP

**Exercícios:**
- Consultor de CEP usando API ViaCEP
- Cotação do dólar usando AwesomeAPI

---

### Dia 15 - Projeto: Consultor de Clima
**Arquivos:** `15/clima-check.py`, `15/historico.txt`

**Conceitos:**
- Projeto completo integrando múltiplos conceitos
- API de clima (wttr.in)
- Manipulação de datas com `datetime`
- Arquivos de log e histórico
- Estruturação de código com funções

**Exercícios:**
- Sistema completo de consulta meteorológica
- Histórico de pesquisas com timestamp
- Tratamento robusto de erros de API

---

### Dia 16 - Introdução à Programação Orientada a Objetos
**Arquivos:** `16/cachorro.py`, `16/banco.py`

**Conceitos:**
- Classes e objetos
- Método `__init__` (construtor)
- Atributos e métodos
- Instanciação de objetos

**Exercícios:**
- Classe `Cachorro` com métodos de comportamento
- Classe `ContaBancaria` com operações financeiras

---

### Dia 17 - Herança
**Arquivos:** `17/inheritance.py`, `17/inheritance2.py`

**Conceitos:**
- Herança de classes
- Função `super()`
- Sobrescrita de métodos
- Hierarquia de classes

**Exercícios:**
- Sistema de funcionários com classe `Gerente` herdando de `Funcionario`
- Hierarquia de veículos com comportamentos específicos

---

### Dia 18 - Polimorfismo
**Arquivos:** `18/polymorphism.py`, `18/polymorphism2.py`

**Conceitos:**
- Polimorfismo em Python
- Sobrescrita de métodos
- Interface comum com comportamentos diferentes
- Uso de listas com objetos polimórficos

**Exercícios:**
- Sistema de banda com instrumentos musicais
- Calculadora de áreas para formas geométricas diferentes

---

### Dias 19-30 - Em Desenvolvimento
Os próximos dias do projeto incluirão tópicos avançados como:
- Decoradores
- Geradores
- Programação funcional
- Banco de dados
- Frameworks web
- Testes unitários
- E muito mais!

## 🚀 Como Usar Este Projeto

1. **Clone o repositório:**
   ```bash
   git clone [url-do-repositorio]
   cd python_zero
   ```

2. **Execute os exercícios:**
   ```bash
   # Para executar um dia específico
   python 01/print.py
   ```

3. **Instale dependências quando necessário:**
   ```bash
   # Para o Dia 13
   pip install pyfiglet
   
   # Para os Dias 14 e 15
   pip install requests
   ```

## 📋 Pré-requisitos

- Python 3.6 ou superior
- Acesso à internet (para exercícios com APIs)
- Editor de código (recomendado: VS Code, PyCharm)

## 🎯 Objetivos de Aprendizado

Ao final dos 30 dias, você terá domínio sobre:

- ✅ Sintaxe básica do Python
- ✅ Estruturas de dados (listas, dicionários)
- ✅ Estruturas de controle (if/else, loops)
- ✅ Funções e modularização
- ✅ Tratamento de exceções
- ✅ Manipulação de arquivos
- ✅ Consumo de APIs
- ✅ Programação orientada a objetos
- ✅ Herança e polimorfismo
- 🔄 Tópicos avançados (em desenvolvimento)

## 🤝 Contribuição

Este é um projeto de estudos pessoal, mas sugestões e melhorias são sempre bem-vindas! Sinta-se livre para:

- Reportar bugs
- Sugerir novos exercícios
- Melhorar a documentação
- Propor tópicos para os próximos dias

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

Desenvolvido com ❤️ durante a jornada de aprendizado em Python.

---

**Happy Coding! 🐍✨**