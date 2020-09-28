# Write a Python program to get OS name, platform and release information.
# Note: just added a few more details and general neatness

import platform

print("\n<><><><><><><><><><><><><><><><><><><><>")

print("\n\n><>< Version       >>>", platform.python_version())
print("><>< Version Tuple >>>", platform.python_version_tuple())
print("><>< Compiler      >>>", platform.python_compiler())
print("><>< Build         >>>", platform.python_build())

print("\n<><> Normal        >>>", platform.platform())
print("<><> Aliased       >>>", platform.platform(aliased=True))
print("<><> Terse         >>>", platform.platform(terse=True))

print("\n>><< System        >>>", platform.system())
print(">><< Node          >>>", platform.node())
print(">><< Release       >>>", platform.release())
print(">><< Version       >>>", platform.version())
print(">><< Machine       >>>", platform.machine())
print(">><< Processor     >>>", platform.processor(),"\n\n")

print("<><><><><><><><><><><><><><><><><><><><><>")