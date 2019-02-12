from autoprep.encoding.encoder import Encoder


class EncoderProvider:
    def get_encoder(self, data):
        encoder = Encoder()
        return encoder