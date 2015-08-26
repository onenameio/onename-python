# onename-python

Python client for Onename's API

### Installation

```
$ pip install onename
```

### Setting up the API Client

```python
>>> from onename import OnenameClient
>>> onename_client = OnenameClient(ONENAME_APP_ID, ONENAME_APP_SECRET)
```

### API Calls

```python
>>> user_profile = onename_client.get_users(['fredwilson', 'naval'])
```

```python
>>> search_results = onename_client.search_users('wenger')
```

```python
>>> registration_payload = {'passname': 'fredwilson', 'recipient_address': 'N6zdUCKq1gJaps76gagBbC5Vc6xBxMdvHc', 'passcard': {'bio': 'I am a VC'}}
>>> onename_client.register_user(registration_payload)
{"status": "success"}
```

```python
>>> user_data = onename_client.get_all_users()
```

```python
>>> onename_client.get_user_stats()
{"stats": {"registrations": "31804"}}
```

```python
>>> payload = {"signed_hex": "00710000015e98119922f0b"}
>>> onename_client.broadcast_transaction(payload)
{"status": "success"}
```

```python
>>> unspents = onename_client.get_unspents('N8PcBQnL4oMuM6aLsQow6iG59yks1AtQX4')
```

```python
>>> names = onename_client.get_names('N8PcBQnL4oMuM6aLsQow6iG59yks1AtQX4')
```

```python
>>> dkim_info = onename_client.get_dkim_info('onename.com')
```
