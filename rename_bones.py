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
        # Print the object's name
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
original_model=[]
migoto_model=[]


def getV(vg_index,object_name):
    vg_idx = vg_index
    o = bpy.data.objects[object_name]
    vs = [ v for v in o.data.vertices if vg_idx in [ vg.group for vg in v.groups ] ]
    return vs,o.vertex_groups[vg_idx]


#get orignal model vertices index
for vg in bpy.data.objects[object_name_original].vertex_groups:
    vertex_source= getV(vg.index,object_name_original)
    vs_index=[x.index for x in vertex_source[0]],vertex_source[1].index,vertex_source[1].name
    original_model.append(vs_index)
    
#get 3dmigoto model vertices index
for vg in bpy.data.objects[object_name_migoto].vertex_groups:
    vertex_source= getV(vg.index,object_name_migoto)
    vs_index=[x.index for x in vertex_source[0]],vertex_source[1].index,vertex_source[1].name
    migoto_model.append(vs_index)
    
for x in original_model:
    for y in migoto_model:
        if (x[0] == y[0]):
            try:
                bpy.data.objects[armature_name].data.bones[x[2]].name = y[2]
            except Exception:
                print(f'couldnt possibly rename bone {x[2]}')
                pass


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
    