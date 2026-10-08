import bvk
import subprocess


def runtime(code):
    ## Definitions ##

    compiler_function = 'dxc -spirv -T ps_6_0 -E main subprocess.hlsl -Fo output_shader.frag.spv'

    ## Writing to a temp file for Spir-V execution ##

    with open('subprocess.hlsl', 'w') as f:
        f.write(code)

    ## Compiling HLSL to Spir-V bin##

    try:
        subprocess.call(compiler_function, shell=True)
    except:
        return 0

    ## Running Spir-V bin##





