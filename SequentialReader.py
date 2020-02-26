from MFRC522 import MFRC522

class SequentialReader():
    CE0_RESET = 22
    CE0_DEVICE = 0
    CE1_DEVICE = 1
    CE1_RESET = 12

    def ReadCE0(self):
        data = None
        Reader = MFRC522(device=self.CE0_DEVICE, reset=self.CE0_RESET)
        data_read = False
        while not data_read:
            (status, TagType) = Reader.MFRC522_Request(Reader.PICC_REQIDL)
            if status == Reader.MI_OK:
                """Card Detected"""
            (status, backData) = Reader.MFRC522_Anticoll()
            if status == Reader.MI_OK:
                data = "".join(str(x) for x in backData)
                data_read = True

        Reader.GPIO_CLEEN()
        return data


    def ReadCE1(self):
        data = None
        Reader = MFRC522(device=self.CE1_DEVICE, reset=self.CE1_RESET)
        data_read = False
        while not data_read:
            (status, TagType) = Reader.MFRC522_Request(Reader.PICC_REQIDL)
            if status == Reader.MI_OK:
                """Card Detected"""
            (status, backData) = Reader.MFRC522_Anticoll()
            if status == Reader.MI_OK:
                data = "".join(str(x) for x in backData)
                data_read = True

        Reader.GPIO_CLEEN()
        return data
