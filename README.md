[![Please do not theme this app](https://stopthemingmy.app/badge.svg)](https://stopthemingmy.app) 
[![Available on Flathub](https://img.shields.io/flathub/downloads/se.sjoerd.Graphs?logo=flathub&labelColor=77767b&color=4a90d9)](https://flathub.org/apps/se.sjoerd.Graphs)
![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue)

# Graphs
Plot and manipulate data in a breeze with Graphs!

![image](https://raw.githubusercontent.com/Sjoerd1993/Graphs/main/data/screenshots/sin_cos.png)


Graphs is a simple, yet powerful tool that allows you to plot and manipulate your data with ease. New data can be imported from a wide variety of filetypes, or generated by equation. All data can be manipulated using a variety of operations.
Apart from regular operations, Graphs also has support for curve fitting on the data, allowing you to effortlessly analyze trends within your datasets.
Graphs supports extensive customization options to change the style of the plots. You can add and edit stylesheets in detail, allowing you to quickly save and apply existing stylesheets on new data. 
Graphs is an excellent fit for both plotting and data manipulation. The plots created with Graphs can be saved in a variety of formats suitable for sharing and presenting to a wide audience, such as in a scientific publication or presentations.
It is also possible to save the plots as vector images, which can be easily edited in programs like Inkscape for further customization and refinement. Graphs is written with the GNOME environment in mind, but should be suitable for any other desktop environment as well.

The operations include:
  - Shifting data
  - Normalizing Data
  - Smoothening data
  - Centering Data
  - Cutting Data
  - Combining Data
  - Translating data
  - Derivative and indefinite integral
  - Fourier Transformations
  - Custom transformations
 
For feedback or general issues, please file an issue [at the Github issue tracker](https://github.com/SjoerdB93/Graphs/issues).

## Install Graphs

### Stable
Since Graphs is developed using GNOME Builder, most testing will be done in a Flatpak environment, and the recommended installation method is therefore to install Graphs from Flathub. 
An official build is also available on the Snap store:

<p>
<a href="https://flathub.org/apps/details/se.sjoerd.Graphs"><img height="62" alt="Download on Flathub" src="https://flathub.org/assets/badges/flathub-badge-en.svg"/></a>&nbsp;&nbsp;
<a href="https://snapcraft.io/graphs"><img height="60" alt="Get it from the Snap Store" src="https://snapcraft.io/static/images/badges/en/snap-store-black.svg"/></a>
</p> 

### Beta
The latest testing version of Graphs is available in the Flathub beta channel. To install the beta, first the Flatpak remote needs to be configured:

```sh
flatpak remote-add --user --if-not-exists flathub-beta https://flathub.org/beta-repo/flathub-beta.flatpakrepo
```

Then, install the application:

```sh
flatpak install --user flathub-beta se.sjoerd.Graphs
```
To run the beta version by default, the following command can be used:

```sh
flatpak make-current se.sjoerd.Graphs beta
```
To switch back to the stable version simply run the same command replacing `beta` with `stable`. A beta version is also available in the beta channel of the Snap Store.
We are always looking for feedback, so feel free to report any issues or suggestions on the Github [issue tracker](https://github.com/Sjoerd1993/Graphs/issues).



## How to build from source
This project is developed in [GNOME Builder](https://developer.gnome.org/documentation/introduction/builder.html). After cloning and opening the project, you can press run to verify you have all correct dependencies installed.
You might need to install meson, if it is not already available on your system.
When the project successfully ran, you can create a Flatpak-bundle on the buildchain menu, which you then can install on your system.

If you want to try the latest development, we urge you to try the Flathub beta branch instead of building yourself.

### Build without flatpak
This project targets the GNOME Platform on Flathub. Manually building Graphs for any other platform is currently **not supported**.

If you want to build without Flatpak anyway these instructions might help:

build-time dependencies: `meson, blueprint-compiler, gettext`

runtime dependencies: `matplotlib, python3-matplotlib-gtk4, scipy, numpy, numexpr, sympy`

The actual package names might vary depending on your distribution, and depending on your distribution additional packages may be required.

building:
```
git clone https://github.com/Sjoerd1993/Graphs.git
cd Graphs
meson setup build
ninja -C build
ninja -C build/ install
```
Uninstall could then be done with the following:
```
ninja -C build/ uninstall
```

Please note, that this install might have issues that the Flatpak version does not.

## How to contribute
### Translations


Graphs is translated using Weblate.
If you wish to contribute to the translation of Graphs, in other languages please check out the project page on [Weblate](https://hosted.weblate.org/engage/graphs/).
We are incredibly grateful to anyone helping to make Graphs available in different languages!

<a href="https://hosted.weblate.org/engage/graphs/">
<img src="https://hosted.weblate.org/widget/graphs/multi-auto.svg" alt="Translation status" />
</a>

### Code 

If you wish to contribute to the code of Graphs, feel free to submit a [Pull request](https://github.com/Sjoerd1993/Graphs/pulls). 
We are always happy for contributions, and new code is generally reviewed within a few days time.

### Feedback and bug reports

If you found an issue or have general feedback, please file an issue at the [issue tracker](https://github.com/Sjoerd1993/Graphs/issues).


## Code of Conduct
This project follows the [GNOME Code of Conduct](https://wiki.gnome.org/Foundation/CodeOfConduct).
