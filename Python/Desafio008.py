medida = float(input('Uma distancia em metros'))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida de  {} metros possui {},KM\n{},HM\n{},DAM\n{},DM\n{},CM\n{},MM'.format(medida, km, hm, dam, dm, cm, mm))