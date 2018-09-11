
#manual custom MESH Topo with
        # 1 AP ->linked to -> 5 stations in wireless mode with 1 mobility
        #when sation one out of range of AP stops connectivity

from mininet.log import setLogLevel, info
from mn_wifi.link import wmediumd, mesh, wifiDirectLink
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
        ap1=net.addAccessPoint('ap1', wlans=2, mode='g',ssid= 'ssid-ap1,', position="0,0,0")
        # ap2=net.addAccessPoint('ap2', wlans=3, mode='g',ssid= 'ssid-ap2,,', position="10,0,0")
        # ap3=net.addAccessPoint('ap3', wlans=3, mode='g',ssid= 'ssid-ap3,,', position="0,10,0")
        #ap4=net.addAccessPoint('ap4', wlans=3, mode='g',ssid= 'ssid-ap3,,', position="0,10,0")

        sta1=net.addStation('sta1', wlans=2, ssid='ssid-sta1,', min_x=110, max_x=300, min_y=100, max_y=300, min_v=5, max_v=10)
        sta2=net.addStation('sta2', wlans=2, ssid='ssid-sta2,', position='-10,20,0')
        sta3=net.addStation('sta3', wlans=2, ssid='ssid-sta3,', position='0,20,0')
        sta4=net.addStation('sta4', wlans=2, ssid='ssid-sta4,', position='10,20,0')
        sta5=net.addStation('sta5', wlans=2, ssid='ssid-sta5,', position='10,60,0')
        # sta4=net.addStation('sta4')
        # sta5=net.addStation('sta5')



        #ap4=net.add

        info( "=======>Creating controller<========= \n")
        c1=net.addController('c0', controller=Controller, ip='127.0.0.1',port=6633)

        info( "=======>configuring wifi nodes<========= \n")
        net.configureWifiNodes()
        net.plotGraph(max_x=300, max_y=300)
        net.setMobilityModel(time=0, model='RandomDirection', max_x=400, max_y=400, seed=20)
        #info( "=======>configuring association control AP<========= \n")
        #net.configureWifiNodes()
        #net.auto_association()

        info("=========><creating links and associations============\n")
        net.addLink(sta1, ap1, channel=1)
        net.addLink(sta2, ap1, channel=1)
        net.addLink(sta3, ap1, channel=1)
        net.addLink(sta4, ap1, channel=1)
        net.addLink(sta5, ap1, channel=1)



        #net.addLink(sta1, intf='sta1-wlan01', cls=wifiDirectLink)
        #net.addLink(sta2, intf='sta2-wlan01', cls=wifiDirectLink)
        # net.addLink(sta2, intf='sta2-wlan2', ssid='mesh-ssid', cls=mesh, channel=3)
        # net.addLink(sta3, intf='sta3-wlan2', ssid='mesh-ssid', cls=mesh, channel=3)
        # net.addLink(sta4, intf='sta4-wlan2', ssid='mesh-ssid', cls=mesh, channel=3)
        # net.addLink(sta5, intf='sta5-wlan2', ssid='mesh-ssid', cls=mesh, channel=3)



        # net.addLink(ap3, sta5)

        #net.addLink(ap1, intf='ap1-wlan2', ssid='mesh-ssid', cls=mesh, channel=5)
        # net.addLink(ap2, intf='ap2-wlan3', ssid='mesh-ssid', cls=mesh, channel=5)
        # net.addLink(ap3, intf='ap3-wlan3', ssid='mesh-ssid', cls=mesh, channel=5)
        # #net.addLink(ap4, intf='ap4-wlan2', ssid='mesh-ssid', cls=mesh, channel=5)


        # ap1.setIP('10.0.0.2/24', intf='ap1-wlan1')
        # ap2.setIP('10.0.1.2/24', intf='ap2-wlan1')
        # ap1.cmd('route add -net 10.0.0.0/24 gw 10.0.0.2')
        # ap2.cmd('route add -net 10.0.1.0/24 gw 10.0.1.2')

        #net.auto_association()



        info( "=======>starting the network<========= \n")
        net.build()
        c1.start()
        ap1.start([c1])
        # ap2.start([c1])
        # ap3.start([c1])
        #ap4.start([c1])


        CLI_wifi(net)

        net.stop()



class CustomController:

    pass

if __name__=='__main__':
   # print(setLogLevel('info'))
    setLogLevel('info')
    ct=CustomTopo()

