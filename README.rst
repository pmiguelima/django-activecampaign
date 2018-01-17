=====
ActiveCampaign
=====

...

Quick start
-----------

1. Add "activecampaign" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'activecampaign',
    ]

2. Add configurations to your setting::

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

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create campaigns (you'll need the Admin app enabled).