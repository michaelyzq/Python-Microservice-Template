from eureka.client import EurekaClient
import logging

logging.basicConfig()


ec = EurekaClient("python-service-dev",
                  eureka_domain_name="python-service",
                  eureka_port=9100,
                  data_center="MyOwn",
                  eureka_url="http://127.0.0.1:9100/eureka/",                
                  host_name="PC002746.tfprod.taifook.com:python-service-dev:7001",
                  port="7000",
                  secure_vip_address="127.0.0.1",
                  secure_port="7001"
                
)
def register():
    print 'register eurekaClient'
    print ec.get_eureka_urls()
    print ec.register()
    print ec.update_status("UP")  
    print 'heartbeat eurekaClient'
    print ec.heartbeat()
    

def delete():
    print 'delete eurekaClient'
    print ec.delete()