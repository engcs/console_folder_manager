<h1 align="center">CONSOLE PARA AUTOMAÇÃO DE PASTAS DE CLIENTES</h1>

<p align="center">Aplicação destinada a automatizar parte do processo real da gestão de pastas <br> de clientes para um pequeno negócio local
de prestação de serviços.</p>

<p align="center">
 <a href="#recursos">Recursos</a> •
 <a href="#rodando-a-aplicação">Rodando a Aplicação</a> •
 <a href="#tecnologias">Tecnologias</a> •
 <a href="#personalização-do-menu-de-contexto-no-windows">Personalização do Menu de Contexto no Windows</a> •
 <a href="#autor">Autor</a>
</p>

---

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Made with python" height="30">
  <img src="http://ForTheBadge.com/images/badges/made-with-python.svg" alt="Made with python" height="30" align="right">
  <img src="http://ForTheBadge.com/images/badges/built-with-love.svg" alt="Made with python" height="30" align="right">
</p>
<br>

## Recursos
- [x] Listagem, criação e remoção de pastas de cliente :tada:
- [x] Visualização e edição de detalhes para cada cliente :tada:
- [x] Formatação de mensagens com colorização :tada:
- [x] Makefile para automação de pequenas tarefas :tada:
- [x] Personalização do menu de contexto do Windows para rodar em qualquer pasta :tada:
- [x] Testes unitários do utils.py :tada:

### Funcionamento

* É possível listas as pastas de cliente, que neste caso estavam no formato padronizado `CLT0000`.
A criação de pastas com templates e autonumeração faz partes das features.

* Também é possível visualizar detalhes do cliente por meio do carregamento de um arquivo '.yaml' dentro de cada pasta de cliente 'CLT'

* A edição dos arquivos de detalhe '.yaml' pode ser realizada usando a opção "editar detalhes", que chama o notepad do Windows.

## Rodando a Aplicação
asdasd

### Pré-Requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Python](https://www.python.org/).

## Tecnologias
asdasd

## Personalização do Menu de Contexto no Windows

Também foi adicionado um script para adicionar a chamada da aplicação pricipal por meio do menu de contexto,
clicando em uma área vazia da pasta.

Não foi testado com versões anteriores ao Windows 10, mas muito provavelmente é compatível.

Para adicionar o menu, basta rodar o Makefile dentro da pasta raiz do projeto da seguinte forma:

```bash
# Para registrar a chave do menu de contexto execute o seguinte comando dentro da pasta raiz da aplicação
$ make registrar-menu
```

## Autor
<div>
  <p align="center">
    <img title="CRISTIAN SOUSA" src="https://avatars.githubusercontent.com/engcs" height="100" width="100" />
  </p>
  <p align="center" >
    Made with 💜 <br>by CRISTIAN SOUSA 👋
  </p>
</div>
