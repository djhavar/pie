import matplotlib.pyplot as plt

activities = ['eat','sleep','work','play']

slices=['2','8','7','7']

activities  =['blue','green','yellow','red']

plt.pie(slices,labels = activities  ,colors=activities, 
        startangle=91,shadow=False, explode = (0,0,0,0) ,radius=1.0,autopct='%0.00001f%%')

plt.legend()            

plt.show()                                                                                                                                                                










































































































r