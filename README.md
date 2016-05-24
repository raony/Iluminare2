# iluminare2

[![Build Status](https://snap-ci.com/raony/Iluminare2/branch/master/build_image)](https://snap-ci.com/raony/Iluminare2/branch/master)

## Rodar local

O projeto roda com python 3 e Django 1.9. É fortemente recomendado que você use
[virtualenv](https://virtualenv.pypa.io/en/latest/) para isolar as dependências.

```
    $ git clone https://github.com/raony/Iluminare2.git
    $ cd Iluminare2
    $ pip install -r configs/core.txt
    $ python manage.py runserver
```

## Staging

Iluminare2 possui um ambiente de staging no Heroku na seguinte URL:

https://iluminare2.herokuapp.com/

Quando um novo push é recebido pelo repositório no Github, o [Snap-CI](https://snap-ci.com)
baixa o código e roda os testes:

```
$ python manage.py test
```

E se os testes passarem, faz o deploy no Heroku.

## Conexão com o Banco de Dados

A conexão é atualizada a partir de uma variável de ambiente, utilizando o
[dj_database_url](https://github.com/kennethreitz/dj-database-url). Se não houver
variável de ambiente com a string de conexão, ele utiliza o que está no `settings.py`
que é um sqlite para teste em ambiente de desenvolvimento.`

Exemplo de string de conexão:

```
$ export DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
```

## Servindo os arquivos estáticos

Arquivos estáticos são servidos pelo [whitenoise](https://github.com/evansd/whitenoise)
diretamente a partir do servidor de aplicação, que no caso é o [gunicorn](http://gunicorn.org/).
