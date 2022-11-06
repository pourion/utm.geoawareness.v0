from vpython import scene, box, color, vec, vector, wtext, slider, button, winput
import types


def setup_user_controls(world):
    user_controls = types.SimpleNamespace()

    user_controls.running = True

    # pause and run button
    def Run(b):
        user_controls.running = not user_controls.running
        if user_controls.running:
            b.text = "Pause"
        else:
            b.text = "Run"
    button(text="Pause", pos=world.scene.title_anchor, bind=Run)

    # region of interest min corner position
    world.scene.caption = "Update the region of interest: \n\n"

    def set_min_corner_x(s):
        wt_min_x.text = '{:1.2f}'.format(s.value)

    def set_min_corner_y(s):
        wt_min_y.text = '{:1.2f}'.format(s.value)

    def set_min_corner_z(s):
        wt_min_z.text = '{:1.2f}'.format(s.value)

    def set_max_corner_x(s):
        wt_max_x.text = '{:1.2f}'.format(s.value)

    def set_max_corner_y(s):
        wt_max_y.text = '{:1.2f}'.format(s.value)

    def set_max_corner_z(s):
        wt_max_z.text = '{:1.2f}'.format(s.value)

    # min x
    world.scene.append_to_caption(
        'Minimum corner point of the region of interest\n')
    world.scene.append_to_caption(
        'x coordinate: ')
    min_x_slider = slider(
        min=-1000,
        max=1000,
        value=-300,
        length=220,
        bind=set_min_corner_x,
        right=15
    )
    wt_min_x = wtext(text='{:1.2f}'.format(min_x_slider.value))
    world.scene.append_to_caption(' meters\n')

    # min y
    world.scene.append_to_caption(
        'y coordinate: ')
    min_y_slider = slider(
        min=-1000,
        max=1000,
        value=-300,
        length=220,
        bind=set_min_corner_y,
        right=15
    )
    wt_min_y = wtext(text='{:1.2f}'.format(min_y_slider.value))
    world.scene.append_to_caption(' meters\n')

    # min z
    world.scene.append_to_caption(
        'z coordinate: ')
    min_z_slider = slider(
        min=-500,
        max=500,
        value=0,
        length=220,
        bind=set_min_corner_z,
        right=15
    )
    wt_min_z = wtext(text='{:1.2f}'.format(min_z_slider.value))
    world.scene.append_to_caption(' meters\n\n')

    # max x
    world.scene.append_to_caption(
        'Maximum corner point of the region of interest\n')
    world.scene.append_to_caption(
        'x coordinate: ')
    max_x_slider = slider(
        min=-1000,
        max=1000,
        value=200,
        length=220,
        bind=set_max_corner_x,
        right=15
    )
    wt_max_x = wtext(text='{:1.2f}'.format(max_x_slider.value))
    world.scene.append_to_caption(' meters\n')

    # max y
    world.scene.append_to_caption(
        'y coordinate: ')
    max_y_slider = slider(
        min=-1000,
        max=1000,
        value=200,
        length=220,
        bind=set_max_corner_y,
        right=15
    )
    wt_max_y = wtext(text='{:1.2f}'.format(max_y_slider.value))
    world.scene.append_to_caption(' meters\n')

    # max z
    world.scene.append_to_caption(
        'z coordinate: ')
    max_z_slider = slider(
        min=-500,
        max=500,
        value=200,
        length=220,
        bind=set_max_corner_z,
        right=15
    )
    wt_max_z = wtext(text='{:1.2f}'.format(max_z_slider.value))
    world.scene.append_to_caption(' meters\n\n')

    # user interface for adding receiver email address
    # initialize email sending flag as False at the start
    user_controls.email_sent_flag = False
    world.scene.append_to_caption(
        'Email address for receiving notifications. \n')

    def save_email(b):
        user_controls.receiver_email_address = receiver_email_address_widget.text
        saved_email_addres.text = '\n Saved email address is: {}\n'.format(
            receiver_email_address_widget.text)
    receiver_email_address_widget = winput(
        text="name@email.com", width=300, bind=save_email)
    button(text="Save", bind=save_email)
    saved_email_addres = wtext(
        text='\n Saved email address is: {}\n'.format(receiver_email_address_widget.text))

    user_controls.region_of_interest_min_corner_x = min_x_slider
    user_controls.region_of_interest_min_corner_y = min_y_slider
    user_controls.region_of_interest_min_corner_z = min_z_slider
    user_controls.region_of_interest_max_corner_x = max_x_slider
    user_controls.region_of_interest_max_corner_y = max_y_slider
    user_controls.region_of_interest_max_corner_z = max_z_slider
    user_controls.receiver_email_address = receiver_email_address_widget.text

    return user_controls


def update_region_of_interest(region_of_interest, user_controls):
    min_corner = vec(
        user_controls.region_of_interest_min_corner_x.value,
        user_controls.region_of_interest_min_corner_y.value,
        user_controls.region_of_interest_min_corner_z.value
    )
    max_corner = vec(
        user_controls.region_of_interest_max_corner_x.value,
        user_controls.region_of_interest_max_corner_y.value,
        user_controls.region_of_interest_max_corner_z.value
    )

    size_x = (max_corner.x - min_corner.x)
    size_y = (max_corner.y - min_corner.y)
    size_z = (max_corner.z - min_corner.z)
    x = min_corner.x + size_x / 2
    y = min_corner.y + size_y / 2
    z = min_corner.z + size_z / 2
    position = vec(x, y, z)
    size = vec(size_x, size_y, size_z)
    region_of_interest.pos = position
    region_of_interest.size = size

    region_of_interest.min_corner_position = min_corner
    region_of_interest.max_corner_position = max_corner

    return region_of_interest
