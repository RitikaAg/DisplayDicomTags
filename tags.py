import pydicom
bmode_ds = pydicom.read_file("bmode.dcm")#reading the file
ttfm_ds = pydicom.read_file('ttfm.dcm')#reading the file

with open('bmode_dtags.txt', 'w+') as f:
    for item in bmode_ds.keys():
        f.write("%s\n" % item)#writing tags to file
f.close()
with open('ttfm_dtags.txt', 'w+') as f1:
    for item in ttfm_ds.keys():
        f1.write("%s\n" % item)#writing tags to file
f1.close()
