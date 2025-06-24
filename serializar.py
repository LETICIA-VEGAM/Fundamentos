import pickle

info = [35, 88, 3.14, 16]

with open("./fundamentos/ArchivosSerial.bin", "wb") as binFile:
    pickle.dump(info, binFile)
print("Archivo binario escrito")
