import maya.mel as mm
import maya.cmds as mc

mm.eval("paneLayout -e -manage false $gMainPane") #Disable viewport
objects = mc.ls( selection=True )

for x in range(len(objects)) :
        mc.select(objects[x])
        objects[x] = mc.rename(objects[x].replace('High', ''))
        mm.eval('polyCrunch')
        mc.setAttr( 'polygonCruncherSettingsNode1.keepTextures', 1)
        mc.setAttr( 'polygonCruncherSettingsNode1.keepVertexColors', 1)
        mc.setAttr( 'polygonCruncherSettingsNode1.vcMode', 2)
        mc.setAttr( 'polygonCruncherSettingsNode1.vcTolerance', 0)
        mc.setAttr( 'polygonCruncherSettingsNode1.keepNormals', 1)
        mc.setAttr( 'polygonCruncherSettingsNode1.autoCalculate', 1)
        #Star Poly Reducing
        mc.setAttr( 'polygonCruncherSettingsNode1.optimizationRatio', 25)
        mm.eval('duplicate -rr;')
        mc.rename(objects[x]+ 'LOD0')
        mc.select(objects[x])
        mc.setAttr( 'polygonCruncherSettingsNode1.optimizationRatio', 20)
        mm.eval('duplicate -rr;')
        mc.rename(objects[x]+ 'LOD1')
        mc.select(objects[x])
        mc.setAttr( 'polygonCruncherSettingsNode1.optimizationRatio', 15)
        mm.eval('duplicate -rr;')
        mc.rename(objects[x]+ 'LOD2')
        mc.select(objects[x]+ 'LOD0', objects[x]+ 'LOD1', objects[x]+ 'LOD2')
        mm.eval('LevelOfDetailGroup;')
        mm.eval('FBXExportInputConnections -v 0')
        mm.eval('FBXExport -f "D:/OPM/' + objects[x] + '.fbx" -s') #The location of output fbx file
        mc.delete(objects[x], 'LOD_Group_1')

mm.eval("paneLayout -e -manage true $gMainPane") #Enable viewport