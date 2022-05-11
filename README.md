# ADS-JMS - Audio Data Storage

currently it can generate `WAV` files using `generatewav.py` file with different sampling rates and frequencies.

still need to implement error detection methods such as CRC

## Usage

To install the needed packages, type `pip install -r req.txt` (or use `pip3` for python3).   
If you want to use sine waves above human hearing, the sampling rate needs to comply with the frequency you are using, eg.: If you want to use frequencies above 22 kHz the sampling rate has to be comply to `sampling_rate = maximum_frequency * 2`. Currently the output has to be combined manually, but i am looking for an option to automate this process.

## To-Do

 - [x] Create header to distinguish filetypes and frequencys used (implemented as `custom` header)
 - [ ] Implement different filetypes to encode
 - [ ] Figure out maximum usable sample rate and frequency
 - [ ] Figure out usage of multiple channels
 - [ ] Implant data stream into audio file
 - [ ] Automate audio injection
 - [ ] Extract data stream from audio file
 - [ ] Error Detection (only applicable to decoding)
 - [ ] (Potential encoding and decoding)

Some form of error detection comes with the custom header, since we use a predefined standard to store information like High-Bit / Low-Bit frequencies, sampling rate and sample duration.

## Credits

This directory has been forked from https://github.com/stackbuffer/ads - all credits for the initial release go to him


## Donations

If you enjoy my work, why not buy me a coffee?      
[![paypal](https://www.paypalobjects.com/en_US/DK/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/donate/?hosted_button_id=K5KVUTX6HJHXU)

Of course, if you choose to enjoy it for free, I also appreciate it.