# onename-python

Python client for Onename's API

### Getting started

```
pip install -r requirements.txt
```

```python
from lib.client import Client

client = Client(ONENAME_APP_ID, ONENAME_APP_SECRET)
```

### API Calls

```python
user_profile = client.get_user('fredwilson')
```

```python
registration_payload = {'passname' : 'fredwilson', 'recipient_address' : 'N6zdUCKq1gJaps76gagBbC5Vc6xBxMdvHc', 'passcard' : {'bio' : 'I am a VC'}}
registration_status = client.register_user(registration_payload)
```

```python
search_results = client.get_search('wenger')
```

```python
user_stats = client.get_stats()
```

```python
payload = {"signed_hex" : "00710000015e98119922f0b"}
client.broadcast_transaction(payload)
```

```python
address = client.get_address('N8PcBQnL4oMuM6aLsQow6iG59yks1AtQX4')
```