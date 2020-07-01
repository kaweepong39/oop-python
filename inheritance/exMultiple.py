class Camera:
  def take_photo(self):
    print("Take a photo")

  def delete_photo(self):
    print("delete a photo")  

class Phone:
  def call(self, number):
    print("calling {}".format(number))

  def send_sms(self, message, number):
    print("sending {} to {}".format(message, number))

# Multiple inheritance 
class Smartphone(Camera, Phone):
  pass

s = Smartphone()
s.take_photo()
s.call("085-12-3333")
s.send_sms("Hello my friend", "085-12-3333")


