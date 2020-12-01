class VotersElligubility(Exception):
    def __int__(self):
        super()

try:
    age = "12"
    print("Age is "+str(age))
    if age<18:
        raise VotersElligubility

except VotersElligubility:
    print("Age is less than 18")
except TypeError:
    print("Age is not numeric")

else:
    print("Age is greater than or equal to 18")

finally:
    print("End of the program")