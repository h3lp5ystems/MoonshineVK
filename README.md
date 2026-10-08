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

• Mvk currently only supports compute shaders due to the 1000+ lines of boilerplate required for running</br>
fragment shaders.</br>

## bvk
### Vulkan Bottle for Moonshine

• Bvk is the absolute 95% finished Vulkan 1.4 wrapper for Python that uses near to 18,000 lines of code to</br>
fully incorporate the Vulkan Graphics Library into python. Now that we have released 0.1.0 we are working on</br>
using bvk to load compute shaders through mvk.</br>

## applepie
### Vulkan Barrel framework for GOlang

• Applepie is an experimental moonshine implementation of bvk for Go.

## Install

Use the following install command to install</br>
`pip install moonshinevk==0.1.0`</br>

## Official Website

https://h3lp5ystems.github.io/MoonshineVK/</br>

## Powered by Vulkan 1.4

<img width="375" height="125" alt="Vulkan_Logo" src="https://github.com/user-attachments/assets/601fc25b-5c3d-4531-b3c3-538b4c918022" />


