<div align="center">

![Status](https://img.shields.io/badge/Status-Finalizado-%109955c1?style=for-the-badge)
# GMaps Scrapper
</div>
<div style="text-align:justify;">
Este é um Web Scrapper que coleta o nome, endereço e telefone de restaurantes listados no GoogleMaps

</div>

<div align="center">

![Issues](https://img.shields.io/github/issues/Chamoouske/GMapsScraping) ![Forks](https://img.shields.io/github/forks/Chamoouske/GMapsScraping) ![Stars](https://img.shields.io/github/stars/Chamoouske/GMapsScraping) ![Licence](https://img.shields.io/github/license/Chamoouske/GMapsScraping) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
</div>

---
<div align="center">

## Menu de navegação
</div>

- [Pré-requisitos](#pré-requisitos)
    - [Instalação dos pré-requisitos](#instalação-dos-pré-requisitos)
    - [Rodar a aplicação](#rodar-a-aplicação)
    - [Criação do arquivo exe](#criação-do-arquivo-exe)
    - [Descrição do comando de criação do exe](#descrição-do-comando)
- [Principais tecnologias utilizadas](#principais-tecnologias-utilizadas)
- [Autor](#autor)
- [Licença](#sob-a-licença-mit)

---
<div align="center">

## Pré-requisitos
</div>
<div style="text-align:justify;">
A explicação começará supondo que você já tem o Python instalado na sua máquina. 

>- [Aqui](https://python.org.br/instalacao-windows/) ensina instalar o Python no Windows.
>- [Aqui](https://python.org.br/instalacao-linux/) ensina instalar o Python no Linux.

> Para informações adicionais, acesse o [Site Oficial](https://www.python.org/) do Python.
</div>

### Instalação dos pré-requisitos

```bash
# Clone o repositório
git clone https://github.com/Chamoouske/GMapsScraping.git

# Acesse a pasta do projeto
cd GMapsScraping

# Crie um ambiente virtual (opcional)
python -m venv venv

# Instale as depêndencias
pip install -r requeriments.txt

```

### Rodar a aplicação
```bash
python main.py
```

### Criação do arquivo .exe
[Aqui](https://drive.google.com/drive/folders/1OQH8bnTqI_qp6aat5kBNqVbJdrsUd11n) você pode baixar o exe deste projeto, sem precisar criar manualmente.
```bash
pyinstaller main.py -n GMapsScrapper --onefile -w -i ./data/app.ico

```
### Descrição do comando:
- <code>pyinstaller</code> - É chamada da Lib pyinstaller, que cria o arquivo .exe.
- <code>main.py</code> - É nome do arquivo principal da aplicação (o arquivo central da aplicação).
- <code>-n GMapsScrapper</code> - <code>-n</code> é a flag do pyinstaller para definir o nome que será colocado no arquivo exe, aqui, o nome colocado foi <code>GMapsScrapper</code>.
- <code>--onefile</code> - É a flag que gera apenas um arquivo exe, e não uma pasta com vários arquivos, como uma instalação padrão realizada por vários softwares.
- <code>-w</code> - É a flag que indica que não será aberta uma janela do bash,pois usamos a biblioteca TKinter para a criar uma janela para o usuário interagir.
- <code>-i ./data/app.ico</code> - <code>-i</code> é a flag para definir o caminho para o arquivo que será usado como ícone do exe (opcional).

---
<div align="center">

## Principais tecnologias utilizadas
</div>

- [Python](https://www.python.org/)
- [Selenium](https://selenium-python.readthedocs.io/index.html)

---
<div align="center">

## Autor
<a href='https://github.com/Chamoouske' target="_blank">
<img src="https://github.com/Chamoouske.png" style="width:100px; border-radius:50%" />
</a>

Feito com ❤️ por [Ajax Lima](https://github.com/Chamoouske)

[![Twitter Badge](https://img.shields.io/badge/-@chamoouske-1ca0f1?style=flat-square&labelColor=1ca0f1&logo=twitter&logoColor=white&link=https://twitter.com/chamoouske)](https://twitter.com/chamoouske) [![Linkedin Badge](https://img.shields.io/badge/-Ajax%20Lima-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/ajaxlima/)](https://www.linkedin.com/in/ajaxlima/) [![Gmail Badge](https://img.shields.io/badge/-ajaxlima94@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:ajaxlima94@gmail.com)](mailto:ajaxlima94@gmail.com)

---
## Sob a licença [MIT](/LICENSE)
![Licence](https://img.shields.io/github/license/Chamoouske/PrintersMaintenanceFlask)
</div>