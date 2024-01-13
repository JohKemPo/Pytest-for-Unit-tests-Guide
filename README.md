
<div align="center">
  <img src="[README] images/pytest.png"width=" 150px">
  <img src="[README] images/python.png"width=" 150px">
  <h1>Guia prático de Testes unitáriso com Pytest</h1>
</div>

<p align = "justify"> &emsp; Este repositório fornece um guia sobre testes unitários utilizando o framework Pytest. A estrutura pytest facilita a gravação de testes pequenos e legíveis e pode ser dimensionada para suportar testes funcionais complexos para aplicativos e bibliotecas.</p>


<h2 align="center">S U M A R I O</h2>
<br>

1. [Instalação e configuração do Pytest.](#capitulo1)
    1. [Instalação](#subcapitulo1_1)
1. [Estrutura básica de um teste usando Pytest.](#capitulo2)
    1. [Caixa de ferramentas](#subcapitulo2_1)
1. [Asserts e verificações de testes.](#capitulo3)
    1. [Subcapitulo](#subcapitulo3_1):
        - Tópico
1. [Fixtures e configurações de teste.](#capitulo4)
    1. [Subcapitulo](#subcapitulo4_1):
        - Tópico
1. [Execução e relatórios de testes.](#capitulo5)
    1. [Subcapitulo](#subcapitulo5_1):
        - Tópico
1. [Apêndice](#apendice)
    1. [Ambiente virtual](#env):
        - [Miniconda](#miniconda)
        - [Venv](#venv)

<br><hr>

<!-- CAPITULO 1 -->

<h2 id="capitulo1">Instalação do Pytest e organização:</h2>
<h3 id="subcapitulo1_1">Instalação</h3>
<p align = "justify"> &emsp; Para começar, certifique-se de ter o Python e o gerenciador de pacotes pip instalados em seu sistema. Em seguida, execute o seguinte comando no terminal para instalar o Pytest:
</p>


```bash
# requeriments.txt
pytest==x.x.x    
pytest-cov==x.x.x   
pytest-mock==x.x.x  
pytest-watch==x.x.x     
pytest-xdist==x.x.x     
```

- Instalação das bibliotecas:

```bash
pip install -r requeriments.txt
```
Configurações de ambiente, acesse a seção [Ambiente virtual](#env).

<h3 id="">Estrutura de diretórios</h3>
<p align = "justify"> &emsp;Organize seu projeto em uma estrutura de diretórios. Por exemplo:</p>

```bash
Projeto/
├── app/
│   ├── utils/
│   │   ├── __init__.py
│   │   └── util.py
│   ├── __init__.py
│   └── codigo.py
├── tests/
│   ├── utils/
│   │   └── test_util.py
│   └── test_codigo.py
└── requirements.txt
```

<h3 id="">Descoberta de testes em Python</h3>

Pytest implementa a seguinte descoberta de teste padrão, os nomes dos testes devem seguir o modelo `test_*.py` or `*_test.py`, [Mais informações na documentação](https://docs.pytest.org/en/7.4.x/explanation/goodpractices.html#test-discovery).

<!-- CAPITULO 2 -->

<h2 id="capitulo2">Estrutura básica de um teste usando Pytest:</h2>
<h3 id="subcapitulo2_1">Subcapitulo</h3>
<p align = "justify"> &emsp;Organize seu projeto em uma estrutura de diretórios. Por exemplo:</p>


<!-- CAPITULO 3 -->

<h2 id="capitulo3">Fixtures e configurações de teste:</h2>
<h3 id="subcapitulo3_1">Subcapitulo</h3>
<p align = "justify"> &emsp;Organize seu projeto em uma estrutura de diretórios. Por exemplo:</p>

<!-- CAPITULO 4 -->

<h2 id="capitulo4">Execução e relatórios de testes:</h2>
<h3 id="subcapitulo4_1">Subcapitulo</h3>
<p align = "justify"> &emsp;Organize seu projeto em uma estrutura de diretórios. Por exemplo:</p>

<!-- APENDICE -->

<h2 id="apendice">Apêndice </h2>

<h3 id="env">Criação  de Ambiente Virtual em Python e instalação das dependências</h3>

**`Crie somente um ambiente virtual, após isso instale as dependências descritas na fase de instalação de dependências.`**

<br>
<h3 id="miniconda">(Opçãp 1) Criação - miniconda:</h3>

1. Baixar o instalador miniconda:
```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```
2. Executando o instalador:
```
bash Miniconda3-latest-Linux-x86_64.sh
```
3. Iniciar coda:
```
conda init
```
4. Listar env existentes:
```
conda env list
```
5. Criar env com pytoh3.10:
```
conda create -n <name env> python=3.10
```
6. Ativar env:
```
conda activate <name env>
```

7. Deletar .sh
```
rm Miniconda3-latest-Linux-x86_64.sh
```

<br>
<h3 id="venv">(Opçãp 2) Criação - venv:</h3>

Para criar um ambiente virtual em Python, você pode usar a biblioteca padrão chamada `venv`. Siga as etapas abaixo para criar e ativar um ambiente virtual usando o `venv`:

1. Verifique se o Python 3 está instalado:
Abra o terminal e execute o seguinte comando:
```
python3 --version
```
2. Se o Python 3 já estiver instalado, você verá a versão instalada. Caso contrário, siga para o próximo passo.

3. Instale o Python 3:

No terminal, execute os comandos apropriados de acordo com a distribuição Linux que você está usando.

```
sudo apt install python3
```

4. Instale o pip:

```
sudo apt install python3-pip
```

5. Instale o pacote venv:
O pacote venv permite criar ambientes virtuais isolados. No terminal, execute o seguinte comando:

```
sudo apt install python3-venv
```

6. Para criação do ambiente virtual:
Navegue até o diretório onde deseja criar o ambiente virtual.

7. Digite o seguinte comando para criar um novo ambiente virtual:

```
python3 -m venv nome_do_ambiente
```

*Substitua "nome_do_ambiente" pelo nome que você deseja dar ao seu ambiente virtual.*

8. Para ativar o ambiente virtual, execute o comando apropriado de acordo com o seu sistema operacional:

```
source nome_do_ambiente/bin/activate
```

9. Agora, o ambiente virtual está ativado. Você pode instalar pacotes e executar seus projetos dentro dele sem afetar o ambiente global do Python.

Quando você terminar de trabalhar com o ambiente virtual, pode desativá-lo usando o comando:

```
deactivate
```

### **Extra**

Configurar para conda sempre inciarlizar em uma determinada env:

```
conda env list
export CONDA_DEFAULT_ENV="/caminho/para/env"
```

### **Instalação das dependências**

1. Instalação das dependências do projeto no **ambiente virtual**:

```
# instalar bibliotecas especificadas em um único arquivo
pip install -r requirements.txt

# instalar bibliotecas especificadas em multiplos arquivos
pip install -r requirements_1.txt -r requirements_2.txt
```
  
<br>
<h1 id="Equipe">Equipe</h1><br>

<div align="center">

|     Desenvolvedor              |           GitHub             |       LinkedIn     |
|--------------------------------|------------------------------|--------------------|
|👤 João Vitor Moraes            |<https://github.com/JohKemPo>   |<https://www.linkedin.com/in/joao-vitor-de-moraes/>|
</div>
