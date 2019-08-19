bl_info = {
    "name" : "Dot Loops",
    "author" : "Filipe Dias",
    "description" : "Alternate selection of parallel loops starting from the active edges.",
    "blender" : (2, 80, 0),
    "version" : (1, 0, 0),
    "category" : "Mesh"
}

import bpy
from bpy.types import Operator
from bpy.props import IntProperty

class DL_OT_SelectDotLoops(Operator):
    """Select parallel and interleaved loops starting from the active edge."""
    bl_idname = "mesh.dotloop"
    bl_label = "Dot Loops"
    bl_options = {'REGISTER', 'UNDO'}

    step = IntProperty(
        name='Step',
        description='Step between selected edges.',
        default=1,
        min=1
    )

    selection = IntProperty(
        name='Selection',
        description='Number of selected loops between intervals.',
        default=1,
        min=1
    )

    offset = IntProperty(
        name='Offset',
        description='Offset from the start edge.',
        default=0
    )
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.ops.mesh.loop_multi_select(ring=True)
        bpy.ops.mesh.select_nth(nth=self.step+1, skip=self.selection, offset=self.offset)
        bpy.ops.mesh.loop_multi_select(ring=False)

        return {'FINISHED'} 

def dotloops_button(self, contex):
    layout = self.layout
    layout.operator(DL_OT_SelectDotLoops.bl_idname)

def register():
    bpy.utils.register_class(DL_OT_SelectDotLoops)
    bpy.types.VIEW3D_MT_select_edit_mesh.append(dotloops_button)

def unregister():
    bpy.utils.unregister_class(DL_OT_SelectDotLoops)
    bpy.types.VIEW3D_MT_select_edit_mesh.remove(dotloops_button)

if __name__ == "__main__":
    register()