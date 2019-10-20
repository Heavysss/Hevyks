# Незаконченная программа которая должна выводить погоду и температуру на экран
# Хз что тут не так делал всё как в инструкции(Скорее всего нет)))

from pyowm import OWM

API_key = '5880dd4978294824c9eee84271852002'
owm = OWM(API_key)

owm_ru = OWM(language='ru') # Russian
from pyowm.caches.lrucache import LRUCache
cache = LRUCache()

obs = owm.weather_at_place('Kiev')
w = obs.get_weather()
w.get_temperature(u'celsius')['temp']

print(w)