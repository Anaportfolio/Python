from email.mime import image
import qrcode 

# Colocando o Link
link = input ("Digite o link: ")

# Colocando o nome que deseja salvar no QRcode
text = input("Digite o nome que deseja salvar: ")

# Transformando o Link em um QRcode
image = qrcode.make(link)

# Salvando o QRcode em JPG
image.save(text +".jpg")