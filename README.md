# ADS-JMS - Audio Data Storage

currently it can generate `WAV` files using `generatewav.py` file with different sampling rates and frequencies.

still need to implement error detection methods such as CRC

## Usage

To install the needed packages, type `pip install -r req.txt` (or use `pip3` for python3). 

Also you will need to make sure to have ffmpeg and ffprobe installed.

If you want to use sine waves above human hearing, the sampling rate needs to comply with the frequency you are using, eg.: If you want to use frequencies above 22 kHz the sampling rate has to be comply to `sampling_rate = maximum_frequency * 2`. Currently the output has to be combined manually, but i am looking for an option to automate this process.

| :warning: WARNING          |
|:---------------------------|
| I should warn you that currently only the encoding and injecting works. I am working on a solution to decode the data.|

## File structure

The generated audio file will start with a 7 bit long header_len section. This section encodes the bit length of the header (ranging from 0 to 127 bits long). Following this are a maximum of 127 bits as header. It is split up as follows:

## Header Types

### Short

This header consists of a single indicator bit followed by up to 126 bits containing the data_len section. (max. data amount: 7.24*10^75 bits)

The indicator bit will always be 0 for a short header.


### Long / Custom

The long (or custom) header contains all metadata in case any of it was changed for the rest of the file.

It is setup as follows:

 - 1 indicator bit (always set to 1)
 - 6 bits encoding the low bit frequency (in kHz)
 - 6 bits encoding the high bit frequency (in kHz)
 - 7 bits encoding the sampling rate (in kHz)
 - 4 bits encoding the ms value
 - 24 bits encoding the file type contained in the wav output (as a string)
 - up to 79 bits encoding data_len (max data amount: 3.65*10^47 bits)

## Command Line Arguments

## Spectrum Analysis Example

The Decoder currently output a file with the complete spectrum analysis. It will look something like this:

[](./fig.png)

If we zoom in on the header area we get this:

[](./fig_zoom_header.png)

## To-Do

 - [x] Create header to distinguish filetypes and frequencys used (implemented as `long/custom` header)
 - [ ] Implement different filetypes to encode
 - [ ] Figure out minimum/maximum usable sample rate and frequency
 - [ ] Figure out usage of multiple channels
 - [x] Implant data stream into audio file
 - [x] Automate audio injection
 - [ ] Extract data stream from audio file
 - [ ] Error Detection (only applicable to decoding)
 - [ ] (Potential encrypting and decrypting)

Some form of error detection comes with the custom header, since we use a predefined standard to store information like High-Bit / Low-Bit frequencies, sampling rate and sample duration.

Note: Implanting works, but the implanted audio is very loud, a way to lower the volume still has to be found.

If you don't specify a input file, you will get only the generated audio.

## Supported Filetypes

 - [x] Text: txt
 - [ ] Archives: zip, rar, 7z, tar
 - [ ] Audio: wav, mp3 (potentially flac or alac)

## Credits

This directory has been forked from https://github.com/stackbuffer/ads - all credits for the initial release go to him


## Donations

If you enjoy my work, why not buy me a coffee?      
[![paypal](https://www.paypalobjects.com/en_US/DK/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/donate/?hosted_button_id=K5KVUTX6HJHXU)

Of course, if you choose to enjoy it for free, I also appreciate it.
