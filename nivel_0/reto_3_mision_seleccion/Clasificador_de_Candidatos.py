experiencia = int(input("Años de experiencia: "))
python = input("¿Sabe Python? (si/no): ").lower() == "si"
maestria = input("¿Tiene maestría? (si/no): ").lower() == "si"
ingles = input("¿Habla inglés? (si/no): ").lower() == "si"
faltas = input("¿Tiene faltas éticas? (si/no): ").lower() == "si"

if faltas:
    print("❌ Descartado automáticamente")
else:
    if (experiencia > 5 and python) or (maestria and ingles):
        print("✅ Pre-seleccionado")
    else:
        print("⚠️ No apto")