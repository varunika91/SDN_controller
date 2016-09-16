#Custom topology 

from mininet.topo import Topo

class MyTopo( Topo ):
    def __init__( self ):
        "Create custom topo."
        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        left1 = self.addHost( 'h1', ip= "10.0.1.2/24", defaultRoute = "via 10.0.1.1" )
        left2 = self.addHost( 'h2', ip= "10.0.1.3/24", defaultRoute = "via 10.0.1.1")
	
        rt1 = self.addHost( 'h3', ip= "10.0.2.2/24", defaultRoute = "via 10.0.2.1" )
        rt2 = self.addHost( 'h4', ip= "10.0.2.3/24", defaultRoute = "via 10.0.2.1")
        rt3 = self.addHost( 'h5', ip= "10.0.2.4/24", defaultRoute = "via 10.0.2.1")
        
        sw1 = self.addSwitch( 's1',dpid= "1")
        sw2 = self.addSwitch( 's2',dpid= "2")
 
        # Add links
        self.addLink( left1,sw1 )
        self.addLink( left2,sw1 )
    
        
        self.addLink( sw1,sw2 )
        
        self.addLink( rt1,sw2 )
        self.addLink( rt2,sw2 )
        self.addLink( rt3,sw2 )
        
        #self.addLink( 'h1', 's1', 0,1 )
        #self.addLink( 'h2', 's1', 0,2 )
        #self.addLink( 'h3', 's1', 0,3 )
        
topos = { 'mytopo': ( lambda: MyTopo() ) }


