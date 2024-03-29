import maya.mel as mm
import maya.cmds as mc

mm.eval("paneLayout -e -manage false $gMainPane") #Disable viewport

objects = mc.ls( selection=True )
mc.artAttrSkinPaintCtx('artAttrSkinPaintCtx') #Run this line just for once

for x in range(len(objects)) :
        mc.select(objects[x])
        objects[x] = mc.rename(objects[x].replace('High', ''))
        mc.rename(objects[x]+ 'mesh0') #Create new mesh for vertex paint
        mc.polyReduce( ver=1, p=0, rpo=0)
        mc.setToolTo('artAttrSkinPaintCtx')
        mc.artAttrSkinPaintCtx('artAttrSkinPaintCtx', edit=True, ifl='C:/Fuzz.jpg') #The location of fuzz map
        '''LOD0 Output Setting'''
        mc.select(objects[x]+ 'mesh1')
        mc.rename(objects[x].replace('mesh1', '') + 'LOD0')
        mc.select(objects[x]+ 'LOD0')
        mm.eval('FBXExportInputConnections -v 0')
        mm.eval('FBXExport -f "C:/OPM/' + objects[x] + 'LCD0.fbx" -s') #The location of output fbx file
        '''LOD1 Output Setting'''
        mc.select(objects[x]+ 'mesh0')
        mc.setAttr( 'polyReduce1.percentage', 80)
        mc.select(objects[x]+ 'LOD0')
        mc.rename(objects[x].replace('LOD0', '') + 'LOD1')
        mc.select(objects[x]+ 'LOD1')
        mm.eval('FBXExportInputConnections -v 0')
        mm.eval('FBXExport -f "C:/OPM/' + objects[x] + 'LCD1.fbx" -s') #The location of output fbx file
        '''LOD2 Output Setting'''
        mc.select(objects[x]+ 'mesh0')
        mc.setAttr( 'polyReduce1.percentage', 85)
        mc.select(objects[x]+ 'LOD1')
        mc.rename(objects[x].replace('LOD1', '') + 'LOD2')
        mc.select(objects[x]+ 'LOD2')
        mm.eval('FBXExportInputConnections -v 0')
        mm.eval('FBXExport -f "C:/OPM/' + objects[x] + 'LCD2.fbx" -s') #The location of output fbx file
        mc.delete( objects[x]+ 'mesh0', objects[x]+ 'LOD2')

mm.eval("paneLayout -e -manage true $gMainPane") #Enable viewport