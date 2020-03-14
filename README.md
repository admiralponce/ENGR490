# ENGR490

to grab missionplanner info

pip install dronekit
pip install pymavlink



from dronekit import connect, VehicleMode, LocationGlobaleRelative, Command, LocationGlobal
from pymavlink import mavutil

def mission_load(vehice) :
    
    cmds = vehicle.commands 
    cmds.download()
    cmds.wait_read()
    
def download_mission(vehicle):
    cmds = vehicle.commands
    cmds.download()
    cmds.wait_read()
    
def get_current_mission(vehicle):
    
    print("getting mission")
    download_mission(vehicle)
    missionList = []
    n_wp = 0
    
    for wp in vehicle.commands:
        missionList.append(wp)
        n_wp +=1
    return n_wp, missionList
    
get_info(vehicle, lat, long, alt):
  download_mission()
  cmds = vehicle.commands
  
vehicle = connect('udp:127.0.0.1:14551')
  
  
  #example of print
  print(vehicle.commands.count)
  print(vehicle.location.global_relative_fram.alt)
