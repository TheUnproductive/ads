# ADS-JMS - Audio Data Storage

currently it can generate `WAV` files using `generatewav.py` file with different sampling rates and frequencies.

still need to implement error detection methods such as CRC

## Usage

To install the needed packages, type `pip install -r req.txt` (or use `pip3` for python3).   
If you want to use sine waves above human hearing, the sampling rate needs to comply with the frequency you are using, eg.: If you want to use frequencies above 22 kHz the sampling rate has to be comply to `sampling_rate = maximum_frequency * 2`. Currently the output has to be combined manually, but i am looking for an option to automate this process.

## Header Types

### Standard

This header will be used as a standard, basically all of the settings are unchanged.

Space required: ca. 29.2 KB

### Short

This header is basically the same as the standard header, except that it takes up less space.

Space required: ca. 5.92 KB

### Custom

This header is to be used when encoding with different frequencies and sampling rates.

It will create a header with data as follows:

`start_sequence -> "custom" -> breaker_freq -> f1 -> breaker_freq -> f2 -> breaker_freq -> rate -> breaker_freq -> ms -> breaker_freq -> filetype -> header_ending`

The header_ending currently is just the start_sequence repeated.

Space required (with default values): 95.8 KB

## To-Do

 - [x] Create header to distinguish filetypes and frequencys used (implemented as `custom` header)
 - [ ] Implement different filetypes to encode
 - [ ] Figure out maximum usable sample rate and frequency
 - [ ] Figure out usage of multiple channels
 - [x] Implant data stream into audio file
 - [x] Automate audio injection
 - [ ] Extract data stream from audio file
 - [ ] Error Detection (only applicable to decoding)
 - [ ] (Potential encoding and decoding)

Some form of error detection comes with the custom header, since we use a predefined standard to store information like High-Bit / Low-Bit frequencies, sampling rate and sample duration.

## Supported Filetypes

 - [x] Text: txt
 - [ ] Archives: zip, rar, 7z, tar
 - [ ] Audio: wav, mp3, flac

## Credits

This directory has been forked from https://github.com/stackbuffer/ads - all credits for the initial release go to him


## Donations

If you enjoy my work, why not buy me a coffee?      
[![paypal](https://www.paypalobjects.com/en_US/DK/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/donate/?hosted_button_id=K5KVUTX6HJHXU)

Of course, if you choose to enjoy it for free, I also appreciate it.
