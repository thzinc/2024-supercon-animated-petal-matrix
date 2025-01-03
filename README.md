# Animations on Petal Matrix for the 2024 Hackaday Supercon 8 badge

Demo to play animated images on the Petal Matrix

## "Image Animations" Quickstart

1. Copy the contents of [`image_animations`](./image_animations/) to the Pico.
2. Run it!

### Building

If you want to create your own images, create a 1-bit bitmap that is 9 pixels tall and at least 9 pixels wide, then use the [`convert.py`](./convert.py) script

```shell
$ python convert.py helloworld.bmp
Generating 54 frames
[b'\x00\x03\t\x07\x12\x08\x00\x00', b'\x01\x06\x01\x06qF\x00\x00', b'\x02\x08\x01>\x08#\t\x01', b'\x04\x10\x07\x024P\x07\x02', b'\x08#\t\rZ(\x01>', b'qF\x02\x16U&\x01\x06', b'\x12\t\x05\x1723\t\x07', b'\x15\x12\x05\x0e\x01\x1a\x06\x06', b'\x18"\x03\x02\x00\x0f\x01=', b'rC\x01\x00pD\x0f\x02', b'\x0f\x00\x00<\x08 \r\x1e', b"t \x06\x02tP\x05'", b'\x10c\t=\n(\x00&', b'\x19F\x06\x025V\x00\x04', b'\x12\x0b\t\rJ+\t\x01', b'\x05\x16\x02\x12E&\x06\x02', b'\n)\x05\x112s\t=', b'uR\x04\x0c\t:\x06\x02', b'\x08"\x02\x02\x04\x0f\x01=', b'rC\x01\x01\x02\x04\x0e\x02', b'\x0f\x00\x00\x00\x01\x02\x0c\x1c', b't \x00\x00pC\x05!', b'\x00`\x00\x1c\x08 \x06"', b'\x08@\x06\x02t`\x00\x1c', b'p\x03\x01\x1d\n0\x00\x00', b'\x01\x02\x06\x02uj\x00\x00', b'\x02\x03\x01\x1d\n7\x01\x01', b'\x05\x02\x06\x025J\x0e\x02', b"\n#\x01\rJ'\x05\x1d", b'uB\x02\x12E"\x0e"', b'\n!\x05\x112s\x05\x1d', b'uB\x04\x0c\t:\x06"', b'\x08"\x02\x02tO\x01\x1d', b'rC\x01\x1dJ$\x0e\x02', b'\x0f\x00\x06\x12\x05\x12\x0c\x1c', b't#\x05\x01rK\x05!', b'\x01b\x00<\t&\x06"', b'\nB\x06\x024S\t\x1d', b'v\x03\t\rJ(\x06\x02', b'\r&\x02\x12E&\x00<', b'ri\x05\x11rs\t\x01', b'\x05R\x04<\t:\x06\x02', b'\x08"\x06\x02\x04\x1f\x01=', b'rC\t\x01\x02\x0c\x0e\x02', b'\x0f\x06\x00\x00\x01\x06\x0c\x1c', b'v(\x00\x00\x00\x03\r!', b'\x04p\x00\x00\x00\x00\x06"', b'\x08`\x00\x00\x00\x00\x00<', b'p@\x00\x00\x00\x00\x00\x00', b'\x00\x00\x00\x00\x00\x00\x00\x00', b'\x00\x00\x00\x00\x00\x00\x00\x00', b'\x00\x00\x00\x00\x00\x00\x00\x00', b'\x00\x00\x00\x00\x00\x00\x00\x00', b'\x00\x00\x00\x00\x00\x00\x00\x00']
```

Copy the array (starting with `[b'` and ending with `']`) into a variable in [`images.py`](./badge/images.py) and then reference it in [`main.py`](./badge/main.py).

## "Fireworks" Quickstart

1. Copy the contents of [`fireworks`](./fireworks/) to the Pico.
2. Run it!

## Code of Conduct

We are committed to fostering an open and welcoming environment. Please read our [code of conduct](CODE_OF_CONDUCT.md) before participating in or contributing to this project.

## Contributing

We welcome contributions and collaboration on this project. Please read our [contributor's guide](CONTRIBUTING.md) to understand how best to work with us.

## License and Authors

[![Daniel James logo](https://secure.gravatar.com/avatar/eaeac922b9f3cc9fd18cb9629b9e79f6.png?size=16)) Daniel James](https://thzinc.com)

[![license](https://img.shields.io/github/license/thzinc/2024-supercon-iot-petal-matrix.svg)](https://github.com/thzinc/2024-supercon-iot-petal-matrix/blob/master/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/thzinc/2024-supercon-iot-petal-matrix.svg)](https://github.com/thzinc/2024-supercon-iot-petal-matrix/graphs/contributors)

This software is made available by Daniel James under the MIT license.
