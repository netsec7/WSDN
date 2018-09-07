
#manual custom MESH Topo with
        # three AP with each station
        #

from mininet.log import setLogLevel, info
from mn_wifi.link import wmediumd, mesh
from mn_wifi.cli import CLI_wifi
from mn_wifi.net import Mininet_wifi
from mn_wifi.wmediumdConnector import interference
from mininet.node import Controller
from mn_wifi.node import OVSKernelAP
from mininet.link import Link, Intf, TCLink, TCULink



class CustomTopo:
    def __init__(self):

        info( "=======>Creating AP and baseStations<========= \n")
        net=Mininet_wifi(controller=Controller, wmediumd_mode=interference, link=wmediumd, accessPoint=OVSKernelAP)
        ap1=net.addAccessPoint('ap1', wlans=4, mode='g',ssid= 'ssid-ap1,', position="20,10,10")
        ap2=net.addAccessPoint('ap2', wlans=4, mode='g',ssid= 'ssid-ap2,', position="10,20,10")
        ap3=net.addAccessPoint('ap3', wlans=4, mode='g',ssid= 'ssid-ap3,', position="20,10,10")
        sta1=net.addStation('sta1')
        sta2=net.addStation('sta2')
        sta3=net.addStation('sta3')

        info( "=======>Creating controller<========= \n")
        c1=net.addController('Controller0',controller=Controller, ip='127.0.0.1',
                           port=6633)

        info( "=======>configuring wifi nodes<========= \n")
        net.configureWifiNodes()
        net.plotGraph(max_x=80, max_y=80)
        #info( "=======>configuring association control AP<========= \n")
        #net.configureWifiNodes()
        #net.auto_association()

        info("=========><creating links and associations============\n")
        net.addLink(ap1,sta1)
        net.addLink(ap2,sta2)
        net.addLink(ap3,sta3)
        net.addLink(ap1, intf='ap1-wlan1', ssid='mesh-ssid', cls=mesh)
        net.addLink(ap2, intf='ap2-wlan1', ssid='mesh-ssid', cls=mesh)
        net.addLink(ap3, intf='ap3-wlan1', ssid='mesh-ssid', cls=mesh)

        info( "=======>starting the network<========= \n")
        net.build()
        c1.start()
        ap1.start([c1])
        ap2.start([c1])
        ap3.start([c1])

        CLI_wifi(net)

        net.stop()



class CustomController:
    pass

if __name__=='__main__':
   # print(setLogLevel('info'))
    setLogLevel('info')
    ct=CustomTopo()

