# MoonshineVK
Your one stop shop for all things vulkan in python.

Features:

• Embed Vulkan HLSL code directly into Python that compiles to fast SPIR-V at runtime!</br>
• Use the built in moonshine bottle vulkan python wrapper to use vulkan directly in python, no extra install!</br>
• Make and run compute, vertex and fragment shaders directly inside python for AI, Graphics and Games.</br>

Whatever it is use MoonShineVK

## What is 'bvk' and what is 'mvk', and what's the difference?
This section discusses all project and package files.</br>

## mvk
### Moonshine Vulkan Package for Python

• Mvk is the main Moonshine Vulkan HLSL library for compiling HLSL into Spir-V and running it at runtime.</br>


## bvk
### Vulkan Bottle for Moonshine

• Bvk is the absolute 95% finished Vulkan 1.4 wrapper for Python that uses near to 18,000 lines of code to</br>
fully incorporate the Vulkan Graphics Library into python. Now that we have released 0.1.0 we are working on</br>
using bvk to load compute shaders through mvk.</br>

## apple barrel
### Vulkan Barrel framework for GOlang

• Applepie is an experimental moonshine implementation of bvk for Go.

> [!TIP]
> AppleBarrel Goland currently contains a library breaking bug with a missing</br>
> function type that won't let it compile.</br>

## Install

> [!WARNING]
> Due to unforeseen circumstances MoonshineVK's base bvk library</br>
> has seen a high increase in bugs and errors due to an outdated</br>
> wrapper formula likely built for Vulkan 1.2. Due to this we have</br>
> stopped all progress on mvk for HLSL and moved onto those bugs.</br>
> Now that we have finally got it to import and run without breaking</br>
> errors we will release the bvk-universal.py, this file will not be</br>
> installable through pip and any pip install for moonshine is outdated</br>
> and will not work when running. As well as this the main bvk looks for</br>
> the libvulkan library file depending on your operating system and so</br>
> you will need to find the file referenced on yor PC and update it in the</br>
> bvk-universal.py depending on your username and other folder paths.</br>
> Finally we are sad to announce MoonshineVK will no longer be receiving</br>
> any new features and will just be updated occasionally if ever for bugfixes.</br> 
https://github.com/h3lp5ystems/MoonshineVK/blob/main/bvk-universal.py
## Official Website (Look to section above for installing MoonshineVK or BVK.)

https://h3lp5ystems.github.io/MoonshineVK/</br>

## Powered by Vulkan 1.4

<img width="375" height="125" alt="Vulkan_Logo" src="https://github.com/user-attachments/assets/601fc25b-5c3d-4531-b3c3-538b4c918022" />

> [!IMPORTANT]
> As well as all text listed above this repository is also really unconventional and cluttered.

