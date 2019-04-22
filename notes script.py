import pandas as pd
import requests

r = requests.get('https://api.github.com/events')
r.text