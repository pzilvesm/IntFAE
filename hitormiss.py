import numpy 

x = numpy.random.uniform(low=0.0, high=1.0 , size= 1000)
y = numpy.random.uniform(low=0.0, high=1.0 , size= 1000)


inside_disk = x**2+y**2<1


disk_area = numpy.sum(inside_disk)/1000
print(disk_area)