
import pickle

shoplistfile = 'shoplist.data'
shoplist = ['Яблоки','Манго','Морковь','Картошка','Киви']
shoplist2 = ['Ogurcu','Mandarinu']

f = open(shoplistfile, 'wb')
pickle.dump(shoplist,f)
pickle.dump(shoplist2,f)
f.close()

del shoplist
del shoplist2

f = open(shoplistfile,'rb')
shoperlist = pickle.load(f)
shoperlist2 = pickle.load(f)
print(shoperlist)
print(shoperlist2)
