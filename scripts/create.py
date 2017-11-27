from mininet.net import Mininet
from mininet.node import RemoteController, OVSKernelAP
from mininet.link import TCLink
from random import randint
'''from multiprocessing import Process, Queue
import multiprocessing as mp'''


def create(count_st, count_ap):
    mini = Mininet(controller=RemoteController, link=TCLink, accessPoint=OVSKernelAP)

    list_st = []
    for x in range(1, count_st+1):
        list_st.append(mini.addStation("sta"+str(x), mac='00:00:00:00:00:0'+str(x), ip='10.0.0.'+str(x)+'/8'))

    list_ap = []
    for y in range(1, count_ap+1):
        list_ap.append(mini.addAccessPoint('ap'+str(y), ssid='test_ssid'+str(y), mode='g', channel=str(y+1), position=str(randint(0, 100))+','+str(randint(0, 100))+',0'))

    c1 = mini.addController('c1', controller=RemoteController)

    mini.configureWifiNodes()
    mini.plotGraph(max_x=100, max_y=100)
    mini.seed(20)

    "*** Available models: RandomWalk, TruncatedLevyWalk, RandomDirection, RandomWayPoint, GaussMarkov, ReferencePoint, TimeVariantCommunity ***"
    mini.startMobility(time=0, model='RandomDirection', max_x=100, max_y=100, min_v=0.5, max_v=0.8)

    print "*** Starting network"
    mini.build()
    c1.start()
    for x in range(0, count_ap):
        list_ap[x].start([c1])


create(3, 1)
