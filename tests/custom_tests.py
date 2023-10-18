#!/usr/bin/env python3
import sys
import os
sys.path.append(os.getcwd())
import language_tool_python

print(f"Testing...")
spell = language_tool_python.LanguageTool("fr-FR", newSpellings=["Amalia", "Cerbèron"])
result = spell.check("Amalia est une petite elfe qui vie dans la forêt avec son chien Cerbèron.")
print(result)
assert(len(result) == 0)
spell.close()

spell = language_tool_python.LanguageTool("fr-FR")
result = spell.check("Amalia est une petite elfe qui vie dans la forêt avec son chien Cerbèron.")
print(result)
assert(len(result) == 2)
spell.close()

print(f"Testing...")
spell = language_tool_python.LanguageTool("en-GB", newSpellings=["Amalia", "Cerbèron"])
result = spell.check("Amalia is a little elf who lives in the forest with her dog Cerbèron.")
print(result)
assert(len(result) == 0)
spell.close()

spell = language_tool_python.LanguageTool("en-GB")
result = spell.check("Amalia is a little elf who lives in the forest with her dog Cerbèron.")
print(result)
assert(len(result) == 2)
spell.close()

print("###################################################")
print("##################### SUCCESS #####################")
print("###################################################")