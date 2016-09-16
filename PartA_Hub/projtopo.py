#Custom topology 

from mininet.topo import Topo

class MyTopo( Topo ):
    def __init__( self ):
        "Create custom topo."
        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        self.addHost( 'h1', ip= "10.0.1.100/24", defaultRoute = "via 10.0.1.1" )
        self.addHost( 'h2', ip= "10.0.2.100/24", defaultRoute = "via 10.0.2.1")
        self.addHost( 'h3', ip= "10.0.3.100/24", defaultRoute = "via 10.0.3.1")
        #self.addHost( 'h4', ip= "10.0.2.3/24", defaultRoute = "via 10.0.2.1")
        #self.addHost( 'h5', ip= "10.0.2.4/24", defaultRoute = "via 10.0.2.1")	
        self.addSwitch( 's1',dpid= "1")
        #self.addSwitch( 's2',dpid= "2")
        
        # Add links
        self.addLink( 'h1', 's1', 0,1 )
        self.addLink( 'h2', 's1', 0,2 )
        self.addLink( 'h3', 's1', 0,3 )
        
topos = { 'mytopo': ( lambda: MyTopo() ) }
