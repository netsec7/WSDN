
#manual custom MESH Topo with
        # three AP with each station (ap3 has 3 stations sta3,sta4, sta5)
        #worked however, topoloyg is flooded due mesh thus either of the station unbale to reach the destination
        # customMEsh4 will be designed with improval
        # topology worked

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


        net=Mininet_wifi(controller=Controller, wmediumd_mode=interference, link=wmediumd, accessPoint=OVSKernelAP)
        info( "=======>Creating AP and Stations<========= \n")
        ap1=net.addAccessPoint('ap1', wlans=3,  mode='g',ssid= 'ssid-ap1,ssid-ap2,', position="0,0,0")
        ap2=net.addAccessPoint('ap2', wlans=3, mode='g',ssid= 'ssid-ap2,ssid-ap2,', position="10,0,0")
        ap3=net.addAccessPoint('ap3', wlans=3, mode='g',ssid= 'ssid-ap3,ssid-ap2,', position="0,10,0")

        sta1=net.addStation('sta1', mac='00:00:00:00:00:11', ip='192.168.1.1/24', position='10,-10,10')
        sta2=net.addStation('sta2', mac='00:00:00:00:00:12', ip='192.168.2.1/24', position='-10,10,0')
        sta3=net.addStation('sta3', mac='00:00:00:00:00:13', ip='192.168.3.1/24', position='10,10,20')
        sta4=net.addStation('sta4', mac='00:00:00:00:00:14', ip='192.168.3.2/24')
        sta5=net.addStation('sta5', mac='00:00:00:00:00:15', ip='192.168.3.3/24')


        #ap4=net.add

        info( "=======>Creating controller<========= \n")
        c1=net.addController('c0',controller=Controller, ip='127.0.0.1',port=6633)

        info( "=======>configuring wifi nodes<========= \n")
        net.configureWifiNodes()
        #net.plotGraph(max_x=80, max_y=80)
        #info( "=======>configuring association control AP<========= \n")
        #net.configureWifiNodes()
        #net.auto_association()

        info("=========><creating links and associations============\n")
        net.addLink(sta1, ap1)
        net.addLink(ap2, sta2)
        net.addLink(ap3, sta3)
        net.addLink(ap3, sta4)
        net.addLink(ap3, sta5)

        net.addLink(ap1, intf='ap1-wlan2', ssid='mesh-ssid', cls=mesh, channel=5)
        net.addLink(ap2, intf='ap2-wlan2', ssid='mesh-ssid', cls=mesh, channel=5)
        net.addLink(ap3, intf='ap3-wlan2', ssid='mesh-ssid', cls=mesh, channel=5)

        """ap1 interfaces set IP"""
        ap1.setIP('192.168.1.254/24', intf='ap1-wlan1') #for station
        ap1.setIP('192.168.4.1/24', intf='ap1-wlan2') #for APs

        """ap2 interface set IP"""
        ap2.setIP('192.168.2.254/24', intf='ap2-wlan1') #for station
        ap2.setIP('192.168.4.2/24', intf='ap2-wlan2')#for APs

        """ap2 interface set IP"""
        ap3.setIP('192.168.3.254/24', intf='ap3-wlan1') #for station
        ap3.setIP('192.168.4.3/24', intf='ap3-wlan2')#for APs


        # ap1.cmd('route add -net 10.0.0.0/24 gw 10.0.0.2')
        # ap2.cmd('route add -net 10.0.1.0/24 gw 10.0.1.2')

        """configuring route static"""
        ap1.cmd('route add -net 192.168.2.0/24 gw 192.168.4.2')
        ap1.cmd('route add -net 192.168.3.0/24 gw 192.168.4.3')
        ap1.cmd('route add -net 192.168.1.0/24 gw 192.168.1.1')
        #ap1.cmd('route add 192.168.1.0/24 gw 192.168.1.1')

        ap2.cmd('route add -net 192.168.1.0/24 gw 192.168.4.1')
        ap2.cmd('route add -net 192.168.3.0/24 gw 192.168.4.3')
        ap2.cmd('route add -net 192.168.2.0/24 gw 192.168.2.1')

        ap3.cmd('route add -net 192.168.1.0/24 gw 192.168.4.1')
        ap3.cmd('route add -net 192.168.2.0/24 gw 192.168.4.2')
        ap3.cmd('route add -net 192.168.3.0/24 gw 192.168.3.1')

        #net.auto_association()ap1.cmd('route add -net 10.0.0.0/24 gw 10.0.0.2')



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

