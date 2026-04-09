Title:Create a flowchart and pseudocode to convert temperatures.
Declaration: nilaiSuhu, satuanAsal, satuanAkhir
Implementation:
if (satuanAsal = "C" and satuanAkhir = "F')
hasil = (nilaiSuhu*9/5) + 32
Else if (satuanAsal = "C" and satuanAkhir = "K")
hasil = nilaiSuhu + 273
Else If (satuanAsal = "F" AND satuanAkhir = "C")
    hasil = (nilaiSuhu - 32) * 5/9
Else If (satuanAsal = "F" AND satuanAkhir = "K")
    hasil = (nilaiSuhu - 32) * 5/9 + 273
Else If (satuanAsal = "K" AND satuanAkhir = "C")
    hasil = nilaiSuhu - 273
Else If (satuanAsal = "K" AND satuanAkhir = "F")
    hasil = (nilaiSuhu - 273) * 9/5 + 32

display hasil