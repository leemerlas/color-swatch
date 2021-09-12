# color-swatch


# How to extend Swatch API to support BRGB

### Step 1: 
In the `views.py` file inside the `swatch_api` directory, add a new view where it would still contain the same iterating logic for generating five different values. But the additional logic would be a translate function, where it would map the new BRGB range (0 to 10000 INCLUSIVE) to the standard RGB range (0 to 256 INCLUSIVE).

### Step 2:
The translation needs to be done before returning the new values. Also, the returned values should be in RGB format, since the front-end would only know how to consume RGB and HSL formats.

## Notes
If there is a need to add a new color space with custom values, the way to go would be to make sure to map it to a standard range of values, like RGB or HSL. 

