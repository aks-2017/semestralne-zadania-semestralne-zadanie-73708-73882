from mininet.net import Mininet
from mininet.node import Controller, OVSKernelAP
from mininet.link import TCLink
from random import randint
import Node


class MiniWifi:
    mini = 0

    def __init__(self):
        self.mini = Mininet(controller=Controller, link=TCLink, accessPoint=OVSKernelAP)

    def create(self, count_st, count_ap):
        list_st = []
        for x in range(1, count_st+1):
            list_st.append(self.mini.addStation("sta"+str(x), mac='00:00:00:00:00:0'+str(x), ip='10.0.0.'+str(x)+'/8', range=30))

        list_ap = []
        for y in range(1, count_ap+1):
            list_ap.append(self.mini.addAccessPoint('ap'+str(y), ssid='test_ssid'+str(y), mode='g', channel=str(y+1), position=str(randint(0, 100))+','+str(randint(0, 100))+',0', range=70))

        c1 = self.mini.addController('c1', controller=Controller)

        self.mini.configureWifiNodes()

        for x in range(0, count_ap):
            for y in range(x, count_ap):
                if x == y:
                    continue
                else:
                    self.mini.addLink(list_ap[x], list_ap[y])

        self.mini.plotGraph(max_x=100, max_y=100)
        self.mini.seed(20)

        "*** Available models: RandomWalk, TruncatedLevyWalk, RandomDirection, RandomWayPoint, GaussMarkov, ReferencePoint, TimeVariantCommunity ***"
        self.mini.startMobility(time=0, model='RandomDirection', max_x=100, max_y=100, min_v=0.5, max_v=0.8, range=50)

        print "*** Starting network"
        self.mini.build()
        c1.start()
        for x in range(0, count_ap):
            list_ap[x].start([c1])

    def ping_all(self, hosts=None, timeout=None):
        packets = 0
        lost = 0
        ploss = None
        out_string = ""
        if not hosts:
            hosts = self.mini.hosts + self.mini.stations
            out_string += '*** Ping: testing ping reachability\n'
        for node in hosts:
            out_string += '%s -> ' % node.name
            for dest in hosts:
                if node != dest:
                    opts = ''
                    if timeout:
                        opts = '-W %s' % timeout
                    if dest.intfs:
                        result = node.cmdPrint('ping -c1 %s %s' % (opts, dest.IP()))
                        sent, received = self.mini._parsePing(result)
                    else:
                        sent, received = 0, 0
                    packets += sent
                    if received > sent:
                        out_string += '*** Error: received too many packets\n'
                        out_string += '%s' % result
                        node.cmdPrint('route')
                        exit(1)
                    lost += sent - received
                    out_string += ('%s ' % dest.name) if received else 'X '
            out_string += '\n'
        if packets > 0:
            ploss = 100.0 * lost / packets
            received = packets - lost
            out_string += "*** Results: %i%% dropped (%d/%d received)\n" % (ploss, received, packets)
        else:
            ploss = 0
            out_string += "*** Warning: No packets sent\n"
        print out_string
        return out_string

    def ret_info(self):
        array = []

        for x in range(0, len(self.mini.accessPoints)):
            string_pos = str(self.mini.accessPoints[x].params['position'][0]) + " " + str(self.mini.accessPoints[x].params['position'][1])
            string_name = self.mini.accessPoints[x].name
            node = Node.make_node(string_name, string_pos, 'ap')
            array.append(node)

        for y in range(0, len(self.mini.stations)):
            string_pos = str(self.mini.stations[y].params['position'][0]) + " " + str(
                self.mini.stations[y].params['position'][1])
            string_name = self.mini.stations[y].name
            node = Node.make_node(string_name, string_pos, 'st')
            array.append(node)

        return array


