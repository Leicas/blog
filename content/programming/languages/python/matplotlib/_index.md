---
author: gbmhunter
categories: [ "Programming", "Programming Languages", "Python" ]
date: 2018-11-29
description: "Matplotlib tutorial including useful tricks and tips with code examples."
draft: false
lastmod: 2019-05-02
tags: [ "matplotlib", "Python", "code", "programming", "graphs", "numpy", "pyplot", "pie charts", "charts", "Basemap", "plotting" ]
title: "matplotlib"
type: page
---

## Importing

`matplotlib`, just like `numpy`, is one of those libraries which has so much legacy behind the import statement that it's worth breaking Python style rules and using the `at` keyword to change the name of the imported library. Traditionally, `matplotlib.pyplot` is imported as `plt`, with the statement:

```py
import matplotlib.pyplot as plt
```

## Using subplots

```py
# Create two plots, in a grid with 2 rows and 1 column
# (plots will be stacked vertically)
fig, axs = plt.subplots(1, 2)

ax1 = axs[0]
ax2 = axs[1]

# Use each axX object normally...
```

## Two Y-Axis Example

```py
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y1 = x**2
y2 = np.sin(x)

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()

ax1.plot(x, y1, color='g')
ax2.plot(x, y2, color='b')

fig.subtitle('Two Y-Axis Example')
ax1.set_xlabel('x')
ax1.set_ylabel('y1')
ax2.set_ylabel('y2')

plt.show()
```

This will produce the following graph:

{{< figure src="/images/programming/languages/python/matplotlib-two-y-axis-example.png" width="500px" caption="Example matplotlib graph using two separate Y-axis." >}}

## Matching The Legend Text Color To The Plot Line Color

It can be a handy visual aid to set the legend color to the same color as the corresponding line on the plot. This can be done with the following code:

```py
fig, ax = plt.subplots()

x = np.linspace(0, 10, 100)
y_x = x
y_2x = 2*x
y_3x = 3*x

ax.plot(x, y_x, label='$y = x$')
ax.plot(x, y_2x, label='$y = 2x$')
ax.plot(x, y_3x, label='$y = 3x$')

leg = ax.legend()

# Set legend text color to line color
for line, text in zip(leg.get_lines(), leg.get_texts()):
    text.set_color(line.get_color())

plt.title('Legend Text Color Matches Plot Line Color')

plt.savefig('legend-text-color-matches-plot-line-color.png')
```

This will produce a plot which looks like:

{{% img src="legend-text-color-matches-plot-line-color.png" width="700px" %}}

## Creating Animated Plots

When using the `pillow` writer, the GIF will not loop. When using the `imagemagick` writer, the GIF will loop.

## Using The Basemap

{{% warning %}}
As of 2016, `Basemap` has been deprecated. However, it is still a viable choice for plotting maps in Python/Jupyter.
{{% /warning %}}

```py
from mpl_toolkits.basemap import Basemap
```

### Using A Specific Axis

Rather than `Basemap` automatically using/creating an axis for you, you can instead take a more object-orientated approach (which I recommend) and provide `Basemap` with the `Axis` object to use for drawing the map:

```py
fig = plt.figure(figsize=(15,10))
ax = fig.add_subplot(111)
map = Basemap(ax=ax) # Pass in the axis object to draw the basemap in
# Proceed as usual
```

### Adjusting The Size Of The Map

You can adjust the size of a basemap by calling `plt.figure(figsize(15,15))` before making any calls to the `Basemap` class:

```py
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

plt.figure(figsize(15, 10)) # Adjust the size of the map
map = Basemap()
```