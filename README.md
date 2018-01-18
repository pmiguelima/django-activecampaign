django-activecampaign
===================

Instalação
-------------
```bash
$ pip install django-activecampaign==0.1.2
```

Após a instalação configure seu settings.py:

```python
    #settings.py

    INSTALLED_APPS = [
        ...
        'activecampaign',
    ]
```
E adicione as seguintes variaveis no mesmo arquivo:

```python
    #settings.py

    ACTIVECAMPAIGN_PATH = ''
    ACTIVECAMPAIGN_PASS = ''
    ACTIVECAMPAIGN_SENDER_NAME = ''
    ACTIVECAMPAIGN_SENDER_ADDR1 = ''
    ACTIVECAMPAIGN_SENDER_CITY = ''
    ACTIVECAMPAIGN_SENDER_COUNTRY = ''
    ACTIVECAMPAIGN_SENDER_COUNTRY = ''
    ACTIVECAMPAIGN_FROMMAIL = ''
    ACTIVECAMPAIGN_NAME = ''
    ACTIVECAMPAIGN_REPLAY = ''
```
Execute as migrações caso queira armazenar os dados em seu banco de dados:

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```


