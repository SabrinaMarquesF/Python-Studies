medida = float(input('Distância em metros'))
cm = medida * 100
mm = medida * 1000
km = medida/1000
dam = medida/10
hm = medida/1000
print('A distância em {}m é igual a {} cm e {} mm'.format(medida, cm,mm))
print('E possui {}km, {}dam e {}hm'.format(km, dam, hm))