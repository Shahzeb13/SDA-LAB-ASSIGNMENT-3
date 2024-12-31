from abc import ABC, abstractmethod

# Define an abstract base class for the Driver
class Driver(ABC):
    
    @abstractmethod
    def initialize(self):
        pass
    
    @abstractmethod
    def get_device_status(self):
        pass
    
    @abstractmethod
    def send_data(self, data):
        pass

# Old driver that uses legacy APIs
class OldDriver(Driver):
    
    def initialize(self):
        print("Initializing old driver using legacy methods...")
        
    def get_device_status(self):
        return "Old Driver Status"
    
    def send_data(self, data):
        print(f"Sending data via old driver: {data}")

# New driver that uses modern APIs
class NewDriver(Driver):
    
    def initialize(self):
        print("Initializing new driver using modern methods...")
        
    def get_device_status(self):
        return "New Driver Status"
    
    def send_data(self, data):
        print(f"Sending data via new driver: {data}")

#### Adapter for backward compatibility (Old Driver Wrapper)

class OldDriverAdapter(Driver):
    """
    Adapter class to ensure backward compatibility with the old driver.
    It wraps the old driver in a way that it can be used with the new system.
    """
    
    def __init__(self, old_driver: OldDriver):
        self.old_driver = old_driver
    
    def initialize(self):
        # Use legacy initialization method
        print("Using adapter to initialize the old driver...")
        self.old_driver.initialize()
        
    def get_device_status(self):
        # Use the old driver to get the status
        return self.old_driver.get_device_status()
    
    def send_data(self, data):
        # Use the old driver to send data
        self.old_driver.send_data(data)
