import os
import bpy
import glob
import pathlib

def join_meshes():
    bpy.ops.object.select_all(action='DESELECT')

    mesh_objs = [m for m in bpy.context.scene.objects if m.type == 'MESH']

    for obj in mesh_objs:
        obj.select_set(state=True)
        bpy.context.view_layer.objects.active = obj

    bpy.ops.object.join()


#obj_path = os.path.join("C:\\Users\\USER\\plateau\\533946_2\\") #Windows
obj_path = bpy.path.abspath('') #Mac

p_temp = pathlib.Path(obj_path)
result = [str(p) for p in p_temp.glob('**/*.obj')]

print(result)

#「fbx」で終わるファイルのリストを取得します
obj_list = [item for item in result if item[-3:] == 'obj'] # obj, fbx, vrm, etc...

# obj_listの文字列をループし、ファイルをシーンに追加します
for item in obj_list:
    path_to_file = os.path.join(obj_path, item)
    bpy.ops.import_scene.obj(filepath = path_to_file) ## obj, fbx, vrm, etc...

join_meshes()


