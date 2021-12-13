import krpc
import ksp_server_connect_script as kspserverconnectscript
import time


def getvalue():
    vessel = kspserverconnectscript.conn.space_center.active_vessel
    obt_frame = vessel.orbit.body.non_rotating_reference_frame
    srf_frame = vessel.orbit.body.reference_frame
    obt_speed = vessel.flight(obt_frame).speed
    srf_speed = vessel.flight(srf_frame).speed
    heading = round(vessel.flight(srf_frame).heading, 0)
    lon = round(vessel.flight(srf_frame).longitude, 4)
    getValue = heading
    # return getValue
    return lon

## THIS LOOP OF CODE WORKS...
##while True:
##    obt_speed = vessel.flight(obt_frame).speed
##    srf_speed = vessel.flight(srf_frame).speed
##    heading = round(vessel.flight(srf_frame).heading,0)
##    #getvalue = print('VOrbit= %.1f m/s, \n VSurf= %.1f m/s' %
##    #      (obt_speed, srf_speed))
##    time.sleep(.3)
##    #getvalue = print(f'Heading ={heading} degrees')
##    getvalue = heading
##    print(getvalue)
