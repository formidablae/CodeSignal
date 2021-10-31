mainimport numpy
def newRoadSystem(roadRegister):
    npRoadRegister = numpy.array(roadRegister)
    for i in range(len(roadRegister)):
        if numpy.count_nonzero(npRoadRegister[i,:]) != numpy.count_nonzero(npRoadRegister[:,i]): return False
    return True