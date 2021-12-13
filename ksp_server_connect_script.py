import krpc


conn = krpc.connect(
    name='Python',
    address='127.0.0.1',
    rpc_port=50000, stream_port=50001)



# vessel = conn.space_center.active_vessel
# obt_frame = vessel.orbit.body.non_rotating_reference_frame
# srf_frame = vessel.orbit.body.reference_frame
# obt_speed = vessel.flight(obt_frame).speed
# srf_speed = vessel.flight(srf_frame).speed
# heading = round(vessel.flight(srf_frame).heading, 0)
# getValue = heading



## THIS LOOP WORKS...
##while True:
##    obt_speed = vessel.flight(obt_frame).speed
##    srf_speed = vessel.flight(srf_frame).speed
##    heading = round(vessel.flight(srf_frame).heading,0)
##    #getvalue = print('VOrbit= %.1f m/s, \n VSurf= %.1f m/s' %
##    #      (obt_speed, srf_speed))
##    time.sleep(.3)
##    #getvalue = print(f'Heading ={heading} degrees')
##    getvalue = heading
##    #print(getvalue)
