# bpyインポート
import bpy
# math インポート
import math

# メッシュオブジェクトの作成
# 引数
# 戻り値
def make_cube_mesh():
  # Cubeオブジェクトを作成する
  bpy.ops.mesh.primitive_cube_add(\
    # 配置場所の指定
    location=( 0, 0, 3 ),\
    # 回転の指定
    rotation=( math.pi/3, 0, 0 ),\
  )
  # 作成したオブジェクトの参照を取得する
  ob = bpy.context.scene.objects.active
  # 名前を変更する
  ob.name='MakeCube'
  # スケールを変更する
  ob.scale=( 1, 1, 1 )
  # 選択状態を解除する
  ob.select=False
  return