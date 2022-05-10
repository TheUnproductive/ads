# ADS-JMS - Audio Data Storage

currently it can generate `WAV` files using `generatewav.py` file with different sampling rates and frequencies.

still need to implement error detection methods such as CRC

## Usage

To install the needed packages, type `pip install -r req.txt` (or use `pip3` for python3).   
If you want to use sine waves above human hearing, the sampling rate needs to comply with the frequency you are using, eg.: If you want to use frequencies above 22 kHz the sampling rate has to be comply to `sampling_rate = maximum_frequency * 2`. Currently the output has to be combined manually, but i am looking for an option to automate this process.

## To-Do

 - Create header to distinguish filetypes and frequencys used
 - Automate audio injection
 - Figure out maximum usable frequency
 - Figure out maximum usable sample rate
 - Figure out usage of multiple channels
 - Implant data stream into audio file
 - Extract data stream from audio file
 - Error Detection (only applicable to decoding)
 - (Potential encoding and decoding)

## Credits

This directory has been forked from https://github.com/stackbuffer/ads - all credits for the initial release go to him


## Donations

If you enjoy my work, why not buy me a coffee?      
[![paypal](https://www.paypalobjects.com/en_US/DK/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/donate/?hosted_button_id=K5KVUTX6HJHXU)

Of course, if you choose to enjoy it for free, I also appreciate it.