#Author: Team Code-ologists
import numpy
import matplotlib.pyplot


def bubbleSort(num_list):
    '''
    This fun() will sort the list provided as argument.
    And after each iteration barGraph() will be involked
    '''
    for posi in xrange(0, len(num_list) - 1, 1):
        for posj in xrange(0, len(num_list) - 1 - posi, 1):
            print num_list
            if num_list[posj] > num_list[posj+1]:
                num_list[posj], num_list[posj+1] = num_list[posj+1], num_list[posj]
            barGraph(num_list, posi+1, posj+1)

    return num_list


def barGraph(num_list, posi, posj):
    '''
    This fun() will create a new bar graph for every iteration
    passed to it
    '''
    N = len(num_list)
    ind = numpy.arange(N)
    width = 0.5
    matplotlib.pyplot.bar(ind, num_list, width, color='b')
    matplotlib.pyplot.xlabel("Iteration : %d" % (posi))
    matplotlib.pyplot.pause(0.5)
    matplotlib.pyplot.show()
    matplotlib.pyplot.gcf().clear()

if __name__ == '__main__':
    '''
    Main fun(), execution starts here
    '''
    num_list = [
        10, 5, 8,
        4 , 1, 9
        ]
    print num_list
    matplotlib.pyplot.ion()
    bubbleSort(num_list)
