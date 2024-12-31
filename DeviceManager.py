class DeviceManager:
    
    def __init__(self, driver: Driver):
        self.driver = driver
        self.driver.initialize()
    
    def check_device_status(self):
        status = self.driver.get_device_status()
        print(f"Device Status: {status}")
    
    def send_device_data(self, data):
        self.driver.send_data(data)

# Function to detect driver version (Simulated)
def detect_driver_version(driver_type: str):
    if driver_type == "old":
        return OldDriver()
    elif driver_type == "new":
        return NewDriver()
    else:
        raise ValueError("Unknown driver type!")

# Simulate software running with backward compatibility for old drivers
def main():
    # Simulate detecting an old driver
    driver_type = "old"  # This could be dynamic in real-world applications
    driver = detect_driver_version(driver_type)
    
    # If old driver, wrap it with an adapter for backward compatibility
    if isinstance(driver, OldDriver):
        driver = OldDriverAdapter(driver)
    
    # Initialize the device manager with the compatible driver
    device_manager = DeviceManager(driver)
    
    # Check device status and send data
    device_manager.check_device_status()
    device_manager.send_device_data("Test Data")

    # Now, let's simulate running with a new driver
    driver_type = "new"
    driver = detect_driver_version(driver_type)
    
    # Initialize the device manager with the new driver
    device_manager = DeviceManager(driver)
    
    # Check device status and send data
    device_manager.check_device_status()
    device_manager.send_device_data("Test Data")

if __name__ == "__main__":
    main()
