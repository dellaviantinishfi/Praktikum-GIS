import shapefile

w = shapefile.Writer('soal12', shapeType=shapefile.POLYGON)
w.shapeType

w.field("kolom1", "C")


w.record("ngek", "satu")
w.record("ngok","dua")
w.record("brat","tiga")
w.record("brot","empat")
w.record("cret","lima")
w.record("crot","enam")
w.record("crut","tujuh")



w.poly([[[-5, 5], [5, 5], [10, -5], [-5, -5], [-5, 5]]])
w.poly([[[6, 1], [4, 4], [1, 3], [8, 3], [6, 1]]])

