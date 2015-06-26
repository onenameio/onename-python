# onename-python
Python client for Onename's API

##Documentation:
pip install -r requirements.txt

from lib.client import Client

client = Client(ONENAME_APP_ID, ONENAME_APP_SECRET)


###Definition

GET https://api.onename.com/v1/users/{passnames}

#####Example Request	
	client.get_user('fredwilson')	


#####Example Response

	{
	  "fredwilson": {
	    "profile": {
	      "avatar": {
	        "url": "https://s3.amazonaws.com/kd4/fredwilson1"
	      },
	      "bio": "I am a VC",
	      "bitcoin": {
	        "address": "1Fbi3WDPEK6FxKppCXReCPFTgr9KhWhNB7"
	      },
	      "cover": {
	        "url": "https://s3.amazonaws.com/dx3/fredwilson"
	      },
	      "facebook": {
	        "proof": {
	          "url": "https://facebook.com/fred.wilson.963871/posts/10100401430876108"
	        },
	        "username": "fred.wilson.963871"
	      },
	      "graph": {
	        "url": "https://s3.amazonaws.com/grph/fredwilson"
	      },
	      "location": {
	        "formatted": "New York City"
	      },
	      "name": {
	        "formatted": "Fred Wilson"
	      },
	      "twitter": {
	        "proof": {
	          "url": "https://twitter.com/fredwilson/status/533040726146162689"
	        },
	        "username": "fredwilson"
	      },
	      "v": "0.2",
	      "website": "http://avc.com"
	    },
	    "verifications": [
	      {
	        "identifier": "fredwilson",
	        "proof_url": "https://twitter.com/fredwilson/status/533040726146162689",
	        "service": "twitter",
	        "valid": true
	      },
	      {
	        "identifier": "fred.wilson.963871",
	        "proof_url": "https://facebook.com/fred.wilson.963871/posts/10100401430876108",
	        "service": "facebook",
	        "valid": true
	      }
	    ]
	  }
	}


###Definition
POST https://api.onename.com/v1/users

#####Example Request:
	payload = {'passname' : 'fredwilson', 'recipient_address' : 'N6zdUCKq1gJaps76gagBbC5Vc6xBxMdvHc', 'passcard' : {'bio' : 'I am a VC'}}

	client.register_user(payload)

#####Example Response:
	{
	    "status": "success"
	}


###Definition
GET https://api.onename.com/v1/search

#####Example Request

	client.get_search('wenger')

#####Example Response:

	{
	  "results": [
	    {
	      "profile": {
	        "avatar": {
	          "url": "https://pbs.twimg.com/profile_images/1773890030/aew_artistic_bigger.gif"
	        },
	        "bio": "VC at USV.com",
	        "bitcoin": {
	          "address": "1QHDGGLEKK7FZWsBEL78acV9edGCTarqXt"
	        },
	        "cover": {
	          "url": "https://s3.amazonaws.com/dx3/albertwenger"
	        },
	        "facebook": {
	          "proof": {
	            "url": "https://www.facebook.com/albertwenger/posts/10152554952070219"
	          },
	          "username": "albertwenger"
	        },
	        "github": {
	          "proof": {
	            "url": "https://gist.github.com/albertwenger/03c1b5db3880998115fa"
	          },
	          "username": "albertwenger"
	        },
	        "graph": {
	          "url": "https://s3.amazonaws.com/grph/albertwenger"
	        },
	        "location": {
	          "formatted": "New York"
	        },
	        "name": {
	          "formatted": "Albert Wenger"
	        },
	        "twitter": {
	          "proof": {
	            "url": "https://twitter.com/albertwenger/status/499594071401197568"
	          },
	          "username": "albertwenger"
	        },
	        "v": "0.2",
	        "website": "http://continuations.com"
	      },
	      "username": "albertwenger"
	    }
	  ]
	}


###Definition
GET https://api.onename.com/v1/users

#####Example Request:
	client.get_stats()

#####Example Response

	{
	  "stats": {
	    "registrations": "29235"
	  }
	}

###Definition

POST https://api.onename.com/v1/transactions

####Example Request

	payload = {"signed_hex" : "00710000015e98119922f0b"}

	client.broadcast_transaction(payload)

####Example Response

	{
	    "status": "success"
	}


###Definition

GET https://api.onename.com/v1/addresses/{address}

####Example Request

	client.get_address('N8PcBQnL4oMuM6aLsQow6iG59yks1AtQX4')

####Example Response

	{
	  "names_owned": [], 
	  "unspent_outputs": [
	    {
	      "amount": 99.995, 
	      "scriptPubKey": {
	        "addresses": [
	          "NBSffD6N6sABDxNooLZxL26jwGetiFHN6H"
	        ], 
	        "asm": "OP_DUP OP_HASH160 a31521da4d3df0d48a7aa7e1d8dadf0e0e862d8d OP_EQUALVERIFY OP_CHECKSIG", 
	        "hex": "76a914a31521da4d3df0d48a7aa7e1d8dadf0e0e862d8d88ac", 
	        "reqSigs": 1, 
	        "type": "pubkeyhash"
	      }, 
	      "txid": "e06501a48267c26e0ccf85823531be2301291cf582d1e422a69db5a59033e6e5", 
	      "vout": "1"
	    }, 
	    {
	      "amount": 378.26213117, 
	      "scriptPubKey": {
	        "addresses": [
	          "NBSffD6N6sABDxNooLZxL26jwGetiFHN6H"
	        ], 
	        "asm": "OP_DUP OP_HASH160 a31521da4d3df0d48a7aa7e1d8dadf0e0e862d8d OP_EQUALVERIFY OP_CHECKSIG", 
	        "hex": "76a914a31521da4d3df0d48a7aa7e1d8dadf0e0e862d8d88ac", 
	        "reqSigs": 1, 
	        "type": "pubkeyhash"
	      }, 
	      "txid": "3e3926dd5dc42a3f2d41139bf650d15becfe77bd2143071b09b9b22ca88ad55d", 
	      "vout": "1"
	    }
	  ]
	}

