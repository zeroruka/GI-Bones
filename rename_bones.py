import bpy

# Select the armature and then run script
armature_name = bpy.context.active_object.name

object_name_original = 'Body'
if not bpy.context.active_object:
    raise RuntimeError("The selected object is not an armature.")
if bpy.context.active_object.type != "ARMATURE" or armature_name not in bpy.data.objects:
    raise RuntimeError("Error: No object selected.")

bpy.ops.object.scale_clear()
bpy.context.view_layer.objects.active = bpy.data.objects[armature_name]
bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.transform.mirror(constraint_axis=(True, False, False))
bpy.ops.object.transform_apply(scale=True, rotation=False)

vertex_groups = [vg.name for vg in bpy.data.objects[object_name_original].vertex_groups]
pairs = {old:new for old,new in zip(vertex_groups, sorted(vertex_groups))}
name_mapping = {new: str(i) for i, (_, new) in enumerate(pairs.items())}
for vertex_group in bpy.data.objects[object_name_original].vertex_groups:
    armature_obj = bpy.data.objects[armature_name].data
    armature_obj.bones[vertex_group.name].name = vertex_group.name = name_mapping[vertex_group.name]

new_armature_name = f"{armature_name}_sorted"
bpy.data.objects[armature_name].name = new_armature_name
bpy.context.view_layer.objects.active = bpy.data.objects[new_armature_name]
obj = bpy.data.objects.get(new_armature_name)
obj.parent = None
bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
obj.rotation_euler[0] = -1.5708
bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
obj.rotation_euler[0] = 1.5708

for obj in bpy.data.objects:
    if obj.name != new_armature_name:
        for child in obj.children:
            bpy.data.objects.remove(child)
        bpy.data.objects.remove(obj)
