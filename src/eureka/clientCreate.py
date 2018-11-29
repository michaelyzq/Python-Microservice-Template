from eureka.client import EurekaClient
import logging

logging.basicConfig()


ec = EurekaClient("Python_Service_Dev",
                  eureka_domain_name="python_client",
                  eureka_port=9000,
                  data_center="MyOwn",
                  eureka_url="http://127.0.0.1:9100/eureka/",                
                  vip_address="127.0.0.1",
                  host_name="PC002746.tfprod.taifook.com:client-server-dev:7000",
                  port="7000",
                  secure_vip_address="127.0.0.1",
                  secure_port="7001"
                
)



if __name__ == '__main__':
      
    print ec.get_eureka_urls()
    print ec.register()
    print ec.update_status("UP")  
    print ec.heartbeat()
    
    
def register():
    print ec.get_eureka_urls()
    print ec.register()
    print ec.update_status("UP")  
    print ec.heartbeat()