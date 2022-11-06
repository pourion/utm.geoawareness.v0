from vpython import scene, box, color, vec, vector, sphere, rate
import types


def setup_world():
    world = types.SimpleNamespace()

    # timestep for updating the world in seconds
    world.dt = 0.3

    # camera/scene view
    simulated_environment = scene
    simulated_environment.width = 800
    simulated_environment.height = 600
    simulated_environment.background = color.gray(0.95)
    simulated_environment.range = 1200
    simulated_environment.forward = vec(0, 1.3, -1)

    simulated_environment.caption = """To rotate "camera", drag with right button or Ctrl-drag.
    To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
    On a two-button mouse, middle is left + right.
    To pan left/right and up/down, Shift-drag.
    Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""

    # thin rectangle representing the ground
    ground = box(
        pos=vec(0, 0, 0),
        opacity=1,
        size=vec(1500, 1500, 0.1),
        color=color.gray(0.7)
    )
    # some basic boxes representing a few buildings
    building_1 = add_box(vec(100, 100, 0), vec(20, 20, 120), color.blue)
    building_2 = add_box(vec(-40, 30, 0), vec(24, 15, 70), color.blue)
    building_3 = add_box(vec(10, 10, 0), vec(24, 15, 70), color.blue)
    building_4 = add_box(vec(60, 50, 0), vec(24, 15, 70), color.blue)
    building_5 = add_box(vec(100, -200, 0), vec(24, 15, 70), color.blue)

    world.scene = simulated_environment
    world.ground = ground

    return world


def add_box(
    location=vec(0, 0, 0),
    size=vec(0, 0, 0),
    color=color.blue,
    opacity=1.0,
    z_offset=0
):
    building_location = vec(location.x, location.y, size.z/2 + z_offset)
    building = box(pos=building_location, size=size,
                   color=color, opacity=opacity)
    return building


def add_region_of_interest(
    min_corner=vec(0, 0, 0),
    max_corner=vec(400, 400, 400),
    opacity=0.1,
    color=color.green
):
    size_x = (max_corner.x - min_corner.x)
    size_y = (max_corner.y - min_corner.y)
    size_z = (max_corner.z - min_corner.z)
    x = min_corner.x + size_x / 2
    y = min_corner.y + size_y / 2
    z = min_corner.z + size_z / 2
    position = vec(x, y, z)
    size = vec(size_x, size_y, size_z)

    region_of_interest = box(
        pos=position,
        size=size,
        opacity=opacity,
        color=color
    )

    region_of_interest.min_corner_position = min_corner
    region_of_interest.max_corner_position = max_corner

    return region_of_interest


def check_drone_intrusion(
    region_of_interest,
    drones=[]
):
    intrusion = False
    for drone in drones:
        if region_of_interest.min_corner_position.x < drone.pos.x < region_of_interest.max_corner_position.x and \
            region_of_interest.min_corner_position.y < drone.pos.y < region_of_interest.max_corner_position.y and \
                region_of_interest.min_corner_position.z < drone.pos.z < region_of_interest.max_corner_position.z:
            region_of_interest.color = color.red
            intrusion = True
        else:
            region_of_interest.color = color.green
            intrusion = False

    return intrusion
