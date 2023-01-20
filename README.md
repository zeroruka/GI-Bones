# GI Bones

Repo for all anime game character armatures blend files for easier modding.

# How to use?

1. Clone the entire repository or download individual blend files that you need
2. Open the corresponding armature blend file in Blender
3. Make sure you are in Object Mode
4. Copy the armature and paste it into your modded character blend file
5. Hold down shift and select all 3dmigoto files (files that are imported using the GIMI plugin)
6. Hold down ctrl and select the armature
7. You do either of the following to apply the armature to the model:
   - Right click on the model and select "Armature Deform -> With Empty Groups"
   - Or, press ctrl + p and select "Armature Deform -> With Empty Groups"
   - Or, add a new armature modifier to each of the 3dmigoto files and select the armature as the object
8. Now you can use the armature to test weights/etc.
9. To use the armature, select the armature and switch to pose mode to move bones around.

**Note: Some armatures does not fully work and needs manual fixing, please report any issues you find in the issues tab.**

**Your contrbution is highly appreciated, please help to populate this repo with more armatures if you can!**

# How to use script

Script (rename_bones.py) is originally made by Modder4869#4818, modified by me for easier use.

1. Import the base fbx model using BetterFBX. FBX model files can be found in [GI-Assets](https://github.com/zeroruka/GI-Assets)
2. Import the corresponding 3dmigoto dump using GIMI. 3dmigoto dump files can be found in [GI-Model-Importer-Assets](https://github.com/SilentNightSound/GI-Model-Importer-Assets)
3. Make sure the armature is selected
4. Run the script
5. If nothing goes wrong, the script should rename all the bones in the armature to the corresponding bone names in the 3dmigoto dump
6. Recursive delete unused data blocks (optional)
