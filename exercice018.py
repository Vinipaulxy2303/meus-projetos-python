import math
angulo=int(input('me de um anguolo:'))
cos=math.cos(math.radians(angulo))
sen=math.sin(math.radians(angulo))
tan=math.tan(math.radians(angulo))
print('Você me de {}ºC\nO cosseno é {:0.3f}\n E o seno é {:0.3f}\n E a tangenete é {:0.3f}'.format(angulo, cos, sen, tan))