import pydicom
bmode_ds = pydicom.read_file("bmode.dcm")
ttfm_ds = pydicom.read_file('ttfm.dcm')

with open('bmode_dtags.txt', 'w+') as f:
    for item in bmode_ds.keys():
        f.write("%s\n" % item)
f.close()
with open('ttfm_dtags.txt', 'w+') as f1:
    for item in ttfm_ds.keys():
        f1.write("%s\n" % item)
f1.close()
