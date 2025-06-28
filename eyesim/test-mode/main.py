import pygame


def setup(screen, eyesy):
    """v3: Changed parameter name from 'etc' to 'eyesy'"""
    pass


def draw(screen, eyesy):
    """v3: Changed parameter name from 'etc' to 'eyesy'"""
    xmid = eyesy.xres // 2
    ymid = eyesy.yres // 2
    
    # Demonstrate v3 features: use color_picker_lfo for dynamic colors
    if eyesy.knob4 < 0.5:
        # Traditional color picker
        color = eyesy.color_picker(eyesy.knob1)
    else:
        # v3: New color_picker_lfo with rate control
        lfo_rate = (eyesy.knob4 - 0.5) * 4.0  # 0 to 2.0 range
        color = eyesy.color_picker_lfo(eyesy.knob1, lfo_rate)
    
    pygame.draw.circle(
        surface=screen,
        color=color, 
        center=(xmid, ymid),
        radius=10*eyesy.knob2 * max(eyesy.audio_in) / 2**8,
        width=int(10*eyesy.knob3),
    )
    eyesy.color_picker_bg(eyesy.knob5)
