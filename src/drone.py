from vpython import scene, box, color, vec, vector, sphere, rate
from src.utils import add_region_of_interest


def add_drone(
    flight_min_position=vec(0, 0, 0),
    flight_max_position=vec(100, 100, 100),
    initial_position=vec(0, 0, 0),
    initial_speed=vec(1, 1, 1),
    mass=1.0,
    make_trail=True,
    retain_trail_length=15,
    color=color.yellow,
    sphere_radius=10,
    region_of_interest_display=False,
    region_of_interest_color=color.cyan,
    region_of_interest_opacity=0.1
):
    if region_of_interest_display:
        simulation_flight_region = add_region_of_interest(
            min_corner=flight_min_position,
            max_corner=flight_max_position,
            color=region_of_interest_color,
            opacity=region_of_interest_opacity
        )

    drone = sphere(
        pos=initial_position,
        color=color,
        radius=sphere_radius,
        make_trail=make_trail,
        retain=retain_trail_length
    )
    drone.mass = mass
    drone.p = initial_speed
    drone.flight_min_position = flight_min_position
    drone.flight_max_position = flight_max_position

    return drone


def move_drone(drone, dt=0.3):
    drone.pos = drone.pos + (drone.p / drone.mass) * dt
    if not (drone.flight_max_position.x > drone.pos.x > drone.flight_min_position.x):
        drone.p.x = -drone.p.x
    if not (drone.flight_max_position.y > drone.pos.y > drone.flight_min_position.y):
        drone.p.y = -drone.p.y
    if not (drone.flight_max_position.z > drone.pos.z > drone.flight_min_position.z):
        drone.p.z = -drone.p.z
