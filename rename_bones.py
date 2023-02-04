import bpy

# Select the armature and then run script

armature_name = bpy.context.active_object.name

# Make sure an object is selected
if bpy.context.active_object:
    if bpy.context.active_object.type == "ARMATURE":
        pass
    else:
        raise RuntimeError("The selected object is not an armature.")
else:
    raise RuntimeError("Error: No object selected.")
import bpy

found = False
# Iterate through all objects in the scene
for obj in bpy.data.objects:
    # Check if the object's name contains "Body-vb"
    if "Body-vb" in obj.name:
        object_name_migoto = obj.name
        found = True
        break

if not found:
    raise RuntimeError("Error: 3dmogoto object not found")

# Seperate bones
if armature_name in bpy.data.objects:
    bpy.ops.object.scale_clear()
    bpy.context.view_layer.objects.active = bpy.data.objects[armature_name]
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # Mirror the object along the x-axis
    bpy.ops.transform.mirror(constraint_axis=(True, False, False))
    bpy.ops.object.transform_apply(scale=True, rotation=False)
    
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.armature.select_all(action='SELECT')
    bpy.ops.armature.separate()
    bpy.ops.object.mode_set(mode='OBJECT')
    
else:
    raise RuntimeError("Error: No object selected.")


for obj in bpy.data.objects:
    if obj.type == "ARMATURE" and obj.name != armature_name:
        armature_name = obj.name
        break


object_name_original='Body'

bpy.context.view_layer.objects.active=bpy.data.objects[object_name_original]
bpy.ops.object.vertex_group_sort(sort_type='NAME')
for vertex_group in bpy.data.objects['Body'].vertex_groups:
    try:
        bpy.data.armatures[armature_name].bones[vertex_group.name].name = str(vertex_group.index)
        vertex_group.name = str(vertex_group.index)
    except Exception as e:
        raise RuntimeError(e)


new_armature_name = f"{object_name_migoto.split('Body')[0]} Armature"
if armature_name in bpy.data.objects:
    # Rename armature
    bpy.data.objects[armature_name].name = new_armature_name
    bpy.context.view_layer.objects.active = obj
    
    # Clear parent and apply transforms
    obj = bpy.data.objects.get(new_armature_name)
    obj.parent = None
    obj.rotation_euler[0] = -1.5708
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    obj.rotation_euler[0] = 1.5708
else:
    raise RuntimeError("Error: Object not found.")

# Delete all unnecessary data
for obj in bpy.data.objects:
    if obj.name != new_armature_name:
        # Remove the object from the scene
        for child in obj.children:
            bpy.data.objects.remove(child)
        bpy.data.objects.remove(obj)
    