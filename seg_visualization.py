import matplotlib.pyplot as plt
from patplotlib.patches import Rectangle
from mpl_toolkits.axes_gird1 import make_axes_locatable
from mmseg.apis import show_result_pyplot
import os

def visualization():
   img = show_result_pyplot(model, img_path, result, opacity=0.5, show=True)
    
    fig, ax = plt.subplots(figsize=(10,5))
    plt.title(sample_img[num])
    ax.imshow(img)

    divider = make_axes_locatable(ax)
    ax_legend = divider.append_axes("right", 4, pad=0.1)
    ax_legend.set_xlim(0, 500)
    ax_legend.set_ylim(1000, 0)
    ax_legend.set_axis_off()

    margin_x = 20
    margin_y = 10
    base_y = 10
    swatch_width = 100
    swatch_height = 50
    swatch_start_x = 0
    text_start_x = swatch_width + margin_x

    for i, (cls, occupied) in enumerate(sorted(zip(seg_classes, seg_occupied), key=lambda t: t[1], reverse=True)):
        color = ADE20K_PALETTES[cls].copy()
        for j in range(3):
            color[j] /= 255.
        color += [1.]

        ax_legend.add_patch(
            Rectangle(xy=(swatch_start_x, base_y + (swatch_height + margin_y) * i), facecolor=color, width=swatch_width, height=swatch_height)
        )

        ax_legend.text(text_start_x,
                       base_y + (swatch_height / 2) + (swatch_height + margin_y) * i,
                       f'{ADE20K_CLASSES[cls]} ({format(occupied, "2.2%")})',
                       fontsize=12,
                       horizontalalignment='left',
                       verticalalignment='center')

    plt.savefig('./result/result_{}.png'.format(sample_img[num]))3
