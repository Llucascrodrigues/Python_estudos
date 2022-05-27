import math
import numpy as np
import matplotlib.pyplot as pt

cartesiano=np.array(([1,0,0],[0,1,0],[0,0,1]))
w=(float(input('angulo rotacionado do no ref em graus ')))
w=np.deg2rad(w)

ref_rot=np.array(([math.cos(w),-math.sin(w),0],[math.sin(w),math.cos(w),0],[0,0,1]))
ref_novo=np.dot(cartesiano,ref_rot)
print(np.around(ref_novo,2))

#imprimir o gráfico
#pt.plot(x,y)
#pt.show()
