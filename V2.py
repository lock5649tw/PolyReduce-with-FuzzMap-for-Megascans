import maya.mel as mm
import maya.cmds as mc

mm.eval("paneLayout -e -manage false $gMainPane") #Disable viewport
objects = mc.ls( selection=True )

for x in range(len(objects)) :
        mc.select(objects[x])
        objects[x] = mc.rename(objects[x].replace('High', ''))
        mm.eval('polyCrunch')
        '''Poly Cruncher Setting'''
        mc.setAttr( 'polygonCruncherSettingsNode1.keepTextures', 1)
        mc.setAttr( 'polygonCruncherSettingsNode1.keepVertexColors', 1)
        mc.setAttr( 'polygonCruncherSettingsNode1.vcMode', 2)
        mc.setAttr( 'polygonCruncherSettingsNode1.vcTolerance', 0)
        mc.setAttr( 'polygonCruncherSettingsNode1.keepNormals', 1)
        mc.setAttr( 'polygonCruncherSettingsNode1.autoCalculate', 1)
        '''LOD0 Output Setting'''
        mc.setAttr( 'polygonCruncherSettingsNode1.optimizationRatio', 25)
        mc.rename(objects[x]+ 'LOD0')
        mm.eval('FBXExportInputConnections -v 0')
        mm.eval('FBXExport -f "C:/OPM/' + objects[x] + 'LCD0.fbx" -s') #The location of output fbx file
        '''LOD1 Output Setting'''
        mc.setAttr( 'polygonCruncherSettingsNode1.optimizationRatio', 20)
        mc.rename(objects[x]+ 'LOD1')
        mm.eval('FBXExportInputConnections -v 0')
        mm.eval('FBXExport -f "C:/OPM/' + objects[x] + 'LCD1.fbx" -s') #The location of output fbx file
        '''LOD2 Output Setting'''
        mc.setAttr( 'polygonCruncherSettingsNode1.optimizationRatio', 15)
        mc.rename(objects[x]+ 'LOD2')
        mm.eval('FBXExportInputConnections -v 0')
        mm.eval('FBXExport -f "C:/OPM/' + objects[x] + 'LCD2.fbx" -s') #The location of output fbx file
        mc.delete(objects[x]+ 'LOD2')

mm.eval("paneLayout -e -manage true $gMainPane") #Enable viewport