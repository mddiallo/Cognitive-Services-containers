import requests

from pprint import pprint

sentiment_uri = "http://localhost:5000/text/analytics/v3.0/sentiment"

documents = {'documents' : [
  {'id': '1', 'language': 'en', 'text': 'I had a wonderful experience! The rooms were wonderful and the staff was helpful.'},
  {'id': '2', 'language': 'en', 'text': 'I had a terrible time at the hotel. The staff was rude and the food was awful.'},  
  {'id': '3', 'language': 'es', 'text': 'Los caminos que llevan hasta Monte Rainier son espectaculares y hermosos.'},
  {'id': '4', 'language': 'fr', 'text': 'Nous sommes tres content du service fourni par le prestataire du diner'},  
  {'id': '5', 'language': 'es', 'text': 'La carretera estaba atascada. Había mucho tráfico el día de ayer.'}
]}

response  = requests.post(sentiment_uri, json=documents)
languages = response.json()

pprint(languages)