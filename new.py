# mininet'in topoloji oluşturulması ve controllere bağlanması için gereken kütüphanelerine yüklenmesi
from mininet.topo import Topo
from mininet.node import Controller, RemoteController
from mininet.cli import CLI

# topoloji sınıfının oluşturulması
class MyTopo( Topo ):
	
    # özel topoloji'nin host, switch ve link (bağlantılarının oluşturulması).
    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )
        s4 = self.addSwitch( 's4' )

        # Add links
        self.addLink( h1, s1 )
        self.addLink( s1, s2 )
        self.addLink( s1, s3 )
        self.addLink( s2, s4 )
        self.addLink( s3, s4 )
        self.addLink( s4, h2 )

# Topolojinin çalışması için sanal ortam oluşturuluyor
topos = { 'mytopo': ( lambda: MyTopo() ) }
