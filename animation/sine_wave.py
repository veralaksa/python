#
# sine_wave.py
# Animate a sine wave and save it as MP4 file
# Sparisoma Viridi | https://github.com/dudung/cookbook
# 20220331 Create this program by modifying original one [1].
# 
# 1. marlise23, "Python unknown file extension .mp4",
#    Stack Overflow, 20 Oct 2019,
#    url https://stackoverflow.com/q/58469357/9475509
#    [20220331].
#

# url https://realpython.com/python-import/
# Make code in one module available in anothe
import numpy as np

# url https://www.w3schools.com/python/ref_keyword_from.asp
# Import only certain section from a module
from matplotlib import pyplot as plt
from matplotlib import animation

# url https://matplotlib.org/3.5.1/api/_as_gen/matplotlib.pyplot.figure.html
# Create a new figure, or activate an existing figure
fig = plt.figure()

# url https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.axes.html
# Add an axes to the current figure and make it the current axes
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))

# url https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.axes.Axes.plot.html
# Plot y versus x as lines and/or markers
line, = ax.plot([], [], lw=2)

# url https://stackoverflow.com/q/58469357/9475509
# Initialize each frame by plotting the background
def init():
  # url https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_data
	# Set the x and y data
  line.set_data([], [])
  return line,

# url https://stackoverflow.com/q/58469357/9475509
# Call sequentially plotted function
def animate(i):
  # url https://numpy.org/doc/stable/reference/generated/numpy.linspace.html
	# Return evenly spaced numbers over a specified interval
  x = np.linspace(0, 2, 1000)

  # url https://numpy.org/doc/stable/reference/generated/numpy.sin.html
  # Trigonometric sine, element-wise
  y = np.sin(2 * np.pi * (x - 0.01 * i))

  # url https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_data
  line.set_data(x, y)
  return line,

# url https://matplotlib.org/3.5.1/api/_as_gen/matplotlib.animation.FuncAnimation.html
# Makes an animation by repeatedly calling a function func
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)

# url https://matplotlib.org/2.0.2/api/_as_gen/matplotlib.animation.Animation.save.html
# Saves a movie file by drawing every frame
anim.save('sine_wave_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

# url https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.show.html
# Display all open figures
plt.show()
