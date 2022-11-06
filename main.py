from vpython import scene, box, color, vec, vector, sphere, rate
from utils import add_region_of_interest, setup_world, check_drone_intrusion
from drone import add_drone, move_drone
from user_controls import setup_user_controls, update_region_of_interest
from email_service import send_email_alert

world = setup_world()

user_controls = setup_user_controls(world)

region_of_interest_min_corner = vec(-300, -300, 10)
region_of_interest_max_corner = vec(300, 300, 400)
region_of_interest = add_region_of_interest(
    min_corner=region_of_interest_min_corner,
    max_corner=region_of_interest_max_corner,
    opacity=0.2
)


# drone
flight_min_position = vec(-500, -500, 0)
flight_max_position = vec(500, 500, 300)
drone_initial_position = vec(100, 100, 100)
drone_initial_speed = vec(10, 20, 0)

drone = add_drone(
    flight_min_position=flight_min_position,
    flight_max_position=flight_max_position,
    region_of_interest_display=False,
    initial_position=drone_initial_position,
    initial_speed=drone_initial_speed
)


while True:
    rate(100)
    if user_controls.running:
        update_region_of_interest(region_of_interest, user_controls)
        move_drone(drone)
        intrusion = check_drone_intrusion(region_of_interest, drones=[drone])
        # send email notification if there is any intrusion
        if intrusion and user_controls.email_sent_flag is False:
            send_email_alert(str(user_controls.receiver_email_address))
            user_controls.email_sent_flag = True
            print("Notification sent to: {}".format(
                user_controls.receiver_email_address))
        if intrusion is False and user_controls.email_sent_flag is True:
            user_controls.email_sent_flag = False
